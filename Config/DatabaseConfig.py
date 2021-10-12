import json

from Config.BaseConfig import BaseConfig
from Config.EnvironmentConfig import get_environment_variable


class DatabaseConfig(BaseConfig):
    _instance = None

    def __init__(self):
        super().__init__()

        with open(BaseConfig.get_instance().DB_CONFIG_PATH, "r") as f:
            content = json.load(f)
            self.STORAGE_SERVICE_DB_HOST = get_environment_variable(
                "STORAGE_SERVICE_DB_HOST") if get_environment_variable(
                "STORAGE_SERVICE_DB_HOST") else content["STORAGE_SERVICE_DB_HOST"]
            self.STORAGE_SERVICE_DB_PORT = int(get_environment_variable(
                "STORAGE_SERVICE_DB_PORT")) if get_environment_variable(
                "STORAGE_SERVICE_DB_PORT") else content["STORAGE_SERVICE_DB_PORT"]
            self.STORAGE_SERVICE_DB_NAME = get_environment_variable(
                "STORAGE_SERVICE_DB_NAME") if get_environment_variable(
                "STORAGE_SERVICE_DB_NAME") else content["STORAGE_SERVICE_DB_NAME"]
            self.STORAGE_SERVICE_DB_USER = get_environment_variable(
                "STORAGE_SERVICE_DB_USER") if get_environment_variable(
                "STORAGE_SERVICE_DB_USER") else content["STORAGE_SERVICE_DB_USER"]
            self.STORAGE_SERVICE_DB_PASSWORD = get_environment_variable(
                "STORAGE_SERVICE_DB_PASSWORD") if get_environment_variable("STORAGE_SERVICE_DB_PASSWORD") else content[
                "STORAGE_SERVICE_DB_PASSWORD"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DatabaseConfig()
        return cls._instance

    def convert_to_dictionary(self):
        return {
            "host": self.STORAGE_SERVICE_DB_HOST,
            "port": self.STORAGE_SERVICE_DB_PORT,
            "db": self.STORAGE_SERVICE_DB_NAME,
            "user": self.STORAGE_SERVICE_DB_USER,
            "password": self.STORAGE_SERVICE_DB_PASSWORD
        }

    def get_connection_url(self):
        return f"mysql://" \
               f"{self.STORAGE_SERVICE_DB_USER}:{self.STORAGE_SERVICE_DB_PASSWORD}" \
               f"@" \
               f"{self.STORAGE_SERVICE_DB_HOST}:{self.STORAGE_SERVICE_DB_PORT}" \
               f"/" \
               f"{self.STORAGE_SERVICE_DB_NAME}"
