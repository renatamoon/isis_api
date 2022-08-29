# PROJECT IMPORTS
from src.domain.models.weather.models import CoordinatesModel, CityModel
from src.transport.weather.transport import GetWeather


class WeatherAPIService:

    transport = GetWeather

    @classmethod
    def get_weather_information_coordinates(
            cls, coordinates_model: CoordinatesModel
    ):
        weather_info = cls.transport.get_coordinate_weather(
            lat=coordinates_model.latitude,
            lon=coordinates_model.latitude
        )

        weather_response, temperature = cls.__get_weather_information(
            weather_info=weather_info
        )

        return weather_response, temperature

    @classmethod
    def get_weather_information_by_city(
            cls, city_model: CityModel
    ):
        weather_info = cls.transport.get_city_weather(
            city_name=city_model.city
        )

        weather_response, temperature = cls.__get_weather_information(
            weather_info=weather_info
        )

        return weather_response, temperature

    @classmethod
    def __get_weather_information(
            cls,
            weather_info: dict
    ):
        city = weather_info.get("name")
        temperature = weather_info.get("main").get("temp")
        description = weather_info.get("weather").pop().get("description")

        weather_response = {
            "city": city,
            "temperature": cls.__convert_kelvin_to_celsius(
                kelvin_temperature=temperature
            ),
            "description": description
        }

        return weather_response, temperature

    @staticmethod
    def __convert_kelvin_to_celsius(kelvin_temperature: float):
        converted_celsius = kelvin_temperature - 273.15
        celsius = round(converted_celsius, 2)
        return celsius
