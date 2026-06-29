from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run import Run


T = TypeVar("T", bound="ListRunsResponse")


@_attrs_define
class ListRunsResponse:
    """
    Attributes:
        runs (list[Run] | Unset): The runs on this page, newest first.
        next_page_token (str | Unset): The token to pass as page_token to fetch the next page. Empty when there are no
            more results.
    """

    runs: list[Run] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()
                runs.append(runs_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runs is not UNSET:
            field_dict["runs"] = runs
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run import Run

        d = dict(src_dict)
        _runs = d.pop("runs", UNSET)
        runs: list[Run] | Unset = UNSET
        if _runs is not UNSET:
            runs = []
            for runs_item_data in _runs:
                runs_item = Run.from_dict(runs_item_data)

                runs.append(runs_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_runs_response = cls(
            runs=runs,
            next_page_token=next_page_token,
        )

        list_runs_response.additional_properties = d
        return list_runs_response

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
