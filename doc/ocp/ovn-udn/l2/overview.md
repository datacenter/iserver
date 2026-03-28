# UDN w/L2 Topology

[[Back]](../README.md)

User defined network with layer 2 topology provides flat east-west network across the nodes. All connected applications (pod/vm) are in single broadcast domain.

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
- [multicast connectivity](./multicast.md)

[[Back]](../README.md)