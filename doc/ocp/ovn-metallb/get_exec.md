# MetalLB - Get FRR exec output

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)

```
# iserver get ocp metallb --cluster bm1 -v exec --node bm1-3 --cmd "show bgp ipv4 summary"

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1

FRR speaker-g8lz6 [bm1-3]
-------------------------

IPv4 Unicast Summary (VRF default):
BGP router identifier 66.66.66.12, local AS number 64667 vrf-id 0
BGP table version 3
RIB entries 1, using 192 bytes of memory
Peers 1, using 725 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
6.6.6.6         4      64600       294       295        0    0    0 04:48:17            0        1 N/A

Total number of neighbors 1
```

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)