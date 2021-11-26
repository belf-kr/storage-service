from .ApplicationConfig import ApplicationConfig
from .DatabaseConfig import DatabaseConfig
from .UploadConfig import UploadConfig
from .OAuthConfig import OAuthConfig

app = ApplicationConfig.get_instance()
db = DatabaseConfig.get_instance()
upload = UploadConfig.get_instance()
oauth = OAuthConfig.get_instance()