from tortoise.models import Model
from tortoise.fields import CharField, UUIDField


class File(Model):
    id = UUIDField(pk=True)
    file_name = CharField(max_length=100, null=False)
    original_file_name = CharField(max_length=255, null=False)
    mimetypes = CharField(max_length=100, null=False)

    class Meta:
        tablename = "file"

    def __str__(self):
        return self.original_file_name
