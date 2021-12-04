from enum import unique, Enum


@unique
class Body(Enum):
    FILE_ID = 'file_id'

    def str(self):
        return self.value
