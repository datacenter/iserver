# OVNKubernetes BGP - Timer

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

## Default

- keepalive: 60s
- hold time: 180s

```
bm1-1# show bgp neighbors 6.6.6.6
BGP neighbor is 6.6.6.6, remote AS 64600, local AS 64667, external link
  Hold time is 180 seconds, keepalive interval is 60 seconds
  Configured hold time is 180 seconds, keepalive interval is 60 seconds
```

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
        holdTime: "90s"
        keepaliveTime: "30s"
      - address: 6.6.6.7
        asn: 64600
        ebgpMultiHop: true
        holdTime: "90s"
        keepaliveTime: "30s"
```

Triggered configuration

```
router bgp 64667
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 timers 30 90
 neighbor 6.6.6.7 remote-as 64600
 neighbor 6.6.6.7 timers 30 90
```

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 vrf kali_test
BGP neighbor is 66.66.66.10, remote AS 64667, ebgp link, Peer index 5
  Last read 00:00:10, hold time = 90, keepalive interval is 30 seconds
```

[[Back]](../../README.md)