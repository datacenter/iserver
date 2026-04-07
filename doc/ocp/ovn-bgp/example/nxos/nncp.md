# OVNKubernetes - Peering with Nexus NX-OS fabric

[[Back]](./README.md)

![Overview](../../../images/ovn-bgp/overview.png)

## Goal

- cluster node should have bond interface with upstream switches in active-standby mode
- per cluster node IPv4 address from the same subnet extended via upstream ToR devices
- static route to looback ips used for bpg peering

## Task

> [!NOTE]
> Showing only one cluster node configuration for brevity. Other nodes have different ipv4 address only.

```
[
    {
        "k8s": {
            "__enabled__": true,
            "items": [
                {
                    "__type__": "nncp",
                    "node": "bm1-1",
                    "policy": "my-policy",
                    "delete": true,
                    "check": true,
                    "interfaces": [
                        {
                            "type": "eth",
                            "name": "ens11f0",
                            "state": "up",
                            "ipv4": "none"
                        },
                        {
                            "type": "eth",
                            "name": "ens11f1",
                            "state": "up",
                            "ipv4": "none"
                        },
                        {
                            "type": "bond",
                            "name": "bond666",
                            "state": "up",
                            "mode": "active-backup",
                            "port": "ens11f0,ens11f1",
                            "ipv4": "66.66.66.10/24"
                        }
                    ],
                    "routes": [
                        {
                            "destination": "6.6.6.6/32",
                            "gateway": "66.66.66.66",
                            "interface": "bond666"
                        },
                        {
                            "destination": "6.6.6.7/32",
                            "gateway": "66.66.66.66",
                            "interface": "bond666"
                        }
                    ]
                }
            ]
        }
    }
]
```

## Applied Configuration

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy-527a6e439f10
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: ens11f0
      state: up
      type: ethernet
    - ipv4:
        enabled: false
      name: ens11f1
      state: up
      type: ethernet
    - ipv4:
        address:
        - ip: 66.66.66.10
          prefix-length: 24
        dhcp: false
        enabled: true
      link-aggregation:
        mode: active-backup
        port:
        - ens11f0
        - ens11f1
      name: bond666
      state: up
      type: bond
    routes:
      config:
      - destination: 6.6.6.6/32
        next-hop-address: 66.66.66.66
        next-hop-interface: bond666
      - destination: 6.6.6.7/32
        next-hop-address: 66.66.66.66
        next-hop-interface: bond666
  nodeSelector:
    kubernetes.io/hostname: bm1-1
```

[[Back]](./README.md)