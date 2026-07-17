from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_attempt_error import OperationAttemptError


T = TypeVar("T", bound="OperationError")


@_attrs_define
class OperationError:
    """Why an operation failed, when it did.

    Attributes:
        code (str | Unset): Stable machine-readable failure class (for example runtime_unavailable or
             operation_conflict).
        message (str | Unset): Human-readable description of the failure.
        last_attempt (OperationAttemptError | Unset): One failed, retried attempt's cause on an operation that later
            ended without succeeding.
    """

    code: str | Unset = UNSET
    message: str | Unset = UNSET
    last_attempt: OperationAttemptError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        last_attempt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_attempt, Unset):
            last_attempt = self.last_attempt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if last_attempt is not UNSET:
            field_dict["last_attempt"] = last_attempt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation_attempt_error import OperationAttemptError

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        _last_attempt = d.pop("last_attempt", UNSET)
        last_attempt: OperationAttemptError | Unset
        if isinstance(_last_attempt, Unset):
            last_attempt = UNSET
        else:
            last_attempt = OperationAttemptError.from_dict(_last_attempt)

        operation_error = cls(
            code=code,
            message=message,
            last_attempt=last_attempt,
        )

        operation_error.additional_properties = d
        return operation_error

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
