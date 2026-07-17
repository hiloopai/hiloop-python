from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartVolumePushResponse")


@_attrs_define
class StartVolumePushResponse:
    """
    Attributes:
        push_id (str | Unset): The push handle. Pass it to PublishVolumeVersion once the manifest and all content blobs
            are
             uploaded.
        manifest_upload_url (str | Unset): Short-lived pre-authorized URL to PUT the manifest (the JSON file listing:
            per file its path,
             mode, size, content digest, and chunk list) to. The URL is bound to this push's staging
             location; the request needs no additional credentials.
        expires_in_seconds (int | Unset): How long the upload URL stays valid, in seconds.
        max_manifest_bytes (str | Unset): The largest manifest the server accepts for this push, in bytes.
    """

    push_id: str | Unset = UNSET
    manifest_upload_url: str | Unset = UNSET
    expires_in_seconds: int | Unset = UNSET
    max_manifest_bytes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        push_id = self.push_id

        manifest_upload_url = self.manifest_upload_url

        expires_in_seconds = self.expires_in_seconds

        max_manifest_bytes = self.max_manifest_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if push_id is not UNSET:
            field_dict["push_id"] = push_id
        if manifest_upload_url is not UNSET:
            field_dict["manifest_upload_url"] = manifest_upload_url
        if expires_in_seconds is not UNSET:
            field_dict["expires_in_seconds"] = expires_in_seconds
        if max_manifest_bytes is not UNSET:
            field_dict["max_manifest_bytes"] = max_manifest_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        push_id = d.pop("push_id", UNSET)

        manifest_upload_url = d.pop("manifest_upload_url", UNSET)

        expires_in_seconds = d.pop("expires_in_seconds", UNSET)

        max_manifest_bytes = d.pop("max_manifest_bytes", UNSET)

        start_volume_push_response = cls(
            push_id=push_id,
            manifest_upload_url=manifest_upload_url,
            expires_in_seconds=expires_in_seconds,
            max_manifest_bytes=max_manifest_bytes,
        )

        start_volume_push_response.additional_properties = d
        return start_volume_push_response

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
