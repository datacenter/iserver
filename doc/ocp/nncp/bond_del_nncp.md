## Inteface Bond 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete bond | [Link](./bond_del_cli.md) | [Link](./bond_del_json.md) | See Below | [Link](./bond_del_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - name: bond666
      state: absent
      type: bond
```

[[Back]](./README.md)