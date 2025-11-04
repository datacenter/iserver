## Complex Scenario

Add linux bridge with bonded vlan upstream as per the following diagram

![UC1](../images/ocp_nncp_uc1.png)

Check how to delete such setup at the bottom of the page.

JSON | NNCP CRD | Outcome
 --- | --- | ---
See Below | [Link](./uc1_add_nncp.md) | [Link](./uc1_add_outcome.md)

### Input

```
[
    {
        "node": "_all_",
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
```

Notes:
- delete (true|false(def)) attribute controls if nncp policy is deleted once it is applied
- check (true(def)|false) attribute controls if logical checks are made against the NodeNetworkState object per node e.g., interface name
- node attribute controls on the nodeSelector value in NNCP CRD
  - value "_all_" has no associated nodeSelector value
  - value "_workers_" configures "node-role.kubernetes.io/worker: ''" as nodeSelector
  - any other value is expected to be proper node name in the clsuter and configures "kubernetes.io/hostname: 'value" as nodeSelector

### Execution

```
# iserver create k8s nncp --file C:\tmp\nncp.json 
Cluster: my-cluster (type: ocp)

Get nns data
------------
- my-node

Check nns data
--------------
- my-node ethernet interface found: enp216s0f0

Get nns data
------------
- my-node

Check nns data
--------------
- my-node ethernet interface found: enp216s0f1

Get nns data
------------
- my-node

Check nns data
--------------
- my-node bond interface not found: bond666
- my-node ethernet interface found: enp216s0f0
- my-node ethernet interface found: enp216s0f1

Get nns data
------------
- my-node

Check nns data
--------------
- [WARNING] my-node base interface not found: bond666
- my-node vlan interface not found: bond666.666

Get nns data
------------
- my-node

Check nns data
--------------
- my-node linux bridge interface not found: br666
- [WARNING] my-node upstream interface not found: bond666.666

Generated CRDs
--------------

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


Continue [Y/N]? y

Create NNCP
-----------
- my-policy
Waiting for [1]: my-policy
Status: Available
NNCP deleted
```

## Delete input

```
[
    {
        "node": "_all_",
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
```

## Generated NNCP CRD

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