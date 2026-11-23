# OVNKubernetes BGP - MD5 authentication

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

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
        password: topsecret
      - address: 6.6.6.7
        asn: 64600
        ebgpMultiHop: true
        password: topsecret
```

Triggered configuration

```
router bgp 64667
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 password topsecret
 neighbor 6.6.6.7 remote-as 64600
 neighbor 6.6.6.7 password topsecret
```

## Nexus NX-OS

```
router bgp 64600
  vrf kali_test
    neighbor 66.66.66.0/24
      remote-as 64667
      password 3 4f14e72cd068426ecf66a5dc62d1f203
```

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 vrf kali_test
BGP neighbor is 66.66.66.10, remote AS 64667, ebgp link, Peer index 5
  TCP MD5 authentication is set (enabled)
```

[[Back]](../../README.md)