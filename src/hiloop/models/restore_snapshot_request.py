from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capability_requirement import CapabilityRequirement
    from ..models.capture_spec import CaptureSpec
    from ..models.egress_policy import EgressPolicy
    from ..models.resource_spec import ResourceSpec
    from ..models.restore_snapshot_request_labels import RestoreSnapshotRequestLabels
    from ..models.sandbox_image import SandboxImage
    from ..models.secret_binding import SecretBinding


T = TypeVar("T", bound="RestoreSnapshotRequest")


@_attrs_define
class RestoreSnapshotRequest:
    """Retired snapshot-restore compatibility request. Clean sandbox-cell deployments return
    unsupported; resume an exact sealed BranchFS workspace into a fresh runtime generation instead.

       Attributes:
           snapshot_id (str | Unset):
           project_id (str | Unset):
           name (str | Unset):
           image (SandboxImage | Unset): Explicit immutable environment selection. A create must name a deployment profile
               or exact OCI
                environment; omitting the image does not select a provider default.
           resources (ResourceSpec | Unset):
           requested_capabilities (list[CapabilityRequirement] | Unset):
           labels (RestoreSnapshotRequestLabels | Unset):
           contents (str | Unset): Required snapshot semantics for the restore. Omitted, the restore requires the
               snapshot's
                recorded effective semantics — restoring any snapshot with a minimal request is compatible by
                construction, like the omitted image and resources fields. An explicit value must match the
                snapshot's effective semantics exactly unless allow_fallback is set.
           allow_fallback (bool | Unset): Accept lower effective semantics than an explicit `contents` requirement. Has no
               effect when
                `contents` is omitted: the inherited requirement already matches the snapshot.
           capture (CaptureSpec | Unset):
           egress (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
               EGRESS_MODE_UNSPECIFIED leaves
                outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
                runtime supports.
           secrets (list[SecretBinding] | Unset): Secret bindings for the restored sandbox. Resolved per child; never
               inherited from the snapshot.
           execute_as_workload (str | Unset): Optional registered workload name to run the restored sandbox as. A restore
               declares its
                executing identity anew — a snapshot carries data, not authority — so nothing is inherited: when
                set, the restored sandbox is workload-classed (the caller must hold launch rights and the name
                must be registered); when empty, it executes as the restorer's own identity.
    """

    snapshot_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    image: SandboxImage | Unset = UNSET
    resources: ResourceSpec | Unset = UNSET
    requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
    labels: RestoreSnapshotRequestLabels | Unset = UNSET
    contents: str | Unset = UNSET
    allow_fallback: bool | Unset = UNSET
    capture: CaptureSpec | Unset = UNSET
    egress: EgressPolicy | Unset = UNSET
    secrets: list[SecretBinding] | Unset = UNSET
    execute_as_workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        project_id = self.project_id

        name = self.name

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        requested_capabilities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requested_capabilities, Unset):
            requested_capabilities = []
            for requested_capabilities_item_data in self.requested_capabilities:
                requested_capabilities_item = requested_capabilities_item_data.to_dict()
                requested_capabilities.append(requested_capabilities_item)

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        contents = self.contents

        allow_fallback = self.allow_fallback

        capture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capture, Unset):
            capture = self.capture.to_dict()

        egress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.egress, Unset):
            egress = self.egress.to_dict()

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        execute_as_workload = self.execute_as_workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if image is not UNSET:
            field_dict["image"] = image
        if resources is not UNSET:
            field_dict["resources"] = resources
        if requested_capabilities is not UNSET:
            field_dict["requested_capabilities"] = requested_capabilities
        if labels is not UNSET:
            field_dict["labels"] = labels
        if contents is not UNSET:
            field_dict["contents"] = contents
        if allow_fallback is not UNSET:
            field_dict["allow_fallback"] = allow_fallback
        if capture is not UNSET:
            field_dict["capture"] = capture
        if egress is not UNSET:
            field_dict["egress"] = egress
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if execute_as_workload is not UNSET:
            field_dict["execute_as_workload"] = execute_as_workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_requirement import CapabilityRequirement
        from ..models.capture_spec import CaptureSpec
        from ..models.egress_policy import EgressPolicy
        from ..models.resource_spec import ResourceSpec
        from ..models.restore_snapshot_request_labels import RestoreSnapshotRequestLabels
        from ..models.sandbox_image import SandboxImage
        from ..models.secret_binding import SecretBinding

        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        _image = d.pop("image", UNSET)
        image: SandboxImage | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = SandboxImage.from_dict(_image)

        _resources = d.pop("resources", UNSET)
        resources: ResourceSpec | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ResourceSpec.from_dict(_resources)

        _requested_capabilities = d.pop("requested_capabilities", UNSET)
        requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
        if _requested_capabilities is not UNSET:
            requested_capabilities = []
            for requested_capabilities_item_data in _requested_capabilities:
                requested_capabilities_item = CapabilityRequirement.from_dict(requested_capabilities_item_data)

                requested_capabilities.append(requested_capabilities_item)

        _labels = d.pop("labels", UNSET)
        labels: RestoreSnapshotRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = RestoreSnapshotRequestLabels.from_dict(_labels)

        contents = d.pop("contents", UNSET)

        allow_fallback = d.pop("allow_fallback", UNSET)

        _capture = d.pop("capture", UNSET)
        capture: CaptureSpec | Unset
        if isinstance(_capture, Unset):
            capture = UNSET
        else:
            capture = CaptureSpec.from_dict(_capture)

        _egress = d.pop("egress", UNSET)
        egress: EgressPolicy | Unset
        if isinstance(_egress, Unset):
            egress = UNSET
        else:
            egress = EgressPolicy.from_dict(_egress)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[SecretBinding] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = SecretBinding.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        execute_as_workload = d.pop("execute_as_workload", UNSET)

        restore_snapshot_request = cls(
            snapshot_id=snapshot_id,
            project_id=project_id,
            name=name,
            image=image,
            resources=resources,
            requested_capabilities=requested_capabilities,
            labels=labels,
            contents=contents,
            allow_fallback=allow_fallback,
            capture=capture,
            egress=egress,
            secrets=secrets,
            execute_as_workload=execute_as_workload,
        )

        restore_snapshot_request.additional_properties = d
        return restore_snapshot_request

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
