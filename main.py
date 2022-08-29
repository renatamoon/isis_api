# STANDARD IMPORTS
import uvicorn

# PROJECT IMPORTS
from src.routers.base_router import BaseRouter


app = BaseRouter.register_routers()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
