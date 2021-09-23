from sanic import Blueprint
from .download import download
from .upload import upload

api = Blueprint.group(
    download,
    upload,
    version=1,
    version_prefix="/api/v"
)
