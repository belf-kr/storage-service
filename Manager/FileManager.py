import aiofiles

from sanic.request import File

from Common.CommonDefines import CommonDefines
from Models.File import File as FileModel


class FileManager:
    @staticmethod
    async def write(file: File, file_model: FileModel) -> None:
        file_path = f"{CommonDefines.get_instance().UPLOAD_PATH}/{file_model.file_name}"
        async with aiofiles.open(file_path, 'wb') as fp:
            await fp.write(file.body)
        await fp.close()


