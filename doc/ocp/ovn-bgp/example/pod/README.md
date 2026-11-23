# OVNKubernetes BGP - POD CIDR

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/route-advertisements)

The goal is advertise POD CIDR to network fabric using [route advertisement](../../kb/route_advertisement.md) configuration object. 

> [!NOTE]
> Every cluster node will announce its own POD CIDR

![Overview](../../../images/ovn-bgp/overview.png)

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
  name: pod
spec:
  advertisements:
  - PodNetwork
  networkSelectors:
  - networkSelectionType: DefaultNetwork
  frrConfigurationSelector:
    matchLabels:
      fabric: nxos
  nodeSelector: {}  
```

```
$ oc get routeadvertisements pod -o yaml
status:
  conditions:
  - lastTransitionTime: "2026-04-01T08:21:22Z"
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
openshift-frr-k8s   ovnk-generated-l9m2c   29m
openshift-frr-k8s   ovnk-generated-t4mgj   29m
openshift-frr-k8s   ovnk-generated-zz58b   29m
openshift-frr-k8s   test                   18h
```

```
$ oc get frrconfigurations.frrk8s.metallb.io -n openshift-frr-k8s ovnk-generated-l9m2c -o yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
spec:
  bgp:
    routers:
    - asn: 64667
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
            - 10.128.0.0/23
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
            - 10.128.0.0/23
        toReceive:
          allowed:
            mode: filtered
      prefixes:
      - 10.128.0.0/23
  nodeSelector:
    matchLabels:
      kubernetes.io/hostname: bm1-1
  raw: {}
```

## Advertised routes (FRR)

```
bm1-1# show bgp ipv4 unicast neighbors 6.6.6.6 advertised-routes 
BGP table version is 18, local router ID is 66.66.66.10, vrf id 0
Default local pref 100, local AS 64667

    Network          Next Hop            Metric LocPrf Weight Path
 *> 10.128.0.0/23    0.0.0.0                  0         32768 i
```

## Received routes (NXOS)

```
leaf-A# show bgp ipv4 unicast neighbors 66.66.66.10 routes vrf kali_test

Peer 66.66.66.10 routes for address family IPv4 Unicast:
BGP table version is 82, Local Router ID is 6.6.6.6

   Network            Next Hop            Metric     LocPrf     Weight Path
*>e10.128.0.0/23      66.66.66.10              0                     0 64667 i
```

```
leaf-A# show ip route vrf kali_test
10.128.0.0/23, ubest/mbest: 1/0
    *via 66.66.66.10, [20/0], 00:26:28, bgp-64600, external, tag 64667
10.129.0.0/23, ubest/mbest: 1/0
    *via 66.66.66.11, [20/0], 00:26:28, bgp-64600, external, tag 64667
10.130.0.0/23, ubest/mbest: 1/0
    *via 66.66.66.12, [20/0], 00:26:28, bgp-64600, external, tag 64667
```

[[Back]](../../README.md)