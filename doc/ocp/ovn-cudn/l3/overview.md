# CUDN w/L3 Topology

[[Back]](../README.md)

A layer 3 topology creates a unique layer 2 segment for each node in a cluster. The layer 3 routing mechanism interconnects these segments so that virtual machines and pods that are hosted on different nodes can communicate with each other.

## Features

EW overlay-on-the-wire | NS Masq | Service | NetworkPolicy | MultinetworkPolicy
--- | --- | --- | --- | ---
:white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x:

## Provisioning

- Step 1: [Namespace](./namespace.md)
- Step 2: [CUDN](./cudn.md)
- Step 3: [POD](./pod.md)
- Step 4: [VM](./vm.md)
- Full deployment example in [task-way](./task.md)

## Use cases

- [unicast connectivity](./unicast.md)

[[Back]](../README.md)