import json

from Config.BaseConfig import BaseConfig
from Config.EnvironmentConfig import get_environment_variable


class ApplicationConfig:
    _instance = None

    def __init__(self):
        super().__init__()
        path = BaseConfig.get_instance().APP_CONFIG_PATH

        with open(path, "r") as json_file:
            content = json.load(json_file)
            self.STORAGE_SERVICE_APP_NAME = get_environment_variable(
                "STORAGE_SERVICE_APP_NAME") if get_environment_variable("STORAGE_SERVICE_APP_NAME") else content[
                "STORAGE_SERVICE_APP_NAME"]
            self.STORAGE_SERVICE_VERSION = get_environment_variable(
                "STORAGE_SERVICE_VERSION") if get_environment_variable("STORAGE_SERVICE_VERSION") else content[
                "STORAGE_SERVICE_VERSION"]
            self.STORAGE_SERVICE_HOST = get_environment_variable("STORAGE_SERVICE_HOST") if get_environment_variable(
                "STORAGE_SERVICE_HOST") else content["STORAGE_SERVICE_HOST"]
            self.STORAGE_SERVICE_PORT = int(
                get_environment_variable("STORAGE_SERVICE_PORT")) if get_environment_variable(
                "STORAGE_SERVICE_PORT") else content["STORAGE_SERVICE_PORT"]
            self.STORAGE_SERVICE_ACCESS_LOG = bool(get_environment_variable(
                "STORAGE_SERVICE_ACCESS_LOG")) if get_environment_variable("STORAGE_SERVICE_ACCESS_LOG") else \
                content["STORAGE_SERVICE_ACCESS_LOG"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ApplicationConfig()
        return cls._instance
