# OVNKubernetes BGP - Route advertisement

[[Back]](../README.md)

`RouteAdvertisements` is cluster-scoped object that allows sharing [pod](../example/pod/README.md) and egress IP routes between OpenShift cluster and the provider network. 

> [!NOTE]
> `RouteAdvertisements` CRD is added to the cluster once BGP with route advertisement feature is [enabled](./enable_route_advertisement.md)

## Example

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

## FRRConfiguration selection

Route advertisement must select [FRRConfiguration](./configuration.md) that will be augmented with generated configuration based on route advertisement content as well as OpenShift cluster state.

```
apiVersion: k8s.ovn.org/v1
kind: RouteAdvertisements
metadata:
  name: pod
spec:
  frrConfigurationSelector:
    matchLabels:
      fabric: nxos
```

where spec.frrConfigurationSelector labels match 

```
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: fabric-peering
  namespace: openshift-frr-k8s
  labels:
    fabric: nxos
spec:
  ...
```

In case no frr configuration is selected

```
$ oc get routeadvertisements.k8s.ovn.org 
NAME      STATUS
default   Not Accepted: configuration pending: no FRRConfigurations selected
```

[[Back]](../README.md)