## Interface Ethernet 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Configure IP address | [Link](./eth_ip_cli.md) | [Link](./eth_ip_json.md) | See Below | [Link](./eth_ip_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 10.66.66.66
          prefix-length: 24
        dhcp: false
        enabled: true
      name: eno1
      state: up
      type: ethernet
```

[[Back]](./README.md)