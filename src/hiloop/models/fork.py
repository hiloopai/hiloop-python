from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Fork")


@_attrs_define
class Fork:
    """Retained wire type for retired fork compatibility RPCs. Clean sandbox-cell deployments do not
    create or return fork records.

       Attributes:
           id (str | Unset):
           tenant_id (str | Unset):
           source_sandbox_id (str | Unset):
           child_sandbox_id (str | Unset):
           implementation (str | Unset):
           effective_semantics_json (str | Unset):
           intermediate_snapshot_id (str | Unset):
           operation_id (str | Unset):
           child_run_id (str | Unset): The child run this fork created.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    source_sandbox_id: str | Unset = UNSET
    child_sandbox_id: str | Unset = UNSET
    implementation: str | Unset = UNSET
    effective_semantics_json: str | Unset = UNSET
    intermediate_snapshot_id: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    child_run_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        source_sandbox_id = self.source_sandbox_id

        child_sandbox_id = self.child_sandbox_id

        implementation = self.implementation

        effective_semantics_json = self.effective_semantics_json

        intermediate_snapshot_id = self.intermediate_snapshot_id

        operation_id = self.operation_id

        child_run_id = self.child_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if source_sandbox_id is not UNSET:
            field_dict["source_sandbox_id"] = source_sandbox_id
        if child_sandbox_id is not UNSET:
            field_dict["child_sandbox_id"] = child_sandbox_id
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if effective_semantics_json is not UNSET:
            field_dict["effective_semantics_json"] = effective_semantics_json
        if intermediate_snapshot_id is not UNSET:
            field_dict["intermediate_snapshot_id"] = intermediate_snapshot_id
        if operation_id is not UNSET:
            field_dict["operation_id"] = operation_id
        if child_run_id is not UNSET:
            field_dict["child_run_id"] = child_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        source_sandbox_id = d.pop("source_sandbox_id", UNSET)

        child_sandbox_id = d.pop("child_sandbox_id", UNSET)

        implementation = d.pop("implementation", UNSET)

        effective_semantics_json = d.pop("effective_semantics_json", UNSET)

        intermediate_snapshot_id = d.pop("intermediate_snapshot_id", UNSET)

        operation_id = d.pop("operation_id", UNSET)

        child_run_id = d.pop("child_run_id", UNSET)

        fork = cls(
            id=id,
            tenant_id=tenant_id,
            source_sandbox_id=source_sandbox_id,
            child_sandbox_id=child_sandbox_id,
            implementation=implementation,
            effective_semantics_json=effective_semantics_json,
            intermediate_snapshot_id=intermediate_snapshot_id,
            operation_id=operation_id,
            child_run_id=child_run_id,
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
