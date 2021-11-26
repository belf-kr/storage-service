from os import getenv


class OAuthConfig:
    _instance = None

    def __init__(self):
        super().__init__()
        stage = getenv("STAGES")

        self.HTTP = "http"

        if stage:
            self.PORT = 8080
            self.URL = f"{self.HTTP}://oauth-server.{stage}.svc.cluster.local:{self.PORT}"
        else:
            self.PORT = 3001
            self.URL = f"{self.HTTP}://localhost:{self.PORT}"

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = OAuthConfig()
        return cls._instance
