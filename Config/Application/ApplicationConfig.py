import json

from Config.BaseConfig import BaseConfig


class ApplicationConfig:
    _instance = None

    def __init__(self):
        print("[ApplicationConfig] __init__")
        super().__init__()
        path = BaseConfig.get_instance().APP_CONFIG_PATH

        with open(path, "r") as json_file:
            content = json.load(json_file)
            self.APP_NAME = content["APP_NAME"]
            self.VERSION = content["VERSION"]
            self.HOST = content["HOST"]
            self.PORT = content["PORT"]
            self.ACCESS_LOG = content["ACCESS_LOG"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ApplicationConfig()
        return cls._instance
