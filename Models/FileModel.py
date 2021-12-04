from tortoise.fields import CharField, UUIDField, DatetimeField, IntField
from tortoise.models import Model

from Config import upload


class FileModel(Model):
    """
    ORM File Model
    """
    id = UUIDField(pk=True)
    ext = CharField(max_length=100, null=False)
    mime_type = CharField(max_length=100, null=False)
    last_update_datetime = DatetimeField(auto_now=True)
    file_size = IntField()
    user_id = IntField()

    class Meta:
        tablename = "file"

    def get_file_name(self) -> str:
        """
        Get file name
        :return: string
        """
        return f"{str(self.id)}.{self.ext}"

    def get_abs_path(self) -> str:
        """
        Get abs file path
        :return: string
        """
        return f"{upload.UPLOAD_ABS_PATH}/{self.pk}"

    def to_dict(self) -> dict:
        return {
            "id": str(self.pk),
            "ext": self.ext,
            "full_name": self.get_file_name(),
            "mime_type": self.mime_type,
            "last_update": str(self.last_update_datetime),
            "file_size": self.file_size,
            "user_id": self.user_id
        }
