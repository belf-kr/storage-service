from functools import wraps
from sanic.response import empty
from sanic.request import Request
from Common.Request import Headers
from http import HTTPStatus
from Config import oauth
import aiohttp
import jwt


class JsonWebToken:
    @staticmethod
    async def is_validated_json_web_token(authorization: str):
        if not authorization:
            return False

        if not authorization.startswith('Bearer'):
            return False

        async with aiohttp.ClientSession(headers={"Authorization": authorization}) as session:
            async with session.get(oauth.URL + "/api/users/token/valid") as res:
                return res.status == HTTPStatus.OK

    @staticmethod
    def get_payload(authorization: str):
        payload: dict[str, any] = {}
        if authorization.startswith('Bearer'):
            authorization = authorization.split('Bearer')[-1]
            authorization = authorization.strip()
            payload = jwt.decode(jwt=authorization, options={"verify_signature": False})
        return payload

    @staticmethod
    def only_validated():
        def decorator(f):
            @wraps(f)
            async def decorated_function(request: Request, *args, **kwargs):
                value = request.headers.get(Headers.AUTHORIZATION.value)
                is_authorized = await JsonWebToken.is_validated_json_web_token(authorization=value)
                if is_authorized:
                    response = await f(request, *args, **kwargs)
                    return response
                else:
                    return empty(status=HTTPStatus.FORBIDDEN)
            return decorated_function

        return decorator
