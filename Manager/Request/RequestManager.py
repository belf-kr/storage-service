from sanic import Request


class RequestManager:

    @staticmethod
    def convert_request_headers_to_dictionary(headers: Request.headers) -> dict:
        request_body = {}
        for key in headers.keys():
            request_body[key] = headers.get(key)
        return request_body

    @staticmethod
    def get_content_length(request: Request) -> int:
        content_length = 0
        if RequestManager.has_content_length(request):
            content_length = int(request.headers.get('content-length'))
        return content_length

    @staticmethod
    def has_content_length(request: Request) -> bool:
        return 'content-length' in request.headers.keys()

