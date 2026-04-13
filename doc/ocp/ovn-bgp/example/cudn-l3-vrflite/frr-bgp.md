# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md)

## BGP

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b in vrf context
- peering with leaf's loopback interface

## FRR

```
# iserver get ocp ovn-bgp -v session                           

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------+-----------+-------------+-----+
| 1  | bm1-1 | frr-k8s-n6sbf | 68.68.0.6 | Established | N/A |
| 2  | bm1-1 | frr-k8s-n6sbf | 68.68.0.7 | Established | N/A |
| 3  | bm1-1 | frr-k8s-n6sbf | 67.67.0.7 | Established | N/A |
| 4  | bm1-1 | frr-k8s-n6sbf | 67.67.0.6 | Established | N/A | 
| 5  | bm1-2 | frr-k8s-rl2vf | 68.68.0.6 | Established | N/A |
| 6  | bm1-2 | frr-k8s-rl2vf | 67.67.0.7 | Established | N/A |
| 7  | bm1-2 | frr-k8s-rl2vf | 67.67.0.6 | Established | N/A |
| 8  | bm1-2 | frr-k8s-rl2vf | 68.68.0.7 | Established | N/A |
| 9  | bm1-3 | frr-k8s-57sdg | 68.68.0.7 | Established | N/A |
| 10 | bm1-3 | frr-k8s-57sdg | 67.67.0.6 | Established | N/A | 
| 11 | bm1-3 | frr-k8s-57sdg | 68.68.0.6 | Established | N/A |
| 12 | bm1-3 | frr-k8s-57sdg | 67.67.0.7 | Established | N/A |
+----+-------+---------------+-----------+-------------+-----+
```

```
# iserver get ocp ovn-bgp --cmd "show bgp vrf blue ipv4 unicast summary" --node bm1-1 -v exec

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP router identifier 67.67.67.10, local AS number 64667 vrf-id 20081
BGP table version 2
RIB entries 0, using 0 bytes of memory
Peers 2, using 1449 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
67.67.0.6       4      64600        95        89        0    0    0 00:44:52            0        0 N/A
67.67.0.7       4      64600        47        37        0    0    0 00:32:41            0        0 N/A

Total number of neighbors 2
```

```
get ocp ovn-bgp --cmd "show bgp vrf red ipv4 unicast summary" --node bm1-1 -v exec 

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP router identifier 68.68.68.10, local AS number 64667 vrf-id 20084
BGP table version 2
RIB entries 0, using 0 bytes of memory
Peers 2, using 1449 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
68.68.0.6       4      64600        95        90        0    0    0 00:45:14            0        0 N/A
68.68.0.7       4      64600        45        35        0    0    0 00:30:24            0        0 N/A

Total number of neighbors 2
```

[[Back]](./README.md)