# CUDN Namespace Selection

[[Back]](./README.md) 

Cluster User Defined Network (CUDN) is cluster-scope object and at the same time it selects the namespaces where the cudn is operational.

Namespace selection by name or label.

If the CUDN is primary, then selected namespaces must be defined with `k8s.ovn.org/primary-user-defined-network` label.

## Namespace selection by name

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: tenant-a
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-a1
      - island-a2
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.0.0/24
    topology: Layer2
```

## Namespace selection by label

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: tenant-a
spec:
  namespaceSelector:
    matchLabels:
    - "tenant": "a",
    - "tenant": "b"
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.0.0/24
    topology: Layer2
```

## Namespace ready for primary (c)udn

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
  name: island
```

[[Back]](./README.md) 