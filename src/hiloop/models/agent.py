from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_launch_acl import AgentLaunchAcl


T = TypeVar("T", bound="Agent")


@_attrs_define
class Agent:
    """A registered agent identity, scoped to the caller's tenant.

    Attributes:
        id (str | Unset): The agent's stable id.
        name (str | Unset): The agent's registered name — unique within the tenant, and how the agent is displayed in
             attribution everywhere. Lowercase letters, digits, `.`, `_`, and `-`; must start and end with
             a letter or digit; at most 100 characters.
        description (str | Unset): A free-text description of what the agent is for. May be empty.
        launch_acl (AgentLaunchAcl | Unset): A per-agent launch ACL: which principals may launch a run or sandbox as the
            agent.
        created_by (str | Unset): Stable id of the principal that registered the agent, when recorded.
        created_at (str | Unset): When the agent was registered (RFC 3339).
        updated_at (str | Unset): When the agent's registration or ACL was last changed (RFC 3339).
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    launch_acl: AgentLaunchAcl | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        launch_acl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.launch_acl, Unset):
            launch_acl = self.launch_acl.to_dict()

        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if launch_acl is not UNSET:
            field_dict["launchAcl"] = launch_acl
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_launch_acl import AgentLaunchAcl

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _launch_acl = d.pop("launchAcl", UNSET)
        launch_acl: AgentLaunchAcl | Unset
        if isinstance(_launch_acl, Unset):
            launch_acl = UNSET
        else:
            launch_acl = AgentLaunchAcl.from_dict(_launch_acl)

        created_by = d.pop("createdBy", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        agent = cls(
            id=id,
            name=name,
            description=description,
            launch_acl=launch_acl,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        agent.additional_properties = d
        return agent

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
