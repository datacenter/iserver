# MetalLB - BGP Peer

[[Back]](../README.md) [[iserver-way]](../create_peer.md)

`BGPPeer` custom resource is added and monitored by MetalLB [operator](./operator.md). It identifies the BGP router for MetalLB to communicate with, the AS number of the router, the AS number for MetalLB, and customizations for route advertisement. MetalLB advertises the routes for service load-balancer IP addresses to one or more BGP peers.

## Spec

Refer to [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html-single/ingress_and_load_balancing/index#nw-metallb-bgppeer-cr_configure-metallb-bgp-peers) for complete spec.

> [!CAUTION]
> BGPPeer spec parameters are case-sensitive and unknown silently ignored

Parameter | Type | Description
--- | --- | ---
myASN | int | cluster-wide ASN i.e. all BGPPeer CRs must have the same value
peerASN | int | ASN of remote end of the bgp session
peerAddress | string | remote neighbor's address
sourceAddress | string | optional, must be ipv4
peerPort | integer | optional, def. 179
holdTime | string | optional, min. 3s, def 180s
keepaliveTime | string | optional, requires and less than holdTime if defined, def. 60s
ebgpMultihop | boolean | optional, defaults to 255 (non-configurable)
routerID | string | optional and cluster-wide if defined
password | string | optional md5 password
passwordSecret | string | optional reference to basic-auth Secret that must be in metallb-system namespace
bfdProfile | string | optional reference to BFD
nodeSelector | object | match expression and labels based definition to select subset of nodes to apply bgp peering configuration

## CRD Example

```
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  namespace: metallb-system
  name: leaf1
spec:
  peerAddress: 6.6.6.6
  peerASN: 64600
  myASN: 64667
  ebgpMultiHop: true
```

## Triggered configration

```
router bgp 64667
 no bgp ebgp-requires-policy
 no bgp default ipv4-unicast
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
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
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 deny any
!
ipv6 prefix-list 6.6.6.6-allowed-ipv6 seq 1 deny any
!
route-map 6.6.6.6-in deny 20
exit
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-allowed-ipv4
exit
!
route-map 6.6.6.6-out permit 2
 match ipv6 address prefix-list 6.6.6.6-allowed-ipv6
exit
```

## Status

> [!CAUTION]
> BGPPeer has no status

```
# iserver get ocp metallb --cluster bm1 --node bm1-1 --cmd "show bgp ipv4 unicast summary" -v exec

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1

FRR speaker-wlgdt [bm1-1]
-------------------------
BGP router identifier 66.66.66.10, local AS number 64667 vrf-id 0
BGP table version 0
RIB entries 0, using 0 bytes of memory
Peers 1, using 725 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
6.6.6.6         4      64600         9         6        0    0    0 00:03:03            0        0 N/A

Total number of neighbors 1
```

[[Back]](../README.md) [[iserver-way]](../create_peer.md)