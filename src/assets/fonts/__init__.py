import os
from pathlib import Path

from PIL import ImageFont

current_directory = Path(__file__).parent


class Comfortaa:
    def _get_font(filename: str, size: int) -> ImageFont.truetype:
        return ImageFont.truetype(os.path.join(current_directory, filename), size)

    @staticmethod
    def regular(size: int = 36) -> ImageFont.truetype:
        return Comfortaa._get_font("Comfortaa-Regular.ttf", size)

    @staticmethod
    def medium(size: int = 96) -> ImageFont.truetype:
        return Comfortaa._get_font("Comfortaa-Medium.ttf", size)
