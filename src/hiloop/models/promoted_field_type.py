from enum import Enum


class PromotedFieldType(str, Enum):
    PROMOTED_TYPE_BOOL = "PROMOTED_TYPE_BOOL"
    PROMOTED_TYPE_F64 = "PROMOTED_TYPE_F64"
    PROMOTED_TYPE_I64 = "PROMOTED_TYPE_I64"
    PROMOTED_TYPE_STR = "PROMOTED_TYPE_STR"
    PROMOTED_TYPE_UNSPECIFIED = "PROMOTED_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
