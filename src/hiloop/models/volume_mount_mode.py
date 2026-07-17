from enum import Enum


class VolumeMountMode(str, Enum):
    VOLUME_MODE_RO = "VOLUME_MODE_RO"
    VOLUME_MODE_RW = "VOLUME_MODE_RW"
    VOLUME_MODE_UNSPECIFIED = "VOLUME_MODE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
