from Common.CommonPath import CommonPath


class BaseConfig:

    _instance = None

    def __init__(self):
        print("[BaseConfig] __init__")
        self.COMMON_PATH = CommonPath.get_instance()
        self.DB_CONFIG_PATH = self.COMMON_PATH.DB_CONFIG_ABS_PATH
        self.APP_CONFIG_PATH = self.COMMON_PATH.APP_CONFIG_ABS_PATH

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = BaseConfig()
        return cls._instance

