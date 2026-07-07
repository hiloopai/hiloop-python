from enum import Enum


class AgentLaunchAclPolicy(str, Enum):
    AGENT_LAUNCH_POLICY_MEMBERS = "AGENT_LAUNCH_POLICY_MEMBERS"
    AGENT_LAUNCH_POLICY_RESTRICTED = "AGENT_LAUNCH_POLICY_RESTRICTED"
    AGENT_LAUNCH_POLICY_UNSPECIFIED = "AGENT_LAUNCH_POLICY_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
