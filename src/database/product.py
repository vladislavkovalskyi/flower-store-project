from tortoise import Model
from tortoise.fields import IntField, FloatField, CharField


class Product(Model):
    id = IntField(pk=True)
    name = CharField(max_length=255, null=False)
    price = FloatField(null=False)
    quantity = IntField(default=0, null=False)
    description = CharField(max_length=255, null=True)

    @property
    def stock(self):
        return self.quantity > 0
