from http import HTTPStatus

from sanic import Blueprint
from sanic.request import Request, File
from sanic.response import empty, json
from sanic_gzip import Compress

import API
from Common.Request import Headers, Query
from Manager.File.FileManager import FileManager
from Middleware.Authorization import JsonWebToken

upload = Blueprint(name="api_upload", url_prefix="/upload")
compress = Compress()


@upload.post("/")
@compress.compress()
@JsonWebToken.only_validated()
async def file_upload(request: Request):
    """
    Upload physical and logical single file data
    :param request:
    :return:
    """
    payload = JsonWebToken.get_payload(request.headers.get(Headers.AUTHORIZATION.value))
    user_id = payload.get('user_id')

    if not user_id:
        return empty(status=HTTPStatus.BAD_REQUEST)

    error_code = FileManager.validate_files(request.files)

    if not error_code.is_success():
        return json(
            body={
                "message": error_code.get_error_message()
            },
            status=HTTPStatus.BAD_REQUEST
        )

    file: File = request.files.get('file')
    file_model = await FileManager.create_file_model(file, user_id)

    request.app.add_task(
        FileManager.upload_file(
            file,
            str(file_model.pk)
        )
    )

    location = f"{API.api.version_prefix}{API.api.version}{API.download.url_prefix}"
    location += f"?{Query.FILE_ID.value}={str(file_model.pk)}"
    headers = {
        "Location": location,
        "Access-Control-Allow-Origin": "*"
    }

    return empty(status=HTTPStatus.CREATED, headers=headers)
