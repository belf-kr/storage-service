from tortoise.models import Model
from tortoise.fields import CharField, UUIDField, DatetimeField

from aiofiles import os as async_os

from Common.CommonDefines import CommonDefines


class File(Model):
    id = UUIDField(pk=True)
    file_name = CharField(max_length=100, null=False)
    ext = CharField(max_length=100, null=False)
    mime_type = CharField(max_length=100, null=False)
    last_update_datetime = DatetimeField(auto_now=True)

    class Meta:
        tablename = "file"

    def get_full_file_name(self):
        return self.file_name+self.ext

    def get_file_path(self) -> str:
        return f"{CommonDefines.get_instance().UPLOAD_PATH}/{self.pk}"

    async def get_file_size(self) -> int:
        return (await async_os.stat(self.get_file_path())).st_size

    @staticmethod
    def get_file_path_by_id(file_id: str):
        return f"{CommonDefines.get_instance().UPLOAD_PATH}/{file_id}"

    async def to_dict(self):
        return {
            "id": str(self.pk),
            "file_name": self.file_name,
            "ext": self.ext,
            "full_name": self.get_full_file_name(),
            "mime_type": self.mime_type,
            "last_update": str(self.last_update_datetime),
            "file_size": await self.get_file_size()
        }