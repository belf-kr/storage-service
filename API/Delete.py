from sanic import Blueprint, Request
from sanic_gzip import Compress

from Manager.File.FileManager import FileManager

delete = Blueprint(name="api_delete", url_prefix="/delete")
compress = Compress()


@delete.delete("/")
@compress.compress()
async def file_delete(request: Request):
    await FileManager.delete_file_from_request(request)

    # TODO: HTTP status 코드 처리
    return
