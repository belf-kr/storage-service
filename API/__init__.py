from sanic import Blueprint
from .Download import download
from .Upload import upload
from .Information import information

api = Blueprint.group(
    download,
    upload,
    information,
    version=1,
    version_prefix="/api/v"
)
