# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](../../README.md)

![Overview](../../../images/ovn-bgp/cudn-vrf-lite.png)

## Goal

BGP advertise [cluster user defined networks](../../../ovn-cudn/README.md) using **VRF-Lite in FRR**.

> [!NOTE]
> FRR on every cluster node expected to advertise hostSubnet allocated from CUDN CIDR

## Networking setup

Requirements
- [OVN-K routing via host](./host-routing.md)
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- two vrfs (blue and red)
- vlan encapsulation per vrf
- route to leaf loopback interface via bond vlan per vrf

Details
- [NodeNetworkConfigurationPolicy](./create-nncp.md), [task-way](./create-nncp-task.md)
- [cluster node ip stack](./nns-nncp.md)
- [leaf state](./nxos-nncp.md)

## BGP Peering

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b in vrf context
- peering with leaf's loopback interface

Details
- [enable ovn-bgp](../../feature_enable.md)
- [FRRConfiguration](./create-frr.md)
- [frr state](./frr-bgp.md)
- [leaf state](./nxos-bgp.md)

## CUDN

Requirements
- primary cudn
- L3 topology
- assigned with two namespaces each
- bgp:enabled labeled
- cudn blue: 69.69.100.0/24 with hostSubnet:28
- cudn red: 69.69.100.0/24 with hostSubnet:28
- cudn subnets bgp advertised within vrf as such no problem with overal from bgp perspective

Details
- [cudn crds](./cudn-crd.md), [task-way](./cudn-crd-task.md)
- [cluster node ip stack](./nns-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks within vrf

Details
- [enable route advertisements](../../ra_enable.md)
- [RouteAdvertisements](./create-ra.md)
- [frr state](./frr-cudn.md)
- [leaf state](./nxos-cudn.md)

[[Back]](../../README.md)