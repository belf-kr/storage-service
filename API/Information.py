from uuid import UUID

from tortoise.queryset import QuerySet
from sanic import Blueprint, json as sanic_json

from Models.File import File as FileModel

information = Blueprint(name="api_information", url_prefix="/")


@information.get("/info/<file_id:uuid>")
async def information_by_id(_, file_id: UUID):
    file_model = await FileModel.get(id=file_id)
    data = await file_model.to_dict()
    return sanic_json(body=data)


@information.get("/info/size/<size:int>")
async def information_all(_, size: int):
    file_models: list[FileModel] = await QuerySet(FileModel).limit(size).order_by("-last_update_datetime")
    data = [await file_model.to_dict() for file_model in file_models]
    return sanic_json(body={
        "data": data
    })
