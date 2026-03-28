# Cluster User Defined Network (CUDN) - Primary

[[Back]](./README.md)

Usage for primary interface of Pod or Virtual Machine
- pod connects to primary cudn automatically without any extra configuration
- virtual machine must be [configured](./l2/vm.md) to connect to primary cudn

Provisioning
- namespace-scope with single primar per namespace
- topology [L2](./l2/overview.md) or [L3](./l3/overview.md)
- topology [localnet](./localnet/overview.md) **not supported**
- subnet mandatory for L3 with max one v4 and one v6 cidr defined

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: ypl2
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-y1
      - island-y2
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.0.0/24
    topology: Layer2
```

## Single primary enforcement

```
"status": {
    "conditions": [
        {
            "lastTransitionTime": "2026-03-20T14:29:41Z",
            "message": "primary network already exist in namespace \"island-a\": \"a-l2-p1\"",
            "reason": "SyncError",
            "status": "False",
            "type": "NetworkCreated"
        }
    ]
}
```

[[Back]](./README.md)