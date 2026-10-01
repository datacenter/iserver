# Private Network - Virtual Machine attachment

[[Back]](../README.md) [[Next]](./map.md)

Kubevirt VM can attach to private network using its primary and/or secondary (multus) interfaces as defined using **annotation** as well as `spec.template`
- VM cannot start if the target Private Network does not exist
- annotation takes effect **only** during the initial creation of the virtual machine

>[!CAUTION]
>Secondary interface attachment may require explicit ip stack configuration e.g., cloudInit, network data or any other vm-specific method for ip and routing configuration

## Primary network attachment

Scenario: private network `X` with ipv4 address `Y`
Notes:
- no reference to privnet subnet
- no reference to network attachment definition
- no reference to virtual machine's namespace
- `bridge` interface mode required

```yaml
spec:
  template:
    metadata:
      annotations:
        privnet.isovalent.com/network-attachment: '{"network": "X", "ipv4": "Y"}'
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: default
      networks:
      - name: default
        pod: {}
```

Refer to [example](../ew-test/vm3.md) for more details.

## Secondary network attachment

Scenario: Kubevirt VM in Namespace `N` with secondary connection to private network `X` with ipv4 address `Y` belonging to subnet `Z`
Notes:
- `NetworkAttachmentDefinition` reference in `spec.template.spec.networks[].multus.networkName` using `N/X-Z` format
- nad auto-generation feature must be[enabled](../enable.md)
- `bridge` interface mode required


```yaml
spec:
  template:
    metadata:
      annotations:
        privnet.isovalent.com/secondary-network-attachments: '[{"network": "X", "ipv4": "Y"}]'
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: eth1
      networks:
      - multus:
          networkName: N/X-Z
        name: eth1
```

Refer to [example](../ew-test/vm4.md) for more details.

## Primary and secondary network attachment

Combination of two attachments as above. Refer to [example](../ew-test/vm6.md) for more details.

[[Back]](../README.md) [[Next]](./map.md)