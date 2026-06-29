from enum import Enum


class SendExecutionInputRequestSignal(str, Enum):
    EXEC_SIGNAL_EOF = "EXEC_SIGNAL_EOF"
    EXEC_SIGNAL_INTERRUPT = "EXEC_SIGNAL_INTERRUPT"
    EXEC_SIGNAL_KILL = "EXEC_SIGNAL_KILL"
    EXEC_SIGNAL_TERMINATE = "EXEC_SIGNAL_TERMINATE"
    EXEC_SIGNAL_UNSPECIFIED = "EXEC_SIGNAL_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
