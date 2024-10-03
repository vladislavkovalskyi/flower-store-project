import json

from mubble import Dispatch, Message
from mubble.rules import HasText

from openai import OpenAI

from src.config import OPENAI_TOKEN, OPENAI_ORGANIZATION, OPENAI_PROJECT
from src.database import User, ChatHistory
from src.llm.tools import tools
from src.llm.llm_doings import (
    calculate_delivery_cost,
    get_datetime,
    get_product_list,
    check_stock,
    get_user_city,
    update_city,
    add_product_to_cart,
    get_cart_products,
    clear_cart,
    remove_product_from_cart,
    make_order,
)

client = OpenAI(
    api_key=OPENAI_TOKEN,
    organization=OPENAI_ORGANIZATION,
    project=OPENAI_PROJECT,
)

dp = Dispatch()

tool_objects = {
    "calculate_delivery_cost": calculate_delivery_cost,
    "get_datetime": get_datetime,
    "get_product_list": get_product_list,
    "check_stock": check_stock,
    "get_user_city": get_user_city,
    "update_city": update_city,
    "add_product_to_cart": add_product_to_cart,
    "get_cart_products": get_cart_products,
    "clear_cart": clear_cart,
    "remove_product_from_cart": remove_product_from_cart,
    "make_order": make_order,
}


@dp.message(HasText())
async def llm_handler(message: Message, user: User):
    chat_history: ChatHistory = await user.chat_history.first()

    prompt = message.text.unwrap()
    chat_history.data.append(
        {"role": "user", "content": f"user_id: {user.id}\n{prompt}"}
    )
    await chat_history.save()

    response = client.chat.completions.create(
        model="gpt-4o", messages=chat_history.data, tools=tools
    )

    print(response.choices[0])
    result_message = response.choices[0]

    if result_message.message.tool_calls:
        for tool_call in result_message.message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            if tool_name in tool_objects:
                tool = tool_objects[tool_name]
                result = await tool(**tool_args)
                print(1, f"{result=}", end="\n\n")

                chat_history.data.append(
                    {
                        "role": "assistant",
                        "content": str(result),
                        "tool_call_id": tool_call.id,
                    }
                )
                await chat_history.save()

        new_response = client.chat.completions.create(
            model="gpt-4o", messages=chat_history.data
        )
        print(3, new_response.choices[0], end="\n\n")

        if new_response.choices[0].message.content is not None:
            await message.answer(str(new_response.choices[0].message.content))
    else:
        if result_message.message.content is not None:
            await message.answer(str(result_message.message.content))
            print(4)

    if result_message.message.content is not None:
        chat_history.data.append(
            {"role": "assistant", "content": result_message.message.content}
        )
        await chat_history.save()
        print(5)
