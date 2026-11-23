# MetalLB - Get FRR configuration

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)

```
# iserver get ocp metallb --cluster bm1 -v frr --node bm1-3

OpenShift Workflow - OVNKubernetes - Get metallb information
============================================================

OpenShift Cluster: bm1

FRR speaker-g8lz6 [bm1-3]
-------------------------
Building configuration...

Current configuration:
!
frr version 8.5.3
frr defaults traditional
hostname bm1-3
log file /etc/frr/frr.log informational
log timestamp precision 3
no ip forwarding
no ipv6 forwarding
service integrated-vtysh-config
!
router bgp 64667
 no bgp ebgp-requires-policy
 no bgp default ipv4-unicast
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 ebgp-multihop
 !
 address-family ipv4 unicast
  network 1.1.1.1/32
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-in in
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 permit 1.1.1.1/32
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
!
ip nht resolve-via-default
!
ipv6 nht resolve-via-default
!
end
```

[[Back]](./README.md) [[State]](./get_state.md) [[Cli]](./get_cli.md) [[CRD]](./get_crd.md) [[Exec]](./get_exec.md) [[FRR]](./get_frr.md)