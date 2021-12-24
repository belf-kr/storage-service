import json
from os import getenv

from Common import path


class OAuthConfig:
    _instance = None

    def __init__(self):
        super().__init__()
        stage = getenv("STAGES")

        self.HTTP = "http"

        with open(path.APP_CONFIG_ABS_PATH, "r") as json_file:
            content = json.load(json_file)

            self.IS_DOCKER = content["STORAGE_SERVICE_IS_USING_DOCKER"]

        if stage:
            self.PORT = 8080
            self.URL = f"{self.HTTP}://oauth-server.{stage}.svc.cluster.local:{self.PORT}"
        elif self.IS_DOCKER:
            self.PORT = 3001
            self.URL = f"{self.HTTP}://host.docker.internal:{self.PORT}"
        else:
            self.PORT = 3001
            self.URL = f"{self.HTTP}://localhost:{self.PORT}"

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = OAuthConfig()
        return cls._instance
