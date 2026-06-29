from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Fork")


@_attrs_define
class Fork:
    """
    Attributes:
        id (str | Unset):
        tenant_id (str | Unset):
        source_sandbox_id (str | Unset):
        source_snapshot_id (str | Unset):
        child_sandbox_id (str | Unset):
        fork_node_id (str | Unset):
        implementation (str | Unset):
        effective_semantics_json (str | Unset):
        intermediate_snapshot_id (str | Unset):
        operation_id (str | Unset):
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    source_sandbox_id: str | Unset = UNSET
    source_snapshot_id: str | Unset = UNSET
    child_sandbox_id: str | Unset = UNSET
    fork_node_id: str | Unset = UNSET
    implementation: str | Unset = UNSET
    effective_semantics_json: str | Unset = UNSET
    intermediate_snapshot_id: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        source_sandbox_id = self.source_sandbox_id

        source_snapshot_id = self.source_snapshot_id

        child_sandbox_id = self.child_sandbox_id

        fork_node_id = self.fork_node_id

        implementation = self.implementation

        effective_semantics_json = self.effective_semantics_json

        intermediate_snapshot_id = self.intermediate_snapshot_id

        operation_id = self.operation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if source_sandbox_id is not UNSET:
            field_dict["sourceSandboxId"] = source_sandbox_id
        if source_snapshot_id is not UNSET:
            field_dict["sourceSnapshotId"] = source_snapshot_id
        if child_sandbox_id is not UNSET:
            field_dict["childSandboxId"] = child_sandbox_id
        if fork_node_id is not UNSET:
            field_dict["forkNodeId"] = fork_node_id
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if effective_semantics_json is not UNSET:
            field_dict["effectiveSemanticsJson"] = effective_semantics_json
        if intermediate_snapshot_id is not UNSET:
            field_dict["intermediateSnapshotId"] = intermediate_snapshot_id
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        source_sandbox_id = d.pop("sourceSandboxId", UNSET)

        source_snapshot_id = d.pop("sourceSnapshotId", UNSET)

        child_sandbox_id = d.pop("childSandboxId", UNSET)

        fork_node_id = d.pop("forkNodeId", UNSET)

        implementation = d.pop("implementation", UNSET)

        effective_semantics_json = d.pop("effectiveSemanticsJson", UNSET)

        intermediate_snapshot_id = d.pop("intermediateSnapshotId", UNSET)

        operation_id = d.pop("operationId", UNSET)

        fork = cls(
            id=id,
            tenant_id=tenant_id,
            source_sandbox_id=source_sandbox_id,
            source_snapshot_id=source_snapshot_id,
            child_sandbox_id=child_sandbox_id,
            fork_node_id=fork_node_id,
            implementation=implementation,
            effective_semantics_json=effective_semantics_json,
            intermediate_snapshot_id=intermediate_snapshot_id,
            operation_id=operation_id,
        )

        fork.additional_properties = d
        return fork

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
