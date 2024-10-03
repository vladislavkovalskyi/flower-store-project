from mubble import API, Dispatch, LoopWrapper, Mubble, ParseMode, Token, logger

from src.config import setup_database
from src import middlewares, handlers

logger.set_level("INFO")

dispatch = Dispatch()
dps = [*middlewares.dps, *handlers.dps]

for dp in dps:
    dispatch.load(dp)

loop_wrapper = LoopWrapper()


@loop_wrapper.lifespan.on_startup
async def on_startup():
    await setup_database()


api = API(Token.from_env(path_to_envfile=".env"))
api.default_params["parse_mode"] = ParseMode.HTML

bot = Mubble(
    api=api,
    dispatch=dispatch,
    loop_wrapper=loop_wrapper,
)

bot.run_forever()
