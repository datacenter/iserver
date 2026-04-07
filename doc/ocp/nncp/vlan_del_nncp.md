## Inteface VLAN 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete VLAN | [Link](./vlan_del_cli.md) | [Link](./vlan_del_json.md) | See Below | [Link](./vlan_del_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - name: eno1.666
      state: absent
      type: vlan
      vlan:
        base-iface: eno1
        id: 666
```

[[Back]](./README.md)