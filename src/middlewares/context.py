from mubble import ABCMiddleware, CallbackQuery, Dispatch, Message
from mubble.bot.dispatch.context import Context

from src.database import User, Cart


dp = Dispatch()


@dp.message.register_middleware()
class MessageContextMiddleware(ABCMiddleware[Message]):
    async def pre(self, event: Message, ctx: Context) -> bool:
        user = await User.get_or_none(uid=event.from_user.id)

        if user is None:
            user = await User.create(uid=event.from_user.id)
            cart = await Cart.create()
            user.cart = cart
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
            user.cart = cart
            await user.save()

        ctx.set("user", user)
        return True
