# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[FRR]](./frr-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks

## NX-OS

```
leaf-A# show bgp ipv4 unicast summary vrf kali_test
Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
66.66.66.10     4 64667        433        431      247    0    0 07:07:21 2
66.66.66.11     4 64667        433        431      247    0    0 07:07:21 2
66.66.66.12     4 64667        433        431      247    0    0 07:07:21 2
```

```
leaf-A# show ip route vrf kali_test
69.69.100.0/28, ubest/mbest: 1/0
    *via 66.66.66.10, [20/0], 00:07:54, bgp-64600, external, tag 64667
69.69.100.16/28, ubest/mbest: 1/0
    *via 66.66.66.12, [20/0], 00:07:53, bgp-64600, external, tag 64667
69.69.100.32/28, ubest/mbest: 1/0
    *via 66.66.66.11, [20/0], 00:07:54, bgp-64600, external, tag 64667
69.69.200.0/28, ubest/mbest: 1/0
    *via 66.66.66.10, [20/0], 00:07:59, bgp-64600, external, tag 64667
69.69.200.16/28, ubest/mbest: 1/0
    *via 66.66.66.11, [20/0], 00:07:59, bgp-64600, external, tag 64667
69.69.200.32/28, ubest/mbest: 1/0
    *via 66.66.66.12, [20/0], 00:07:59, bgp-64600, external, tag 64667
```

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes detail vrf kali_test

BGP routing table entry for 69.69.100.0/28, version 243

  Advertised path-id 1, VPN AF advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop, in rib, is extd
  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50012

BGP routing table entry for 69.69.200.0/28, version 234

  Advertised path-id 1, VPN AF advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop, in rib, is extd
  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50012
```

[[Back]](./README.md) [[Route Advertisement]](./create-ra.md) [[FRR]](./frr-cudn.md)