from mubble import Dispatch, Message
from mubble.rules import Command

from src.database import User, Cart
from src.llm_doings.database.user import (
    get_user_city,
    update_city,
    add_product_to_cart,
    get_cart_products,
    clear_cart,
    remove_product_from_cart,
)

dp = Dispatch()


@dp.message(Command("update_city"))
async def update_city_handler(message: Message, user: User):
    city = "Odesa"
    await update_city(user.id, city)
    await message.answer(f"City updated to {city}")


@dp.message(Command("get_user_city"))
async def get_user_city_handler(message: Message, user: User):
    await message.answer(f"City: {await get_user_city(user.id)}")


@dp.message(Command("add_product_to_cart"))
async def add_product_to_cart_handler(message: Message, user: User):
    await add_product_to_cart(user.id, 1, 5)
    await message.answer("Product added to cart")


@dp.message(Command("get_cart_products"))
async def get_cart_products_handler(message: Message, user: User):
    await message.answer(await get_cart_products(user.id))


@dp.message(Command("clear_cart"))
async def clear_cart_handler(message: Message, user: User):
    await clear_cart(user.id)
    await message.answer("Cart cleared")


@dp.message(Command("remove_product_from_cart"))
async def remove_product_from_cart_handler(message: Message, user: User):
    product_id = 1
    await remove_product_from_cart(user.id, product_id)
    await message.answer("Product removed from cart")
