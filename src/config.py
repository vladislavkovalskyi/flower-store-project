from envparse import env
from tortoise import Tortoise
from aioowm import OWM

env.read_envfile(".env")

BOT_TOKEN = env.str("BOT_TOKEN")
OWNER_ID = env.int("OWNER_ID")

OWM_TOKEN = env.str("OWM_TOKEN")
OPENAI_TOKEN = env.str("OPENAI_TOKEN")
OPENAI_ORGANIZATION = env.str("OPENAI_ORGANIZATION")
OPENAI_PROJECT = env.str("OPENAI_PROJECT")


weather_api = OWM(env.str("OWM_TOKEN"))


async def setup_database():
    models = (
        "src.database.user",
        "src.database.product",
        "src.database.cart",
        "src.database.chat_history",
        "src.database.order",
    )

    await Tortoise.init(
        # db_url="sqlite://:memory:",
        db_url="sqlite://db.sqlite",
        modules={"models": models},
    )
    Tortoise.init_models(models, "models")
    await Tortoise.generate_schemas()
