## Complex Scenario

[[Back]](./README.md)

Add bonded vlan interface with static IPv4 routes.

Task | NNCP CRD | Outcome
 --- | --- | ---
See Below | [Link](./uc2_add_nncp.md) | [Link](./uc2_add_outcome.md)

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
              "state": "up",
              "ipv4": "10.66.66.66/24"
            }
          ],
          "routes": [
            {
              "destination": "10.77.77.0/24",
              "gateway": "10.66.66.1",
              "interface": "bond666.666"
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