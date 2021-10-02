from uuid import UUID

from sanic import Blueprint, json as sanic_json

from Models.File import File as FileModel
from sanic_gzip import Compress


information = Blueprint(name="api_information", url_prefix="/info")
compress = Compress()


@information.get("/<file_id:uuid>")
@compress.compress()
async def information_by_id(_, file_id: UUID):
    file_model = await FileModel.get(id=file_id)
    data = await file_model.to_dict()
    return sanic_json(body=data)
