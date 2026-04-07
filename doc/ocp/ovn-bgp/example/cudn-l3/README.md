# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/route-advertisements)

![Overview](../../../images/ovn-bgp/cudn.png)

[Cluster user defined network](../../../ovn-cudn/README.md): primary, topology L3, each assigned with two namespaces, labeled with bgp:enabled
- tenant-blue: 69.69.100.0/24 with hostSubnet:28
- tenant-red: 69.69.200.0/24 with hostSubnet:28
- check [task](./task-cudn.md) for setup details
- check [ip stack](./ip-stack.md) for ip stack state details

Goal := BGP advertise the subnets to upstream network from **default VRF in FRR**.

> [!NOTE]
> FRR on every cluster node expected to advertise hostSubnet allocated from CUDN CIDR

## Base BGP peering

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

## Route Advertisement

> [!NOTE]
> `spec.frrConfigurationSelector` must select frr configuration

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

```
$ oc get routeadvertisements cudn -o yaml
status:
  conditions:
  - lastTransitionTime: "2026-04-01T11:51:27Z"
    message: ovn-kubernetes cluster-manager validated the resource and requested the
      necessary configuration changes
    observedGeneration: 1
    reason: Accepted
    status: "True"
    type: Accepted
  status: Accepted
```

## Generated FRRConfiguration

```
$ oc get frrconfigurations.frrk8s.metallb.io -A
NAMESPACE           NAME                   AGE
openshift-frr-k8s   ovnk-generated-jzngc   3m
openshift-frr-k8s   ovnk-generated-lb2ht   3m
openshift-frr-k8s   ovnk-generated-zbbzm   3m
openshift-frr-k8s   test                   21h
```

```
$ oc get frrconfigurations.frrk8s.metallb.io -n openshift-frr-k8s ovnk-generated-l9m2c -o yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
spec:
  bgp:
    routers:
    - asn: 64667
      imports:
      - vrf: tenant-blue
      - vrf: tenant-red
      neighbors:
      - address: 6.6.6.6
        asn: 64600
        disableMP: true
        dualStackAddressFamily: false
        ebgpMultiHop: true
        passwordSecret: {}
        toAdvertise:
          allowed:
            mode: filtered
            prefixes:
            - 69.69.100.16/28
            - 69.69.200.0/28
        toReceive:
          allowed:
            mode: filtered
      - address: 6.6.6.7
        asn: 64600
        disableMP: true
        dualStackAddressFamily: false
        ebgpMultiHop: true
        passwordSecret: {}
        toAdvertise:
          allowed:
            mode: filtered
            prefixes:
            - 69.69.100.16/28
            - 69.69.200.0/28
        toReceive:
          allowed:
            mode: filtered
      prefixes:
      - 69.69.100.16/28
      - 69.69.200.0/28
    - asn: 64667
      imports:
      - vrf: default
      vrf: tenant-blue
    - asn: 64667
      imports:
      - vrf: default
      vrf: tenant-red
  nodeSelector:
    matchLabels:
      kubernetes.io/hostname: bm1-1
  raw: {}
```

## Triggered FRR configuration

> [!NOTE]
> FRR configuration on one node. Other node have different network and prefix lists configured. VRF subnets are imported to **default VRF** and then BGP advertised

```
router bgp 64667
 address-family ipv4 unicast
  network 69.69.100.16/28
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
 no bgp default ipv4-unicast
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
 no bgp default ipv4-unicast
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
ip prefix-list 6.6.6.6-inpl-ipv4 seq 1 deny any
ip prefix-list 6.6.6.7-inpl-ipv4 seq 1 deny any
ip prefix-list 6.6.6.6-allowed-ipv4 seq 1 permit 69.69.100.16/28
ip prefix-list 6.6.6.6-allowed-ipv4 seq 2 permit 69.69.200.0/28
ip prefix-list 6.6.6.7-allowed-ipv4 seq 1 permit 69.69.100.16/28
ip prefix-list 6.6.6.7-allowed-ipv4 seq 2 permit 69.69.200.0/28
!
ipv6 prefix-list 6.6.6.6-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 6.6.6.7-allowed-ipv6 seq 1 deny any
ipv6 prefix-list 6.6.6.6-inpl-ipv4 seq 2 deny any
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
```

## Advertised routes (FRR)

```
bm1-1# show bgp ipv4 unicast neighbors 6.6.6.6 advertised-routes detail 
BGP table version is 25, local router ID is 66.66.66.10, vrf id 0
Default local pref 100, local AS 64667

BGP routing table entry for 69.69.100.16/28, version 24
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  6.6.6.6 6.6.6.7
  Local
    0.0.0.0 from 0.0.0.0 (66.66.66.10)
      Origin IGP, metric 0, weight 32768, valid, sourced, local, best (First path received)
      Last update: Wed Apr  1 11:51:31 2026

BGP routing table entry for 69.69.200.0/28, version 25
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  6.6.6.6 6.6.6.7
  Local
    0.0.0.0 from 0.0.0.0 (66.66.66.10)
      Origin IGP, metric 0, weight 32768, valid, sourced, local, best (First path received)
      Last update: Wed Apr  1 11:51:31 2026

Total number of prefixes 2
```

## Received routes (NXOS)

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes detail vrf kali_test

BGP routing table entry for 69.69.100.16/28, version 125

  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50012

BGP routing table entry for 69.69.200.0/28, version 117

  AS-Path: 64667 , path sourced external to AS
    66.66.66.10 (metric 0) from 66.66.66.10 (66.66.66.10)
      Origin IGP, MED 0, localpref 100, weight 0
      Extcommunity: RT:64600:50012
```

> [!NOTE]
> Upstream device gets CUDN L3 subnets from every cluster node

```
leaf-A# show ip route vrf kali_test
69.69.100.0/28, ubest/mbest: 1/0
    *via 66.66.66.12, [20/0], 00:18:58, bgp-64600, external, tag 64667
69.69.100.16/28, ubest/mbest: 1/0
    *via 66.66.66.10, [20/0], 00:18:58, bgp-64600, external, tag 64667
69.69.100.32/28, ubest/mbest: 1/0
    *via 66.66.66.11, [20/0], 00:18:58, bgp-64600, external, tag 64667
69.69.200.0/28, ubest/mbest: 1/0
    *via 66.66.66.10, [20/0], 00:19:03, bgp-64600, external, tag 64667
69.69.200.16/28, ubest/mbest: 1/0
    *via 66.66.66.11, [20/0], 00:19:03, bgp-64600, external, tag 64667
69.69.200.32/28, ubest/mbest: 1/0
    *via 66.66.66.12, [20/0], 00:19:03, bgp-64600, external, tag 64667
```

## Primary CUDN enforcement

```
$ oc get routeadvertisements.k8s.ovn.org 
NAME   STATUS
cudn   Not Accepted: configuration error: selected network "cluster_udn_tenant-red" is not the default nor a primary network
```

[[Back]](../../README.md)