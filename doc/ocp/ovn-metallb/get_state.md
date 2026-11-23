# MetalLB - Get state

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)

```
# iserver get ocp metallb --cluster bm1 -v state

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1
Operator metallb-operator found
Metallb instance in l3 mode
bgpBackend undefined (ovn-bgp integrated mode)
Metallb configuration
- IPAddressPool: 0
- BGPPeer: 1
- BFDProfile: 0
- BGPAdvertisement: 0
- Community: 0
- FRRConfiguration: 4

View: state (def), cli, crd, exec, frr, all
```

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)