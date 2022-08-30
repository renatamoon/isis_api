# STANDARD IMPORTS
from unittest.mock import patch

# PROJECT IMPORTS
from src.domain.models.weather.models import CoordinatesModel, CityModel
from src.routers.playlist_weather_router.router import PlaylistWeatherRouter
from src.services.main_service.service import MainServiceWeatherPlaylist
from tests.src.routers.playlist_weather_router.stub_file import router_response_stub


@patch.object(MainServiceWeatherPlaylist, "get_service_response", return_value=router_response_stub)
def test_when_sending_right_params_to_get_playlist_response_then_return_the_expected(
            mock_get_service_response
):
    response = PlaylistWeatherRouter.get_playlist_response(
            coordinate_model=CoordinatesModel(
                **{
                    "latitude": 256.2,
                    "longitude": 258.85
                }
            ),
            city_model=CityModel(
                **{
                    "city": None
                }
            )
        )
    assert response == router_response_stub


@patch.object(MainServiceWeatherPlaylist, "get_service_response", return_value=router_response_stub)
def test_when_sending_right_params_by_city_then_return_the_expected(
            mock_get_service_response
):
    response = PlaylistWeatherRouter.get_playlist_response(
            coordinate_model=CoordinatesModel(
                **{
                    "latitude": None,
                    "longitude": None
                }
            ),
            city_model=CityModel(
                **{
                    "city": "Campinas"
                }
            )
        )
    assert response == router_response_stub
