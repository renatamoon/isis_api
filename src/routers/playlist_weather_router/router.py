# Standard Libs
from fastapi import Request, APIRouter, Depends

from src.domain.models.weather.models import CoordinatesModel, CityModel
from src.services.main_service.service import MainServiceWeatherPlaylist


class PlaylistWeatherRouter:

    __playlist_by_weather_router = APIRouter()

    @staticmethod
    def get_playlist_weather_router():
        return PlaylistWeatherRouter.__playlist_by_weather_router

    @staticmethod
    @__playlist_by_weather_router.get("/get_playlist_weather", tags=["PLAYLIST WEATHER"])
    async def get_playlist_response(
            request: Request,
            coordinate_model: CoordinatesModel = Depends(),
            city_model: CityModel = Depends()
    ):
        response = MainServiceWeatherPlaylist.get_service_response(
            coordinate_model=coordinate_model,
            city_model=city_model
        )
        return response
