from pathlib import Path


current_directory = Path(__file__).parent


class Pathes:
    welcome = current_directory / "welcome.png"
    logo = current_directory / "logo.png"


class Bytes:
    welcome = Pathes.welcome.read_bytes()
    logo = Pathes.logo.read_bytes()
