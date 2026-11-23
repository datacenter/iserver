# CUDN w/Localnet Topology

[[Back]](../README.md)

![Overview](../../images/ovn-cudn/localnet_physical.png)

CUDN w/localnet topology connects **secondary interface** to physical underlay via
- existing `br-ex` (BridgeExternal) that acts as the main gateway between the virtualized domain and external physical network
- dedicated ovs bridge created with `NodeNetworkConfigurationPolicy` object with configurable upstream connection

## Features

EW overlay-on-the-wire | NS Masq | Service | NetworkPolicy | MultinetworkPolicy
--- | --- | --- | --- | ---
:x: | :x: | :x: | :x: | :white_check_mark:

## Provisioning

- Step 1: [OVS](./ovs.md)
- Step 2: [Namespace](./namespace.md)
- Step 3: [CUDN](./cudn.md)
- Step 4: [POD](./pod.md)
- Step 5: [VM](./vm.md)
- Full deployment example in [task-way](./task.md)

## Use cases

- [unicast connectivity](./unicast.md)
- [multicast connectivity](./multicast.md)

[[Back]](../README.md)