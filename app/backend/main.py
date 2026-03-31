import uvicorn

from fastapi import FastAPI

from config import settings
from api.routers import routers

app = FastAPI(
    title=settings.APP_NAME,
)

for router in routers:
    app.include_router(router)

def main():
    uvicorn.run(
        app=app,
        host=settings.HOST,
        port=settings.PORT
    )

if __name__ == "__main__":
    main()