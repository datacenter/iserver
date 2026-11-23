# Virtual Machine

## Configuration Change

Command | Intent | Details
--- | --- | ---
iserver set k8s vm cpu | change cpu topology | [Link](./cpu.md)
iserver set k8s vm memory | change memory | [Link](./memory.md)

## Power State Control

Command | Intent | Details
--- | --- | ---
iserver set k8s vm pause | pause virtual machine | [Link](./pause.md)
iserver set k8s vm restart | restart virtual machine | [Link](./restart.md)
iserver set k8s vm start | start virtual machine | [Link](./start.md)
iserver set k8s vm stop | stop virtual machine | [Link](./stop.md)
iserver set k8s vm unpause | unpause virtual machine | [Link](./unpause.md)

## Example

Virtual Machine | Interface | CNI | Network | Option | Overview | Networking
--- | --- | --- | --- | --- | --- | ---
Cat8kv | management | Cilium | POD | | [Link](./example-cat8k-pod-provisioning.md) | [Link](./example-cat8k-pod-kubevirt.md)
Cat8kv | management | Multus | L3 Bridge | | [Link](./example-cat8k-bridge-l3-provisioning.md) | [Link](./example-cat8k-bridge-l3-kubevirt.md)
Cat8kv | management | Multus | L2 Bridge | | [Link](./example-cat8k-bridge-l2.md) | ---
Cat8kv | management | Multus | L3 Bridge | user-defined mac address | [Link](./example-cat8k-bridge-mac.md) | ---
Cat8kv | secondary | Multus | L3 Bridge | | [Link](./example-cat8k-2nd-bridge-l3-provisioning.md) | [Link](./example-cat8k-2nd-bridge-l3-kubevirt.md)

[[Back]](../Operations.md)