# CUDN w/Localnet Topology - Step 1: OVS

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./namespace.md)

The switched localnet topology interconnects the workloads created as Network Attachment Definitions (NADs) through a cluster-wide logical switch to a physical network.
- existing `br-ex` (BridgeExternal) that acts as the main gateway between the virtualized domain and external physical network
- dedicated ovs bridge created with `NodeNetworkConfigurationPolicy` object with configurable upstream connection
    - physical interface
    - vlan subinterface
    - bond interface

> [!NOTE]
> The localnet value defined in `onv.bridge-mappings.localnet` must match the `physicalNetworkName` of CUDN

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ovs-localnet-y
spec:
  desiredState:
    interfaces:
    - name: ovs-localnet-y
      type: ovs-bridge
      state: up
      bridge:
        allow-extra-patch-ports: true
        options:
          stp: false
          mcast-snooping-enable: true
        port:
        - name: ens11f0
    ovn:
      bridge-mappings:
      - localnet: localnet-y
        bridge: ovs-localnet-y
        state: present
```

[[Back]](./overview.md) [[Prev](./vm.md)] [[Next]](./cudn.md)