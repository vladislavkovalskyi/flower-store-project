from src.database import Product, Order


async def get_product_list() -> str:
    products = await Product.all()

    text = "\n".join(
        [f"{p.id=} {p.name=} {p.price=} {p.description=} {p.stock=}" for p in products]
    )

    return f"[{text}]" if text else "[No products found]"


async def check_stock(product_id: int) -> bool:
    product = await Product.get_or_none(id=product_id)
    return f"[{product.stock}]" if product else "[Product not found]"


async def make_order(
    products_data: str,
    user_id: int,
    total_price: float,
    city: str,
    delivery_address: str,
    client_full_name: str,
) -> str:
    await Order.create(
        products_data=products_data,
        user_id=user_id,
        total_price=total_price,
        city=city,
        delivery_address=delivery_address,
        client_full_name=client_full_name,
    )

    return "[Order created]"
