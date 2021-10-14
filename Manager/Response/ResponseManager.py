from sanic.response import json


class ResponseManager:
    @staticmethod
    def generate_basic_message(status: int, body: dict = None):
        if body is None:
            body = {}
        return json(
            status=status,
            body=body
        )
