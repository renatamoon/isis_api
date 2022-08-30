# PROJECT IMPORTS
from src.domain.exceptions.exceptions import InvalidParamsWereSent
from src.domain.models.weather.models import CoordinatesModel, CityModel
from src.services.spotify.services import SpotifyPlaylistsService
from src.services.weather.services import WeatherAPIService


class MainServiceWeatherPlaylist:

    @classmethod
    def get_playlists(cls, temperature: float) -> list:

        if temperature > 30:
            party_response = SpotifyPlaylistsService.party_playlist_objects()
            return party_response

        if 15 <= temperature <= 30:
            pop_response = SpotifyPlaylistsService.pop_playlist_objects()
            return pop_response

        if 10 <= temperature <= 14:
            rock_response = SpotifyPlaylistsService.rock_playlist_objects()
            return rock_response

        if temperature < 10:
            classic_response = SpotifyPlaylistsService.classic_playlist_objects()
            return classic_response

    @classmethod
    def get_service_response(
            cls,
            coordinate_model: CoordinatesModel = None,
            city_model: CityModel = None
    ):

        if coordinate_model.latitude and coordinate_model.longitude:
            weather_response, temperature = WeatherAPIService.get_weather_information_coordinates(
                coordinates_model=coordinate_model
            )

            playlist_response = cls.get_playlists(
                temperature=temperature
            )

            response_dict = {
                "tracks_for_you": playlist_response,
                "about_your_weather": weather_response
            }

            return response_dict

        elif city_model.city:

            weather_response, temperature = WeatherAPIService.get_weather_information_by_city(
                city_model=city_model
            )

            playlist_response = cls.get_playlists(
                temperature=temperature
            )

            response_dict = {
                "tracks_for_you": playlist_response,
                "about_your_weather": weather_response
            }

            return response_dict

        else:
            raise InvalidParamsWereSent
