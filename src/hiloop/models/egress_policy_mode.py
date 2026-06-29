from enum import Enum


class EgressPolicyMode(str, Enum):
    EGRESS_MODE_ALLOW = "EGRESS_MODE_ALLOW"
    EGRESS_MODE_DENY = "EGRESS_MODE_DENY"
    EGRESS_MODE_UNSPECIFIED = "EGRESS_MODE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
