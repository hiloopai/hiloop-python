from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.port_exposure_auth_mode import PortExposureAuthMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PortExposure")


@_attrs_define
class PortExposure:
    """Public-safe metadata for one exposed sandbox port. Tokens and their stored digests never appear
    on list/read surfaces.

       Attributes:
           sandbox_id (str | Unset):
           port (int | Unset):
           auth_mode (PortExposureAuthMode | Unset):
           url (str | Unset):
           created_at (str | Unset): When this token generation was created (RFC 3339).
    """

    sandbox_id: str | Unset = UNSET
    port: int | Unset = UNSET
    auth_mode: PortExposureAuthMode | Unset = UNSET
    url: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        port = self.port

        auth_mode: str | Unset = UNSET
        if not isinstance(self.auth_mode, Unset):
            auth_mode = self.auth_mode.value

        url = self.url

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if port is not UNSET:
            field_dict["port"] = port
        if auth_mode is not UNSET:
            field_dict["auth_mode"] = auth_mode
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id", UNSET)

        port = d.pop("port", UNSET)

        _auth_mode = d.pop("auth_mode", UNSET)
        auth_mode: PortExposureAuthMode | Unset
        if isinstance(_auth_mode, Unset):
            auth_mode = UNSET
        else:
            auth_mode = PortExposureAuthMode(_auth_mode)

        url = d.pop("url", UNSET)

        created_at = d.pop("created_at", UNSET)

        port_exposure = cls(
            sandbox_id=sandbox_id,
            port=port,
            auth_mode=auth_mode,
            url=url,
            created_at=created_at,
        )

        port_exposure.additional_properties = d
        return port_exposure

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
