from pathlib import Path
from os.path import exists
from os import mkdir


class CommonDefines:
    _instance = None

    def __init__(self):
        print("[CommonDefines] __init__")
        super().__init__()

        self.PROJECT_ABS_PATH = path.abspath(Path(__file__).parent.parent.absolute())
        self.CONFIG_ABS_PATH = self.PROJECT_ABS_PATH + "/config.json"
        self.UPLOAD_PATH = self.PROJECT_ABS_PATH + "/upload"
        if not exists(self.UPLOAD_PATH):
            mkdir(self.UPLOAD_PATH)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = CommonDefines()
        return cls._instance
