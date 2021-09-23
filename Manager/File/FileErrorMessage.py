from Manager.File.FileErrorCode import FileErrorCode


class FileErrorMessage:
    def __init__(self, error_code: FileErrorCode):
        self.error_code = error_code
        self.error_name = error_code.name
        self.error_value = error_code.value

    def __str__(self):
        if self.error_code == FileErrorCode.ERROR_OK:
            return "SUCCESS : OK"
        else:
            return f"ERROR : {self.error_name}"

    def is_success(self) -> bool:
        return self.error_code == FileErrorCode.ERROR_OK

