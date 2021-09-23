from Models.File import File as FileModel


class ResponseHeaderHelper:

    @staticmethod
    async def append_content_length_by_file_id_on_headers(file_id: str, headers: dict):
        return ResponseHeaderHelper.append_content_length_by_file_size_on_headers(
            await FileModel.get_file_path_by_id(file_id),
            headers
        )

    @staticmethod
    def append_content_length_by_file_size_on_headers(file_size: int, headers: dict):
        headers["Content-Length"] = str(file_size)
        return headers
