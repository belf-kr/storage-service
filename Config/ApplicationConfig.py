import json

from Config.BaseConfig import BaseConfig
from Config.EnvironmentConfig import get_environment_variable


class ApplicationConfig:
    _instance = None

    def __init__(self):
        super().__init__()

        self.APP_NAME = "STORAGE_SERVICE"
        self.VERSION = "0.1.2"
        self.HOST = "0.0.0.0"
        if bool(get_environment_variable("STORAGE_SERVICE_IS_PROD")):
            self.PORT = 8000
        else:
            self.PORT = None
        self.ACCESS_LOG = bool(get_environment_variable("STORAGE_SERVICE_ACCESS_LOG"))

        with open(BaseConfig.get_instance().APP_CONFIG_PATH, "r") as json_file:
            content = json.load(json_file)

            if not self.PORT:
                self.PORT = content["STORAGE_SERVICE_PORT"]

            if not self.ACCESS_LOG:
                self.ACCESS_LOG = content["STORAGE_SERVICE_ACCESS_LOG"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ApplicationConfig()
        return cls._instance
