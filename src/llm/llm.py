from openai import OpenAI

from src.config import OPENAI_TOKEN, OPENAI_ORGANIZATION, OPENAI_PROJECT
from src.database import User, ChatHistory

client = OpenAI(
    api_key=OPENAI_TOKEN,
    organization=OPENAI_ORGANIZATION,
    project=OPENAI_PROJECT,
)


async def make_response(prompt: str, user_id: int) -> str:
    user = await User.get_or_none(id=user_id)
    chat_history: ChatHistory = await user.chat_history.first()
    chat_history.data.append(
        {"role": "user", "content": prompt + f"\nUser ID: {user_id}"}
    )
    await chat_history.save()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history.data,
    )

    return response.choices[0].message.content
