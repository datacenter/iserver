# OVNKubernetes BGP - Advertise routes

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

> [!NOTE]
> By default, FRR-K8s does not advertise the prefixes configured as part of a router configuration. To advertise the prefixes, you use the `toAdvertise` parameter

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
  neighbor 6.6.6.7 activate
  neighbor 6.6.6.7 route-map 6.6.6.7-out out
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 permit 69.69.100.0/24
ip prefix-list 6.6.6.6-allowed-ipv4 seq 2 permit 69.69.101.0/24
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-allowed-ipv4
exit
```

## FRR State

```
bm1-1# show bgp ipv4 unicast neighbors 6.6.6.6 advertised-routes 
BGP table version is 11, local router ID is 66.66.66.10, vrf id 0

    Network          Next Hop            Metric LocPrf Weight Path
 *> 69.69.100.0/24   0.0.0.0                  0         32768 i
 *> 69.69.101.0/24   0.0.0.0                  0         32768 i
```

## Remote Neighbor

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes vrf kali_test

   Network            Next Hop            Metric     LocPrf     Weight Path
*>e69.69.100.0/24     66.66.66.10              0                     0 64667 i
*>e69.69.101.0/24     66.66.66.10              0                     0 64667 i
```

[[Back]](../../README.md)