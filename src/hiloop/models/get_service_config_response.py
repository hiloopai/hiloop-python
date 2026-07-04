from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetServiceConfigResponse")


@_attrs_define
class GetServiceConfigResponse:
    """
    Attributes:
        telemetry_endpoint (str | Unset): Client-visible telemetry gRPC endpoint.
        secret_broker_url (str | Unset): Client-visible sandbox-secret broker resolve URL.
        login_url (str | Unset): API URL used to start the browser login flow.
        device_activation_url (str | Unset): Web console URL used to activate an RFC 8628 device-code login.
    """

    telemetry_endpoint: str | Unset = UNSET
    secret_broker_url: str | Unset = UNSET
    login_url: str | Unset = UNSET
    device_activation_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        telemetry_endpoint = self.telemetry_endpoint

        secret_broker_url = self.secret_broker_url

        login_url = self.login_url

        device_activation_url = self.device_activation_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if telemetry_endpoint is not UNSET:
            field_dict["telemetryEndpoint"] = telemetry_endpoint
        if secret_broker_url is not UNSET:
            field_dict["secretBrokerUrl"] = secret_broker_url
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if device_activation_url is not UNSET:
            field_dict["deviceActivationUrl"] = device_activation_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        telemetry_endpoint = d.pop("telemetryEndpoint", UNSET)

        secret_broker_url = d.pop("secretBrokerUrl", UNSET)

        login_url = d.pop("loginUrl", UNSET)

        device_activation_url = d.pop("deviceActivationUrl", UNSET)

        get_service_config_response = cls(
            telemetry_endpoint=telemetry_endpoint,
            secret_broker_url=secret_broker_url,
            login_url=login_url,
            device_activation_url=device_activation_url,
        )

        get_service_config_response.additional_properties = d
        return get_service_config_response

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
