from sanic import Blueprint
from .download import download
from .upload import upload
from .stream import stream

api = Blueprint.group(
    download,
    upload,
    stream,
    version=1,
    version_prefix="/api/v"
)
