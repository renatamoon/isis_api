# STANDARD IMPORTS
from unittest.mock import patch

import pytest

from src.domain.exceptions.exceptions import InvalidParamsWereSent
from src.domain.models.weather.models import CoordinatesModel, CityModel
# PROJECT IMPORTS
from src.services.main_service.service import MainServiceWeatherPlaylist
from src.services.spotify.services import SpotifyPlaylistsService
from src.services.weather.services import WeatherAPIService

# STUBS
from tests.src.services.main_service.file_stub import playlist_object_stub, weather_response_stub_2
from tests.src.services.weather.weather_stubs import weather_response_stub


@patch.object(SpotifyPlaylistsService, "party_playlist_objects", return_value=playlist_object_stub)
def test_when_sending_right_params_to_get_party_playlist_then_return_the_right_playlist(
        mock_party_playlist_objects
):
    response = MainServiceWeatherPlaylist.get_playlists(
        temperature=32.0
    )
    mock_party_playlist_objects.assert_called()
    assert response == playlist_object_stub
    assert isinstance(response, list)


@patch.object(SpotifyPlaylistsService, "pop_playlist_objects", return_value=playlist_object_stub)
def test_when_sending_right_params_to_get_pop_playlist_then_return_the_right_playlist(
        mock_party_playlist_objects
):
    response = MainServiceWeatherPlaylist.get_playlists(
        temperature=16.0
    )
    mock_party_playlist_objects.assert_called()
    assert response == playlist_object_stub
    assert isinstance(response, list)


@patch.object(SpotifyPlaylistsService, "rock_playlist_objects", return_value=playlist_object_stub)
def test_when_sending_right_params_to_get_rock_playlist_then_return_the_right_playlist(
        mock_party_playlist_objects
):
    response = MainServiceWeatherPlaylist.get_playlists(
        temperature=12.0
    )
    mock_party_playlist_objects.assert_called()
    assert response == playlist_object_stub
    assert isinstance(response, list)


@patch.object(SpotifyPlaylistsService, "classic_playlist_objects", return_value=playlist_object_stub)
def test_when_sending_right_params_to_get_classic_playlist_then_return_the_right_playlist(
        mock_party_playlist_objects
):
    response = MainServiceWeatherPlaylist.get_playlists(
        temperature=9.0
    )
    mock_party_playlist_objects.assert_called()
    assert response == playlist_object_stub
    assert isinstance(response, list)


@patch.object(WeatherAPIService, "get_weather_information_by_city", return_value=(weather_response_stub, 25.3))
@patch.object(MainServiceWeatherPlaylist, "get_playlists", return_value=playlist_object_stub)
def test_get_service_response_when_sending_right_params_of_city_then_return_the_expected(
        mock_get_playlists,
        mock_get_weather_information_by_city
):
    response = MainServiceWeatherPlaylist.get_service_response(
        coordinate_model=CoordinatesModel(
            **{"latitude": None, "longitude": None}
        ),
        city_model=CityModel(
            **{"city": "Manaus"}
        )
    )

    response_stub = {
                "tracks_for_you": playlist_object_stub,
                "about_your_weather": weather_response_stub_2
            }

    assert response == response_stub


@patch.object(WeatherAPIService, "get_weather_information_coordinates", return_value=(weather_response_stub, 25.3))
@patch.object(MainServiceWeatherPlaylist, "get_playlists", return_value=playlist_object_stub)
def test_get_service_response_when_sending_right_params_of_latitude_and_longitude_then_return_the_expected(
        mock_get_playlists,
        mock_get_weather_information_by_city
):
    response = MainServiceWeatherPlaylist.get_service_response(
        coordinate_model=CoordinatesModel(
            **{"latitude": 256.22, "longitude": 765.09}
        ),
        city_model=CityModel(
            **{"city": None}
        )
    )

    response_stub = {
                "tracks_for_you": playlist_object_stub,
                "about_your_weather": weather_response_stub_2
            }

    assert response == response_stub


def test_get_service_response_when_sending_no_query_params_of_lat_and_long_nor_city_then_raise_invalid_params_error():
    with pytest.raises(InvalidParamsWereSent):
        MainServiceWeatherPlaylist.get_service_response(
            coordinate_model=CoordinatesModel(
                **{"latitude": None, "longitude": None}
            ),
            city_model=CityModel(
                **{"city": None}
            )
        )
