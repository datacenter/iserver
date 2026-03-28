# UDN w/L2 Topology - Step 1: UDN

[[Back]](./overview.md) [[Prev](./task.md)] [[Next]](./pod.md)

Parameters
- role: Primary or Secondary
- subnets optional
- max one v4 and one v6 subnet

## Primary

> [!NOTE]
> Namespace must be labeled with `k8s.ovn.org/primary-user-defined-network: ''`

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: pl2
  namespace: island-p
spec:
  layer2:
    role: Primary
    subnets:
    - 66.66.0.0/24
  topology: Layer2
```

UDN triggers NAD with the following example configuration

```
{
  "cniVersion":"1.0.0",
  "joinSubnet":"100.65.0.0/16,fd99::/64",
  "name":"island-p_pl2",
  "netAttachDefName":"island-p/pl2",
  "role":"primary",
  "subnets":"66.66.0.0/24",
  "topology":"layer2",
  "transitSubnet":"100.88.0.0/16",
  "type":"ovn-k8s-cni-overlay"
}
```

## Secondary

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: sl2
  namespace: island-p
spec:
  layer2:
    role: Secondary
    subnets:
    - 66.66.1.0/24
  topology: Layer2
```

UDN triggers NAD with the following example configuration

```
{
    "cniVersion":"1.0.0",
    "name":"island-p_sl2",
    "netAttachDefName":"island-p/sl2",
    "role":"secondary",
    "subnets":"66.66.1.0/24",
    "topology":"layer2",
    "type":"ovn-k8s-cni-overlay"
}
```

[[Back]](./overview.md) [[Prev](./task.md)] [[Next]](./pod.md)