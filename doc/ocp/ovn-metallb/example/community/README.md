# MetalLB - Community

[[Back]](../../README.md)

## Goal

- advertise service ips with 666:66 [community](../../kb/community.md)

## Configuration


```
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: adv1
  namespace: metallb-system
  resourceVersion: '18182692'
spec:
  communities:
  - 666:66
```

Triggered configuration

```
ip prefix-list 6.6.6.6-666:66-ip-community-prefixes seq 1 permit 1.1.1.1/32
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-666:66-ip-community-prefixes
 on-match next
 set community 666:66 additive
exit
```

## Remote Neighbor

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes detail vrf kali_test

BGP routing table entry for 1.1.1.1/32, version 212

  Path type: external, path is valid, not best reason: newer EBGP path, no labeled nexthop, is extd
  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Community: 666:66
      Extcommunity: RT:64600:50012
```

[[Back]](../../README.md)