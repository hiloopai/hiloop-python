from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Snapshot")


@_attrs_define
class Snapshot:
    """
    Attributes:
        id (str | Unset):
        tenant_id (str | Unset):
        project_id (str | Unset):
        source_sandbox_id (str | Unset):
        status (str | Unset):
        requested_semantics_json (str | Unset):
        effective_semantics_json (str | Unset):
        size_bytes (str | Unset):
        legal_hold (bool | Unset):
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    source_sandbox_id: str | Unset = UNSET
    status: str | Unset = UNSET
    requested_semantics_json: str | Unset = UNSET
    effective_semantics_json: str | Unset = UNSET
    size_bytes: str | Unset = UNSET
    legal_hold: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        project_id = self.project_id

        source_sandbox_id = self.source_sandbox_id

        status = self.status

        requested_semantics_json = self.requested_semantics_json

        effective_semantics_json = self.effective_semantics_json

        size_bytes = self.size_bytes

        legal_hold = self.legal_hold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if source_sandbox_id is not UNSET:
            field_dict["sourceSandboxId"] = source_sandbox_id
        if status is not UNSET:
            field_dict["status"] = status
        if requested_semantics_json is not UNSET:
            field_dict["requestedSemanticsJson"] = requested_semantics_json
        if effective_semantics_json is not UNSET:
            field_dict["effectiveSemanticsJson"] = effective_semantics_json
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if legal_hold is not UNSET:
            field_dict["legalHold"] = legal_hold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        project_id = d.pop("projectId", UNSET)

        source_sandbox_id = d.pop("sourceSandboxId", UNSET)

        status = d.pop("status", UNSET)

        requested_semantics_json = d.pop("requestedSemanticsJson", UNSET)

        effective_semantics_json = d.pop("effectiveSemanticsJson", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        legal_hold = d.pop("legalHold", UNSET)

        snapshot = cls(
            id=id,
            tenant_id=tenant_id,
            project_id=project_id,
            source_sandbox_id=source_sandbox_id,
            status=status,
            requested_semantics_json=requested_semantics_json,
            effective_semantics_json=effective_semantics_json,
            size_bytes=size_bytes,
            legal_hold=legal_hold,
        )

        snapshot.additional_properties = d
        return snapshot

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
