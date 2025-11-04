## Linux Bridge 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add linux bridge | [Link](./lb_add_cli.md) | [Link](./lb_add_json.md) | See Below | [Link](./lb_add_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy-396f7b280266
spec:
  desiredState:
    interfaces:
    - bridge:
        options:
          stp:
            enabled: false
        port:
        - name: enp216s0f0
      ipv4:
        address:
        - ip: 10.66.66.66
          prefix-length: 24
        dhcp: false
        enabled: true
      name: br666
      state: up
      type: linux-bridge
```

[[Back]](./README.md)