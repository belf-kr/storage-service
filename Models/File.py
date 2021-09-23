from tortoise.models import Model
from tortoise.fields import CharField, UUIDField


class File(Model):
    id = UUIDField(pk=True)
    file_name = CharField(max_length=100, null=False)
    ext = CharField(max_length=100, null=False)

    class Meta:
        tablename = "file"

    def __str__(self):
        return self.file_name+self.ext
