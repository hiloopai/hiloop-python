from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resolve_effective_egress_response_enforcement import ResolveEffectiveEgressResponseEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clamped_entry import ClampedEntry
    from ..models.egress_policy import EgressPolicy
    from ..models.egress_population import EgressPopulation


T = TypeVar("T", bound="ResolveEffectiveEgressResponse")


@_attrs_define
class ResolveEffectiveEgressResponse:
    """
    Attributes:
        resolved (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        enforcement (ResolveEffectiveEgressResponseEnforcement | Unset): How a denial is enforced for the resolved class
            (the winning binding's override, else the tenant
             default).
        winning_selector (str | Unset): The selector of the binding that won under most-specific-wins, or "baseline"
            when no binding
             matched and the tenant baseline applies.
        baseline (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        clamped (list[ClampedEntry] | Unset): Destinations the baseline ceiling removed from the winning binding (empty
            when the baseline won,
             or when the winning binding named nothing outside the baseline).
        population (EgressPopulation | Unset): How many identities a selector covers, for the "who does this apply to"
            display. The count is the
             exact size of the covered set; the sample is a small, illustrative subset (workload names, member
             emails, or key names, depending on the selector), never the full list.
    """

    resolved: EgressPolicy | Unset = UNSET
    enforcement: ResolveEffectiveEgressResponseEnforcement | Unset = UNSET
    winning_selector: str | Unset = UNSET
    baseline: EgressPolicy | Unset = UNSET
    clamped: list[ClampedEntry] | Unset = UNSET
    population: EgressPopulation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolved: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved, Unset):
            resolved = self.resolved.to_dict()

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        winning_selector = self.winning_selector

        baseline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.baseline, Unset):
            baseline = self.baseline.to_dict()

        clamped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clamped, Unset):
            clamped = []
            for clamped_item_data in self.clamped:
                clamped_item = clamped_item_data.to_dict()
                clamped.append(clamped_item)

        population: dict[str, Any] | Unset = UNSET
        if not isinstance(self.population, Unset):
            population = self.population.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if winning_selector is not UNSET:
            field_dict["winning_selector"] = winning_selector
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if clamped is not UNSET:
            field_dict["clamped"] = clamped
        if population is not UNSET:
            field_dict["population"] = population

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clamped_entry import ClampedEntry
        from ..models.egress_policy import EgressPolicy
        from ..models.egress_population import EgressPopulation

        d = dict(src_dict)
        _resolved = d.pop("resolved", UNSET)
        resolved: EgressPolicy | Unset
        if isinstance(_resolved, Unset):
            resolved = UNSET
        else:
            resolved = EgressPolicy.from_dict(_resolved)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: ResolveEffectiveEgressResponseEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = ResolveEffectiveEgressResponseEnforcement(_enforcement)

        winning_selector = d.pop("winning_selector", UNSET)

        _baseline = d.pop("baseline", UNSET)
        baseline: EgressPolicy | Unset
        if isinstance(_baseline, Unset):
            baseline = UNSET
        else:
            baseline = EgressPolicy.from_dict(_baseline)

        _clamped = d.pop("clamped", UNSET)
        clamped: list[ClampedEntry] | Unset = UNSET
        if _clamped is not UNSET:
            clamped = []
            for clamped_item_data in _clamped:
                clamped_item = ClampedEntry.from_dict(clamped_item_data)

                clamped.append(clamped_item)

        _population = d.pop("population", UNSET)
        population: EgressPopulation | Unset
        if isinstance(_population, Unset):
            population = UNSET
        else:
            population = EgressPopulation.from_dict(_population)

        resolve_effective_egress_response = cls(
            resolved=resolved,
            enforcement=enforcement,
            winning_selector=winning_selector,
            baseline=baseline,
            clamped=clamped,
            population=population,
        )

        resolve_effective_egress_response.additional_properties = d
        return resolve_effective_egress_response

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
