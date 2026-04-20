# Metal Kubed

[[Back]](../Operations.md) [[Node power management]](../node-power/README.md)

![Logo](../images/metal-kubed/logo.png) 

[Metal3](https://metal3.io/) aka "Metal Kubed" is an open-source project that provides a set of tools for managing bare-metal infrastructure using Kubernetes. 
- Cluster API Provider - enables the creation and management of physical servers using the Kubernetes Cluster API
- Bare Metal Operator - automates the provisioning of bare-metal servers using the open-source Ironic project
- Ironic - the core component in Metal3 responsible for the provisioning and management of bare metal servers

Metal3 is built-in component in OpenShift cluster with functionality exposed via Console UI and range of crds. 

## Examples

- [Provisioning state](./kb/provisioning_state.md)
- [Operational state](./kb/operational_state.md)
- [Registration](./kb/register.md)
- [Detaching hosts from provisioner](./kb/detach.md)
- [Externally provisioned nodes](./kb/externally_provisioned.md)
- [Unmanaged nodes](./kb/unmanaged.md)
- [Inspection](./kb/inspect.md)
- [Power on](./kb/power_on.md)
- [Power off](./kb/power_off.md)
- [Reboot](./kb/reboot.md)

## Life Cycle Management Commands

> [!CAUTION]
> power management actions are **not** kubernetes friendly, refer to [node power management](../node-power/README.md)

Command | Intent | Details
--- | --- | ---
iserver get ocp bmh | get state | [Link](./get.md)
iserver set ocp bmh --mode node | create node | [Link](./create_node.md)
iserver set ocp bmh --mode bmc | node registration | [Link](./register.md)
iserver set ocp bmh --mode attach | attach host to provisioner | [Link](./attach.md)
iserver set ocp bmh --mode detach | detach host from provisioner | [Link](./detach.md)
iserver set ocp bmh --mode inspect | inspect host | [Link](./inspect.md)
iserver set ocp bmh --mode on | power on the node | [Link](./power_on.md)
iserver set ocp bmh --mode off | power off the node | [Link](./power_off.md)
iserver set ocp bmh --mode reboot | reboot the node | [Link](./reboot.md)
iserver delete ocp bmh --mode node | delete node | [Link](./delete_node.md)

[[Back]](../Operations.md) [[Node power management]](../node-power/README.md)