## Interface Ethernet 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Disable interface with no IP address | [Link](./eth_down_none_cli.md) | [Link](./eth_down_none_json.md) | See Below | [Link](./eth_down_none_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno1
      state: down
      type: ethernet
```

[[Back]](./README.md)