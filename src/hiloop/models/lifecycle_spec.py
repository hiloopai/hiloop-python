from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LifecycleSpec")


@_attrs_define
class LifecycleSpec:
    """Sandbox lifecycle policy: two independent clocks, matching how the completion sweep and the
    lifetime reaper enforce them. This intentionally exposes only the two expiry controls needed by
    public callers; process defaults, environment, and user remain server-managed.

       Attributes:
           lease_secs (str | Unset): Absolute max sandbox lifetime in seconds, regardless of activity — the honest upper
               bound on a
                one-shot `sandbox run` command (default 86400s/24h when omitted) and an opt-in hard cap on a plain
                interactive sandbox (no default cap: an actively-used sandbox may run indefinitely). Nonzero
                values must be between 60 and 86400 (24h) inclusive; zero/omitted uses the pattern's server
                default.
           idle_timeout_secs (str | Unset): Idle timeout in seconds: how long the sandbox may go without activity before
               the lifetime reaper
                stops it. Nonzero values must be between 60 and 86400 inclusive; zero/omitted uses the server
                default (1800s/30min).
    """

    lease_secs: str | Unset = UNSET
    idle_timeout_secs: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lease_secs = self.lease_secs

        idle_timeout_secs = self.idle_timeout_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lease_secs is not UNSET:
            field_dict["lease_secs"] = lease_secs
        if idle_timeout_secs is not UNSET:
            field_dict["idle_timeout_secs"] = idle_timeout_secs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lease_secs = d.pop("lease_secs", UNSET)

        idle_timeout_secs = d.pop("idle_timeout_secs", UNSET)

        lifecycle_spec = cls(
            lease_secs=lease_secs,
            idle_timeout_secs=idle_timeout_secs,
        )

        lifecycle_spec.additional_properties = d
        return lifecycle_spec

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
