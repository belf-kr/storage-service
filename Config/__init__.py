from .ApplicationConfig import ApplicationConfig
from .DatabaseConfig import DatabaseConfig
from .UploadConfig import UploadConfig

app = ApplicationConfig.get_instance()
db = DatabaseConfig.get_instance()
upload = UploadConfig.get_instance()
