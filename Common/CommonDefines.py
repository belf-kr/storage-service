from pathlib import Path
from os import path


class CommonDefines:
    _instance = None

    def __init__(self):
        print("[CommonDefines] __init__")
        super().__init__()

        self.PROJECT_ABS_PATH = path.abspath(Path(__file__).parent.parent.absolute())
        self.CONFIG_ABS_PATH = self.PROJECT_ABS_PATH + "/config.json"

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = CommonDefines()
        return cls._instance
