from tortoise.models import Model
from tortoise.fields import CharField, IntField


class File(Model):
    id = IntField(pk=True)
    file_name = CharField(100)
    original_file_name = CharField(255)
    directory_path = CharField(500)
    extension = CharField(10)

    def __str__(self):
        return self.original_file_name
