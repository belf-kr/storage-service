import json

from Common.CommonDefines import CommonDefines


class CommonPath:
    _instance = None

    def __init__(self):
        with open(CommonDefines.get_instance().CONFIG_ABS_PATH, "r") as json_file:
            content = json.load(json_file)
            self.common_defines = CommonDefines.get_instance()
            self.DB_CONFIG_ABS_PATH = self.common_defines.PROJECT_ABS_PATH + "/" + content["DB_CONFIG_PATH"]
            self.APP_CONFIG_ABS_PATH = self.common_defines.PROJECT_ABS_PATH + "/" + content["APP_CONFIG_PATH"]

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = CommonPath()
        return cls._instance
