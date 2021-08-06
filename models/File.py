from tortoise.models import Model
from tortoise.fields import CharField, UUIDField


class File(Model):
    id = UUIDField(pk=True)
    file_name = CharField(100)
    original_file_name = CharField(255)
    mimetypes = CharField(100)

    class Meta:
        tablename = "file"

    def __str__(self):
        return self.original_file_name
