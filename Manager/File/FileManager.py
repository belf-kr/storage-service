import mimetypes
import os


import aiofiles

from sanic.request import File, Request

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
            ext=ext,
            mime_type=FileManager.guess_mime_type_by_file_name(file.name),
            file_size=len(file.body)
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
        error_code = FileManager.validate_files(request.files)
        file_id: str = ""
        if error_code == FileErrorCode.ERROR_SUCCESS:
            file: File = request.files.get(file_key)
            file_model = await FileManager.create_file_model(file)
            file_id = str(file_model.pk)
            request.app.add_task(FileManager.upload_file(file, file_id))
        return error_code, file_id


