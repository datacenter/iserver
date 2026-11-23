## Complex Scenario

[[Back]](./README.md)

Add linux bridge with bonded vlan upstream as per the following diagram

![UC1](../images/ocp_nncp_uc1.png)

Check how to delete such setup at the bottom of the page.

Task | NNCP CRD | Outcome
 --- | --- | ---
See Below | [Link](./uc1_add_nncp.md) | [Link](./uc1_add_outcome.md)

## Create

```
[
  {
    "k8s": {
      "items": [
        {
          "node": "__all__",
          "policy": "my-policy",
          "delete": true,
          "check": true,
          "interfaces": [
            {
              "type": "eth",
              "name": "enp216s0f0",
              "state": "up"
            },
            {
              "type": "eth",
              "name": "enp216s0f1",
              "state": "up"
            },
            {
              "type": "bond",
              "name": "bond666",
              "state": "up",
              "mode": "active-backup",
              "port": "enp216s0f0,enp216s0f1"
            },
            {
              "type": "vlan",
              "base": "bond666",
              "vlan": 666,
              "state": "up"
            },
            {
              "type": "lb",
              "name": "br666",
              "state": "up",
              "ipv4": "10.66.66.66/24",
              "stp": false,
              "port": "bond666.666"
            }
          ]
        }
      ]
    }
  }
]
```

Notes:
- delete (true|false(def)) attribute controls if nncp policy is deleted once it is applied
- check (true(def)|false) attribute controls if logical checks are made against the NodeNetworkState object per node e.g., interface name
- node attribute controls on the nodeSelector value in NNCP CRD
  - value "__all__" has no associated nodeSelector value
  - value "__workers__" configures "node-role.kubernetes.io/worker: ''" as nodeSelector
  - any other value is expected to be proper node name in the clsuter and configures "kubernetes.io/hostname: 'value" as nodeSelector

## Delete

```
[
  {
    "k8s": {
      "items": [
        {
          "node": "__all__",
          "policy": "my-policy",
          "delete": true,
          "check": true,
          "interfaces": [
            {
              "type": "bond",
              "name": "bond666",
              "state": "absent"
            },
            {
              "type": "vlan",
              "base": "bond666",
              "vlan": 666,
              "state": "absent"
            },
            {
              "type": "lb",
              "name": "br666",
              "state": "absent"
            }
          ]
        }
      ]
    }
  }
]
```

### Generated NNCP CRD

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
    - name: bond666.666
      state: absent
      type: vlan
      vlan:
        base-iface: bond666
        id: 666
    - name: br666
      state: absent
      type: linux-bridge
```

[[Back]](./README.md)