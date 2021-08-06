from uuid import UUID

from sanic import Blueprint, json

download = Blueprint(name="api_download", url_prefix="/")


@download.get("/<file_id:uuid>")
async def download_root(request, file_id: UUID):
    return json(
        {
            "file_id": str(file_id)
        }
    )
