import uuid

import sanic.request
from sanic import Blueprint, json
from sanic.request import Request

from Manager.FileManager import FileManager
from models.File import File as FileModel

upload = Blueprint(name="api_upload", url_prefix="/")


@upload.post("/upload")
async def upload_get(request: Request):

    try:
        file: sanic.request.File = request.files.get('file')
    except KeyError:
        return json({
            "received": False
        })

    if file is None:
        return json({
            "received": False
        })

    file_model = await FileModel.create(
        file_name=uuid.uuid4(),
        mimetypes=file.type,
        original_file_name=file.name
    )

    print(file_model.original_file_name)

    request.app.add_task(FileManager.write(file, file_model))

    return json({
        "received": True,
        "pk": str(file_model.pk)
    })