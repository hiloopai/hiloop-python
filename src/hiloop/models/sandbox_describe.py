from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_spec import ResourceSpec
    from ..models.sandbox_operation_summary import SandboxOperationSummary


T = TypeVar("T", bound="SandboxDescribe")


@_attrs_define
class SandboxDescribe:
    """Describe-altitude detail for one sandbox: what it runs, what it asked for, where it is in its
    lifecycle, and what recently happened to it. Returned only by GetSandbox; list rows stay lean.

       Attributes:
           image_reference (str | Unset): The container image reference the sandbox's spec pinned, when it names one.
           image_digest (str | Unset): The image content digest, when known.
           requested_resources (ResourceSpec | Unset):
           state_since (str | Unset): When the current observed state began (RFC 3339): the completion time of the last
               succeeded
                state-changing operation, or the creation time before any state change.
           lease_expires_at (str | Unset): When the sandbox's keepalive lease expires (RFC 3339). Empty when the sandbox
               has no idle
                timeout.
           lineage_path (str | Unset): The lineage path of the sandbox's run (dotted run ids, root first). Empty without a
               run.
           branch_event_id (str | Unset): The parent event the sandbox's run branched at. Empty for a tree root or no run.
           recent_operations (list[SandboxOperationSummary] | Unset): The sandbox's most recent operations, newest first
               (capped by the server).
           resolved_accelerator_model (str | Unset): Accelerator model selected from requested_resources.gpus.models at
               admission. Empty when the
                sandbox requested no accelerator.
    """

    image_reference: str | Unset = UNSET
    image_digest: str | Unset = UNSET
    requested_resources: ResourceSpec | Unset = UNSET
    state_since: str | Unset = UNSET
    lease_expires_at: str | Unset = UNSET
    lineage_path: str | Unset = UNSET
    branch_event_id: str | Unset = UNSET
    recent_operations: list[SandboxOperationSummary] | Unset = UNSET
    resolved_accelerator_model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_reference = self.image_reference

        image_digest = self.image_digest

        requested_resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested_resources, Unset):
            requested_resources = self.requested_resources.to_dict()

        state_since = self.state_since

        lease_expires_at = self.lease_expires_at

        lineage_path = self.lineage_path

        branch_event_id = self.branch_event_id

        recent_operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_operations, Unset):
            recent_operations = []
            for recent_operations_item_data in self.recent_operations:
                recent_operations_item = recent_operations_item_data.to_dict()
                recent_operations.append(recent_operations_item)

        resolved_accelerator_model = self.resolved_accelerator_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_reference is not UNSET:
            field_dict["image_reference"] = image_reference
        if image_digest is not UNSET:
            field_dict["image_digest"] = image_digest
        if requested_resources is not UNSET:
            field_dict["requested_resources"] = requested_resources
        if state_since is not UNSET:
            field_dict["state_since"] = state_since
        if lease_expires_at is not UNSET:
            field_dict["lease_expires_at"] = lease_expires_at
        if lineage_path is not UNSET:
            field_dict["lineage_path"] = lineage_path
        if branch_event_id is not UNSET:
            field_dict["branch_event_id"] = branch_event_id
        if recent_operations is not UNSET:
            field_dict["recent_operations"] = recent_operations
        if resolved_accelerator_model is not UNSET:
            field_dict["resolved_accelerator_model"] = resolved_accelerator_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_spec import ResourceSpec
        from ..models.sandbox_operation_summary import SandboxOperationSummary

        d = dict(src_dict)
        image_reference = d.pop("image_reference", UNSET)

        image_digest = d.pop("image_digest", UNSET)

        _requested_resources = d.pop("requested_resources", UNSET)
        requested_resources: ResourceSpec | Unset
        if isinstance(_requested_resources, Unset):
            requested_resources = UNSET
        else:
            requested_resources = ResourceSpec.from_dict(_requested_resources)

        state_since = d.pop("state_since", UNSET)

        lease_expires_at = d.pop("lease_expires_at", UNSET)

        lineage_path = d.pop("lineage_path", UNSET)

        branch_event_id = d.pop("branch_event_id", UNSET)

        _recent_operations = d.pop("recent_operations", UNSET)
        recent_operations: list[SandboxOperationSummary] | Unset = UNSET
        if _recent_operations is not UNSET:
            recent_operations = []
            for recent_operations_item_data in _recent_operations:
                recent_operations_item = SandboxOperationSummary.from_dict(recent_operations_item_data)

                recent_operations.append(recent_operations_item)

        resolved_accelerator_model = d.pop("resolved_accelerator_model", UNSET)

        sandbox_describe = cls(
            image_reference=image_reference,
            image_digest=image_digest,
            requested_resources=requested_resources,
            state_since=state_since,
            lease_expires_at=lease_expires_at,
            lineage_path=lineage_path,
            branch_event_id=branch_event_id,
            recent_operations=recent_operations,
            resolved_accelerator_model=resolved_accelerator_model,
        )

        sandbox_describe.additional_properties = d
        return sandbox_describe

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
