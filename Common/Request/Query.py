from enum import unique, Enum


@unique
class Query(Enum):
    FILE_ID = 'file_id'

    def str(self):
        return self.value
