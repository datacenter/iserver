## Inteface Bond 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add bond | [Link](./bond_add_cli.md) | See Below | [Link](./bond_add_nncp.md) | [Link](./bond_add_outcome.md)

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

[[Back]](./README.md)