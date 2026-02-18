# Cilium BGP Control Plane

BGP control plane allows Cilium to advertise cluster-specific routes to connected routers using the Border Gateway Protocol (BGP). This can make Pod networks and/or Services reachable from outside the cluster in environments that support BGP.

Refer to [Isovalent documentation](https://docs.isovalent.com/configuration-guide/networking/bgp/index.html) for details.

## Requirements

Cilium Enterprise CNI

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium bgp -v state | get bgp control plane crds | [Link](./get_state.md)
iserver get ocp cilium bgp -v cli | get `cilium bgp` outputs | [Link](./get_cli.md)
iserver get ocp cilium bgp -v crd | get bgp control plane crds | [Link](./get_crd.md)
iserver set ocp cilium bgp --mode feature | enable bgp control plane | [Link](./enable.md)
iserver set ocp cilium bgp --mode crd | set bgp control plane crds from input file | [Link](./set_crd.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp cilium bgp --mode crd | delete bgp control plane crds in input file | [Link](./delete_crd.md)
iserver delete ocp cilium bgp --mode wipe | delete all bgp control plane crds | [Link](./wipe.md)
iserver delete ocp cilium bgp --mode feature | disable bgp control plane | [Link](./disable.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Extras

- [Example 3-node cluster peering with ACI](./aci.md)

[[Back]](../Operations.md)