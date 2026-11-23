# VRF forwarding table

[[Back]](./README.md)

Every [private network](./private-network.md) has own forwarding table that controls egress packet forwarding i.e. [north-south](./traffic-ns.md). The forwarding table is built based on information received via BGP control plane filtered with [import route target](./import-route-target.md) defined per vrf or private network.

Example

```
$ oc exec -it cilium-4p49w -n cilium -- cilium-dbg shell -- rib/list
Best    VRF     Prefix             Owner            Protocol    NextHop
*       7440    100.64.100.101/32  bgp-instance0    eBGP        VXLANEncap vni 66100 vtep 100.64.20.101 inner-dst-mac 64:00:00:40:64:65
*       7440    100.64.100.102/32  bgp-instance0    eBGP        VXLANEncap vni 66100 vtep 100.64.20.102 inner-dst-mac 64:00:00:40:64:66
*       7440    100.64.100.201/32  bgp-instance0    eBGP        VXLANEncap vni 66100 vtep 100.64.20.201 inner-dst-mac 64:00:00:40:64:c9
*       7440    100.64.100.202/32  bgp-instance0    eBGP        VXLANEncap vni 66100 vtep 100.64.20.202 inner-dst-mac 64:00:00:40:64:ca
*       7441    100.64.200.101/32  bgp-instance0    eBGP        VXLANEncap vni 66200 vtep 100.64.20.101 inner-dst-mac 64:00:00:40:c8:65
*       7441    100.64.200.102/32  bgp-instance0    eBGP        VXLANEncap vni 66200 vtep 100.64.20.102 inner-dst-mac 64:00:00:40:c8:66
*       7441    100.64.200.201/32  bgp-instance0    eBGP        VXLANEncap vni 66200 vtep 100.64.20.201 inner-dst-mac 64:00:00:40:c8:c9
```

[[Back]](./README.md)