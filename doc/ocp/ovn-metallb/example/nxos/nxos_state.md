# OVNKubernetes - Peering with Nexus NX-OS fabric

[[Back]](./README.md)

![Overview](../../../images/ovn-bgp/overview.png)

## All neighbors up

```
leaf-A# show bgp ipv4 unicast summary vrf kali_test
BGP summary information for VRF kali_test, address family IPv4 Unicast
BGP router identifier 6.6.6.6, local AS number 64600
BGP table version is 10, IPv4 Unicast config peers 4, capable peers 3
3 network entries and 4 paths using 988 bytes of memory

Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
66.66.66.10     4 64667        119        120       10    0    0 01:56:49 0
66.66.66.11     4 64667        119        120       10    0    0 01:56:49 0
66.66.66.12     4 64667        119        120       10    0    0 01:56:49 0
```

## Nothing received

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes vrf kali_test

Peer 66.66.66.10 routes for address family IPv4 Unicast:
BGP table version is 10, Local Router ID is 6.6.6.6

   Network            Next Hop            Metric     LocPrf     Weight Path

leaf-A#
```

## Neighbor details

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 vrf kali_test
BGP neighbor is 66.66.66.10, remote AS 64667, ebgp link, Peer index 5
  Peer is an instance of prefix peering 66.66.66.0/24
  BGP version 4, remote router ID 66.66.66.10
  Neighbor previous state = OpenConfirm
  BGP state = Established, up for 01:53:40
  Neighbor vrf: kali_test
  Using loopback66 as update source for this peer
  Peer is directly attached, interface Vlan666
  BFD live-detection is configured and enabled, state is Invalid
    Forced multihop session
  External BGP peer might be up to 5 hops away
  Last read 00:00:40, hold time = 180, keepalive interval is 60 seconds
```

[[Back]](./README.md)