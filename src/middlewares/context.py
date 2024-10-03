from mubble import ABCMiddleware, CallbackQuery, Dispatch, Message
from mubble.bot.dispatch.context import Context

from src.database import User, Cart, ChatHistory


dp = Dispatch()


@dp.message.register_middleware()
class MessageContextMiddleware(ABCMiddleware[Message]):
    async def pre(self, event: Message, ctx: Context) -> bool:
        user = await User.get_or_none(uid=event.from_user.id)

        if user is None:
            user = await User.create(uid=event.from_user.id)
            cart = await Cart.create()
            chat_history = await ChatHistory.create()

            user.cart = cart
            user.chat_history = chat_history
            await user.save()

        ctx.set("user", user)
        return True


@dp.callback_query.register_middleware()
class CallbackContextMiddleware(ABCMiddleware[CallbackQuery]):
    async def pre(self, event: CallbackQuery, ctx: Context) -> bool:
        user = await User.get_or_none(uid=event.from_user.id)

        if user is None:
            user = await User.create(uid=event.from_user.id)
            cart = await Cart.create()
            chat_history = await ChatHistory.create()

            user.cart = cart
            user.chat_history = chat_history
            await user.save()

        ctx.set("user", user)
        return True
