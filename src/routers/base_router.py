# STANDARD IMPORTS
from fastapi import FastAPI, Response, Request
from starlette import status
import json

# PROJECT IMPORTS
from src.routers.playlist_weather_router.router import PlaylistWeatherRouter
from src.domain.exceptions.exceptions import (
    InternalServerError,
    BadRequestError,
    ForbiddenError,
    UnauthorizedError,
    ErrorFetchingWeatherData,
    ClientSecretKeysNotProvided,
    ErrorFetchingSpotifyData,
    InvalidParamsWereSent
)


class BaseRouter:

    app = FastAPI(
        title="ISIS API",
        description="Micro-service able to accept RESTFUL requests receiving as parameter either city name or lat "
                    "long coordinates and returns a playlist (only track names is fine) suggestion according "
                    "to the current temperature.",
    )

    @staticmethod
    def __register_router_playlist():
        weather_playlist_router = PlaylistWeatherRouter.get_playlist_weather_router()
        BaseRouter.app.include_router(weather_playlist_router)
        return BaseRouter.app

    @staticmethod
    def register_routers():
        BaseRouter.__register_router_playlist()

        return BaseRouter.app

    @staticmethod
    @app.middleware("http")
    def middleware_response(request: Request, call_next: callable):
        middleware_service_response = await BaseRouter.__add_process_time_header(
            request=request, call_next=call_next
        )
        return middleware_service_response

    @staticmethod
    def __add_process_time_header(request: Request, call_next):
        try:
            response = await call_next(request)

        except UnauthorizedError as e:
            return Response(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=json.dumps(
                    {"request_status": False, "status": 1, "msg": e.args[0]}
                ),
            )

        except ErrorFetchingWeatherData as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 2, "msg": e.args[0]}
                ),
            )

        except InvalidParamsWereSent as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 9, "msg": e.args[0]}
                ),
            )

        except ClientSecretKeysNotProvided as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 3, "msg": e.args[0]}
                ),
            )

        except ErrorFetchingSpotifyData as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 4, "msg": e.args[0]}
                ),
            )

        except ForbiddenError as e:
            return Response(
                status_code=status.HTTP_403_FORBIDDEN,
                content=json.dumps(
                    {"request_status": False, "status": 5, "msg": e.args[0]}
                ),
            )

        except BadRequestError as e:
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=json.dumps(
                    {"request_status": False, "status": 6, "msg": e.args[0]}
                ),
            )
        except InternalServerError as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 7, "msg": e.args[0]}
                ),
            )

        except Exception as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {
                        "request_status": False,
                        "status": 8,
                        "msg": f"An unexpected error occurred, {e}",
                    }
                ),
            )

        return response
