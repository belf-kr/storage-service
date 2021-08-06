from uuid import UUID

from aiofiles import os as async_os

from sanic import Blueprint, Request
from sanic.response import file_stream

stream = Blueprint(name="api_stream", url_prefix="/")


@stream.get("/")
async def index(request):
    file_path = "/srv/www/whatever.png"

    file_stat = await async_os.stat(file_path)
    headers = {"Content-Length": str(file_stat.st_size)}

    return await file_stream(
        file_path,
        headers=headers,
    )


@stream.get("/stream/mp4?<id:uuid>")
async def stream_root(request: Request, id: UUID):
    return await file_stream(
        "/path/to/sample.mp4",
        chunk_size=1024,
        mime_type="",
        headers={
            "Content-Disposition": "",
            "Content-Type": ""
        }
    )