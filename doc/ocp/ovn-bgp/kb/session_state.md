# OVNKubernetes BGP - Session State

[[Back]](../README.md)

`BGPSessionState` namespaced resource shows the BGP session state of FRR-k8s daemon running inside the pod based on [configuration](./configuration.md) and provider network configuration and state. 

> [!NOTE]
> BGPSessionState CRD is added to the cluster once BGP is [enabled](./enable.md)

## CLI

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

```
$ oc get bgpsessionstates.frrk8s.metallb.io -n openshift-frr-k8s bm1-1-drk4x -o yam
spec: {}
status:
  bfdStatus: N/A
  bgpStatus: Established
  node: bm1-1
  peer: 6.6.6.6
```

## iserver

- [get session](../get_session.md)

[[Back]](../README.md)