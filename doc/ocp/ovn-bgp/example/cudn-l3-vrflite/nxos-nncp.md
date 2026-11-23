# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[BGP]](./nxos-bgp.md) [[CUDN]](./nxos-cudn.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- two vrfs (blue and red)
- vlan encapsulation per vrf
- route to leaf loopback interface via bond vlan per vrf

## NX-OS

> [!NOTE]
> Showing leaf-A only

Physical interface
- with vlan 666 native (used in [non-vrf-lite setup](../cudn-l3/README.md))
- vlan 667 and 668 used for vrf blue and red

```
interface Ethernet1/49
  description bm1-1 ens11f0
  switchport mode trunk
  switchport access vlan 666
  switchport trunk native vlan 666
  spanning-tree port type edge trunk
  no shutdown
```

Vlan interface in anycast-gateway forwarding mode

```
interface Vlan667
  no shutdown
  vrf member blue
  no ip redirects
  ip address 67.67.67.67/24 tag 12345
  no ipv6 redirects
  fabric forwarding mode anycast-gateway
```

```
interface Vlan668
  no shutdown
  vrf member red
  no ip redirects
  ip address 68.68.68.68/24 tag 12345
  no ipv6 redirects
  fabric forwarding mode anycast-gateway
```

Looppback on leaf-a, leaf-b is .7/32

```
interface loopback67
  vrf member blue
  ip address 67.67.0.6/32 tag 12345
```

```
interface loopback68
  vrf member red
  ip address 68.68.0.6/32 tag 12345
```

## Verification

> [!NOTE]
> Cluster node has dedicated vlan interface and IP address configuration per-vrf

Cluster node reachable from both vlan source and loopback source within vrf blue

```
leaf-A# ping 67.67.67.10 vrf blue
64 bytes from 67.67.67.10: icmp_seq=0 ttl=63 time=1.239 ms

leaf-A# ping 67.67.67.10 source-interface loopback 67  vrf blue
64 bytes from 67.67.67.10: icmp_seq=0 ttl=63 time=0.772 ms
```

as well as vrf red

```
leaf-A# ping 68.68.68.10 vrf red
64 bytes from 68.68.68.10: icmp_seq=0 ttl=63 time=20.111 ms

leaf-A# ping 68.68.68.10 source-interface loopback 68 vrf red
64 bytes from 68.68.68.10: icmp_seq=0 ttl=63 time=0.801 ms
```

[[Back]](./README.md) [[BGP]](./nxos-bgp.md) [[CUDN]](./nxos-cudn.md)