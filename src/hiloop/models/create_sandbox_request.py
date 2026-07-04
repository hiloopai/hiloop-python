from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capability_requirement import CapabilityRequirement
    from ..models.capture_spec import CaptureSpec
    from ..models.create_sandbox_request_labels import CreateSandboxRequestLabels
    from ..models.egress_policy import EgressPolicy
    from ..models.lifecycle_spec import LifecycleSpec
    from ..models.resource_spec import ResourceSpec
    from ..models.sandbox_image import SandboxImage
    from ..models.secret_binding import SecretBinding


T = TypeVar("T", bound="CreateSandboxRequest")


@_attrs_define
class CreateSandboxRequest:
    """
    Attributes:
        project_id (str | Unset):
        name (str | Unset):
        image (SandboxImage | Unset):
        resources (ResourceSpec | Unset):
        requested_capabilities (list[CapabilityRequirement] | Unset):
        labels (CreateSandboxRequestLabels | Unset):
        capture (CaptureSpec | Unset):
        egress (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        secrets (list[SecretBinding] | Unset): Secret bindings injected into matching outbound requests. Empty injects
            nothing.
        lifecycle (LifecycleSpec | Unset): Runtime lease policy. Omitted, or lease_secs=0, uses the server default. This
            intentionally exposes
             only the expiry control needed by public callers; process defaults, mounts, environment, and user
             remain server-managed in the first runtime slice.
        description (str | Unset): User-assigned free-text description. Empty leaves the sandbox undescribed.
    """

    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    image: SandboxImage | Unset = UNSET
    resources: ResourceSpec | Unset = UNSET
    requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
    labels: CreateSandboxRequestLabels | Unset = UNSET
    capture: CaptureSpec | Unset = UNSET
    egress: EgressPolicy | Unset = UNSET
    secrets: list[SecretBinding] | Unset = UNSET
    lifecycle: LifecycleSpec | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if capture is not UNSET:
            field_dict["capture"] = capture
        if egress is not UNSET:
            field_dict["egress"] = egress
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_requirement import CapabilityRequirement
        from ..models.capture_spec import CaptureSpec
        from ..models.create_sandbox_request_labels import CreateSandboxRequestLabels
        from ..models.egress_policy import EgressPolicy
        from ..models.lifecycle_spec import LifecycleSpec
        from ..models.resource_spec import ResourceSpec
        from ..models.sandbox_image import SandboxImage
        from ..models.secret_binding import SecretBinding

        d = dict(src_dict)
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
        labels: CreateSandboxRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CreateSandboxRequestLabels.from_dict(_labels)

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

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: LifecycleSpec | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = LifecycleSpec.from_dict(_lifecycle)

        description = d.pop("description", UNSET)

        create_sandbox_request = cls(
            project_id=project_id,
            name=name,
            image=image,
            resources=resources,
            requested_capabilities=requested_capabilities,
            labels=labels,
            capture=capture,
            egress=egress,
            secrets=secrets,
            lifecycle=lifecycle,
            description=description,
        )

        create_sandbox_request.additional_properties = d
        return create_sandbox_request

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
