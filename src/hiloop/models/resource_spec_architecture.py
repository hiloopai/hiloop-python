from enum import Enum


class ResourceSpecArchitecture(str, Enum):
    ARCHITECTURE_AARCH64 = "ARCHITECTURE_AARCH64"
    ARCHITECTURE_UNSPECIFIED = "ARCHITECTURE_UNSPECIFIED"
    ARCHITECTURE_X86_64 = "ARCHITECTURE_X86_64"

    def __str__(self) -> str:
        return str(self.value)
