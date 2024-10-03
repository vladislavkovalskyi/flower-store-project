from envparse import env
from tortoise import Tortoise
from aioowm import OWM

env.read_envfile(".env")

BOT_TOKEN = env.str("BOT_TOKEN")
OWNER_ID = env.int("OWNER_ID")

DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_ADDRESS = env.str("DB_ADDRESS")
DB_PORT = env.int("DB_PORT")

OWM_TOKEN = env.str("OWM_TOKEN")


weather_api = OWM(env.str("OWM_TOKEN"))


async def setup_database():
    models = ("src.database.user", "src.database.product", "src.database.cart")

    await Tortoise.init(
        # db_url="sqlite://:memory:",
        db_url="sqlite://db.sqlite",
        modules={"models": models},
    )
    Tortoise.init_models(models, "models")
    await Tortoise.generate_schemas()