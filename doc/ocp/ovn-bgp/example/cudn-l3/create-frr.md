# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md)

## BGP

Requirements
- local asn 64667, remote asn 64600
- ebgp multihop 
- every cluster node establishes bgp peering with leaf-a and leaf-b
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
      neighbors:
      - address: 6.6.6.6
        asn: 64600
        ebgpMultiHop: true
        disableMP: true
      - address: 6.6.6.7
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
router bgp 64667
 no bgp ebgp-requires-policy
 no bgp hard-administrative-reset
 no bgp default ipv4-unicast
 no bgp graceful-restart notification
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 ebgp-multihop
 neighbor 6.6.6.7 remote-as 64600
 neighbor 6.6.6.7 ebgp-multihop
 !
 address-family ipv4 unicast
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-in in
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
  neighbor 6.6.6.7 activate
  neighbor 6.6.6.7 route-map 6.6.6.7-in in
  neighbor 6.6.6.7 route-map 6.6.6.7-out out
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 deny any
ip prefix-list 6.6.6.6-inpl-ipv4 seq 1 deny any
ip prefix-list 6.6.6.7-allowed-ipv4 seq 1 deny any
ip prefix-list 6.6.6.7-inpl-ipv4 seq 1 deny any
!
ipv6 prefix-list 6.6.6.6-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 6.6.6.6-inpl-ipv4 seq 2 deny any
ipv6 prefix-list 6.6.6.7-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 6.6.6.7-inpl-ipv4 seq 2 deny any
!
route-map 6.6.6.6-out permit 1
 match ip address prefix-list 6.6.6.6-allowed-ipv4
exit
!
route-map 6.6.6.6-out permit 2
 match ipv6 address prefix-list 6.6.6.6-allowed-ipv6
exit
!
route-map 6.6.6.6-in permit 3
 match ip address prefix-list 6.6.6.6-inpl-ipv4
exit
!
route-map 6.6.6.6-in permit 4
 match ipv6 address prefix-list 6.6.6.6-inpl-ipv4
exit
!
route-map 6.6.6.7-out permit 1
 match ip address prefix-list 6.6.6.7-allowed-ipv4
exit
!
route-map 6.6.6.7-out permit 2
 match ipv6 address prefix-list 6.6.6.7-allowed-ipv6
exit
!
route-map 6.6.6.7-in permit 3
 match ip address prefix-list 6.6.6.7-inpl-ipv4
exit
!
route-map 6.6.6.7-in permit 4
 match ipv6 address prefix-list 6.6.6.7-inpl-ipv4
exit
!
ip nht resolve-via-default
!
ipv6 nht resolve-via-default
!
end
```

[[Back]](./README.md)