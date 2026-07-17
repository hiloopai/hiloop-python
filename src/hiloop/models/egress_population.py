from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EgressPopulation")


@_attrs_define
class EgressPopulation:
    r"""How many identities a selector covers, for the "who does this apply to" display. The count is the
    exact size of the covered set; the sample is a small, illustrative subset (workload names, member
    emails, or key names, depending on the selector), never the full list.

       Attributes:
           description (str | Unset): A human-readable summary (e.g. "3 registered workloads", "the admin
               \"a@example.com\"").
           count (str | Unset): The exact number of identities the selector covers (JSON-encoded as a string, per proto3
               JSON).
           sample (list[str] | Unset): A small illustrative sample of the covered identities (may be empty; never the full
               set).
    """

    description: str | Unset = UNSET
    count: str | Unset = UNSET
    sample: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        sample: list[str] | Unset = UNSET
        if not isinstance(self.sample, Unset):
            sample = self.sample

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if sample is not UNSET:
            field_dict["sample"] = sample

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        sample = cast(list[str], d.pop("sample", UNSET))

        egress_population = cls(
            description=description,
            count=count,
            sample=sample,
        )

        egress_population.additional_properties = d
        return egress_population

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
