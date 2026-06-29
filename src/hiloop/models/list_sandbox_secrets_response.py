from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_secret import SandboxSecret


T = TypeVar("T", bound="ListSandboxSecretsResponse")


@_attrs_define
class ListSandboxSecretsResponse:
    """
    Attributes:
        secrets (list[SandboxSecret] | Unset): The secrets on this page, newest first — metadata only, never the value.
        next_page_token (str | Unset): The token to pass as page_token to fetch the next page. Empty when there are no
            more results.
    """

    secrets: list[SandboxSecret] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_secret import SandboxSecret

        d = dict(src_dict)
        _secrets = d.pop("secrets", UNSET)
        secrets: list[SandboxSecret] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = SandboxSecret.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_sandbox_secrets_response = cls(
            secrets=secrets,
            next_page_token=next_page_token,
        )

        list_sandbox_secrets_response.additional_properties = d
        return list_sandbox_secrets_response

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
