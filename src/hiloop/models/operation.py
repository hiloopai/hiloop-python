from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_error import OperationError
    from ..models.operation_result import OperationResult


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
        result (OperationResult | Unset): The typed report of a succeeded operation. The set variant matches the
            operation's kind; kinds
             whose success carries no report (for example a sandbox create or scratch-workspace delete)
             settle with no result.
        error (OperationError | Unset): Why an operation failed, when it did.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    kind: str | Unset = UNSET
    state: str | Unset = UNSET
    result: OperationResult | Unset = UNSET
    error: OperationError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        resource_type = self.resource_type

        resource_id = self.resource_id

        kind = self.kind

        state = self.state

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if state is not UNSET:
            field_dict["state"] = state
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation_error import OperationError
        from ..models.operation_result import OperationResult

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        kind = d.pop("kind", UNSET)

        state = d.pop("state", UNSET)

        _result = d.pop("result", UNSET)
        result: OperationResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = OperationResult.from_dict(_result)

        _error = d.pop("error", UNSET)
        error: OperationError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OperationError.from_dict(_error)

        operation = cls(
            id=id,
            tenant_id=tenant_id,
            resource_type=resource_type,
            resource_id=resource_id,
            kind=kind,
            state=state,
            result=result,
            error=error,
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
