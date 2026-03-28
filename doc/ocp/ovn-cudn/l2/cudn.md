# CUDN w/L2 Topology - Step 2: CUDN

[[Back]](./overview.md) [[Prev](./namespace.md)] [[Next]](./pod.md)

- role: Primary or Secondary
- subnets optional
- max one v4 and one v6 subnet

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: vpl2
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-v1
      - island-v2
  network:
    layer2:
      role: Primary
      subnets:
      - 66.66.0.0/24
    topology: Layer2
```

CUDN triggers NAD with the following example configuration

```
{
  "cniVersion":"1.0.0",
  "joinSubnet":"100.65.0.0/16,fd99::/64",
  "name":"cluster_udn_vpl2",
  "netAttachDefName":"island-v1/vpl2",
  "role":"primary",
  "subnets":"66.66.0.0/24",
  "topology":"layer2",
  "transitSubnet":"100.88.0.0/16",
  "type":"ovn-k8s-cni-overlay"
}
```

[[Back]](./overview.md) [[Prev](./namespace.md)] [[Next]](./pod.md)