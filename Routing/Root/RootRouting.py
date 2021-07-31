from sanic import Request, json, Sanic

from Config.Application.ApplicationConfig import ApplicationConfig

import os


class RootRouting:
    @staticmethod
    async def ping(req: Request):
        return json(
            body={}
        )

    @staticmethod
    async def version(req: Request):
        return json(
            {
                "version": ApplicationConfig.get_instance().VERSION
            }
        )

    @staticmethod
    async def env(req: Request):
        return json(
            {
                **os.environ
            }
        )

    @staticmethod
    def set_routing(app: Sanic):
        app.add_route(RootRouting.ping, "/ping")
        app.add_route(RootRouting.version, "/version")
        app.add_route(RootRouting.env, "/env")
