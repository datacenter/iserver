# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[Task]](./cudn-crd-task.md) [[IP Stack]](./nns-cudn.md)

![Overview](../../../images/ovn-bgp/cudn-vrf-lite.png)

## CUDN

Requirements
- primary cudn
- L3 topology
- assigned with two namespaces each
- bgp:enabled labeled
- cudn blue: 69.69.100.0/24 with hostSubnet:28
- cudn red: 69.69.100.0/24 with hostSubnet:28
- cudn subnets bgp advertised within vrf as such no problem with overal from bgp perspective

## CRD

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: red
  name: island-r1
```

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: red
  name: island-r2
```

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: blue
  name: island-b1
```

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: blue
  name: island-b2
```

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  labels:
    bgp: enabled
  name: blue
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-b1
      - island-b2
  network:
    layer3:
      role: Primary
      subnets:
      - cidr: 69.69.100.0/24
        hostSubnet: 28
    topology: Layer3
```

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  labels:
    bgp: enabled
  name: red
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-r1
      - island-r2
  network:
    layer3:
      role: Primary
      subnets:
      - cidr: 69.69.100.0/24
        hostSubnet: 28
    topology: Layer3
```

[[Back]](./README.md) [[Task]](./cudn-crd-task.md) [[IP Stack]](./nns-cudn.md)