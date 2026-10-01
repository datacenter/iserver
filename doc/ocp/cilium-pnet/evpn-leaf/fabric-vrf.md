# Fabric VRF

[[Back]](./README.md)

VRF configuration 

```
!
! VRF red
!
vrf context red
  vni 66100 l3
  rd auto
  address-family ipv4 unicast
    route-target both auto
    route-target both auto evpn
!
router bgp 64000
  vrf red
    address-family ipv4 unicast
      advertise l2vpn evpn
      redistribute direct route-map fabric-rmap-redist-subnet
      maximum-paths ibgp 2
!
interface nve1
  member vni 66100 associate-vrf
```

```
!
! VRF blue
!
vrf context blue
  vni 66200 l3
  rd auto
  address-family ipv4 unicast
    route-target both auto
    route-target both auto evpn
!
router bgp 64000
  vrf blue
    address-family ipv4 unicast
      advertise l2vpn evpn
      redistribute direct route-map fabric-rmap-redist-subnet
      maximum-paths ibgp 2
!
interface nve1
  member vni 66200 associate-vrf
```

To help testing data plane forwarding, every spine has loopback interface into vrf, example for spine1

```
interface loopback2
  vrf member red
  ip address 100.64.100.101/32 tag 12345
  no shut
!
interface loopback3
  vrf member blue
  ip address 100.64.200.101/32 tag 12345
  no shut
!
```

[[Back]](./README.md)