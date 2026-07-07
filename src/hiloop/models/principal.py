from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Principal")


@_attrs_define
class Principal:
    """The acting principal, as resolved from the caller's credential by the API edge. The API trusts
    the edge-resolved identity; it does not re-authenticate.

       Attributes:
           kind (str | Unset): The kind of principal: "user" (a human identity), "service_account" (a machine credential
                not bound to a user), or "agent" (a credential bound to a registered agent identity).
           id (str | Unset): The principal's stable id: the user's id for a user, the API key's id for a service account
                or an agent.
           email (str | Unset): The user's primary email. Empty for a service-account or agent principal.
           key_id (str | Unset): The presented API key's id. Empty for a browser-session login (no key is involved).
           key_name (str | Unset): The presented API key's name — how this principal is displayed in listings and
               attribution.
                Empty for a browser-session login.
           agent_name (str | Unset): The bound agent's registered name — how an agent principal is displayed in listings
               and
                attribution. Empty unless the presented credential is bound to a registered agent.
    """

    kind: str | Unset = UNSET
    id: str | Unset = UNSET
    email: str | Unset = UNSET
    key_id: str | Unset = UNSET
    key_name: str | Unset = UNSET
    agent_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        id = self.id

        email = self.email

        key_id = self.key_id

        key_name = self.key_name

        agent_name = self.agent_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if key_name is not UNSET:
            field_dict["keyName"] = key_name
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        key_id = d.pop("keyId", UNSET)

        key_name = d.pop("keyName", UNSET)

        agent_name = d.pop("agentName", UNSET)

        principal = cls(
            kind=kind,
            id=id,
            email=email,
            key_id=key_id,
            key_name=key_name,
            agent_name=agent_name,
        )

        principal.additional_properties = d
        return principal

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
