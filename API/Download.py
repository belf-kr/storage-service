from http import HTTPStatus
from uuid import UUID

from sanic import Blueprint
from sanic.response import empty, file_stream
from sanic.request import Request
from sanic_gzip import Compress

from Common import converter
from Common.Request import Query
from Models import FileModel
from tortoise.exceptions import DoesNotExist

download = Blueprint(name="api_download", url_prefix="/download")
compress = Compress()


@download.get("/")
@compress.compress()
async def download_by_id(request: Request):
    """
    Get physical binary data
    :param request:
    :return:
    """
    try:
        queries = converter.query_string_to_dict(request.query_string)
        file_model = await FileModel.get(id=queries.get(Query.FILE_ID.value))
    except DoesNotExist:
        file_model = None

    if not file_model:
        return empty(status=HTTPStatus.NOT_FOUND)

    mime_type = file_model.mime_type
    file_name = file_model.get_file_name()
    file_size = file_model.file_size

    return await file_stream(
        file_model.get_abs_path(),
        chunk_size=1024,
        mime_type=mime_type,
        filename=file_name,
        headers={"Content-Length": str(file_size)}
    )
