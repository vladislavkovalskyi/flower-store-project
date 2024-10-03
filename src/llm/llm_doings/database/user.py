from src.database import User, Cart, CartItem, Product


async def get_user_city(user_id: int) -> str:
    user = await User.get(id=user_id)
    return f"[{user.city}]"


async def update_city(user_id: int, city: str) -> str:
    user = await User.get(id=user_id)
    user.city = city
    await user.save()

    return "[City updated]"


async def add_product_to_cart(user_id: int, product_id: int, quantity: int = 1) -> str:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()
    product = await Product.get_or_none(id=product_id)

    cart_item = await CartItem.filter(cart=cart, product=product).first()

    if cart_item is not None:
        cart_item.quantity += quantity
        await cart_item.save()
    else:
        await CartItem.create(cart=cart, product=product, quantity=quantity)

    all_cart_items = await cart.items.all()
    total_price: float = 0.0
    for item in all_cart_items:
        product = await item.product.first()
        total_price += product.price * item.quantity
    cart.total_price = total_price
    await cart.save()

    return "[Product added to cart]"


async def get_cart_products(user_id: int) -> str:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()

    cart_items: CartItem = await cart.items.all()

    text: str = ""

    for item in cart_items:
        product = await item.product.first()
        text += f"{product.id} {product.name=} {product.price=} {product.description=} {product.stock=}\n"

    return f"[{text}]" if text else "[Cart is empty]"


async def clear_cart(user_id: int) -> str:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()
    await cart.items.all().delete()
    await cart.save()

    return "[Cart is cleared]"


async def remove_product_from_cart(user_id: int, product_id: int) -> str:
    user = await User.get_or_none(id=user_id)
    cart: Cart = await user.cart.first()
    product = await Product.get_or_none(id=product_id)

    if product is not None:
        cart_item = await CartItem.filter(cart=cart, product=product).first()

        if cart_item is not None:
            await cart_item.delete()

            cart.total_price -= product.price * cart_item.quantity
            await cart.save()

    return "[Product removed from cart]"
