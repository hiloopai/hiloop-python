from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_artifact_image import BuildArtifactImage
    from ..models.oci_image import OciImage
    from ..models.provider_native_image import ProviderNativeImage


T = TypeVar("T", bound="SandboxImage")


@_attrs_define
class SandboxImage:
    """
    Attributes:
        oci (OciImage | Unset):
        build_artifact (BuildArtifactImage | Unset):
        provider_native (ProviderNativeImage | Unset): Opaque image reference interpreted by the selected runtime
            adapter.
    """

    oci: OciImage | Unset = UNSET
    build_artifact: BuildArtifactImage | Unset = UNSET
    provider_native: ProviderNativeImage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oci: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oci, Unset):
            oci = self.oci.to_dict()

        build_artifact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build_artifact, Unset):
            build_artifact = self.build_artifact.to_dict()

        provider_native: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_native, Unset):
            provider_native = self.provider_native.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oci is not UNSET:
            field_dict["oci"] = oci
        if build_artifact is not UNSET:
            field_dict["buildArtifact"] = build_artifact
        if provider_native is not UNSET:
            field_dict["providerNative"] = provider_native

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_artifact_image import BuildArtifactImage
        from ..models.oci_image import OciImage
        from ..models.provider_native_image import ProviderNativeImage

        d = dict(src_dict)
        _oci = d.pop("oci", UNSET)
        oci: OciImage | Unset
        if isinstance(_oci, Unset):
            oci = UNSET
        else:
            oci = OciImage.from_dict(_oci)

        _build_artifact = d.pop("buildArtifact", UNSET)
        build_artifact: BuildArtifactImage | Unset
        if isinstance(_build_artifact, Unset):
            build_artifact = UNSET
        else:
            build_artifact = BuildArtifactImage.from_dict(_build_artifact)

        _provider_native = d.pop("providerNative", UNSET)
        provider_native: ProviderNativeImage | Unset
        if isinstance(_provider_native, Unset):
            provider_native = UNSET
        else:
            provider_native = ProviderNativeImage.from_dict(_provider_native)

        sandbox_image = cls(
            oci=oci,
            build_artifact=build_artifact,
            provider_native=provider_native,
        )

        sandbox_image.additional_properties = d
        return sandbox_image

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
