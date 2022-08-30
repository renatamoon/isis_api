# STANDARD IMPORTS
from unittest.mock import patch

# PROJECT IMPORTS
from src.services.spotify.services import SpotifyPlaylistsService
from src.transport.spotify.playlist_transport.transport import GetPlaylistsFromSpotify

# STUBS
from tests.spotify_response_stub import response_playlist_stub
from tests.src.services.spotify.stub_file import list_response_stub


@patch.object(GetPlaylistsFromSpotify, "get_party_playlist", return_value=response_playlist_stub)
def test_party_playlist_objects(
        mock_get_party_playlist
):
    response = SpotifyPlaylistsService.party_playlist_objects()
    assert response == list_response_stub
    assert isinstance(response, list)


@patch.object(GetPlaylistsFromSpotify, "get_pop_playlist", return_value=response_playlist_stub)
def test_pop_playlist_objects(
        mock_get_pop_playlist
):
    response = SpotifyPlaylistsService.pop_playlist_objects()
    assert response == list_response_stub
    assert isinstance(response, list)


@patch.object(GetPlaylistsFromSpotify, "get_rock_playlist", return_value=response_playlist_stub)
def test_rock_playlist_objects(
        mock_get_rock_playlist
):
    response = SpotifyPlaylistsService.rock_playlist_objects()
    assert response == list_response_stub
    assert isinstance(response, list)


@patch.object(GetPlaylistsFromSpotify, "get_classic_playlist", return_value=response_playlist_stub)
def test_classic_playlist_objects(
        mock_get_classic_playlist
):
    response = SpotifyPlaylistsService.classic_playlist_objects()
    assert response == list_response_stub
    assert isinstance(response, list)
