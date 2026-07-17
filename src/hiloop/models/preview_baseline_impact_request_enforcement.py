from enum import Enum


class PreviewBaselineImpactRequestEnforcement(str, Enum):
    EGRESS_ENFORCEMENT_BLOCK = "EGRESS_ENFORCEMENT_BLOCK"
    EGRESS_ENFORCEMENT_UNSPECIFIED = "EGRESS_ENFORCEMENT_UNSPECIFIED"
    EGRESS_ENFORCEMENT_WARN = "EGRESS_ENFORCEMENT_WARN"

    def __str__(self) -> str:
        return str(self.value)
