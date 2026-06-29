from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sandbox")


@_attrs_define
class Sandbox:
    """
    Attributes:
        id (str | Unset):
        tenant_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset):
        desired_state (str | Unset):
        observed_state (str | Unset):
        active_generation (str | Unset):
        version (str | Unset):
        fork_node_id (str | Unset): Fork-tree node that represents this sandbox as a fork source. Present for project-
            backed
             sandboxes; absent project-less sandboxes are not fork sources.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    desired_state: str | Unset = UNSET
    observed_state: str | Unset = UNSET
    active_generation: str | Unset = UNSET
    version: str | Unset = UNSET
    fork_node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        project_id = self.project_id

        name = self.name

        desired_state = self.desired_state

        observed_state = self.observed_state

        active_generation = self.active_generation

        version = self.version

        fork_node_id = self.fork_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if desired_state is not UNSET:
            field_dict["desiredState"] = desired_state
        if observed_state is not UNSET:
            field_dict["observedState"] = observed_state
        if active_generation is not UNSET:
            field_dict["activeGeneration"] = active_generation
        if version is not UNSET:
            field_dict["version"] = version
        if fork_node_id is not UNSET:
            field_dict["forkNodeId"] = fork_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        project_id = d.pop("projectId", UNSET)

        name = d.pop("name", UNSET)

        desired_state = d.pop("desiredState", UNSET)

        observed_state = d.pop("observedState", UNSET)

        active_generation = d.pop("activeGeneration", UNSET)

        version = d.pop("version", UNSET)

        fork_node_id = d.pop("forkNodeId", UNSET)

        sandbox = cls(
            id=id,
            tenant_id=tenant_id,
            project_id=project_id,
            name=name,
            desired_state=desired_state,
            observed_state=observed_state,
            active_generation=active_generation,
            version=version,
            fork_node_id=fork_node_id,
        )

        sandbox.additional_properties = d
        return sandbox

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
