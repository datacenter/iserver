## Inteface VLAN 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add VLAN | [Link](./vlan_add_cli.md) | See Below | [Link](./vlan_add_nncp.md) | [Link](./vlan_add_outcome.md)

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
                "type": "vlan",
                "base": "eno1",
                "vlan": 666,
                "state": "up"
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
- my-node base interface found: eno1
- my-node vlan interface not found: eno1.666

Generated CRDs
--------------

apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
spec:
  desiredState:
    interfaces:
    - name: eno1.666
      state: up
      type: vlan
      vlan:
        base-iface: eno1
        id: 666



Create NNCP
-----------
- my-policy
Waiting for [1]: my-policy
NNCP deleted
```

[[Back]](./README.md)