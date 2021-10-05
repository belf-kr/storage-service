import base64

from sanic.response import file_stream, html, json

from Manager.Response.ResponseHeaderHelper import ResponseHeaderHelper
from Models.File import File as FileModel


class DownloadResponseManager:
    @staticmethod
    async def file_download_stream_message(file_model: FileModel, chunk_size: int = 4096):
        mime_type = file_model.mime_type
        file_name = file_model.get_file_name()
        file_size = file_model.file_size

        header = ResponseHeaderHelper.append_content_length_by_file_size_on_headers(
            file_size, {})

        return await file_stream(
            file_model.get_file_path(),
            chunk_size=chunk_size,
            mime_type=mime_type,
            filename=file_name,
            headers=header
        )

    '''
    Get base64 encoded string from file
    '''

    @staticmethod
    async def get_base64_message_from_file(file_model: FileModel):
        base64_string = ""

        with open(file_model.get_file_path(), 'rb') as file:
            base64_string = base64.b64encode(file.read()).decode("utf-8")
            file.close()
        return base64_string

    '''
    Call method to get base64 encoded string
    '''

    @staticmethod
    async def file_download_to_base64_message(file_model: FileModel):
        result = await DownloadResponseManager.get_base64_message_from_file(file_model)
        json_result = {
            "data": result
        }
        return json(json_result)

    '''
    Get file as html element from base64
    '''

    @staticmethod
    async def file_download_to_html_element_from_base64_message(file_model: FileModel):
        base64_string = await DownloadResponseManager.get_base64_message_from_file(file_model)
        ext = file_model.ext + ";base64,"

        html_string = f"<img src='data:image/{ext}{base64_string}' / >"
        return html(html_string)
