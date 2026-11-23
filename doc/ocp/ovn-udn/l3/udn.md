# UDN w/L3 Topology - Step 1: UDN

[[Back]](./overview.md) [[Prev](./task.md)] [[Next]](./pod.md)

Parameters
- role: Primary or Secondary
- subnets mandatory
- max one v4 and one v6 subnet

## Primary

> [!NOTE]
> Namespace must be labeled with `k8s.ovn.org/primary-user-defined-network: ''`

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: pl3
  namespace: island-q
spec:
  layer3:
    role: Primary
    subnets:
    - cidr: 66.66.0.0/24
      hostSubnet: 28
  topology: Layer3
```

UDN triggers NAD with the following example configuration

```
{
  "cniVersion":"1.0.0",
  "joinSubnet":"100.65.0.0/16,fd99::/64",
  "name":"island-q_pl3",
  "netAttachDefName":"island-q/pl3",
  "role":"primary",
  "subnets":"66.66.0.0/24/28",
  "topology":"layer3",
  "type":"ovn-k8s-cni-overlay"
}
```

## Secondary

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: sl3
  namespace: island-q
spec:
  layer3:
    role: Secondary
    subnets:
    - cidr: 66.66.1.0/24
      hostSubnet: 28
  topology: Layer3
```

UDN triggers NAD with the following example configuration

```
{
  "cniVersion":"1.0.0",
  "name":"island-q_sl3",
  "netAttachDefName":"island-q/sl3",
  "role":"secondary",
  "subnets":"66.66.1.0/24/28",
  "topology":"layer3",
  "type":"ovn-k8s-cni-overlay"
}
```

[[Back]](./overview.md) [[Prev](./task.md)] [[Next]](./pod.md)