from typing import Type

from tortoise import Model


class TortoiseRouter:
    def db_for_read(self, model: Type[Model]):
        return "slave"

    def db_for_write(self, model: Type[Model]):
        return "master"
