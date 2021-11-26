from http import HTTPStatus
from uuid import UUID

from sanic import Blueprint
from sanic.response import empty, file_stream
from sanic_gzip import Compress

from Models.FileModel import FileModel as FileModel

download = Blueprint(name="api_download", url_prefix="/download")
compress = Compress()


@download.get("/<file_id:uuid>")
@compress.compress()
async def download_by_id(_, file_id: UUID):
    """
    Get physical binary data
    :param _: no use
    :param file_id:
    :return:
    """
    file_model = await FileModel.get(id=file_id)

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
