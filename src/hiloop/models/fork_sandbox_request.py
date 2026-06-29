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
    from ..models.fork_sandbox_request_labels import ForkSandboxRequestLabels
    from ..models.resource_spec import ResourceSpec
    from ..models.sandbox_image import SandboxImage
    from ..models.secret_binding import SecretBinding


T = TypeVar("T", bound="ForkSandboxRequest")


@_attrs_define
class ForkSandboxRequest:
    """
    Attributes:
        source_sandbox_id (str | Unset):
        parent_fork_node_id (str | Unset):
        child_fork_node_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset):
        image (SandboxImage | Unset):
        resources (ResourceSpec | Unset):
        requested_capabilities (list[CapabilityRequirement] | Unset):
        labels (ForkSandboxRequestLabels | Unset):
        continuity (str | Unset):
        allow_fallback (bool | Unset):
        capture (CaptureSpec | Unset):
        egress (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        secrets (list[SecretBinding] | Unset): Secret bindings for the child sandbox. Resolved per child; never
            inherited from the snapshot.
    """

    source_sandbox_id: str | Unset = UNSET
    parent_fork_node_id: str | Unset = UNSET
    child_fork_node_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    image: SandboxImage | Unset = UNSET
    resources: ResourceSpec | Unset = UNSET
    requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
    labels: ForkSandboxRequestLabels | Unset = UNSET
    continuity: str | Unset = UNSET
    allow_fallback: bool | Unset = UNSET
    capture: CaptureSpec | Unset = UNSET
    egress: EgressPolicy | Unset = UNSET
    secrets: list[SecretBinding] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_sandbox_id = self.source_sandbox_id

        parent_fork_node_id = self.parent_fork_node_id

        child_fork_node_id = self.child_fork_node_id

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

        continuity = self.continuity

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_sandbox_id is not UNSET:
            field_dict["sourceSandboxId"] = source_sandbox_id
        if parent_fork_node_id is not UNSET:
            field_dict["parentForkNodeId"] = parent_fork_node_id
        if child_fork_node_id is not UNSET:
            field_dict["childForkNodeId"] = child_fork_node_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if image is not UNSET:
            field_dict["image"] = image
        if resources is not UNSET:
            field_dict["resources"] = resources
        if requested_capabilities is not UNSET:
            field_dict["requestedCapabilities"] = requested_capabilities
        if labels is not UNSET:
            field_dict["labels"] = labels
        if continuity is not UNSET:
            field_dict["continuity"] = continuity
        if allow_fallback is not UNSET:
            field_dict["allowFallback"] = allow_fallback
        if capture is not UNSET:
            field_dict["capture"] = capture
        if egress is not UNSET:
            field_dict["egress"] = egress
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_requirement import CapabilityRequirement
        from ..models.capture_spec import CaptureSpec
        from ..models.egress_policy import EgressPolicy
        from ..models.fork_sandbox_request_labels import ForkSandboxRequestLabels
        from ..models.resource_spec import ResourceSpec
        from ..models.sandbox_image import SandboxImage
        from ..models.secret_binding import SecretBinding

        d = dict(src_dict)
        source_sandbox_id = d.pop("sourceSandboxId", UNSET)

        parent_fork_node_id = d.pop("parentForkNodeId", UNSET)

        child_fork_node_id = d.pop("childForkNodeId", UNSET)

        project_id = d.pop("projectId", UNSET)

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

        _requested_capabilities = d.pop("requestedCapabilities", UNSET)
        requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
        if _requested_capabilities is not UNSET:
            requested_capabilities = []
            for requested_capabilities_item_data in _requested_capabilities:
                requested_capabilities_item = CapabilityRequirement.from_dict(requested_capabilities_item_data)

                requested_capabilities.append(requested_capabilities_item)

        _labels = d.pop("labels", UNSET)
        labels: ForkSandboxRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ForkSandboxRequestLabels.from_dict(_labels)

        continuity = d.pop("continuity", UNSET)

        allow_fallback = d.pop("allowFallback", UNSET)

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

        fork_sandbox_request = cls(
            source_sandbox_id=source_sandbox_id,
            parent_fork_node_id=parent_fork_node_id,
            child_fork_node_id=child_fork_node_id,
            project_id=project_id,
            name=name,
            image=image,
            resources=resources,
            requested_capabilities=requested_capabilities,
            labels=labels,
            continuity=continuity,
            allow_fallback=allow_fallback,
            capture=capture,
            egress=egress,
            secrets=secrets,
        )

        fork_sandbox_request.additional_properties = d
        return fork_sandbox_request

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
