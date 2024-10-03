from tortoise import Model
from tortoise.fields import IntField, FloatField, CharField


class Order(Model):
    id = IntField(pk=True)
    user_id = IntField(null=False)
    products_data = CharField(max_length=1024, null=False)

    total_price = FloatField(null=False)

    city = CharField(max_length=150, null=False)
    delivery_address = CharField(max_length=255, null=False)
    client_full_name = CharField(max_length=255, null=False)
