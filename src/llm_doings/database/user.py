from src.database import User, Cart, CartItem, Product


async def update_city(user_id: int, city: str) -> None:
    user = await User.get_or_none(id=user_id)
    if user is not None:
        user.city = city
        await user.save()


async def get_user_city(user_id: int) -> str | None:
    user = await User.get_or_none(id=user_id)
    return user.city if user else None


async def add_product_to_cart(user_id: int, product_id: int, quantity: int) -> None:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()
    product = await Product.get_or_none(id=product_id)

    cart_item = await CartItem.filter(cart=cart, product=product).first()

    if cart_item is not None:
        cart_item.quantity += quantity
        await cart_item.save()
        return
    await CartItem.create(cart=cart, product=product, quantity=quantity)


async def get_cart_products(user_id: int) -> str:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()

    cart_items: CartItem = await cart.items.all()

    text: str = ""

    for item in cart_items:
        product = await item.product.first()
        text += f"{product.id=} {product.name=} {product.price=} {product.description=} {product.stock=}\n"

    return text or "Empty"


async def clear_cart(user_id: int) -> None:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()
    await cart.products.clear()
    await user.save()


async def remove_product_from_cart(user_id: int, product_id: int) -> None:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()
    product = await Product.get_or_none(id=product_id)

    if product is not None:
        await cart.products.remove(product)

        all_products = await cart.products.all()
        total_price = sum(product.price for product in all_products)
        cart.total_price = total_price

        await cart.save()
        await user.save()
