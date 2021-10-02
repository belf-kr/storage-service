from sanic import Blueprint
from .Download import download
from .Upload import upload
from .Information import information
from .Default import default

api = Blueprint.group(
    default,
    download,
    upload,
    information,
    version=1,
    version_prefix="/api/v"
)
