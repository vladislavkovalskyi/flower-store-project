from mubble import InlineKeyboard, InlineButton


report_a_bug = (
    InlineKeyboard().add(
        InlineButton("🐞 Повідомити про помилку", callback_data="report_bug")
    )
).get_markup()
