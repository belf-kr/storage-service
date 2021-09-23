from enum import unique, Enum


@unique
class FileErrorCode(Enum):
    ERROR_SUCCESS = "success"
    ERROR_NOT_FOUND = "file was not found"
    ERROR_KEY_NOT_FOUND = "file key was not found"
    ERROR_VALUE_NOT_FOUND = "file value was not found"
    ERROR_ZERO_SIZE = "file size was zero"
    ERROR_EMPTY_NAME = "file name was empty"

    def to_error_message(self):
        return self.value

    def is_success(self):
        return self == FileErrorCode.ERROR_SUCCESS
