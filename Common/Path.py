import json

from os import path
from pathlib import Path


class CommonPath:
    _instance = None

    def __init__(self):
        self.PROJECT_ABS_PATH = path.abspath(Path(__file__).parent.parent.absolute())
        self.CONFIG_ABS_PATH = self.PROJECT_ABS_PATH + "/config.json"

        with open(self.CONFIG_ABS_PATH, "r") as json_file:
            content = json.load(json_file)
            self.DB_CONFIG_ABS_PATH = self.PROJECT_ABS_PATH + "/" + content["DB_CONFIG_PATH"]
            self.APP_CONFIG_ABS_PATH = self.PROJECT_ABS_PATH + "/" + content["APP_CONFIG_PATH"]
            self.UPLOAD_CONFIG_ABS_PATH = self.PROJECT_ABS_PATH + "/" + content["UPLOAD_CONFIG_PATH"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = CommonPath()
        return cls._instance
