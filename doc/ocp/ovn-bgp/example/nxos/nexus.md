# OVNKubernetes - Peering with Nexus NX-OS fabric

[[Back]](./README.md)

![Overview](../../../images/ovn-bgp/overview.png)

## Leaf A

> [!NOTE]
> Leaf B has similar configuration with different loopback ip address

```
feature bgp
feature bfd
!
vlan 666
  name kali-bgp-test
  vn-segment 30010
!
route-map fabric-rmap-redist-subnet permit 10
  match tag 12345
!
vrf context kali_test
  vni 50012 l3
  rd auto
  address-family ipv4 unicast
    route-target both auto
    route-target both auto evpn
  address-family ipv6 unicast
    route-target both auto
    route-target both auto evpn
!
interface Vlan666
  no shutdown
  vrf member kali_test
  no ip redirects
  ip address 66.66.66.66/24 tag 12345
  no ipv6 redirects
  fabric forwarding mode anycast-gateway
!
interface Ethernet1/49
  description bm1-1 ens11f0
  switchport access vlan 666
  no shutdown
!
interface Ethernet1/50
  description bm1-2 ens11f0
  switchport access vlan 666
  no shutdown
!
interface Ethernet1/51
  description bm1-3 ens11f0
  switchport access vlan 666
  no shutdown
!
interface loopback66
  vrf member kali_test
  ip address 6.6.6.6/32 tag 12345
!
router bgp 64600
  vrf kali_test
    address-family ipv4 unicast
      advertise l2vpn evpn
      redistribute direct route-map fabric-rmap-redist-subnet
      maximum-paths ibgp 2
    address-family ipv6 unicast
      advertise l2vpn evpn
      redistribute direct route-map fabric-rmap-redist-subnet
      maximum-paths ibgp 2
    neighbor 66.66.66.0/24
      bfd multihop
      remote-as 64667
      update-source loopback66
      ebgp-multihop 5
      address-family ipv4 unicast
```

[[Back]](./README.md)