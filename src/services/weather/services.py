# PROJECT IMPORTS
from src.domain.models.weather.models import CoordinatesModel, CityModel
from src.transport.weather.transport import GetWeather


class WeatherAPIService:

    transport = GetWeather

    @classmethod
    def get_weather_information_coordinates(
            cls, coordinates_model: CoordinatesModel
    ) -> tuple:
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
    ) -> tuple:
        city = city_model.city.title()

        weather_info = cls.transport.get_city_weather(
            city_name=city
        )

        weather_response, temperature = cls.__get_weather_information(
            weather_info=weather_info
        )

        return weather_response, temperature

    @classmethod
    def __get_weather_information(
            cls,
            weather_info: dict
    ) -> tuple:
        if weather_info.get("name"):

            city = weather_info.get("name", "Not Informed")
            description = weather_info.get("weather").pop().get("description")

            temperature = weather_info.get("main").get("temp")

            celsius_temperature = cls.__convert_kelvin_to_celsius(temperature)

            weather_response = {
                "city_or_timezone": city,
                "temperature": celsius_temperature,
                "description": description
            }

            return weather_response, celsius_temperature

        timezone = weather_info["timezone"]
        temperature_celsius = weather_info.get("current").get("temp")
        description = weather_info.get("current").get("weather").pop()["description"]

        weather_response = {
            "city_or_timezone": timezone,
            "temperature": temperature_celsius,
            "description": description
        }

        return weather_response, temperature_celsius

    @staticmethod
    def __convert_kelvin_to_celsius(kelvin_temperature: float) -> float:
        converted_celsius = kelvin_temperature - 273.15
        celsius = round(converted_celsius, 2)
        return celsius
