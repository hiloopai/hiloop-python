from enum import Enum


class ExposePortRequestAuthMode(str, Enum):
    PORT_EXPOSURE_AUTH_MODE_PUBLIC = "PORT_EXPOSURE_AUTH_MODE_PUBLIC"
    PORT_EXPOSURE_AUTH_MODE_TOKEN = "PORT_EXPOSURE_AUTH_MODE_TOKEN"
    PORT_EXPOSURE_AUTH_MODE_UNSPECIFIED = "PORT_EXPOSURE_AUTH_MODE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
