from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_launch_acl_policy import AgentLaunchAclPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentLaunchAcl")


@_attrs_define
class AgentLaunchAcl:
    """A per-agent launch ACL: which principals may launch a run or sandbox as the agent.

    Attributes:
        policy (AgentLaunchAclPolicy | Unset): The launch policy: open to all tenant members, or restricted to the
            listed users.
        user_ids (list[str] | Unset): The user ids allowed to launch as this agent. Meaningful only when the policy is
             AGENT_LAUNCH_POLICY_RESTRICTED; empty otherwise.
    """

    policy: AgentLaunchAclPolicy | Unset = UNSET
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: AgentLaunchAclPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = AgentLaunchAclPolicy(_policy)

        user_ids = cast(list[str], d.pop("userIds", UNSET))

        agent_launch_acl = cls(
            policy=policy,
            user_ids=user_ids,
        )

        agent_launch_acl.additional_properties = d
        return agent_launch_acl

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
