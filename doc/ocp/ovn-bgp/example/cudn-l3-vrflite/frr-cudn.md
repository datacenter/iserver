# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[NX-OS]](./nxos-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks within vrf

> [!NOTE]
> the cudn name **must** match the vrf name due to `targetVRF: auto` in RouteAdvertisements CRD

## FRR VRF blue

```
# iserver get ocp ovn-bgp --cmd "show bgp vrf blue ipv4 unicast summary" --node bm1-1 -v exec

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP router identifier 67.67.67.10, local AS number 64667 vrf-id 20081

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
67.67.0.6       4      64600        62        61        0    0    0 00:17:55            0        1 N/A
67.67.0.7       4      64600        15         9        0    0    0 00:05:44            0        1 N/A

Total number of neighbors 2
```

> [!NOTE]
> FRR on every cluster node expected to advertise hostSubnet allocated from CUDN CIDR

```
# iserver get ocp ovn-bgp --cmd "show bgp vrf blue ipv4 unicast" --node bm1-1 -v exec        

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP table version is 1, local router ID is 67.67.67.10, vrf id 20081
Default local pref 100, local AS 64667

    Network          Next Hop            Metric LocPrf Weight Path
 *> 69.69.100.32/28  0.0.0.0                  0         32768 i

Displayed  1 routes and 1 total paths
```

## FRR VRF red

```
# iserver get ocp ovn-bgp --cmd "show bgp vrf red ipv4 unicast summary" --node bm1-1 -v exec 

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP router identifier 68.68.68.10, local AS number 64667 vrf-id 20084

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
68.68.0.6       4      64600        64        63        0    0    0 00:19:20            0        1 N/A
68.68.0.7       4      64600        13         8        0    0    0 00:04:30            0        1 N/A

Total number of neighbors 2
```

> [!NOTE]
> FRR on every cluster node expected to advertise hostSubnet allocated from CUDN CIDR

```
# iserver get ocp ovn-bgp --cmd "show bgp vrf red ipv4 unicast" --node bm1-1 -v exec         

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
BGP table version is 1, local router ID is 68.68.68.10, vrf id 20084
Default local pref 100, local AS 64667

    Network          Next Hop            Metric LocPrf Weight Path
 *> 69.69.100.32/28  0.0.0.0                  0         32768 i

Displayed  1 routes and 1 total paths
```

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[NX-OS]](./nxos-cudn.md)