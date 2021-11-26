import json
import os
from os import mkdir, getenv

from Common import path


class UploadConfig:
    _instance = None

    def __init__(self):
        super().__init__()

        self.UPLOAD_ABS_PATH = getenv("STORAGE_SERVICE_UPLOAD_PATH")

        if not self.UPLOAD_ABS_PATH:
            with open(path.UPLOAD_CONFIG_ABS_PATH, "r") as json_file:
                content = json.load(json_file)
                self.UPLOAD_ABS_PATH = f"{path.PROJECT_ABS_PATH}{content['STORAGE_SERVICE_UPLOAD_PATH']}"

        if not os.path.exists(self.UPLOAD_ABS_PATH):
            mkdir(self.UPLOAD_ABS_PATH)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = UploadConfig()
        return cls._instance
