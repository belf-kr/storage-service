import pymysql

from Config.Database.DatabaseConfig import DatabaseConfig


class DatabaseManager:
    _instance = None

    def __init__(self):
        self.mysql = pymysql.Connect(
            **DatabaseConfig.get_instance().convert_to_dictionary()
        )

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DatabaseManager()
        return cls._instance


