from enum import Enum


class CreateSandboxSecretRequestKind(str, Enum):
    SECRET_KIND_API_KEY = "SECRET_KIND_API_KEY"
    SECRET_KIND_BASIC = "SECRET_KIND_BASIC"
    SECRET_KIND_BEARER = "SECRET_KIND_BEARER"
    SECRET_KIND_CUSTOM = "SECRET_KIND_CUSTOM"
    SECRET_KIND_UNSPECIFIED = "SECRET_KIND_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
