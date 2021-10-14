from sanic import Blueprint
from sanic.response import empty
from sanic_gzip import Compress

default = Blueprint(name="api_default", url_prefix="/default")
compress = Compress()


@default.get("/ping")
@compress.compress()
async def get_ping(_):
    return empty(status=200)
