# UDN w/L3 Topology - CRD

[[Back]](../README.md) [[Prev]](../overview/l3.md) [[Next]](../create/l3_task.md)

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: p1-l3
  namespace: island
spec:
  layer3:
    role: Primary
    subnets:
    - cidr: 66.66.0.0/24
      hostSubnet: 28
  topology: Layer3
```

- role: Primary or Secondary
- mandatory cidr with host subnet
- max one v4 and one v6 subnet can be defined

[[Back]](../README.md) [[Prev]](../overview/l3.md) [[Next]](../create/l3_task.md)