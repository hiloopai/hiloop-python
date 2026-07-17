from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSandboxSecretRequest")


@_attrs_define
class CreateSandboxSecretRequest:
    """
    Attributes:
        name (str | Unset): The secret name — unique within the caller's tenant.
        kind (str | Unset): The credential kind: `api_key`, `bearer`, `basic`, or `custom`. Empty defaults to `custom`;
             any other value is rejected.
        value (str | Unset): The secret value. WRITE-ONLY: stored encrypted and never returned by this API again; the
            proxy
             resolves it at request time.
        dest_host (str | Unset): The outbound host to inject the value into (optional). Must be a bare DNS hostname,
            e.g.
             `api.openai.com` — not a URL; stored in canonical lowercase form.
        dest_header (str | Unset): The header to inject the value as (optional; defaults by kind).
        scheme (str | Unset): The auth scheme prefix (optional; e.g. `Bearer`).
    """

    name: str | Unset = UNSET
    kind: str | Unset = UNSET
    value: str | Unset = UNSET
    dest_host: str | Unset = UNSET
    dest_header: str | Unset = UNSET
    scheme: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind

        value = self.value

        dest_host = self.dest_host

        dest_header = self.dest_header

        scheme = self.scheme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if value is not UNSET:
            field_dict["value"] = value
        if dest_host is not UNSET:
            field_dict["dest_host"] = dest_host
        if dest_header is not UNSET:
            field_dict["dest_header"] = dest_header
        if scheme is not UNSET:
            field_dict["scheme"] = scheme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        kind = d.pop("kind", UNSET)

        value = d.pop("value", UNSET)

        dest_host = d.pop("dest_host", UNSET)

        dest_header = d.pop("dest_header", UNSET)

        scheme = d.pop("scheme", UNSET)

        create_sandbox_secret_request = cls(
            name=name,
            kind=kind,
            value=value,
            dest_host=dest_host,
            dest_header=dest_header,
            scheme=scheme,
        )

        create_sandbox_secret_request.additional_properties = d
        return create_sandbox_secret_request

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
