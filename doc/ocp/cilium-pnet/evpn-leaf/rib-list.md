# VRF forwarding table

[[Back]](./README.md)

Every [private network](./private-network.md) has own forwarding table that controls egress packet forwarding i.e. [north-south](./traffic-ns.md). The forwarding table is built based on information received via BGP control plane filtered with [import route target](./import-route-target.md) with the private network (vrf) scope.

>[!CAUTION]
>Cilium does not support ECMP, so by default all egress traffic from a node uses a single link/VTEP next-hop, even though both node-to-leaf links are up and the ingress direction is actively using both.
 
Example

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF      Prefix               Owner          Protocol    NextHop
*       35644    100.64.200.201/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35644    100.64.200.101/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35644    100.64.200.102/32    bgp-overlay    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.101/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.102/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.202/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
*       35645    100.64.100.201/32    bgp-overlay    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac aa:aa:aa:aa:aa:aa
```

Notes
- route table entries based on bgp-overlay instance as defined in [IsovalentBGPClusterConfig](./server-bgp.md)
- all entries have next hop set to one of the directly connected leafs due to [next hop manipulation](./fabric-bgp.md)
- from kube node perspective, all remote prefixes are "hidden behind the leaf"
- kube nodes do not learn other vteps

[[Back]](./README.md)