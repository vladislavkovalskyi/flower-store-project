from src.config import weather_api


async def get_weather(city: str):
    result = await weather_api.get(city)

    if result.error:
        return {"error": True}

    temperature: float = result.weather.temperature.now
    weather_code: int = result.weather.id
    country: str = result.city.country

    return {
        "error": False,
        "temperature": temperature,
        "weather_code": weather_code,
        "country": country,
    }
