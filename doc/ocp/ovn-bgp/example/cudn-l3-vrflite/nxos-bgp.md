# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[Networking]](./nxos-nncp.md) [[CUDN]](./nxos-cudn.md)

## BGP

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b in vrf context
- peering with leaf's loopback interface

## NX-OS

```
router bgp 64600
  vrf blue
    neighbor 67.67.67.0/24
      bfd multihop
      remote-as 64667
      update-source loopback67
      ebgp-multihop 5
  vrf red
    neighbor 68.68.68.0/24
      bfd multihop
      remote-as 64667
      update-source loopback68
      ebgp-multihop 5
```

```
leaf-A# show bgp ipv4 unicast summary vrf blue
Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
67.67.67.10     4 64667         48         49       29    0    0 00:43:29 0
67.67.67.11     4 64667         48         49       29    0    0 00:43:27 0
67.67.67.12     4 64667         49         50       29    0    0 00:44:18 0

leaf-A# show bgp ipv4 unicast summary vrf red
Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
68.68.68.10     4 64667         48         49       30    0    0 00:43:30 0
68.68.68.11     4 64667         48         49       30    0    0 00:43:29 0
68.68.68.12     4 64667         49         50       30    0    0 00:44:20 0
```

[[Back]](./README.md) [[Networking]](./nxos-nncp.md) [[CUDN]](./nxos-cudn.md)