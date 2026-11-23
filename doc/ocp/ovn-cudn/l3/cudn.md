# CUDN w/L3 Topology - Step 2: CUDN

[[Back]](./overview.md) [[Prev](./namespace.md)] [[Next]](./pod.md)

- role: Primary or Secondary
- subnets mandatory
  - max one v4 and one v6 subnet
  - host subnet

```
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: wpl3
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values:
      - island-w1
      - island-w2
  network:
    layer3:
      role: Primary
      subnets:
      - cidr: 66.66.0.0/24
        hostSubnet: 28
    topology: Layer3
```

CUDN triggers NAD with the following example configuration

```
{
  "cniVersion":"1.0.0",
  "joinSubnet":"100.65.0.0/16,fd99::/64",
  "name":"cluster_udn_wpl3",
  "netAttachDefName":"island-w1/wpl3",
  "role":"primary",
  "subnets":"66.66.0.0/24/28",
  "topology":"layer3",
  "type":"ovn-k8s-cni-overlay"
}
```

[[Back]](./overview.md) [[Prev](./namespace.md)] [[Next]](./pod.md)