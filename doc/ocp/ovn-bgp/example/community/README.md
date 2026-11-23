# OVNKubernetes BGP - Community

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

## Goal

- advertise two prefixes from BGP FRR towards network fabric
- one with 666:66 community

## FRR Configuration

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: fabric-peering
  namespace: openshift-frr-k8s
spec:
  bgp:
    routers:
    - asn: 64667
      neighbors:
      - address: 6.6.6.6
        asn: 64600
        ebgpMultiHop: true
        toAdvertise:
          allowed:
            mode: all
          withCommunity:
          - prefixes:
            - 69.69.100.0/24
            community: 666:66
      - address: 6.6.6.7
        asn: 64600
        ebgpMultiHop: true
        toAdvertise:
          allowed:
            mode: all
      prefixes:
      - 69.69.100.0/24
      - 69.69.101.0/24
```

Triggered configuration

```
router bgp 64667
 address-family ipv4 unicast
  network 69.69.100.0/24
  network 69.69.101.0/24
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
!
ip prefix-list 6.6.6.6-666:66-ip-community-prefixes seq 1 permit 69.69.100.0/24
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-666:66-ip-community-prefixes
 on-match next
 set community 666:66 additive
exit
```

## Remote Neighbor

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes detail vrf kali_test

BGP routing table entry for 69.69.100.0/24, version 59

  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Community: 666:66
      Extcommunity: RT:64600:50012

BGP routing table entry for 69.69.101.0/24, version 53

  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50012
```

[[Back]](../../README.md)