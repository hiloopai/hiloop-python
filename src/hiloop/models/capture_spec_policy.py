from enum import Enum


class CaptureSpecPolicy(str, Enum):
    CAPTURE_POLICY_DISABLED = "CAPTURE_POLICY_DISABLED"
    CAPTURE_POLICY_ENABLED = "CAPTURE_POLICY_ENABLED"
    CAPTURE_POLICY_UNSPECIFIED = "CAPTURE_POLICY_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
