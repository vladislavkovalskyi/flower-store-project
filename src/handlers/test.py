from mubble import Dispatch, Message
from mubble.rules import Command

from src.database import User, ChatHistory

dp = Dispatch()


@dp.message(Command("test"))
async def test_handler(message: Message, user: User):
    ch: ChatHistory = await user.chat_history.first()
    for i in ch.data:
        print(i["role"], i["content"], sep=" - ", end="\n\n")
