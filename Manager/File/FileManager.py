import mimetypes
import os
import uuid

import aiofiles
import aiofiles.os
from sanic.request import File, Request

from Common.UrlTool import get_query_string
from Models.File import File as FileModel
from .FileErrorCode import FileErrorCode


class FileManager:
    @staticmethod
    def validate_files(files: Request.files) -> FileErrorCode:
        if files is None:
            return FileErrorCode.ERROR_NOT_FOUND

        if len(files.keys()) == 0:
            return FileErrorCode.ERROR_KEY_NOT_FOUND

        for file_key in files.keys():
            file: File = files.get(file_key)
            if file is None:
                return FileErrorCode.ERROR_VALUE_NOT_FOUND
            else:
                if len(file.body) == 0:
                    return FileErrorCode.ERROR_ZERO_SIZE
                if len(file.name) == 0:
                    return FileErrorCode.ERROR_EMPTY_NAME

        return FileErrorCode.ERROR_SUCCESS

    @staticmethod
    async def create_file_model(file: File, user_id: int) -> FileModel:
        file_name, ext = os.path.splitext(file.name)
        return await FileModel.create(
            ext=ext,
            mime_type=FileManager.guess_mime_type_by_file_name(file.name),
            file_size=len(file.body),
            user_id=user_id
        )

    @staticmethod
    def guess_mime_type_by_file_name(file_name: str) -> str:
        return mimetypes.guess_type(file_name)[0]

    @staticmethod
    async def upload_file(file: File, file_id: str) -> None:
        file_path = FileModel.get_file_path_by_id(file_id)
        async with aiofiles.open(file_path, 'wb') as fp:
            await fp.write(file.body)
        await fp.close()

    @staticmethod
    async def upload_file_from_request(request: Request, file_key: str) -> tuple[FileErrorCode, str]:
        user_id = request.form.get("userId")
        error_code = FileManager.validate_files(request.files)
        file_id: str = ""
        if error_code == FileErrorCode.ERROR_SUCCESS:
            file: File = request.files.get(file_key)
            file_model = await FileManager.create_file_model(file, user_id)
            file_id = str(file_model.pk)
            request.app.add_task(FileManager.upload_file(file, file_id))
        return error_code, file_id

    @staticmethod
    async def delete_file_from_request(request: Request):
        query_string = get_query_string(request)
        user_id = query_string.get("userId")
        file_id = query_string.get("fileId")

        await FileManager.delete_file_model(file_id, user_id)
        await FileManager.delete_file(file_id)

    @staticmethod
    async def delete_file_model(file_id: uuid, user_id: int):
        model_to_delete = await FileModel.get(id=file_id, user_id=user_id)
        await model_to_delete.delete()

    @staticmethod
    async def delete_file(file_id: uuid):
        file_path = FileModel.get_file_path_by_id(file_id)

        await aiofiles.os.remove(file_path)
