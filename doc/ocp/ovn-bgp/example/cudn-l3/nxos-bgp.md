# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[Networking]](./nxos-nncp.md) [[CUDN]](./nxos-cudn.md)

## BGP

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b
- peering with leaf's loopback interface

## NX-OS

```
router bgp 64600
  vrf kali_test
    neighbor 66.66.66.0/24
      bfd multihop
      remote-as 64667
      update-source loopback66
      ebgp-multihop 5
      address-family ipv4 unicast
        soft-reconfiguration inbound
```

```
leaf-A# show bgp ipv4 unicast summary vrf kali_test
Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
66.66.66.10     4 64667        370        369      231    0    0 06:06:00 0
66.66.66.11     4 64667        370        369      231    0    0 06:06:00 0
66.66.66.12     4 64667        370        369      231    0    0 06:06:00 0
```

[[Back]](./README.md) [[Networking]](./nxos-nncp.md) [[CUDN]](./nxos-cudn.md)