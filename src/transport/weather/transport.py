# STANDARD IMPORTS
import requests
import json
from decouple import config
from loguru import logger

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import ErrorFetchingWeatherData


class GetWeather:

    api_key = config("OPEN_WEATHER_API_KEY")
    base_url_coordinates = config("COORDINATES_URL")
    base_url_per_city = config("CITY_WEATHER_URL")

    @classmethod
    def get_coordinate_weather(cls, lat: str, lon: str) -> dict:
        try:
            base_url = f"{cls.base_url_coordinates}" % (lat, lon, cls.api_key)

            weather_response = requests.get(base_url)

            data = json.loads(weather_response.text)

            return data

        except Exception as ex:
            logger.error(ex=ex)
            raise ErrorFetchingWeatherData

    @classmethod
    def get_city_weather(cls, city_name: str) -> dict:

        try:
            base_url = cls.base_url_per_city + "appid=" + cls.api_key + "&q=" + city_name

            weather_response = requests.get(base_url)

            data = json.loads(weather_response.text)

            return data
        except Exception as ex:
            logger.error(ex=ex)
            raise ErrorFetchingWeatherData
