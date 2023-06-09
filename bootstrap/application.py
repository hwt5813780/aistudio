import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.providers import app_provider
from app.providers import logging_provider
from app.providers import handle_exception
from app.providers import route_provider


def create_app() -> FastAPI:
    logging.info("App initializing")

    app = FastAPI()

    register(app, app_provider)
    register(app, logging_provider)
    register(app, handle_exception)

    boot(app, route_provider)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def register(app, provider):
    logging.info(provider.__name__ + ' registering')
    provider.register(app)


def boot(app, provider):
    logging.info(provider.__name__ + ' booting')
    provider.boot(app)
