from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_details import ErrorDetails


T = TypeVar("T", bound="ErrorBody")


@_attrs_define
class ErrorBody:
    """The envelope every hiloop API error returns. Branch on the stable snake_case code, never on message or the HTTP
    status alone. Client errors (4xx) carry the specific code for the failure; server faults return the generic internal
    (or unavailable for a brief overload shed, with a Retry-After header) plus a request_id.

        Attributes:
            code (str): Stable machine-readable error code in snake_case — the field clients branch on. Examples:
                unauthenticated, permission_denied, not_found, invalid_argument, quota_exceeded, rate_limited, unavailable,
                internal.
            message (str): Human-readable description of the error. Informational only — never parse or match on it; its
                wording may change without notice.
            details (ErrorDetails | Unset): Structured detail payloads an error may carry — one member per detail family, so
                clients can branch without parsing the message.
            request_id (str | Unset): Correlation id present on server faults (5xx) — quote it when contacting support to
                locate the failing request. Omitted on client errors.
    """

    code: str
    message: str
    details: ErrorDetails | Unset = UNSET
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_details import ErrorDetails

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: ErrorDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorDetails.from_dict(_details)

        request_id = d.pop("request_id", UNSET)

        error_body = cls(
            code=code,
            message=message,
            details=details,
            request_id=request_id,
        )

        error_body.additional_properties = d
        return error_body

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
