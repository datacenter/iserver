## Complex Scenario 

Add linux bridge with bonded vlan upstream as per the following diagram

![UC1](../images/ocp_nncp_uc1.png)

JSON | NNCP CRD | Outcome
--- | --- | ---
[Link](./uc1_add_json.md) | See Below | [Link](./uc1_add_outcome.md)

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
    - name: bond666.666
      state: up
      type: vlan
      vlan:
        base-iface: bond666
        id: 666
    - bridge:
        options:
          stp:
            enabled: false
        port:
        - name: bond666.666
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