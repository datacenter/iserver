# Fabric VRF

[[Back]](./README.md) [[addressing scheme]](./address.md)

VRF configuration is on spines **only**
- "route-target import/export 666:<XXXXX>" is only needed if "rewrite-evpn-rt-asn" is not used
- "rewrite-evpn-rt-asn" seems to be applied only in the ingress direction (Cilium to fabric) with this configuration
- "peer type fabric external" is not used because this setup is not running as VXLAN multi site

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
    route-target import 666:66100 evpn
    route-target export 666:66100 evpn
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
    route-target import 666:66200 evpn
    route-target export 666:66200 evpn
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

[[Back]](./README.md) [[addressing scheme]](./address.md)