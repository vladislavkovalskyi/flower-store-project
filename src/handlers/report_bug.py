from mubble import CallbackQuery, Dispatch, MessageReplyHandler, WaiterMachine
from mubble.rules import CallbackData, HasText
from src.config import OWNER_ID

dp = Dispatch()
wm = WaiterMachine(max_storage_size=1024)


@dp.callback_query(CallbackData("report_bug"))
async def report_bug(cq: CallbackQuery):
    message = (
        await cq.ctx_api.send_message(
            cq.chat_id,
            "🐞 <b>Повідомлення про помилку</b>\n\n"
            "📝 Опишіть, будь ласка, як можна <b>детальніше</b>, що саме ви зробили, та яка помилка виникла.",
        )
    ).unwrap()

    result, _ = await wm.wait(
        dp.message,
        (cq.ctx_api, message.chat_id),
        HasText(),
        default=MessageReplyHandler(
            "🤬 Опишіть вашу помилку <b>текстом</b>, будь-ласка."
        ),
    )

    await cq.ctx_api.send_message(
        OWNER_ID, f"🐞 <b>Повідомлення про помилку</b>\n\n{result.text.unwrap()}"
    )
    await cq.ctx_api.edit_message_text(
        "<b>🌸 Дякуємо за ваш внесок в нашу компанію!</b>\n\n<blockquote>📝 Повідомлення про помилку було відправлено!</blockquote>",
        chat_id=cq.chat_id,
        message_id=message.message_id,
    )
