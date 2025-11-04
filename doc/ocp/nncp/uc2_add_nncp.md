## Complex Scenario 

Add bonded vlan interface with static IPv4 routes.

JSON | NNCP CRD | Outcome
--- | --- | ---
[Link](./uc2_add_json.md) | See Below | [Link](./uc2_add_outcome.md)

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - name: enp216s0f0
      state: up
      type: ethernet
    - name: enp216s0f1
      state: up
      type: ethernet
    - link-aggregation:
        mode: active-backup
        port:
        - enp216s0f0
        - enp216s0f1
      name: bond666
      state: up
      type: bond
    - ipv4:
        address:
        - ip: 10.66.66.66
          prefix-length: 24
        dhcp: false
        enabled: true
      name: bond666.666
      state: up
      type: vlan
      vlan:
        base-iface: bond666
        id: 666
    routes:
      config:
      - destination: 10.77.77.0/24
        next-hop-address: 10.66.66.1
        next-hop-interface: bond666.666
```

[[Back]](./README.md)