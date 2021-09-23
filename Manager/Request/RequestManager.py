from sanic import Request


class RequestManager:

    @staticmethod
    def convert_request_headers_to_dictionary(headers: Request.headers) -> dict:
        request_body = {}
        for key in headers.keys():
            request_body[key] = headers.get(key)
        return request_body

    @staticmethod
    def get_file_keys(request: Request) -> list[str]:
        file_keys: list[str] = []
        if RequestManager.is_file_exist(request):
            files: dict = request.files
            return list(files.keys())
        return file_keys

    @staticmethod
    def get_file_count(request: Request):
        try:
            return len(request.files)
        except TypeError:
            return 0

    @staticmethod
    def is_file_exist(request: Request) -> bool:
        return request.files is not None
