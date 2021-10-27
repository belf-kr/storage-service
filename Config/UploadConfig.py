import json
from os import mkdir
from os.path import exists

from Common.CommonDefines import CommonDefines
from Config.BaseConfig import BaseConfig
from Config.EnvironmentConfig import get_environment_variable


class UploadConfig:
    _instance = None

    def __init__(self):
        super().__init__()

        self.UPLOAD_ABS_PATH = get_environment_variable("STORAGE_SERVICE_UPLOAD_ABS_PATH")

        if not self.UPLOAD_ABS_PATH:
            with open(BaseConfig.get_instance().UPLOAD_CONFIG_PATH, "r") as json_file:
                content = json.load(json_file)

                self.UPLOAD_ABS_PATH = CommonDefines.get_instance().PROJECT_ABS_PATH + content["STORAGE_SERVICE_UPLOAD_RELATIVE_PATH"]

        if not exists(self.UPLOAD_ABS_PATH):
            mkdir(self.UPLOAD_ABS_PATH)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = UploadConfig()
        return cls._instance
