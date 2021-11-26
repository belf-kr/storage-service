from http import HTTPStatus

from Common import converter
from Common.Request import Query
from sanic import Blueprint, json
from sanic.request import Request
from sanic.response import empty
from sanic_gzip import Compress
from tortoise.exceptions import DoesNotExist

from Models import FileModel

information = Blueprint(name="api_information", url_prefix="/info")
compress = Compress()


@information.get("/")
@compress.compress()
async def information_by_id(request: Request):
    """
    Get File Meta Information
    :param request:
    :return:
    """

    queries = converter.query_string_to_dict(request.query_string)
    file_id = queries.get(Query.FILE_ID.value)

    if file_id:
        try:
            file_model = await FileModel.get(id=file_id)
        except DoesNotExist:
            file_model = None

        if file_model:
            return json(body=file_model.to_dict())
        else:
            return empty(status=HTTPStatus.NOT_FOUND)
    else:
        return empty(status=HTTPStatus.BAD_REQUEST)
