from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch_hlc import BranchHlc


T = TypeVar("T", bound="Snapshot")


@_attrs_define
class Snapshot:
    """Retained wire type for retired snapshot compatibility RPCs. Use a BranchFS workspace revision
    plus stop/resume for filesystem continuity on clean sandbox-cell deployments.

       Attributes:
           id (str | Unset):
           tenant_id (str | Unset):
           project_id (str | Unset):
           source_sandbox_id (str | Unset): The sandbox whose state the snapshot captured.
           requested_semantics_json (str | Unset):
           effective_semantics_json (str | Unset):
           size_bytes (str | Unset):
           legal_hold (bool | Unset):
           state (str | Unset): Lifecycle state: pending, ready, or failed.
           origin (str | Unset): Who minted the snapshot: user (an explicit request), fork (a fork's recorded branch
               point), or
                recovery. Capability is identical across origins.
           source_run_id (str | Unset): The run the source sandbox was executing at capture. Empty when the source had no
               run.
           branch_event_id (str | Unset): The latest ingested event on the source run's timeline at capture — the branch
               anchor a
                restore's child run derives from. Correlational ("state as of this point on the timeline"),
                never a transactional cut; empty when no event linkage was known.
           branch_hlc (BranchHlc | Unset): A hybrid logical clock coordinate on an event timeline.
           captured_at (str | Unset): When the snapshot's bytes were frozen (RFC 3339). Empty until captured.
           name (str | Unset): User-assigned name. Empty when unset.
           description (str | Unset): User-assigned free-text description. Empty when unset.
           created_by (str | Unset): Stable id of the principal that requested the snapshot (the forking principal for
               fork-minted
                snapshots). Empty when unrecorded.
           created_at (str | Unset): When the snapshot record was created (RFC 3339).
           updated_at (str | Unset): When the snapshot record was last updated (RFC 3339).
           durability (str | Unset): Off-node durability of the snapshot bytes: local (a node-local copy only; does not
               survive
                node loss) or replicated (an off-node copy exists). Resolved live at read time and never
                overstated: a snapshot whose replication cannot be confirmed reports local.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    source_sandbox_id: str | Unset = UNSET
    requested_semantics_json: str | Unset = UNSET
    effective_semantics_json: str | Unset = UNSET
    size_bytes: str | Unset = UNSET
    legal_hold: bool | Unset = UNSET
    state: str | Unset = UNSET
    origin: str | Unset = UNSET
    source_run_id: str | Unset = UNSET
    branch_event_id: str | Unset = UNSET
    branch_hlc: BranchHlc | Unset = UNSET
    captured_at: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    durability: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        project_id = self.project_id

        source_sandbox_id = self.source_sandbox_id

        requested_semantics_json = self.requested_semantics_json

        effective_semantics_json = self.effective_semantics_json

        size_bytes = self.size_bytes

        legal_hold = self.legal_hold

        state = self.state

        origin = self.origin

        source_run_id = self.source_run_id

        branch_event_id = self.branch_event_id

        branch_hlc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_hlc, Unset):
            branch_hlc = self.branch_hlc.to_dict()

        captured_at = self.captured_at

        name = self.name

        description = self.description

        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        durability = self.durability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if source_sandbox_id is not UNSET:
            field_dict["source_sandbox_id"] = source_sandbox_id
        if requested_semantics_json is not UNSET:
            field_dict["requested_semantics_json"] = requested_semantics_json
        if effective_semantics_json is not UNSET:
            field_dict["effective_semantics_json"] = effective_semantics_json
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if legal_hold is not UNSET:
            field_dict["legal_hold"] = legal_hold
        if state is not UNSET:
            field_dict["state"] = state
        if origin is not UNSET:
            field_dict["origin"] = origin
        if source_run_id is not UNSET:
            field_dict["source_run_id"] = source_run_id
        if branch_event_id is not UNSET:
            field_dict["branch_event_id"] = branch_event_id
        if branch_hlc is not UNSET:
            field_dict["branch_hlc"] = branch_hlc
        if captured_at is not UNSET:
            field_dict["captured_at"] = captured_at
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if durability is not UNSET:
            field_dict["durability"] = durability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch_hlc import BranchHlc

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        source_sandbox_id = d.pop("source_sandbox_id", UNSET)

        requested_semantics_json = d.pop("requested_semantics_json", UNSET)

        effective_semantics_json = d.pop("effective_semantics_json", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        legal_hold = d.pop("legal_hold", UNSET)

        state = d.pop("state", UNSET)

        origin = d.pop("origin", UNSET)

        source_run_id = d.pop("source_run_id", UNSET)

        branch_event_id = d.pop("branch_event_id", UNSET)

        _branch_hlc = d.pop("branch_hlc", UNSET)
        branch_hlc: BranchHlc | Unset
        if isinstance(_branch_hlc, Unset):
            branch_hlc = UNSET
        else:
            branch_hlc = BranchHlc.from_dict(_branch_hlc)

        captured_at = d.pop("captured_at", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        durability = d.pop("durability", UNSET)

        snapshot = cls(
            id=id,
            tenant_id=tenant_id,
            project_id=project_id,
            source_sandbox_id=source_sandbox_id,
            requested_semantics_json=requested_semantics_json,
            effective_semantics_json=effective_semantics_json,
            size_bytes=size_bytes,
            legal_hold=legal_hold,
            state=state,
            origin=origin,
            source_run_id=source_run_id,
            branch_event_id=branch_event_id,
            branch_hlc=branch_hlc,
            captured_at=captured_at,
            name=name,
            description=description,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            durability=durability,
        )

        snapshot.additional_properties = d
        return snapshot

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
