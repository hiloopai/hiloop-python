from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretBinding")


@_attrs_define
class SecretBinding:
    """Declares a stored sandbox secret and its intended outbound target. A non-empty binding requires
    native secret_injection at admission. Current production cells do not advertise that capability,
    so the request fails closed until lease-bound cell hydration is available.

       Attributes:
           name (str | Unset): Name of the stored sandbox secret to resolve.
           env (str | Unset): Reserved placeholder environment-variable name for a runtime with native injection.
           bind (str | Unset): Intended outbound target for a runtime with native injection (e.g. a host or header).
           gen_ai_model (str | Unset): Safe model classification to attach to brokered telemetry.
           tool_call (str | Unset): Safe tool-call classification to attach to brokered telemetry.
           redacted_payload_digest (str | Unset): Digest of a redacted brokered payload artifact.
           redacted_payload_media_type (str | Unset): Media type of a redacted brokered payload artifact.
           redacted_payload_size_bytes (str | Unset): Size of a redacted brokered payload artifact.
    """

    name: str | Unset = UNSET
    env: str | Unset = UNSET
    bind: str | Unset = UNSET
    gen_ai_model: str | Unset = UNSET
    tool_call: str | Unset = UNSET
    redacted_payload_digest: str | Unset = UNSET
    redacted_payload_media_type: str | Unset = UNSET
    redacted_payload_size_bytes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        env = self.env

        bind = self.bind

        gen_ai_model = self.gen_ai_model

        tool_call = self.tool_call

        redacted_payload_digest = self.redacted_payload_digest

        redacted_payload_media_type = self.redacted_payload_media_type

        redacted_payload_size_bytes = self.redacted_payload_size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if env is not UNSET:
            field_dict["env"] = env
        if bind is not UNSET:
            field_dict["bind"] = bind
        if gen_ai_model is not UNSET:
            field_dict["gen_ai_model"] = gen_ai_model
        if tool_call is not UNSET:
            field_dict["tool_call"] = tool_call
        if redacted_payload_digest is not UNSET:
            field_dict["redacted_payload_digest"] = redacted_payload_digest
        if redacted_payload_media_type is not UNSET:
            field_dict["redacted_payload_media_type"] = redacted_payload_media_type
        if redacted_payload_size_bytes is not UNSET:
            field_dict["redacted_payload_size_bytes"] = redacted_payload_size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        env = d.pop("env", UNSET)

        bind = d.pop("bind", UNSET)

        gen_ai_model = d.pop("gen_ai_model", UNSET)

        tool_call = d.pop("tool_call", UNSET)

        redacted_payload_digest = d.pop("redacted_payload_digest", UNSET)

        redacted_payload_media_type = d.pop("redacted_payload_media_type", UNSET)

        redacted_payload_size_bytes = d.pop("redacted_payload_size_bytes", UNSET)

        secret_binding = cls(
            name=name,
            env=env,
            bind=bind,
            gen_ai_model=gen_ai_model,
            tool_call=tool_call,
            redacted_payload_digest=redacted_payload_digest,
            redacted_payload_media_type=redacted_payload_media_type,
            redacted_payload_size_bytes=redacted_payload_size_bytes,
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
