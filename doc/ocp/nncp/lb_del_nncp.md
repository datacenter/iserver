## Linux Bridge 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete linux bridge | [Link](./lb_del_cli.md) | [Link](./lb_del_json.md) | See Below | [Link](./lb_del_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - name: br666
      state: absent
      type: linux-bridge
```

[[Back]](./README.md)