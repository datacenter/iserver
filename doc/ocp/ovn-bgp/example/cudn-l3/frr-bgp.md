# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md)

## BGP

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b
- peering with leaf's loopback interface

## FRR

```
# iserver get ocp ovn-bgp -v session                           

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------+---------+-------------+-----+
| ID | Node  | Pod           | Peer    | Status      | BFD |
+----+-------+---------------+---------+-------------+-----+
| 1  | bm1-1 | frr-k8s-n6sbf | 6.6.6.7 | Established | N/A |
| 2  | bm1-1 | frr-k8s-n6sbf | 6.6.6.6 | Established | N/A |
| 3  | bm1-2 | frr-k8s-rl2vf | 6.6.6.6 | Established | N/A |
| 4  | bm1-2 | frr-k8s-rl2vf | 6.6.6.7 | Established | N/A |
| 5  | bm1-3 | frr-k8s-57sdg | 6.6.6.7 | Established | N/A | 
| 6  | bm1-3 | frr-k8s-57sdg | 6.6.6.6 | Established | N/A |
+----+-------+---------------+---------+-------------+-----+
```

```
# iserver get ocp ovn-bgp --cmd "show bgp ipv4 unicast summary" --node bm1-1 -v exec

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP router identifier 66.66.66.10, local AS number 64667 vrf-id 0
BGP table version 0
RIB entries 0, using 0 bytes of memory
Peers 2, using 1449 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
6.6.6.6         4      64600       408       406        0    0    0 06:42:27            0        0 N/A
6.6.6.7         4      64600       408       406        0    0    0 06:42:27            0        0 N/A

Total number of neighbors 2
```

[[Back]](./README.md)