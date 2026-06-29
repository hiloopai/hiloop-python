from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretBinding")


@_attrs_define
class SecretBinding:
    """Binds a stored sandbox secret to a placeholder the agent sees and the outbound target the value is
    injected into. The agent only ever observes the placeholder; the real value is injected in flight
    and never written into the sandbox environment, disk, snapshot, or captured telemetry.

       Attributes:
           name (str | Unset): Name of the stored sandbox secret to resolve.
           env (str | Unset): Placeholder environment variable the agent sees in place of the value.
           bind (str | Unset): Outbound target the resolved value is injected into (e.g. a host or header).
    """

    name: str | Unset = UNSET
    env: str | Unset = UNSET
    bind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        env = self.env

        bind = self.bind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if env is not UNSET:
            field_dict["env"] = env
        if bind is not UNSET:
            field_dict["bind"] = bind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        env = d.pop("env", UNSET)

        bind = d.pop("bind", UNSET)

        secret_binding = cls(
            name=name,
            env=env,
            bind=bind,
        )

        secret_binding.additional_properties = d
        return secret_binding

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
