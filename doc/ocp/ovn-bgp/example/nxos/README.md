# OVNKubernetes BGP - Peering with Nexus NX-OS fabric

[[Back]](../../README.md) [[OpenShift documentation]](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/bgp-routing#nw-metallb-frrconfiguration-crd_about-bgp-routing)

![Overview](../../../images/ovn-bgp/overview.png)

## Pre-requisites

- [enable](../../kb/enable.md) BGP
- configure bond and routing ([link](./nncp.md))
- configure Nexus devices ([link](./nexus.md))

## Configure BGP FRR

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: fabric-peering
  namespace: openshift-frr-k8s
spec:
  bgp:
    routers:
    - asn: 64667
      neighbors:
      - address: 6.6.6.6
        asn: 64600
        ebgpMultiHop: true
      - address: 6.6.6.7
        asn: 64600
        ebgpMultiHop: true
```

Check here for [task-way](./task.md)

## Verify BGP sessions

```
$ oc get bgpsessionstates.frrk8s.metallb.io -A
NAMESPACE           NAME          NODE    PEER      VRF   BGP           BFD
openshift-frr-k8s   bm1-1-drk4x   bm1-1   6.6.6.6         Established   N/A
openshift-frr-k8s   bm1-1-rc4m4   bm1-1   6.6.6.7         Established   N/A
openshift-frr-k8s   bm1-2-4cdrn   bm1-2   6.6.6.7         Established   N/A
openshift-frr-k8s   bm1-2-5x2rv   bm1-2   6.6.6.6         Established   N/A
openshift-frr-k8s   bm1-3-gx4zm   bm1-3   6.6.6.7         Established   N/A
openshift-frr-k8s   bm1-3-q52w9   bm1-3   6.6.6.6         Established   N/A
```

Check [here](./nxos_state.md) for details on nx-os side

[[Back]](../../README.md)