from src.database import Product


async def get_product_list() -> str:
    products = await Product.all()

    text = "\n".join(
        [f"{p.id=} {p.name=} {p.price=} {p.description=} {p.stock=}" for p in products]
    )

    return text


async def check_stock(product_id: int) -> bool:
    product = await Product.get_or_none(id=product_id)
    return product.stock if product else False
