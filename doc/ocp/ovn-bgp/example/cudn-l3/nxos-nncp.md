# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[BGP]](./nxos-bgp.md) [[CUDN]](./nxos-cudn.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- no vlan encapsulation
- route to leaf loopback interface via bond

## NX-OS

> [!NOTE]
> Showing leaf-A only

Physical interface with vlan 666 native

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
interface Vlan666
  no shutdown
  vrf member kali_test
  no ip redirects
  ip address 66.66.66.66/24 tag 12345
  no ipv6 redirects
  fabric forwarding mode anycast-gateway
```

Looppback on leaf-a, leaf-b is 6.6.6.7/32

```
interface loopback66
  vrf member kali_test
  ip address 6.6.6.6/32 tag 12345
```

## Verification

Cluster node (66.66.66.10) reachable from both vlan source and loopback source

```
leaf-A# ping 66.66.66.10 vrf kali_test
64 bytes from 66.66.66.10: icmp_seq=0 ttl=63 time=0.939 ms

leaf-A# ping 66.66.66.10 source-interface loopback 66 vrf kali_test
64 bytes from 66.66.66.10: icmp_seq=0 ttl=63 time=0.796 ms
```

[[Back]](./README.md) [[BGP]](./nxos-bgp.md) [[CUDN]](./nxos-cudn.md)