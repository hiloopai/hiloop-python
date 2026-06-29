from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        id (str | Unset):
        tenant_id (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        kind (str | Unset):
        state (str | Unset):
        result_json (str | Unset):
        error_json (str | Unset):
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    kind: str | Unset = UNSET
    state: str | Unset = UNSET
    result_json: str | Unset = UNSET
    error_json: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        resource_type = self.resource_type

        resource_id = self.resource_id

        kind = self.kind

        state = self.state

        result_json = self.result_json

        error_json = self.error_json

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if state is not UNSET:
            field_dict["state"] = state
        if result_json is not UNSET:
            field_dict["resultJson"] = result_json
        if error_json is not UNSET:
            field_dict["errorJson"] = error_json

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        kind = d.pop("kind", UNSET)

        state = d.pop("state", UNSET)

        result_json = d.pop("resultJson", UNSET)

        error_json = d.pop("errorJson", UNSET)

        operation = cls(
            id=id,
            tenant_id=tenant_id,
            resource_type=resource_type,
            resource_id=resource_id,
            kind=kind,
            state=state,
            result_json=result_json,
            error_json=error_json,
        )

        operation.additional_properties = d
        return operation

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
