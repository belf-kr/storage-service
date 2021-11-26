from http import HTTPStatus
from uuid import UUID

from sanic import Blueprint, json
from sanic.response import empty
from sanic_gzip import Compress

from Models import FileModel

information = Blueprint(name="api_information", url_prefix="/info")
compress = Compress()


@information.get("/<file_id:uuid>")
@compress.compress()
async def information_by_id(_, file_id: UUID):
    """
    Get logical file data
    :param _: no use
    :param file_id: file id
    :return: file metadata
    """
    file_model = await FileModel.get(id=file_id)

    if file_model:
        return json(
            body=file_model.to_dict()
        )
    else:
        return empty(
            status=HTTPStatus.NOT_FOUND
        )
