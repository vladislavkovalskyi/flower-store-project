import asyncio
from io import BytesIO

from PIL import Image
from PIL.ImageDraw import Draw

from mubble import Dispatch, Message
from mubble.rules import StartCommand
from mubble.types import InputFile

from src.assets import images, fonts
from src.keyboards import report_a_bug

dp = Dispatch()


def text_generator(text: str) -> bytes:
    image = Image.open(images.Pathes.welcome)
    draw = Draw(image)
    font = fonts.Comfortaa.regular(80)

    draw.text(
        (image.size[0] // 2, 160), text, "#000000", font, align="center", anchor="ma"
    )

    fp = BytesIO()
    image.save(fp, "PNG")
    setattr(fp, "name", "image.jpg")
    return fp.getvalue()


@dp.message(StartCommand())
async def start(message: Message):
    image: bytes = text_generator(f"{message.from_user.first_name}")

    await message.answer_photo(
        InputFile("welcome.png", image),
        caption=(
            "🌸 Компанія <b>«Flowers Store»</b> вітає тебе!\n\n"
            "🤓 <b>Я твій віртуальний ассистент, який може:</b>\n"
            "<blockquote expandable>"
            "<b>1. Ділитися з тобою каталогом наших товарів</b>\n"
            "<b>2. Розраховувати вартість товару та доставки</b>\n"
            "<b>3. Займитися обробкою твоїх замовлень</b>\n"
            "<b>4. Відповідати на будь-які запитання, повʼязані з нами</b>\n"
            "</blockquote>\n\n"
            "📝 <b>Просто спілкуйся зі мною!</b>"
        ),
        reply_markup=report_a_bug,
    )
    await asyncio.sleep(1.5)
    await message.answer("🤓 Я чекаю на повідомлення від тебе!")
