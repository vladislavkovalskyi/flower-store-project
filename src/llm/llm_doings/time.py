from datetime import datetime


async def get_datetime():
    return f"[{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}]"
