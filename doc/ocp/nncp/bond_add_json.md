## Inteface Bond 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add bond | [Link](./bond_add_cli.md) | See Below | [Link](./bond_add_nncp.md) | [Link](./bond_add_outcome.md)

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
                "type": "bond",
                "name": "bond666",
                "state": "up",
                "ipv4": "10.66.66.66/24",
                "mode": "active-backup",
                "port": "eno1,eno2",
                "mtu": 1400,
                "miimon": "140"
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
Cluster: bm1 (type: ocp)

Get nns data
------------
- ocp-bm1

Check nns data
--------------
- ocp-bm1 bond interface not found: bond666
- ocp-bm1 ethernet interface found: eno1
- ocp-bm1 ethernet interface found: eno2

Generated CRDs
--------------

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


Continue [Y/N]? y

Create NNCP
-----------
- my-policy
Waiting for [1]: my-policy
Waiting for [1]: my-policy
NNCP deleted
```

[[Back]](./README.md)