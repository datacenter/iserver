# MetalLB - BGP Advertisement

[[Back]](../README.md) [[iserver-way]](../create_adv.md)

`BGPAdvertisement` custom resource configures how the cluster announces IP addresses to external peers.

## Spec

Refer to [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html-single/ingress_and_load_balancing/index#nw-metallb-bgpadvertisement-cr_about-advertising-ip-address-pool) for complete spec.

> [!CAUTION]
> BGPAdvertisement spec parameters are case-sensitive and unknown silently ignored. ! ALL ARE OPTIONAL !

Parameter | Type | Description
--- | --- | ---
aggregationLength | int | pecifies the number of bits to include in a 32-bit CIDR mask
aggregationLengthV6 | int | like above for ipv6
communities | string | specifies one or more BGP communities; each community is specified as two 16-bit values separated by the colon character or [community alias](./community.md)
localPref | int | in case of iBGP sessions
ipAddressPools | string | list of [ip address pools](./pool.md) to be advertised selected by name
ipAddressPoolSelectors | string | like above but using match expressions (e.g. labels)
nodeSelectors | string | limit the nodes to announce as next hops, def. all the nodes are announced as next hops
peers | string | limit the advertisement to specific [BGPpeer](./bgp_peer.md) resources selected by name

## CRD Example

```
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: basic
  namespace: metallb-system
```

This will advertise all LoadBalancer service ips (/32) allocated from [ip address pools](./pool.md) via every defined [bgp peer](./bgp_peer.md).

```
leaf-r12a# show bgp ipv4 unicast summary vrf kali_test

Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
66.66.66.10     4 64667         32         31      178    0    0 00:27:13 1
66.66.66.11     4 64667         32         31      178    0    0 00:27:13 1
66.66.66.12     4 64667         29         29      178    0    0 00:25:13 1
```

```
leaf-r12a# show bgp ipv4 unicast vrf kali_test

   Network            Next Hop            Metric     LocPrf     Weight Path
* e69.69.69.1/32      66.66.66.12              0                     0 64667 i
* e                   66.66.66.11              0                     0 64667 i
*>e                   66.66.66.10              0                     0 64667 i
```

[[Back]](../README.md) [[iserver-way]](../create_adv.md)