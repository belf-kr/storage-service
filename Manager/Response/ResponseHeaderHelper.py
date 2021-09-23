from Manager.File.FileManager import FileManager
from Models.File import File


class ResponseHeaderHelper:

    @staticmethod
    def append_content_length_by_file_id_on_headers(file_id: str, headers: dict):
        headers["Content-Length"] = str(FileManager.get_file_size(file_id))
        return headers
