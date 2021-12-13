from http import HTTPStatus
from os import environ

from sanic import Blueprint
from sanic.response import empty, text, json
from sanic_gzip import Compress

from Config import app

default = Blueprint(name="api_default", url_prefix="/default")
compress = Compress()


@default.get("/")
@compress.compress()
async def get_service_name(_):
    return text(app.APP_NAME)


@default.get("/ping")
@compress.compress()
async def get_ping(_):
    return empty(status=HTTPStatus.OK)


@default.get("/version")
@compress.compress()
async def get_version(_):
    return text(app.VERSION)


# @default.get("/env")
# @compress.compress()
# async def get_env(_):
#     env_dict = {}

#     for k, v in environ.items():
#         env_dict[k] = v

#     return json(env_dict)
