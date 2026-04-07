# OVNKubernetes BGP - Configuration

[[Back]](../README.md)

`FRRConfiguration` is namespaced object that exposes configuration intent to Kubernetes API level as described in [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing). 

## Rules

Merging multiple configuration rules for a node
- A configuration must be self-contained (it cannot rely on others)
- A configuration can only add to the existing state
- A more permissive configuration can override a less permissive one
- It's possible to add a new neighbor to a router, or to advertise an additional prefix to a neighbor. However, there is no way to remove a component added by another configuration (for example, you can't remove a neighbor specified in another FRRConfiguration).

Conflicting configuration examples
- different ASN for the same router (in the same VRF)
- different ASN for the same neighbor (with the same IP and port)
- multiple BFD profiles with the same name, but different values

When the daemon cannot merge a set of configurations for a node, it reports the configuration as invalid (through metrics and the Status resource) and leaves the previous valid configuration in place.

## Example

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
```

> [!NOTE]
> route-maps and prefix lists follow default behavior of no-advertise and no-receive

Triggered configuration

```
router bgp 64667
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 ebgp-multihop
 !
 address-family ipv4 unicast
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-in in
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-inpl-ipv4 seq 1 deny any
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 deny any
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-allowed-ipv4
exit
!
route-map 6.6.6.6-in permit 3
 match ip address prefix-list 6.6.6.6-inpl-ipv4
exit
```

## iserver

- [get](../get_config.md)
- [add](../configuration_create.md)
- [delete](../configuration_delete.md)

[[Back]](../README.md)