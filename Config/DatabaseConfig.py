from Config.BaseConfig import BaseConfig
import json


class DatabaseConfig(BaseConfig):
    _instance = None

    def __init__(self):
        super().__init__()

        with open(BaseConfig.get_instance().DB_CONFIG_PATH, "r") as f:
            content = json.load(f)
            self.HOST = content["HOST"]
            self.PORT = content["PORT"]
            self.DB = content["DB"]
            self.USER = content["USER"]
            self.PASSWORD = content["PASSWORD"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DatabaseConfig()
        return cls._instance

    def convert_to_dictionary(self):
        return {
            "host": self.HOST,
            "port": self.PORT,
            "db": self.DB,
            "user": self.USER,
            "password": self.PASSWORD
        }

    def get_connection_url(self):
        return f"mysql://" \
               f"{self.USER}:{self.PASSWORD}" \
               f"@" \
               f"{self.HOST}:{self.PORT}" \
               f"/" \
               f"{self.DB}"
