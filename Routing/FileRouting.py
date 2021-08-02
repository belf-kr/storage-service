from sanic import Request, json, Sanic

from models.FileModel import File


class FileRouting:

    @staticmethod
    async def get_all(request: Request):
        files = await File.all()
        return json({"files": [str(file) for file in files]})

    @staticmethod
    async def get_file(request: Request, pk: int):
        file = await File.get_or_none(pk=pk)
        return json({
            "file": str(file)
        })

    @staticmethod
    def set_routing(app: Sanic):
        __ROUTING_PREFIX__ = "/file"
        app.add_route(FileRouting.get_all, __ROUTING_PREFIX__, methods=["GET"])
        app.add_route(FileRouting.get_file, f"{__ROUTING_PREFIX__}/<pk:int>", methods=["GET"])
