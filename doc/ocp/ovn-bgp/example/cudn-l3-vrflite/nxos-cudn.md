# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[FRR]](./frr-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks within vrf within vrf

> [!NOTE]
> the vrf name in nx-os "blue" and "red" are used to make it easier to read, however, these names are locally significant

## NX-OS: vrf blue

```
leaf-A# show bgp ipv4 unicast summary vrf blue
Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
67.67.67.10     4 64667         24         24       23    0    0 00:20:22 1
67.67.67.11     4 64667         24         24       23    0    0 00:20:21 1
67.67.67.12     4 64667         25         25       23    0    0 00:21:12 1

leaf-A# show ip route vrf blue
69.69.100.0/28, ubest/mbest: 1/0
    *via 67.67.67.11, [20/0], 00:20:28, bgp-64600, external, tag 64667
69.69.100.16/28, ubest/mbest: 1/0
    *via 67.67.67.12, [20/0], 00:21:19, bgp-64600, external, tag 64667
69.69.100.32/28, ubest/mbest: 1/0
    *via 67.67.67.10, [20/0], 00:20:29, bgp-64600, external, tag 64667

leaf-A# show bgp ipv4 unicast neighbors 67.67.67.10 routes detail vrf blue
BGP routing table entry for 69.69.100.32/28, version 21
  AS-Path: 64667 , path sourced external to AS
    67.67.67.10 (metric 0) from 67.67.67.10 (67.67.67.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50013
```

## NX-OS: vrf red

```
leaf-A# show bgp ipv4 unicast summary vrf red
Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
68.68.68.10     4 64667         25         25       24    0    0 00:21:30 1
68.68.68.11     4 64667         25         25       24    0    0 00:21:29 1
68.68.68.12     4 64667         26         26       24    0    0 00:22:20 1

leaf-A# show ip route vrf red
69.69.100.0/28, ubest/mbest: 1/0
    *via 68.68.68.12, [20/0], 00:22:29, bgp-64600, external, tag 64667
69.69.100.16/28, ubest/mbest: 1/0
    *via 68.68.68.11, [20/0], 00:21:38, bgp-64600, external, tag 64667
69.69.100.32/28, ubest/mbest: 1/0
    *via 68.68.68.10, [20/0], 00:21:39, bgp-64600, external, tag 64667

leaf-A# show bgp ipv4 unicast neighbors 68.68.68.10 routes detail vrf red
BGP routing table entry for 69.69.100.32/28, version 21
  AS-Path: 64667 , path sourced external to AS
    68.68.68.10 (metric 0) from 68.68.68.10 (68.68.68.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50014
```

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[FRR]](./frr-cudn.md)