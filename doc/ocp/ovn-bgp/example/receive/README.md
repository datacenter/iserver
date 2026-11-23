# OVNKubernetes BGP - Receive routes

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

> [!NOTE]
> By default, FRR-K8s does not process any prefixes advertised by a neighbor. You can use the `toReceive` parameter to process such addresses.

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
        toReceive:
          allowed:
            mode: all
      - address: 6.6.6.7
        asn: 64600
        ebgpMultiHop: true
        toReceive:
          allowed:
            mode: all
```

Triggered configuration

```
router bgp 64667
  address-family ipv4 unicast
    neighbor 6.6.6.6 route-map 6.6.6.6-in in
    neighbor 6.6.6.7 route-map 6.6.6.7-in in
  exit-address-family
exit
!
ip prefix-list 6.6.6.6-inpl-ipv4 seq 1 permit any
route-map 6.6.6.6-in permit 3
  match ip address prefix-list 6.6.6.6-inpl-ipv4
exit
!
```

Filtering example

```
spec:
  bgp:
    routers:
    - asn: 64667
      neighbors:
      - address: 6.6.6.6
        asn: 64600
        ebgpMultiHop: true
        toReceive:
          allowed:
            prefixes:
            - prefix: 192.168.1.0/24
            - prefix: 192.169.2.0/24
              ge: 25
              le: 28
```

## Remote Neighbor

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 advertised-routes vrf kali_test

Peer 66.66.66.10 routes for address family IPv4 Unicast:
BGP table version is 14, Local Router ID is 6.6.6.6

   Network            Next Hop            Metric     LocPrf     Weight Path
*>r6.6.6.6/32         0.0.0.0                  0        100      32768 ?
*>i6.6.6.7/32         100.65.0.212             0        100          0 ?
*>r7.7.7.7/32         0.0.0.0                  0        100      32768 ?
*>r66.66.66.0/24      0.0.0.0                  0        100      32768 ?
```

## FRR State

```
bm1-1# show bgp ipv4 unicast neighbors 6.6.6.6 routes 
BGP table version is 5, local router ID is 66.66.66.10, vrf id 0
Default local pref 100, local AS 64667

    Network          Next Hop            Metric LocPrf Weight Path
    6.6.6.6/32       6.6.6.6                  0             0 64600 ?
 *> 6.6.6.7/32       6.6.6.6                                0 64600 ?
 *> 7.7.7.7/32       6.6.6.6                  0             0 64600 ?
 *> 66.66.66.0/24    6.6.6.6                  0             0 64600 ?

Displayed  4 routes and 8 total paths
```

## IP route

```
$ ip r
7.7.7.7 nhid 914 via 66.66.66.66 dev bond666 proto bgp metric 20
```

[[Back]](../../README.md)