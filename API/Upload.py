from http import HTTPStatus

from sanic import Blueprint
from sanic.request import Request
from sanic.response import empty
from sanic_gzip import Compress

import aiofiles
import aiofiles.os

import API
from Common.Request import Headers, Query
from Manager.File.FileManager import FileManager

from Middleware.Authorization import JsonWebToken

upload = Blueprint(name="api_upload", url_prefix="/upload")
compress = Compress()


@upload.post("/", stream=True)
@compress.compress()
@JsonWebToken.Middleware.only_validated()
async def file_upload(request: Request):
    """
    Upload physical and logical single file data
    :param request:
    :return:
    """
    user_id = JsonWebToken.get_user_id(request)
    if not user_id:
        return empty(status=HTTPStatus.FORBIDDEN)

    if Headers.CONTENT_TYPE.str() in request.headers.keys():
        try:
            file_mime: str = request.headers.get(Headers.CONTENT_TYPE.str())
            file_type, file_format = file_mime.split("/")
            if file_type != 'image':
                return empty(status=HTTPStatus.NOT_ACCEPTABLE)
        except AttributeError:
            return empty(status=HTTPStatus.BAD_REQUEST)
        except ValueError:
            return empty(status=HTTPStatus.BAD_REQUEST)
    else:
        return empty(status=HTTPStatus.NO_CONTENT)

    if Headers.CONTENT_LENGTH.str() in request.headers.keys():
        file_size = request.headers.get(Headers.CONTENT_LENGTH.str())
        if int(file_size) == 0:
            return empty(status=HTTPStatus.NOT_ACCEPTABLE)
    else:
        return empty(status=HTTPStatus.LENGTH_REQUIRED)

    file_model = await FileManager.create_file_model(file_mime, file_size, user_id)
    if not file_model:
        return empty(status=HTTPStatus.INTERNAL_SERVER_ERROR)

    file_id = file_model.id.__str__()
    file_path = FileManager.get_abs_path_by_id(file_id)

    read_body_size = 0
    try:
        async with aiofiles.open(file_path, 'wb') as fp:
            while True:
                body = await request.stream.read()
                if body is None:
                    break
                await fp.write(body)
                read_body_size += len(body)
            await fp.close()
    finally:
        if int(file_size) != read_body_size:
            await aiofiles.os.remove(file_path)
            await FileManager.delete_file(file_id)
            return empty(status=HTTPStatus.BAD_REQUEST)

    location = f"{API.api.version_prefix}{API.api.version}{API.download.url_prefix}"
    location += f"?{Query.FILE_ID.str()}={file_id}"
    headers = {
        Headers.ACCESS_CONTROL_EXPOSE_HEADERS.str(): "*",
        Headers.LOCATION.str(): location
    }

    return empty(status=HTTPStatus.CREATED, headers=headers)
