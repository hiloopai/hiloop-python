from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_series_point import UsageSeriesPoint


T = TypeVar("T", bound="GetUsageSeriesResponse")


@_attrs_define
class GetUsageSeriesResponse:
    """
    Attributes:
        points (list[UsageSeriesPoint] | Unset): The ordered, contiguous time buckets covering the requested window.
    """

    points: list[UsageSeriesPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_series_point import UsageSeriesPoint

        d = dict(src_dict)
        _points = d.pop("points", UNSET)
        points: list[UsageSeriesPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = UsageSeriesPoint.from_dict(points_item_data)

                points.append(points_item)

        get_usage_series_response = cls(
            points=points,
        )

        get_usage_series_response.additional_properties = d
        return get_usage_series_response

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
