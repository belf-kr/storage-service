from os import environ

from sanic import Blueprint
from sanic.response import empty, text, json
from sanic_gzip import Compress

from Config.ApplicationConfig import ApplicationConfig

default = Blueprint(name="api_default", url_prefix="/default")
compress = Compress()


@default.get("/")
@compress.compress()
async def get_service_name(_):
    return text(ApplicationConfig.get_instance().APP_NAME, status=200)


@default.get("/ping")
@compress.compress()
async def get_ping(_):
    return empty(status=200)


@default.get("/version")
@compress.compress()
async def get_version(_):
    return text(ApplicationConfig.get_instance().VERSION, status=200)


@default.get("/env")
@compress.compress()
async def get_env(_):
    env_dict = {}

    for k, v in environ.items():
        env_dict[k] = v

    return json(env_dict, status=200)
