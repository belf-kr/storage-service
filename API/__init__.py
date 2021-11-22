from sanic import Blueprint

from .Default import default
from .Delete import delete
from .Download import download
from .Information import information
from .Upload import upload

api = Blueprint.group(
    default,
    download,
    upload,
    information,
    delete,
    version=1,
    version_prefix="/api/v"
)
