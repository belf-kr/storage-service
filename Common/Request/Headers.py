from enum import unique, Enum


@unique
class Headers(Enum):
    AUTHORIZATION = 'Authorization'
    CONTENT_LENGTH = 'content-length'
    CONTENT_TYPE = 'content-type'
    LOCATION = 'Location'
    ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"

    def str(self):
        return self.value
