from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.promoted_field_type import PromotedFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PromotedField")


@_attrs_define
class PromotedField:
    """One tenant-declared field promoted from the annotation payload into a typed column for
    filter/sort/join speed. Unpromoted fields stay queryable from the JSON payload. The set of
    promoted fields is part of the immutable schema version: registering a new version re-binds slots,
    while an existing version's bindings never change.

       Attributes:
           field (str | Unset): The payload field name to promote (e.g. "score"). Must be a field the schema's payload
               carries.
           type_ (PromotedFieldType | Unset): The storage type to lift the field into.
           identity (bool | Unset): Whether this field is part of the latest-wins supersession identity. The default
               supersession key
                is the annotated target plus the schema name; declaring identity fields refines it (e.g. mark an
                "annotator" field identity to keep the latest write per annotator). Identity fields must be
                promoted, since dedup partitions on the typed column.
           bloom (bool | Unset): Request a point-lookup bloom filter for this field (str only; default false). Useful for a
                high-cardinality promoted id queried by exact match.
           slot (str | Unset): The server-assigned physical column the field binds to (read-only; ignored on a register
               request,
                populated on the stored/returned schema).
    """

    field: str | Unset = UNSET
    type_: PromotedFieldType | Unset = UNSET
    identity: bool | Unset = UNSET
    bloom: bool | Unset = UNSET
    slot: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        identity = self.identity

        bloom = self.bloom

        slot = self.slot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identity is not UNSET:
            field_dict["identity"] = identity
        if bloom is not UNSET:
            field_dict["bloom"] = bloom
        if slot is not UNSET:
            field_dict["slot"] = slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PromotedFieldType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PromotedFieldType(_type_)

        identity = d.pop("identity", UNSET)

        bloom = d.pop("bloom", UNSET)

        slot = d.pop("slot", UNSET)

        promoted_field = cls(
            field=field,
            type_=type_,
            identity=identity,
            bloom=bloom,
            slot=slot,
        )

        promoted_field.additional_properties = d
        return promoted_field

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
