# UDN w/L2 Topology - CRD

[[Back]](../README.md) [[Prev]](../overview/l2.md) [[Next]](../create/l2_task.md)

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: a-l2-p1
  namespace: island-a
spec:
  layer2:
    role: Primary
    subnets:
    - 66.66.1.0/24
  topology: Layer2
```

- role: Primary or Secondary
- subnet optional
- if subnet not defined, ipam.disabled property must be set
- max one v4 and one v6 subnet can be defined

[[Back]](../README.md) [[Prev]](../overview/l2.md) [[Next]](../create/l2_task.md)