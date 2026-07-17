from enum import Enum


class CreateSandboxRequestNetworkMode(str, Enum):
    NETWORK_MODE_NONE = "NETWORK_MODE_NONE"
    NETWORK_MODE_SANDBOX = "NETWORK_MODE_SANDBOX"
    NETWORK_MODE_UNSPECIFIED = "NETWORK_MODE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
