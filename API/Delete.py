from http import HTTPStatus

from sanic import Blueprint, Request
from sanic.response import empty, json
from sanic_gzip import Compress

from Common import converter
from Common.Request import Query
from MiddleWare.Authorization import JsonWebToken
from Common.Request import Headers
from Manager import FileManager


delete = Blueprint(name="api_delete", url_prefix="/delete")
compress = Compress()


@delete.delete("/")
@compress.compress()
@JsonWebToken.only_validated()
async def file_delete(request: Request):
    """
    Delete logical and physical file data
    :param request:
    :return:
    """
    query_string = converter.query_string_to_dict(request.query_string)

    value = request.headers.get(Headers.AUTHORIZATION.value)

    payload = JsonWebToken.get_payload(value)
    user_id = payload.get('user_id')
    file_id = query_string.get(Query.FILE_ID.value)

    status = HTTPStatus.OK

    if not user_id or not file_id:
        return empty(status=HTTPStatus.BAD_REQUEST)

    error_code = await FileManager.delete_file_model(file_id, user_id)

    if error_code.is_success():
        request.app.add_task(FileManager.delete_file(file_id))
    else:
        status = HTTPStatus.INTERNAL_SERVER_ERROR

    return json(
        body={
            "message": error_code.get_error_message()
        },
        status=status
    )