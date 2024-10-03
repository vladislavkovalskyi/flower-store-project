from .enums import WeatherCodes


WEATHER_PRICE_MULTIPLIERS = {
    # Гроза
    WeatherCodes.THUNDERSTORM_LIGHT_RAIN: 1.2,  # Легкая гроза с дождём
    WeatherCodes.THUNDERSTORM_RAIN: 1.3,  # Гроза с дождём
    WeatherCodes.THUNDERSTORM_HEAVY_RAIN: 1.4,  # Гроза с сильным дождём
    WeatherCodes.LIGHT_THUNDERSTORM: 1.1,  # Легкая гроза
    WeatherCodes.THUNDERSTORM: 1.25,  # Гроза
    WeatherCodes.HEAVY_THUNDERSTORM: 1.35,  # Сильная гроза
    WeatherCodes.RAGGED_THUNDERSTORM: 1.3,  # Рваная гроза
    WeatherCodes.THUNDERSTORM_LIGHT_DRIZZLE: 1.15,  # Гроза с моросью
    WeatherCodes.THUNDERSTORM_DRIZZLE: 1.2,  # Гроза с моросящим дождём
    WeatherCodes.THUNDERSTORM_HEAVY_DRIZZLE: 1.25,  # Гроза с сильным моросящим дождём
    # Морось
    WeatherCodes.LIGHT_DRIZZLE: 1.05,  # Слабая морось
    WeatherCodes.DRIZZLE: 1.1,  # Морось
    WeatherCodes.HEAVY_DRIZZLE: 1.15,  # Сильный дождь
    WeatherCodes.LIGHT_RAIN_AND_DRIZZLE: 1.08,  # Легкий дождь и морось
    WeatherCodes.DRIZZLE_RAIN: 1.1,  # Моросящий дождь
    WeatherCodes.HEAVY_DRIZZLE_RAIN: 1.2,  # Сильный моросящий дождь
    WeatherCodes.SHOWER_DRIZZLE: 1.2,  # Ливень и морось
    WeatherCodes.HEAVY_SHOWER_DRIZZLE: 1.25,  # Сильный ливень и морось
    WeatherCodes.DRIZZLE_SHOWER: 1.2,  # Изморось
    # Дождь
    WeatherCodes.LIGHT_RAIN: 1.1,  # Легкий дождь
    WeatherCodes.MODERATE_RAIN: 1.15,  # Умеренный дождь
    WeatherCodes.HEAVY_RAIN: 1.25,  # Сильный дождь
    WeatherCodes.VERY_HEAVY_RAIN: 1.3,  # Очень сильный дождь
    WeatherCodes.EXTREME_RAIN: 1.4,  # Жёсткий дождь
    WeatherCodes.FREEZING_RAIN: 1.35,  # Холодный дождь
    WeatherCodes.LIGHT_SHOWER_RAIN: 1.15,  # Легкий ливень
    WeatherCodes.SHOWER_RAIN: 1.2,  # Ливень
    WeatherCodes.HEAVY_SHOWER_RAIN: 1.3,  # Сильный ливень
    WeatherCodes.RAGGED_SHOWER_RAIN: 1.25,  # Рваный душ под дождем
    # Снег
    WeatherCodes.LIGHT_SNOW: 1.1,  # Легкий снег
    WeatherCodes.SNOW: 1.2,  # Снег
    WeatherCodes.HEAVY_SNOW: 1.3,  # Снегопад
    WeatherCodes.SLEET: 1.25,  # Мокрый снег
    WeatherCodes.LIGHT_SHOWER_SLEET: 1.2,  # Легкий дождь с мокрым снегом
    WeatherCodes.SHOWER_SLEET: 1.25,  # Мокрый снег
    WeatherCodes.LIGHT_RAIN_AND_SNOW: 1.15,  # Небольшой дождь и снег
    WeatherCodes.RAIN_AND_SNOW: 1.2,  # Дождь и снег
    WeatherCodes.LIGHT_SHOWER_SNOW: 1.15,  # Легкий снегопад
    WeatherCodes.SHOWER_SNOW: 1.25,  # Сильный снегопад
    WeatherCodes.HEAVY_SHOWER_SNOW: 1.35,  # Очень сильный снегопад
    # Атмосфера
    WeatherCodes.MIST: 1.05,  # Утренний туман
    WeatherCodes.SMOKE: 1.1,  # Дым
    WeatherCodes.HAZE: 1.05,  # Водный туман
    WeatherCodes.DUST_WHIRLS: 1.15,  # Песчано-пыльные вихри
    WeatherCodes.FOG: 1.05,  # Ясный туман
    WeatherCodes.SAND: 1.2,  # Песок
    WeatherCodes.DUST: 1.15,  # Пыль
    WeatherCodes.VOLCANIC_ASH: 1.3,  # Вулканический пепел
    WeatherCodes.SQUALLS: 1.25,  # Шквалы
    WeatherCodes.TORNADO: 1.5,  # Торнадо
    # Небо, облака
    WeatherCodes.CLEAR_SKY: 1.0,  # Чистое небо
    WeatherCodes.FEW_CLOUDS: 1.02,  # Очень мало облаков
    WeatherCodes.SCATTERED_CLOUDS: 1.03,  # Мало облаков
    WeatherCodes.BROKEN_CLOUDS: 1.05,  # Облачно
    WeatherCodes.OVERCAST_CLOUDS: 1.1,  # Сильно облачно
}


def calculate_delivery_cost(
    base_cost: float, weather_code: int, temperature: float
) -> float:
    """
    # Calculate delivery cost based on weather and temperature
    * `base_cost` - base delivery cost
    * `weather_code` - weather code
    * `temperature` - temperature in Celsius

    ## Returns
    * `final_cost` - final delivery cost
    """
    weather_multiplier = WEATHER_PRICE_MULTIPLIERS.get(weather_code, 1.0)
    temperature_multiplier = (
        1.15 if temperature > 30 else 1.1 if temperature <= 0 else 1.0
    )

    multiplier = weather_multiplier + temperature_multiplier
    final_cost = base_cost * multiplier

    return final_cost
