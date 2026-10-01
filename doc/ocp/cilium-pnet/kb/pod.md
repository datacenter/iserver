# Private Network - POD attachment

[[Back]](../README.md) [[Next]](./vm.md)

POD can attach to private network using its primary and/or secondary (multus) interfaces as defined using **annotation**
- POD cannot start if the target Private Network does not exist
- annotation takes effect **only** during the initial creation of the Pod

## Primary network attachment

Scenario: private network `X` with ipv4 address `Y`
Notes:
- no reference to privnet subnet
- no reference to network attachment definition
- no reference to POD's namespace

```yaml
metadata:
  annotations:
    privnet.isovalent.com/network-attachment: '{"network": "X", "ipv4": "Y"}'
```

Refer to [example](../ew-test/p1.md) for more details.

## Secondary network attachment

Scenario: POD in namespace `N` with secondary connection to private network `X`, ipv4 address `Y` belonging to subnet `Z`
Notes:
- `N/X-Z` refers to `NetworkAttachmentDefinition` custom resource auto-generated as long as that functionality is [enabled](../enable.md)
- multiple network attachments can be defined

```yaml
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: N/X-Z@eth1
    privnet.isovalent.com/secondary-network-attachments: '[{"network": "X", "ipv4":"Y"}]'
```

Refer to [example](../ew-test/p2.md) for more details.

## Primary and secondary network attachment

Combination of two attachments as above. Refer to [example](../ew-test/p5.md) for more details.

[[Back]](../README.md) [[Next]](./vm.md)