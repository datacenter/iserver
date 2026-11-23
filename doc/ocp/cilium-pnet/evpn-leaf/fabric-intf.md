# Leaf 

[[Back]](./README.md) [[Next]](./fabric-bgp.md)

## loopbacks

Leaf | Type | IP | Interface
--- | --- | --- | ---
Leaf1 | routing | 100.64.10.201/32 | loopback0
Leaf1 | vtep | 100.64.20.201/32 | loopback1
Leaf1 | vrf:red | 100.64.100.201/32 | loopback2
Leaf1 | vrf:blue | 100.64.200.201/32 | loopback3
Leaf2 | routing | 100.64.10.202/32 | loopback0
Leaf2 | vtep | 100.64.20.202/32 | loopback1
Leaf2 | vrf:red | 100.64.100.202/32 | loopback2
Leaf2 | vrf:blue | 100.64.200.202/32 | loopback3

>[!NOTE]
>Leaf1 showed only for brevity

```
interface loopback0
  description Routing loopback interface
  ip address 100.64.10.201/32
  ip router ospf UNDERLAY area 0.0.0.0
  ip pim sparse-mode
!
interface loopback1
  description VTEP loopback interface
  ip address 100.64.20.201/32
  ip router ospf UNDERLAY area 0.0.0.0
  ip pim sparse-mode
!
interface loopback2
  vrf member red
  ip address 100.64.100.201/32 tag 12345
!
interface loopback3
  vrf member blue
  ip address 100.64.200.201/32 tag 12345
```

## p2p connection with server (RFC5549)

Leaf | Interface | IP address | Server
--- |--- | --- | --- 
Leaf1 | Ethernet1/11 | **IPv6 link-local** | bm1-1 eno5
Leaf2 | Ethernet1/11 | **IPv6 link-local** | bm1-1 eno6
Leaf1 | Ethernet1/12 | **IPv6 link-local** | bm1-2 eno5
Leaf2 | Ethernet1/12 | **IPv6 link-local** | bm1-2 eno6
Leaf1 | Ethernet1/13 | **IPv6 link-local** | bm1-2 eno5
Leaf2 | Ethernet1/13 | **IPv6 link-local** | bm1-2 eno6

>[!NOTE]
>Leaf1 showed only for brevity

```
interface Ethernet1/11
  description bm1-1 eno5
  ttag
  ttag-strip
  mtu 9216
  fec fc-fec
  medium p2p
  ip forward
  ipv6 address use-link-local-only
  ipv6 link-local use-bia
  no shutdown
!
interface Ethernet1/12
  description bm1-2 eno5
  ttag
  ttag-strip
  mtu 9216
  fec fc-fec
  medium p2p
  ip forward
  ipv6 address use-link-local-only
  ipv6 link-local use-bia
  no shutdown
!
interface Ethernet1/13
  description bm1-3 eno5
  ttag
  ttag-strip
  mtu 9216
  fec fc-fec
  medium p2p
  ip forward
  ipv6 address use-link-local-only
  ipv6 link-local use-bia
  no shutdown
```

[[Back]](./README.md) [[Next]](./fabric-bgp.md)