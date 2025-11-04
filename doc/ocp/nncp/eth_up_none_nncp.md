## Interface Ethernet 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Enable interface with no IP address | [Link](./eth_up_none_cli.md) | [Link](./eth_up_none_json.md) | See Below | [Link](./eth_up_none_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno1
      state: up
      type: ethernet
```

[[Back]](./README.md)