## Inteface Bond 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add bond | [Link](./bond_add_cli.md) | [Link](./bond_add_json.md) | See Below | [Link](./bond_add_outcome.md)

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
      link-aggregation:
        mode: active-backup
        options:
          miimon: '140'
        port:
        - eno1
        - eno2
      mtu: 1400
      name: bond666
      state: up
      type: bond
```

[[Back]](./README.md)