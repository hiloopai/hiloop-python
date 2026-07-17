from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_error import OperationError


T = TypeVar("T", bound="SandboxOperationSummary")


@_attrs_define
class SandboxOperationSummary:
    """One recent operation on a sandbox, summarized for the describe view.

    Attributes:
        id (str | Unset):
        kind (str | Unset):
        state (str | Unset):
        created_at (str | Unset): When the operation was created (RFC 3339).
        updated_at (str | Unset): When the operation last transitioned (RFC 3339). Equal to created_at until the first
             transition; the completion time once the operation is terminal.
        error (OperationError | Unset): Why an operation failed, when it did.
    """

    id: str | Unset = UNSET
    kind: str | Unset = UNSET
    state: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    error: OperationError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        state = self.state

        created_at = self.created_at

        updated_at = self.updated_at

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if state is not UNSET:
            field_dict["state"] = state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation_error import OperationError

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        state = d.pop("state", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _error = d.pop("error", UNSET)
        error: OperationError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OperationError.from_dict(_error)

        sandbox_operation_summary = cls(
            id=id,
            kind=kind,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            error=error,
        )

        sandbox_operation_summary.additional_properties = d
        return sandbox_operation_summary

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
