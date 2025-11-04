## Linux Bridge 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add linux bridge | [Link](./lb_add_cli.md) | See Below | [Link](./lb_add_nncp.md) | [Link](./lb_add_outcome.md)

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
                "type": "lb",
                "name": "br666",
                "state": "up",
                "ipv4": "10.66.66.66/24",
                "stp": false,
                "port": "enp216s0f0"
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
- ocp-my-cluster

Check nns data
--------------
- ocp-my-cluster linux bridge interface not found: br666
- ocp-my-cluster upstream interface found: enp216s0f0

Generated CRDs
--------------

apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy
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

Continue [Y/N]? y

Create NNCP
-----------
- my-policy
Waiting for [1]: my-policy
Status: Available
NNCP deleted
```

[[Back]](./README.md)