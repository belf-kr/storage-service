from uuid import UUID

from sanic import Blueprint
from sanic_gzip import Compress

from Manager.Response.DownloadResponse.DownloadResponseManager import DownloadResponseManager
from Models.File import File as FileModel

download = Blueprint(name="api_download", url_prefix="/download")
compress = Compress()


@download.get("/<file_id:uuid>")
@compress.compress()
async def download_by_id(_, file_id: UUID):
    file_model = await FileModel.get(id=file_id)
    return await DownloadResponseManager.file_download_stream_message(file_model)


@download.get("/base64/<file_id:uuid>")
@compress.compress()
async def download_base64_by_id(_, file_id: UUID):
    file_model = await FileModel.get(id=file_id)
    return await DownloadResponseManager.file_download_to_base64_message(file_model)


@download.get("/base64/html/<file_id:uuid>")
@compress.compress()
async def download_html_element_by_id(_, file_id: UUID):
    file_model = await FileModel.get(id=file_id)
    return await DownloadResponseManager.file_download_to_html_element_from_base64_message(file_model)
