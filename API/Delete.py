from sanic import Blueprint, Request
from sanic.response import empty
from sanic_gzip import Compress

from Manager.File.FileManager import FileManager

delete = Blueprint(name="api_delete", url_prefix="/delete")
compress = Compress()


@delete.delete("/")
@compress.compress()
async def file_delete(request: Request):
    await FileManager.delete_file_from_request(request)

    return empty(status=200)
