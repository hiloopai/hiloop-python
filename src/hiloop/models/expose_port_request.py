from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expose_port_request_auth_mode import ExposePortRequestAuthMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExposePortRequest")


@_attrs_define
class ExposePortRequest:
    """
    Attributes:
        sandbox_id (str | Unset):
        port (int | Unset):
        auth_mode (ExposePortRequestAuthMode | Unset): Defaults to token authentication. Public mode is reserved and
            rejected in v1.
    """

    sandbox_id: str | Unset = UNSET
    port: int | Unset = UNSET
    auth_mode: ExposePortRequestAuthMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        port = self.port

        auth_mode: str | Unset = UNSET
        if not isinstance(self.auth_mode, Unset):
            auth_mode = self.auth_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if port is not UNSET:
            field_dict["port"] = port
        if auth_mode is not UNSET:
            field_dict["auth_mode"] = auth_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id", UNSET)

        port = d.pop("port", UNSET)

        _auth_mode = d.pop("auth_mode", UNSET)
        auth_mode: ExposePortRequestAuthMode | Unset
        if isinstance(_auth_mode, Unset):
            auth_mode = UNSET
        else:
            auth_mode = ExposePortRequestAuthMode(_auth_mode)

        expose_port_request = cls(
            sandbox_id=sandbox_id,
            port=port,
            auth_mode=auth_mode,
        )

        expose_port_request.additional_properties = d
        return expose_port_request

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
