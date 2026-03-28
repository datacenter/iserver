# User Defined Network (UDN) - Secondary

[[Back]](./README.md)

Secondary UDN is for extra interface connection of Pod or Virtual Machine
- pod must be [configured](./l2/pod.md) to connect to secondary udn
- virtual machine must be [configured](./l2/vm.md) to connect to secondary udn

Provisioning
- namespace-scope with multiple secondary per namespace
- topology [L2](./l2/overview.md), [L3](./l3/overview.md) or [localnet](./localnet/overview.md)
- subnet mandatory for L3 with max one v4 and one v6 cidr defined

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: ysphy
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-y1
      - island-y2
  network:
    localnet:
      physicalNetworkName: localnet-y
      role: Secondary
      subnets:
      - 66.66.1.0/24
    topology: Localnet
```

[[Back]](./README.md)