## Inteface VLAN 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add VLAN | [Link](./vlan_add_cli.md) | [Link](./vlan_add_json.md) | See Below | [Link](./vlan_add_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - name: eno1.666
      state: up
      type: vlan
      vlan:
        base-iface: eno1
        id: 666
```

[[Back]](./README.md)