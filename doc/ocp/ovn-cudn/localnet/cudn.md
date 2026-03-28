# CUDN w/Localnet Topology - Step 3: CUDN

[[Back]](./overview.md) [[Prev](./namespace.md)] [[Next]](./pod.md)

> [!NOTE]
> physicalNetworkName e.g., `localnet-y` must be configured as bridge mapping in [Step 1](./ovs.md)

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

CUDN triggers NAD with the following example configuration

```
{
    "cniVersion":"1.0.0",
    "mtu":1500,
    "name":"cluster_udn_ysphy",
    "netAttachDefName":"island-y1/ysphy",
    "physicalNetworkName":"localnet-y",
    "role":"secondary",
    "subnets":"66.66.1.0/24",
    "topology":"localnet",
    "type":"ovn-k8s-cni-overlay"
}
```

[[Back]](./overview.md) [[Prev](./namespace.md)] [[Next]](./pod.md)