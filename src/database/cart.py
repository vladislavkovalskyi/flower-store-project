from tortoise import Model
from tortoise.fields import IntField, FloatField, ForeignKeyField, ReverseRelation


class Cart(Model):
    id = IntField(pk=True)
    total_price = FloatField(default=0.0, null=False)
    delivery_price = FloatField(default=0.0, null=False)
    items: ReverseRelation["CartItem"]


class CartItem(Model):
    id = IntField(pk=True)
    cart = ForeignKeyField("models.Cart", related_name="items")
    product = ForeignKeyField("models.Product", related_name="cart_items")
    quantity = IntField(default=1, null=False)
