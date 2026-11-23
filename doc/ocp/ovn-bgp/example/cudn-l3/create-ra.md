# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[FRR]](./frr-cudn.md) [[NX-OS]](./nxos-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks

## RouteAdvertisements CRD

> [!NOTE]
> `spec.frrConfigurationSelector` must select frr configuration by label

```
apiVersion: k8s.ovn.org/v1
kind: RouteAdvertisements
metadata:
  name: cudn
spec:
  advertisements:
  - PodNetwork
  networkSelectors:
  - networkSelectionType: ClusterUserDefinedNetworks
    clusterUserDefinedNetworkSelector:
      networkSelector:
        matchLabels:
          bgp: "enabled"
  frrConfigurationSelector:
    matchLabels:
      fabric: nxos
  nodeSelector: {}
```

Expected

```
  status:
    conditions:
    - lastTransitionTime: "2026-04-11T16:19:21Z"
      message: ovn-kubernetes cluster-manager validated the resource and requested
        the necessary configuration changes
      observedGeneration: 1
      reason: Accepted
      status: "True"
      type: Accepted
    status: Accepted
```

## Generated configuration

> [!NOTE]
> VRF subnets are imported to **default VRF** and then BGP advertised

```
$ oc get frrconfigurations.frrk8s.metallb.io -A
NAMESPACE           NAME                   AGE
openshift-frr-k8s   fabric-peering         7h4m
openshift-frr-k8s   ovnk-generated-5674w   4m38s
openshift-frr-k8s   ovnk-generated-g7lm2   4m38s
openshift-frr-k8s   ovnk-generated-sh4hs   4m38s
```

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
 no bgp default ipv4-unicast
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 neighbor 6.6.6.6 remote-as 64600
 neighbor 6.6.6.6 ebgp-multihop
 neighbor 6.6.6.7 remote-as 64600
 neighbor 6.6.6.7 ebgp-multihop
 !
 address-family ipv4 unicast
  network 69.69.100.0/28
  network 69.69.200.0/28
  neighbor 6.6.6.6 activate
  neighbor 6.6.6.6 route-map 6.6.6.6-in in
  neighbor 6.6.6.6 route-map 6.6.6.6-out out
  neighbor 6.6.6.7 activate
  neighbor 6.6.6.7 route-map 6.6.6.7-in in
  neighbor 6.6.6.7 route-map 6.6.6.7-out out
  import vrf tenant-blue
  import vrf tenant-red
 exit-address-family
 !
 address-family ipv6 unicast
  import vrf tenant-blue
  import vrf tenant-red
 exit-address-family
exit
!
router bgp 64667 vrf tenant-blue
 no bgp ebgp-requires-policy
 no bgp hard-administrative-reset
 no bgp default ipv4-unicast
 no bgp graceful-restart notification
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 !
 address-family ipv4 unicast
  import vrf default
 exit-address-family
 !
 address-family ipv6 unicast
  import vrf default
 exit-address-family
exit
!
router bgp 64667 vrf tenant-red
 no bgp ebgp-requires-policy
 no bgp hard-administrative-reset
 no bgp default ipv4-unicast
 no bgp graceful-restart notification
 bgp graceful-restart preserve-fw-state
 no bgp network import-check
 !
 address-family ipv4 unicast
  import vrf default
 exit-address-family
 !
 address-family ipv6 unicast
  import vrf default
 exit-address-family
exit
!
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 permit 69.69.100.0/28
ip prefix-list 6.6.6.6-allowed-ipv4 seq 2 permit 69.69.200.0/28
ip prefix-list 6.6.6.6-inpl-ipv4 seq 1 deny any
ip prefix-list 6.6.6.7-allowed-ipv4 seq 1 permit 69.69.100.0/28
ip prefix-list 6.6.6.7-allowed-ipv4 seq 2 permit 69.69.200.0/28
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

[[Back]](./README.md) [[FRR]](./frr-cudn.md) [[NX-OS]](./nxos-cudn.md)