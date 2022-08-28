import uvicorn
from src.routers.routers import app

app = BaseRouter.register_routers()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
