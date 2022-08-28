# STANDARD IMPORTS
from fastapi import FastAPI, Request, Response
from starlette import status
import json

# THIRD PART IMPORTs
from loguru import logger

from src.domain.exceptions.exceptions import DataNotFoundError, InternalServerError, BadRequestError, ForbiddenError, \
    UnauthorizedError


class BaseRouter:

    app = FastAPI(
        title="ISIS API",
        description="micro-service able to accept RESTful requests receiving as parameter either city name or lat "
                    "long coordinates and returns a playlist (only track names is fine) suggestion according "
                    "to the current temperature.",
    )

    @staticmethod
    def __register_router_exchange():
        exchange_router = ExchangeRouter.get_exchange_router()
        BaseRouter.app.include_router(exchange_router)
        return BaseRouter.app

    @staticmethod
    def register_routers():
        BaseRouter.__register_router_exchange()

        return BaseRouter.app

    @staticmethod
    @app.middleware("http")
    async def middleware_response(request: Request, call_next: callable):
        middleware_service_response = await BaseRouter.__add_process_time_header(
            request=request, call_next=call_next
        )
        return middleware_service_response

    @staticmethod
    async def __add_process_time_header(request: Request, call_next):
        try:
            response = await call_next(request)

        except UnauthorizedError as e:
            logger.error(erro=e)
            return Response(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=json.dumps(
                    {"request_status": False, "status": 2, "msg": e.args[0]}
                ),
            )

        except ForbiddenError as e:
            return Response(
                status_code=status.HTTP_403_FORBIDDEN,
                content=json.dumps(
                    {"request_status": False, "status": 3, "msg": e.args[0]}
                ),
            )

        except BadRequestError as e:
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=json.dumps(
                    {"request_status": False, "status": 4, "msg": e.args[0]}
                ),
            )
        except InternalServerError as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 5, "msg": e.args[0]}
                ),
            )

        except DataNotFoundError as e:
            logger.error(erro=e)
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 14, "msg": e.args[0]}
                ),
            )

        except Exception as err:
            logger.error(erro=err)
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {
                        "request_status": False,
                        "status": 6,
                        "msg": "An unexpected error ocurred",
                    }
                ),
            )

        return response
