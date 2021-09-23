from sanic import Blueprint, json
from sanic.request import Request

from Manager.File.FileManager import FileManager
from Manager.Request.RequestManager import RequestManager
from Manager.Response.UploadFileResponse.UploadResponseManager import UploadResponseManager

upload = Blueprint(name="api_upload", url_prefix="/")


@upload.post("/upload")
async def file_upload(request: Request):
    error_code, file_pk = await FileManager.upload_file_from_request(request, 'file')
    return UploadResponseManager.generate_file_message(error_code=error_code, pk=file_pk)


@upload.post('/upstream', stream=True)
async def upstream(request: Request):
    return json(
        RequestManager.convert_request_headers_to_dictionary(request.headers)
    )
