from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeBlobUpload")


@_attrs_define
class VolumeBlobUpload:
    """The upload decision for one requested blob.

    Attributes:
        digest (str | Unset): The blob's content digest, echoed from the request.
        present (bool | Unset): True when the blob already exists in the volume store — skip the upload; content is
             deduplicated by digest.
        upload_url (str | Unset): Short-lived pre-authorized URL to PUT the blob's bytes to. Empty when `present` is
            true. The
             URL is bound to the blob's content-addressed location; the request needs no additional
             credentials.
    """

    digest: str | Unset = UNSET
    present: bool | Unset = UNSET
    upload_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digest = self.digest

        present = self.present

        upload_url = self.upload_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if present is not UNSET:
            field_dict["present"] = present
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        digest = d.pop("digest", UNSET)

        present = d.pop("present", UNSET)

        upload_url = d.pop("upload_url", UNSET)

        volume_blob_upload = cls(
            digest=digest,
            present=present,
            upload_url=upload_url,
        )

        volume_blob_upload.additional_properties = d
        return volume_blob_upload

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
