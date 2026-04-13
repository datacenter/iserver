# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md)

## BGP

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b in vrf context
- peering with leaf's loopback interface

## FRR

> [!CAUTION]
> `disableMP` must be set to true

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: fabric-peering
  namespace: openshift-frr-k8s
  labels:
    fabric: nxos
spec:
  bgp:
    routers:
    - asn: 64667
      vrf: blue
      neighbors:
      - address: 67.67.0.6
        asn: 64600
        ebgpMultiHop: true
        disableMP: true
      - address: 67.67.0.7
        asn: 64600
        ebgpMultiHop: true
        disableMP: true
    - asn: 64667
      vrf: red
      neighbors:
      - address: 68.68.0.6
        asn: 64600
        ebgpMultiHop: true
        disableMP: true
      - address: 68.68.0.7
        asn: 64600
        ebgpMultiHop: true
        disableMP: true
```

## Generated configuration

```
# iserver get ocp ovn-bgp --cluster bm1 --cmd "show run" --node bm1-1 -v exec 


OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

FRR frr-k8s-n6sbf [bm1-1]
-------------------------
Building configuration...

Current configuration:
!
frr version 8.5.3
frr defaults traditional
hostname bm1-1
log file /etc/frr/frr.log informational
log timestamp precision 3
no ip forwarding
no ipv6 forwarding
service integrated-vtysh-config
!
router bgp 64667 vrf blue
 no bgp ebgp-requires-policy
 no bgp default ipv4-unicast
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 67.67.0.6 remote-as 64600
 neighbor 67.67.0.6 ebgp-multihop
 neighbor 67.67.0.7 remote-as 64600
 neighbor 67.67.0.7 ebgp-multihop
 !
 address-family ipv4 unicast
  neighbor 67.67.0.6 activate
  neighbor 67.67.0.6 route-map 67.67.0.6-blue-in in
  neighbor 67.67.0.6 route-map 67.67.0.6-blue-out out
  neighbor 67.67.0.7 activate
  neighbor 67.67.0.7 route-map 67.67.0.7-blue-in in
  neighbor 67.67.0.7 route-map 67.67.0.7-blue-out out
 exit-address-family
exit
!
router bgp 64667 vrf red
 no bgp ebgp-requires-policy
 no bgp default ipv4-unicast
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 68.68.0.6 remote-as 64600
 neighbor 68.68.0.6 ebgp-multihop
 neighbor 68.68.0.7 remote-as 64600
 neighbor 68.68.0.7 ebgp-multihop
 !
 address-family ipv4 unicast
  neighbor 68.68.0.6 activate
  neighbor 68.68.0.6 route-map 68.68.0.6-red-in in
  neighbor 68.68.0.6 route-map 68.68.0.6-red-out out
  neighbor 68.68.0.7 activate
  neighbor 68.68.0.7 route-map 68.68.0.7-red-in in
  neighbor 68.68.0.7 route-map 68.68.0.7-red-out out
 exit-address-family
exit
!
ip prefix-list 67.67.0.6-blue-inpl-ipv4 seq 1 deny any
ip prefix-list 67.67.0.7-blue-inpl-ipv4 seq 1 deny any
ip prefix-list 68.68.0.6-red-inpl-ipv4 seq 1 deny any
ip prefix-list 68.68.0.7-red-inpl-ipv4 seq 1 deny any
ip prefix-list 67.67.0.6-blue-allowed-ipv4 seq 1 deny any
ip prefix-list 67.67.0.7-blue-allowed-ipv4 seq 1 deny any
ip prefix-list 68.68.0.6-red-allowed-ipv4 seq 1 deny any
ip prefix-list 68.68.0.7-red-allowed-ipv4 seq 1 deny any
!
ipv6 prefix-list 67.67.0.6-blue-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 67.67.0.6-blue-inpl-ipv4 seq 2 deny any
ipv6 prefix-list 67.67.0.7-blue-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 67.67.0.7-blue-inpl-ipv4 seq 2 deny any
ipv6 prefix-list 68.68.0.6-red-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 68.68.0.6-red-inpl-ipv4 seq 2 deny any
ipv6 prefix-list 68.68.0.7-red-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 68.68.0.7-red-inpl-ipv4 seq 2 deny any
!
route-map 67.67.0.6-blue-out permit 1
 match ip address prefix-list 67.67.0.6-blue-allowed-ipv4
exit
!
route-map 67.67.0.6-blue-out permit 2
 match ipv6 address prefix-list 67.67.0.6-blue-allowed-ipv6
exit
!
route-map 67.67.0.6-blue-in permit 3
 match ip address prefix-list 67.67.0.6-blue-inpl-ipv4
exit
!
route-map 67.67.0.6-blue-in permit 4
 match ipv6 address prefix-list 67.67.0.6-blue-inpl-ipv4
exit
!
route-map 67.67.0.7-blue-out permit 1
 match ip address prefix-list 67.67.0.7-blue-allowed-ipv4
exit
!
route-map 67.67.0.7-blue-out permit 2
 match ipv6 address prefix-list 67.67.0.7-blue-allowed-ipv6
exit
!
route-map 67.67.0.7-blue-in permit 3
 match ip address prefix-list 67.67.0.7-blue-inpl-ipv4
exit
!
route-map 67.67.0.7-blue-in permit 4
 match ipv6 address prefix-list 67.67.0.7-blue-inpl-ipv4
exit
!
route-map 68.68.0.6-red-out permit 1
 match ip address prefix-list 68.68.0.6-red-allowed-ipv4
exit
!
route-map 68.68.0.6-red-out permit 2
 match ipv6 address prefix-list 68.68.0.6-red-allowed-ipv6
exit
!
route-map 68.68.0.6-red-in permit 3
 match ip address prefix-list 68.68.0.6-red-inpl-ipv4
exit
!
route-map 68.68.0.6-red-in permit 4
 match ipv6 address prefix-list 68.68.0.6-red-inpl-ipv4
exit
!
route-map 68.68.0.7-red-out permit 1
 match ip address prefix-list 68.68.0.7-red-allowed-ipv4
exit
!
route-map 68.68.0.7-red-out permit 2
 match ipv6 address prefix-list 68.68.0.7-red-allowed-ipv6
exit
!
route-map 68.68.0.7-red-in permit 3
 match ip address prefix-list 68.68.0.7-red-inpl-ipv4
exit
!
route-map 68.68.0.7-red-in permit 4
 match ipv6 address prefix-list 68.68.0.7-red-inpl-ipv4
exit
!
ip nht resolve-via-default
!
ipv6 nht resolve-via-default
!
end


View: state (def), cli, config, exec, frr, ra, ra-config, session, all

```

[[Back]](./README.md)