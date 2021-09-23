import uuid
from typing import Optional

import aiofiles

from sanic.request import File, Request

from Common.CommonDefines import CommonDefines
from .FileErrorCode import FileErrorCode
from Models.File import File as FileModel
from ..Request.RequestManager import RequestManager


class FileManager:
    @staticmethod
    async def write_file(file: File) -> None:
        file_path = f"{CommonDefines.get_instance().UPLOAD_PATH}/{file.name}"
        async with aiofiles.open(file_path, 'wb') as fp:
            await fp.write(file.body)
        await fp.close()

    @staticmethod
    def check_file_from_request(request: Request, request_file_key: str = "file") -> FileErrorCode:

        if RequestManager.has_content_length(request):
            return FileErrorCode.ERROR_NOT_FOUND

        files: dict = request.files

        if files is None or {}:
            return FileErrorCode.ERROR_NOT_FOUND

        if request_file_key not in files.keys():
            return FileErrorCode.ERROR_KEY_NOT_FOUND

        file: File = files.get(request_file_key)

        if file.name == '':
            return FileErrorCode.ERROR_EMPTY_NAME

        if len(file.body) == 0:
            return FileErrorCode.ERROR_ZERO_SIZE

        return FileErrorCode.ERROR_SUCCESS

    @staticmethod
    async def upload_file_from_request(request: Request, file_key: str) -> (FileErrorCode, uuid.UUID):

        error_code = FileManager.check_file_from_request(request, file_key)
        pk = None

        if error_code == FileErrorCode.ERROR_SUCCESS:
            file: File = request.files.get(file_key)

            file_model = await FileModel.create(
                file_name=uuid.uuid4(),
                mimetypes=file.type,
                original_file_name=file.name
            )

            pk = file_model.pk

            request.app.add_task(FileManager.write_file(file))

        return error_code, pk
