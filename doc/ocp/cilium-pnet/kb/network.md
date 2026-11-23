# Private Network - Create network

[[Back]](../README.md) [[iserver-way]](../create_network.md) [[Next]](./pod.md)

[ClusterwidePrivateNetwork](./icpn.md) custom resource defines private network instance e.g.,

```bash
iserver set ocp cilium pnet --mode network --network pnet1 --cidr4 10.10.10.0/24
```

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: blue
spec:
  subnets:
  - name: subnet-0
    cidrv4: 10.10.10.0/24
  networkAttachmentDefinitions:
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: test
```

Notes:
- at least one of `cidrv4`/`cidrv6` is required per subnet
- cidr value is immutable once configured
- cidr cannot overlap between the subnets within private network instance
- no overlap limitations across private network instances
- max. 256 subnets per network
- `spec:networkAttachmentDefinitions` is optional and will trigger network attachment definition creation in selected namespaces for secondary interface attachment

Other fields:
- [spec.subnets[].routes](./network_routes.md)
- [spec.subnets[].dhcp](./network_dhcp.md)
- [spec.vni](./network_vni.md)
- [spec.networkBridges](./network_inb.md)

[[Back]](../README.md) [[iserver-way]](../create_network.md) [[Next]](./pod.md)