from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_blob_upload import VolumeBlobUpload


T = TypeVar("T", bound="RequestVolumeBlobUploadsResponse")


@_attrs_define
class RequestVolumeBlobUploadsResponse:
    """
    Attributes:
        uploads (list[VolumeBlobUpload] | Unset): One entry per distinct requested digest: either already present, or an
            upload URL.
        expires_in_seconds (int | Unset): How long the returned upload URLs stay valid, in seconds.
    """

    uploads: list[VolumeBlobUpload] | Unset = UNSET
    expires_in_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uploads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.uploads, Unset):
            uploads = []
            for uploads_item_data in self.uploads:
                uploads_item = uploads_item_data.to_dict()
                uploads.append(uploads_item)

        expires_in_seconds = self.expires_in_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uploads is not UNSET:
            field_dict["uploads"] = uploads
        if expires_in_seconds is not UNSET:
            field_dict["expires_in_seconds"] = expires_in_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_blob_upload import VolumeBlobUpload

        d = dict(src_dict)
        _uploads = d.pop("uploads", UNSET)
        uploads: list[VolumeBlobUpload] | Unset = UNSET
        if _uploads is not UNSET:
            uploads = []
            for uploads_item_data in _uploads:
                uploads_item = VolumeBlobUpload.from_dict(uploads_item_data)

                uploads.append(uploads_item)

        expires_in_seconds = d.pop("expires_in_seconds", UNSET)

        request_volume_blob_uploads_response = cls(
            uploads=uploads,
            expires_in_seconds=expires_in_seconds,
        )

        request_volume_blob_uploads_response.additional_properties = d
        return request_volume_blob_uploads_response

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
