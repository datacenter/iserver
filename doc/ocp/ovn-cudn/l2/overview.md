# CUDN w/L2 Topology

[[Back]](../README.md)

Cluster user defined network with layer 2 topology provides flat east-west network across the nodes for selected namespaces. All connected applications (pod/vm) are in single broadcast domain.

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
- [multicast connectivity](./multicast.md)

[[Back]](../README.md)