# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[FRR]](./frr-cudn.md) [[NX-OS]](./nxos-cudn.md)

## Route Advertisement

Requirements
- frr advertises cudn pod networks within vrf

## targetVRF

> [!NOTE]
> the cudn name **must** match the vrf name due to `targetVRF: auto` in RouteAdvertisements CRD

When the targetVRF field is omitted, the routes are leaked and advertised over the default VRF. Additionally, routes that were imported to the default VRF after the definition of the initial FRRConfiguration object are also imported into the blue VRF.

When the targetVRF is set to auto so that advertisements occur within the VRF device that corresponds to the individual networks that are selected. In this scenario, the pod subnet for blue is advertised over the blue VRF device, and the pod subnet for red is advertised over the red VRF device. Additionally, each BGP session imports routes to only the corresponding CUDN VRF as defined by the initial FRRConfiguration object.

Refer to details [here](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/route-advertisements#advertising-pod-ips-from-a-user-defined-network-over-bgp-with-vpn_about-route-advertisements).

## RouteAdvertisements CRD

> [!NOTE]
> `spec.frrConfigurationSelector` must select frr configuration by label

```
apiVersion: k8s.ovn.org/v1
kind: RouteAdvertisements
metadata:
  name: cudn
spec:
  targetVRF: auto
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
    - lastTransitionTime: "2026-04-13T08:48:16Z"
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
> CUDN subnets are advertised within the per-vrf sessions

```
$ oc get frrconfigurations.frrk8s.metallb.io -A
NAMESPACE           NAME                   AGE
openshift-frr-k8s   fabric-peering         41m
openshift-frr-k8s   ovnk-generated-fhzw6   34m
openshift-frr-k8s   ovnk-generated-nml55   34m
openshift-frr-k8s   ovnk-generated-z95vd   34m
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
  network 69.69.100.32/28
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
  network 69.69.100.32/28
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
ip prefix-list 67.67.0.6-blue-allowed-ipv4 seq 1 permit 69.69.100.32/28
ip prefix-list 67.67.0.7-blue-allowed-ipv4 seq 1 permit 69.69.100.32/28
ip prefix-list 68.68.0.6-red-allowed-ipv4 seq 1 permit 69.69.100.32/28
ip prefix-list 68.68.0.7-red-allowed-ipv4 seq 1 permit 69.69.100.32/28
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

[[Back]](./README.md) [[FRR]](./frr-cudn.md) [[NX-OS]](./nxos-cudn.md)