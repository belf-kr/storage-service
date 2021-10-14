from uuid import UUID

from sanic import Blueprint
from sanic.request import Request
from sanic_gzip import Compress

from Manager.File.FileManager import FileManager
from Manager.Response.UploadResponse.UploadResponseManager import UploadResponseManager

upload = Blueprint(name="api_upload", url_prefix="/upload")
compress = Compress()


@upload.post("/")
@compress.compress()
async def file_upload(request: Request):
    # TODO : Need to be more functional and optional like compressor func or like that
    error_code, file_pk = await FileManager.upload_file_from_request(request, 'file')

    print(error_code, file_pk)
    return UploadResponseManager.generate_file_message(error_code=error_code, pk=file_pk)


@upload.patch("/<file_id:uuid>")
@compress.compress()
async def file_patch(request: Request, file_id: UUID):
    # TODO : Need To Update Func Impl
    ...


@upload.delete("/<file_id:uuid>")
@compress.compress()
async def file_delete(request: Request, file_id: UUID):
    # TODO : Need To Delete Func Impl
    ...


@upload.post('/background', stream=True)
@compress.compress()
async def file_stream_upload(request: Request):
    # TODO : Need To Streaming Uploading Func Impl
    ...
