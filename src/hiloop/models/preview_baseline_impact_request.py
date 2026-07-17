from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preview_baseline_impact_request_enforcement import PreviewBaselineImpactRequestEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="PreviewBaselineImpactRequest")


@_attrs_define
class PreviewBaselineImpactRequest:
    """
    Attributes:
        baseline (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        enforcement (PreviewBaselineImpactRequestEnforcement | Unset): The proposed default enforcement disposition
            (informational; does not affect the destination
             diff).
    """

    baseline: EgressPolicy | Unset = UNSET
    enforcement: PreviewBaselineImpactRequestEnforcement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.baseline, Unset):
            baseline = self.baseline.to_dict()

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egress_policy import EgressPolicy

        d = dict(src_dict)
        _baseline = d.pop("baseline", UNSET)
        baseline: EgressPolicy | Unset
        if isinstance(_baseline, Unset):
            baseline = UNSET
        else:
            baseline = EgressPolicy.from_dict(_baseline)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: PreviewBaselineImpactRequestEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = PreviewBaselineImpactRequestEnforcement(_enforcement)

        preview_baseline_impact_request = cls(
            baseline=baseline,
            enforcement=enforcement,
        )

        preview_baseline_impact_request.additional_properties = d
        return preview_baseline_impact_request

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
