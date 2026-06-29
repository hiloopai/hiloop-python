from enum import Enum


class FilterOp(str, Enum):
    FILTER_OP_CONTAINS = "FILTER_OP_CONTAINS"
    FILTER_OP_EQ = "FILTER_OP_EQ"
    FILTER_OP_EXISTS = "FILTER_OP_EXISTS"
    FILTER_OP_GT = "FILTER_OP_GT"
    FILTER_OP_GTE = "FILTER_OP_GTE"
    FILTER_OP_LT = "FILTER_OP_LT"
    FILTER_OP_LTE = "FILTER_OP_LTE"
    FILTER_OP_NE = "FILTER_OP_NE"
    FILTER_OP_UNSPECIFIED = "FILTER_OP_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
