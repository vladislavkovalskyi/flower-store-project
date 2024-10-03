from tortoise import Model
from tortoise.fields import IntField, CharField, ForeignKeyField, BigIntField


class User(Model):
    id = IntField(pk=True)
    uid = BigIntField(null=False)
    city = CharField(max_length=255, null=True)
    cart = ForeignKeyField("models.Cart", related_name="user", null=True)
    chat_history = ForeignKeyField("models.ChatHistory", related_name="user", null=True)
