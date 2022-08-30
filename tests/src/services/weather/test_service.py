# STANDARD IMPORTS
from unittest.mock import patch, MagicMock
import pytest

# PROJECT IMPORTS
from src.domain.models.weather.models import CoordinatesModel, CityModel
from src.services.weather.services import WeatherAPIService
from src.transport.weather.transport import GetWeather

# STUB IMPORTS
from tests.src.services.weather.weather_stubs import (
    weather_response_stub,
    params_coordinates,
    response_tuple
)


@patch.object(GetWeather, "get_coordinate_weather", return_value=MagicMock())
@patch.object(WeatherAPIService, "_WeatherAPIService__get_weather_information", return_value=(
        weather_response_stub, "27.14"
))
def test_get_weather_information_coordinates_when_sending_right_params_then_return_the_expected(
        mock_get_coordinate_weather,
        mock_get_weather_information
):
    response = WeatherAPIService.get_weather_information_coordinates(
        coordinates_model=CoordinatesModel(**params_coordinates)
    )

    assert response == response_tuple
    assert isinstance(response, tuple)


def test_get_weather_information_coordinates_when_sending_wrong_params_then_raise_error():
    with pytest.raises(AttributeError):
        WeatherAPIService.get_weather_information_coordinates(
            coordinates_model=None
        )


@patch.object(GetWeather, "get_coordinate_weather", return_value=MagicMock())
@patch.object(WeatherAPIService, "_WeatherAPIService__get_weather_information", return_value=(
        weather_response_stub, "27.14"
))
def test_get_weather_information_by_city_when_sending_city_right_params_then_return_the_expected(
        mock_get_coordinate_weather,
        mock_get_weather_information
):
    response = WeatherAPIService.get_weather_information_by_city(
        city_model=CityModel(**{"city": "Delhi"})
    )

    assert response == response_tuple
    assert isinstance(response, tuple)


def test_get_weather_information_by_city_when_sending_wrong_params_then_raise_error():
    with pytest.raises(AttributeError):
        WeatherAPIService.get_weather_information_by_city(
            city_model=None
        )
