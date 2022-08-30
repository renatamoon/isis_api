# STANDARD IMPORTS
from unittest.mock import patch

# PROJECT IMPORTS
from src.services.main_service.service import MainServiceWeatherPlaylist
from src.services.spotify.services import SpotifyPlaylistsService

# STUBS
from tests.src.services.main_service.file_stub import playlist_object_stub


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
