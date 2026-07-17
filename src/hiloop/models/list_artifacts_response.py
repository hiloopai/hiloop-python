from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact


T = TypeVar("T", bound="ListArtifactsResponse")


@_attrs_define
class ListArtifactsResponse:
    """
    Attributes:
        artifacts (list[Artifact] | Unset): The artifacts on this page, newest first. Metadata only — an artifact's
            payload rides
             `GET /v1/artifacts/{id}:payload`.
        next_page_token (str | Unset): The token to pass as page_token to fetch the next page. Empty when there are no
            more results.
    """

    artifacts: list[Artifact] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.artifacts, Unset):
            artifacts = []
            for artifacts_item_data in self.artifacts:
                artifacts_item = artifacts_item_data.to_dict()
                artifacts.append(artifacts_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifacts is not UNSET:
            field_dict["artifacts"] = artifacts
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact import Artifact

        d = dict(src_dict)
        _artifacts = d.pop("artifacts", UNSET)
        artifacts: list[Artifact] | Unset = UNSET
        if _artifacts is not UNSET:
            artifacts = []
            for artifacts_item_data in _artifacts:
                artifacts_item = Artifact.from_dict(artifacts_item_data)

                artifacts.append(artifacts_item)

        next_page_token = d.pop("next_page_token", UNSET)

        list_artifacts_response = cls(
            artifacts=artifacts,
            next_page_token=next_page_token,
        )

        list_artifacts_response.additional_properties = d
        return list_artifacts_response

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
