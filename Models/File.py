from tortoise.models import Model
from tortoise.fields import CharField, UUIDField, DatetimeField, IntField

from Common.CommonDefines import CommonDefines


class File(Model):
    id = UUIDField(pk=True)
    ext = CharField(max_length=100, null=False)
    mime_type = CharField(max_length=100, null=False)
    last_update_datetime = DatetimeField(auto_now=True)
    file_size = IntField()

    class Meta:
        tablename = "file"

    def get_file_name(self):
        return str(self.id) + self.ext

    def get_file_path(self) -> str:
        return f"{CommonDefines.get_instance().UPLOAD_PATH}/{self.pk}"

    @staticmethod
    def get_file_path_by_id(file_id: str):
        return f"{CommonDefines.get_instance().UPLOAD_PATH}/{file_id}"

    async def to_dict(self):
        return {
            "id": str(self.pk),
            "ext": self.ext,
            "full_name": self.get_file_name(),
            "mime_type": self.mime_type,
            "last_update": str(self.last_update_datetime),
            "file_size": self.file_size
        }