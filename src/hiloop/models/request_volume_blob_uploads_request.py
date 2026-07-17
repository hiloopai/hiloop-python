from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_blob_ref import VolumeBlobRef


T = TypeVar("T", bound="RequestVolumeBlobUploadsRequest")


@_attrs_define
class RequestVolumeBlobUploadsRequest:
    """
    Attributes:
        volume_id (str | Unset): The volume the blobs are being pushed for.
        blobs (list[VolumeBlobRef] | Unset): The blobs to upload, at most 512 per request. Repeat the call in batches
            for larger pushes;
             it is read-only on the volume itself, so batches may run concurrently.
    """

    volume_id: str | Unset = UNSET
    blobs: list[VolumeBlobRef] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_id = self.volume_id

        blobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blobs, Unset):
            blobs = []
            for blobs_item_data in self.blobs:
                blobs_item = blobs_item_data.to_dict()
                blobs.append(blobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if blobs is not UNSET:
            field_dict["blobs"] = blobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_blob_ref import VolumeBlobRef

        d = dict(src_dict)
        volume_id = d.pop("volume_id", UNSET)

        _blobs = d.pop("blobs", UNSET)
        blobs: list[VolumeBlobRef] | Unset = UNSET
        if _blobs is not UNSET:
            blobs = []
            for blobs_item_data in _blobs:
                blobs_item = VolumeBlobRef.from_dict(blobs_item_data)

                blobs.append(blobs_item)

        request_volume_blob_uploads_request = cls(
            volume_id=volume_id,
            blobs=blobs,
        )

        request_volume_blob_uploads_request.additional_properties = d
        return request_volume_blob_uploads_request

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
