from datetime import datetime


async def get_time():
    return datetime.now().strftime("%H:%M:%S")


async def get_date():
    return datetime.now().strftime("%d.%m.%Y")
