from tortoise import Model
from tortoise.fields import IntField, JSONField, DatetimeField
from src.llm.prompts import entry


class ChatHistory(Model):
    id = IntField(pk=True)
    data = JSONField(default=[{"role": "system", "content": entry.prompt}], null=False)
    last_update = DatetimeField(auto_now=True)