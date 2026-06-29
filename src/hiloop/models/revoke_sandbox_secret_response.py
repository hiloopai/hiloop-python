from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_secret import SandboxSecret


T = TypeVar("T", bound="RevokeSandboxSecretResponse")


@_attrs_define
class RevokeSandboxSecretResponse:
    """
    Attributes:
        secret (SandboxSecret | Unset): A sandbox-secret record — metadata only, never the value.
    """

    secret: SandboxSecret | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_secret import SandboxSecret

        d = dict(src_dict)
        _secret = d.pop("secret", UNSET)
        secret: SandboxSecret | Unset
        if isinstance(_secret, Unset):
            secret = UNSET
        else:
            secret = SandboxSecret.from_dict(_secret)

        revoke_sandbox_secret_response = cls(
            secret=secret,
        )

        revoke_sandbox_secret_response.additional_properties = d
        return revoke_sandbox_secret_response

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
