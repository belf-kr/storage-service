from http import HTTPStatus

from Manager.File.FileErrorCode import FileErrorCode
from Manager.Response.ResponseManager import ResponseManager


class UploadResponseManager:
    @staticmethod
    def generate_file_message(error_code: FileErrorCode, pk: str):
        status = HTTPStatus.BAD_REQUEST
        body = {
            "success": False
        }
        if error_code.is_success():
            status = HTTPStatus.OK
            body["file_pk"] = pk
            body["success"] = True
        else:
            body["message"] = error_code.to_error_message()
        return ResponseManager.generate_basic_message(
            status=status,
            body=body
        )
