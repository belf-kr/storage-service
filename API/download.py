from uuid import UUID

from sanic import Blueprint
from sanic.response import file_stream

from Manager.File.FileManager import FileManager
from Manager.Response.ResponseHeaderHelper import ResponseHeaderHelper
from Models.File import File

download = Blueprint(name="api_download", url_prefix="/")


@download.get("/download/<file_id:uuid>")
async def download_root(_, file_id: UUID):
    file_name = str(await File.get(id=file_id))
    file_path = FileManager.get_file_path(str(file_id))
    headers = {}
    headers = ResponseHeaderHelper.append_content_length_by_file_id_on_headers(str(file_id), headers)
    return await file_stream(
        file_path,
        headers=headers,
        filename=file_name
    )

