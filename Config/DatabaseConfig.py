import json

from Config.BaseConfig import BaseConfig
from Config.EnvironmentConfig import get_environment_variable


class DatabaseConfig(BaseConfig):
    _instance = None

    def __init__(self):
        super().__init__()

        if get_environment_variable("STORAGE_SERVICE_IS_PROD"):
            self.DB_HOST = get_environment_variable("STORAGE_SERVICE_DB_HOST")
            self.DB_PORT = get_environment_variable("STORAGE_SERVICE_DB_PORT")
            self.DB_NAME = get_environment_variable("STORAGE_SERVICE_DB_NAME")
            self.DB_USER = get_environment_variable("STORAGE_SERVICE_DB_USER")
            self.DB_PASSWORD = get_environment_variable("STORAGE_SERVICE_DB_PASSWORD")

        else:
            with open(BaseConfig.get_instance().DB_CONFIG_PATH, "r") as f:
                content = json.load(f)

                self.DB_HOST = content["STORAGE_SERVICE_DB_HOST"]
                self.DB_PORT = content["STORAGE_SERVICE_DB_PORT"]
                self.DB_NAME = content["STORAGE_SERVICE_DB_NAME"]
                self.DB_USER = content["STORAGE_SERVICE_DB_USER"]
                self.DB_PASSWORD = content["STORAGE_SERVICE_DB_PASSWORD"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DatabaseConfig()
        return cls._instance

    def convert_to_dictionary(self):
        return {
            "host": self.DB_HOST,
            "port": self.DB_PORT,
            "db": self.DB_NAME,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD
        }

    def get_connection_url(self):
        return f"mysql://" \
               f"{self.DB_USER}:{self.DB_PASSWORD}" \
               f"@" \
               f"{self.DB_HOST}:{self.DB_PORT}" \
               f"/" \
               f"{self.DB_NAME}"
