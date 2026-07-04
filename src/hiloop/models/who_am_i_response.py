from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.principal import Principal
    from ..models.tenant_ref import TenantRef


T = TypeVar("T", bound="WhoAmIResponse")


@_attrs_define
class WhoAmIResponse:
    """
    Attributes:
        principal (Principal | Unset): The acting principal, as resolved from the caller's credential by the API edge.
            The API trusts
             the edge-resolved identity; it does not re-authenticate.
        tenant (TenantRef | Unset): The tenant the caller acts in.
    """

    principal: Principal | Unset = UNSET
    tenant: TenantRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        principal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.principal, Unset):
            principal = self.principal.to_dict()

        tenant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if principal is not UNSET:
            field_dict["principal"] = principal
        if tenant is not UNSET:
            field_dict["tenant"] = tenant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.principal import Principal
        from ..models.tenant_ref import TenantRef

        d = dict(src_dict)
        _principal = d.pop("principal", UNSET)
        principal: Principal | Unset
        if isinstance(_principal, Unset):
            principal = UNSET
        else:
            principal = Principal.from_dict(_principal)

        _tenant = d.pop("tenant", UNSET)
        tenant: TenantRef | Unset
        if isinstance(_tenant, Unset):
            tenant = UNSET
        else:
            tenant = TenantRef.from_dict(_tenant)

        who_am_i_response = cls(
            principal=principal,
            tenant=tenant,
        )

        who_am_i_response.additional_properties = d
        return who_am_i_response

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
