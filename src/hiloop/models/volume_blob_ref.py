from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeBlobRef")


@_attrs_define
class VolumeBlobRef:
    """One content blob (a whole small file, or one chunk of a larger file) the client intends to
    upload, identified by its digest.

       Attributes:
           digest (str | Unset): The blob's content digest (`blake3:<hex>`).
           size_bytes (str | Unset): The blob's exact size in bytes. Verified against the stored object before a version
                referencing the blob can be published.
    """

    digest: str | Unset = UNSET
    size_bytes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digest = self.digest

        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        digest = d.pop("digest", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        volume_blob_ref = cls(
            digest=digest,
            size_bytes=size_bytes,
        )

        volume_blob_ref.additional_properties = d
        return volume_blob_ref

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
