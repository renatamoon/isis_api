# STANDARD IMPORTS
import requests
from decouple import config
from loguru import logger
from requests import Response

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import ErrorFetchingSpotifyData
from src.transport.spotify.token_transport.transport import SpotifyAPI


class GetPlaylistsFromSpotify:

    # ACCESS_KEYS
    client_id = config("CLIENT_ID")
    client_secret = config("CLIENT_SECRET_KEY")

    # ENDPOINTS URLS
    party_playlist = config("PARTY_PLAYLIST_URL")
    pop_playlist = config("POP_PLAYLIST_URL")
    rock_playlist = config("ROCK_PLAYLIST_URL")
    classic_playlist = config("CLASSIC_PLAYLIST_URL")

    @classmethod
    def get_party_playlist(cls) -> Response:
        headers = cls.__get_access_token_and_reader()

        try:
            response = requests.get(
                url=cls.party_playlist, headers=headers
            )
            return response.json()

        except Exception as ex:
            logger.error(ex=ex)
            raise ErrorFetchingSpotifyData

    @classmethod
    def get_pop_playlist(cls) -> Response:
        try:
            headers = cls.__get_access_token_and_reader()

            response = requests.get(
                url=cls.party_playlist, headers=headers
            )
            return response.json()

        except Exception as ex:
            logger.error(ex=ex)
            raise ErrorFetchingSpotifyData

    @classmethod
    def get_rock_playlist(cls) -> Response:
        try:
            headers = cls.__get_access_token_and_reader()

            response = requests.get(
                url=cls.party_playlist, headers=headers
            )
            return response.json()

        except Exception as ex:
            logger.error(ex=ex)
            raise ErrorFetchingSpotifyData

    @classmethod
    def get_classic_playlist(cls) -> Response:
        try:
            headers = cls.__get_access_token_and_reader()

            response = requests.get(
                url=cls.party_playlist, headers=headers
            )
            return response.json()

        except Exception as ex:
            logger.error(ex=ex)
            raise ErrorFetchingSpotifyData

    @classmethod
    def __get_access_token_and_reader(cls) -> dict:

        spotify = SpotifyAPI(
            client_id=cls.client_id,
            client_secret=cls.client_secret
        )

        spotify.perform_auth()

        access_token = spotify.access_token

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        return headers
