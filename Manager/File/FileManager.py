import uuid
from typing import Optional

import aiofiles
import aiofiles.os
from sanic.request import File, Request
from tortoise.exceptions import OperationalError

from Config.UploadConfig import UploadConfig
from Models.FileModel import FileModel
from .FileErrorCode import FileErrorCode
from tortoise.exceptions import DoesNotExist


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
    async def create_file_model(mime_type: str, file_size: int, user_id: int) -> Optional[FileModel]:
        try:
            _, file_ext = mime_type.split("/")
            return await FileModel.create(
                ext=file_ext,
                mime_type=mime_type,
                file_size=file_size,
                user_id=user_id
            )
        except AttributeError:
            return None
        except ValueError:
            return None

    @staticmethod
    def get_abs_path_by_id(file_id: str) -> str:
        """
        Get abs path by id
        :param file_id:
        :return:
        """
        return f"{UploadConfig.get_instance().UPLOAD_ABS_PATH}/{file_id}"

    @staticmethod
    async def upload_file(file: File, file_id: str) -> None:
        """
        upload
        :param file:
        :param file_id:
        :return:
        """
        file_path = FileManager.get_abs_path_by_id(file_id)
        async with aiofiles.open(file_path, 'wb') as fp:
            await fp.write(file.body)
        await fp.close()

    @staticmethod
    async def delete_file_model(file_id: uuid, user_id: int) -> FileErrorCode:
        """

        :param file_id:
        :param user_id:
        :return:
        """
        error_code = FileErrorCode.ERROR_SUCCESS
        try:
            model_to_delete = await FileModel.get(id=file_id, user_id=user_id)
            if model_to_delete:
                try:
                    await model_to_delete.delete()
                except OperationalError:
                    error_code = FileErrorCode.ERROR_OPERATION
        except DoesNotExist:
            error_code = FileErrorCode.ERROR_NOT_EXIST

        return error_code

    @staticmethod
    async def delete_file(file_id: uuid):
        await aiofiles.os.remove(FileManager.get_abs_path_by_id(file_id))
