from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Identity")


@_attrs_define
class Identity:
    """The caller's identity, as resolved from their credential by the API edge. The API trusts this
    resolved identity; it does not re-authenticate.

       Attributes:
           org_id (str | Unset): x-hiloop-org-id — the organization the caller acts in.
           tenant_id (str | Unset): x-hiloop-tenant-id — the tenant the caller acts in (drives app.tenant_id / RLS
               downstream).
           user_id (str | Unset): x-hiloop-user-id — the user, when the credential is user-scoped; empty for service keys.
           auth_method (str | Unset): x-hiloop-auth-method — how the caller authenticated (e.g. "api_key", "session").
           scope (str | Unset): x-hiloop-scope — the granted scope, when present.
    """

    org_id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    auth_method: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        tenant_id = self.tenant_id

        user_id = self.user_id

        auth_method = self.auth_method

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if auth_method is not UNSET:
            field_dict["authMethod"] = auth_method
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = d.pop("orgId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        user_id = d.pop("userId", UNSET)

        auth_method = d.pop("authMethod", UNSET)

        scope = d.pop("scope", UNSET)

        identity = cls(
            org_id=org_id,
            tenant_id=tenant_id,
            user_id=user_id,
            auth_method=auth_method,
            scope=scope,
        )

        identity.additional_properties = d
        return identity

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
