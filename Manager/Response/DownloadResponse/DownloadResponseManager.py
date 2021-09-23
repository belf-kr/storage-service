from http import HTTPStatus

from sanic.response import file_stream

from Manager.Response.ResponseHeaderHelper import ResponseHeaderHelper
from Models.File import File as FileModel


class DownloadResponseManager:
    @staticmethod
    async def file_download_stream_message(file_model: FileModel, chunk_size: int = 4096):

        mime_type = file_model.mime_type
        file_name = file_model.get_full_file_name()
        file_size = await file_model.get_file_size()

        header = ResponseHeaderHelper.append_content_length_by_file_size_on_headers(file_size, {})

        return await file_stream(
            file_model.get_file_path(),
            chunk_size=chunk_size,
            mime_type=mime_type,
            filename=file_name,
            headers=header
        )
