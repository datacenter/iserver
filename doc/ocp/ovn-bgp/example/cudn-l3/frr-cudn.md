# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[NX-OS]](./nxos-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks

## FRR

```
# iserver get ocp ovn-bgp --cmd "show bgp ipv4 unicast summary" --node bm1-1 -v exec      

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP router identifier 66.66.66.10, local AS number 64667 vrf-id 0
BGP table version 2
RIB entries 3, using 576 bytes of memory
Peers 2, using 1449 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
6.6.6.6         4      64600       429       429        0    0    0 07:03:29            0        2 N/A
6.6.6.7         4      64600       429       429        0    0    0 07:03:29            0        2 N/A

Total number of neighbors 2
```

```
# iserver get ocp ovn-bgp --cmd "show bgp ipv4 unicast" --node bm1-1 -v exec

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm7-1]
-------------------------
BGP table version is 2, local router ID is 66.66.66.10, vrf id 0

    Network          Next Hop            Metric LocPrf Weight Path
 *> 69.69.100.0/28   0.0.0.0                  0         32768 i
 *> 69.69.200.0/28   0.0.0.0                  0         32768 i

Displayed  2 routes and 2 total paths
```

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[NX-OS]](./nxos-cudn.md)