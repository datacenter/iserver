# UDN w/L3 Topology

[[Back]](../README.md)

A layer 3 topology creates a unique layer 2 segment for each node in a cluster. The layer 3 routing mechanism interconnects these segments so that virtual machines and pods that are hosted on different nodes can communicate with each other. 

## Features

Role | EW | NS | Service | NetworkPolicy | MultinetworkPolicy
--- | --- | --- | --- | --- | ---
Primary | :white_check_mark: w/overlay | :white_check_mark: w/masq | :white_check_mark: | :white_check_mark: | :x:
Secondary | :white_check_mark: w/overlay | :x: | :x: | :x: | :white_check_mark:

## Provisioning

- Step 1: [UDN](./udn.md)
- Step 2: [POD](./pod.md)
- Step 3: [VM](./vm.md)
- Full deployment example in [task-way](./task.md)

## Use cases

- [unicast connectivity](./unicast.md)

[[Back]](../README.md)