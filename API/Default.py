from sanic import Blueprint
from sanic_gzip import Compress
from sanic.response import empty

default = Blueprint(name="api_default", url_prefix="/default")
compress = Compress()


@default.get("/ping")
@compress.compress()
async def getPing(_):
    return empty(status=200)
