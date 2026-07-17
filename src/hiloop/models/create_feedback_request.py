from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFeedbackRequest")


@_attrs_define
class CreateFeedbackRequest:
    """
    Attributes:
        title (str | Unset): A short summary of the report. Required; at most 300 characters.
        surface (str | Unset): The product surface the report is about. Required; one of `cli`, `api`, `web`, `sandbox`,
             `telemetry`, `annotations`, `docs`, or `other`.
        severity (str | Unset): How severe the problem is. Optional; one of `critical`, `high`, `medium`, or `low`.
            Leave it
             empty for general feedback that is not a bug.
        body (str | Unset): Free-form feedback text. Optional; at most 10,000 characters.
        expected (str | Unset): What was expected to happen. Optional; at most 10,000 characters.
        actual (str | Unset): What actually happened. Optional; at most 10,000 characters.
        repro (str | Unset): Steps to reproduce the problem. Optional; at most 10,000 characters.
        evidence (list[str] | Unset): Correlation keys — run, event, or artifact ids — linking the report to recorded
            telemetry.
             Optional; at most 50 entries, each at most 256 characters.
        fingerprint (str | Unset): A stable, content-derived deduplication key (for example `<surface>/<short-slug>`).
            Enforced:
             a submission whose fingerprint already exists returns the original report's id instead of
             storing (and surfacing) a duplicate, which makes retrying a lost response safe. When omitted,
             the server derives one from the report's content, so re-sending an identical report also
             converges. Optional; at most 300 characters.
        hiloop_version (str | Unset): The hiloop client version that produced the report. Optional; at most 100
            characters.
    """

    title: str | Unset = UNSET
    surface: str | Unset = UNSET
    severity: str | Unset = UNSET
    body: str | Unset = UNSET
    expected: str | Unset = UNSET
    actual: str | Unset = UNSET
    repro: str | Unset = UNSET
    evidence: list[str] | Unset = UNSET
    fingerprint: str | Unset = UNSET
    hiloop_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        surface = self.surface

        severity = self.severity

        body = self.body

        expected = self.expected

        actual = self.actual

        repro = self.repro

        evidence: list[str] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = self.evidence

        fingerprint = self.fingerprint

        hiloop_version = self.hiloop_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if surface is not UNSET:
            field_dict["surface"] = surface
        if severity is not UNSET:
            field_dict["severity"] = severity
        if body is not UNSET:
            field_dict["body"] = body
        if expected is not UNSET:
            field_dict["expected"] = expected
        if actual is not UNSET:
            field_dict["actual"] = actual
        if repro is not UNSET:
            field_dict["repro"] = repro
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if hiloop_version is not UNSET:
            field_dict["hiloop_version"] = hiloop_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        surface = d.pop("surface", UNSET)

        severity = d.pop("severity", UNSET)

        body = d.pop("body", UNSET)

        expected = d.pop("expected", UNSET)

        actual = d.pop("actual", UNSET)

        repro = d.pop("repro", UNSET)

        evidence = cast(list[str], d.pop("evidence", UNSET))

        fingerprint = d.pop("fingerprint", UNSET)

        hiloop_version = d.pop("hiloop_version", UNSET)

        create_feedback_request = cls(
            title=title,
            surface=surface,
            severity=severity,
            body=body,
            expected=expected,
            actual=actual,
            repro=repro,
            evidence=evidence,
            fingerprint=fingerprint,
            hiloop_version=hiloop_version,
        )

        create_feedback_request.additional_properties = d
        return create_feedback_request

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
