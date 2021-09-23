import os

from aiofiles import os as async_os

import aiofiles

from sanic.request import File, Request

from Common.CommonDefines import CommonDefines
from .FileErrorCode import FileErrorCode
from Models.File import File as FileModel


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
    async def create_file_model(file: File) -> FileModel:
        file_name, ext = os.path.splitext(file.name)
        return await FileModel.create(
            file_name=file_name,
            ext=ext
        )

    @staticmethod
    async def upload_file(file: File, file_id: str) -> None:
        file_path = FileManager.get_file_path(file_id)
        async with aiofiles.open(file_path, 'wb') as fp:
            await fp.write(file.body)
        await fp.close()

    @staticmethod
    def get_file_path(file_id: str) -> str:
        return f"{CommonDefines.get_instance().UPLOAD_PATH}/{file_id}"

    @staticmethod
    async def upload_file_from_request(request: Request, file_key: str) -> tuple[FileErrorCode, str]:
        error_code = FileManager.validate_files(request.files)
        file_id: str = ""
        if error_code == FileErrorCode.ERROR_SUCCESS:
            file: File = request.files.get(file_key)
            file_model = await FileManager.create_file_model(file)
            file_id = str(file_model.pk)
            request.app.add_task(FileManager.upload_file(file, file_id))
        return error_code, file_id

    @staticmethod
    async def get_file_size(file_id: str) -> int:
        return (await async_os.stat(FileManager.get_file_path(file_id))).st_size

