# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[CRD]](./create-nncp.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- two vrfs (blue and red)
- vlan encapsulation per vrf
- route to leaf loopback interface via bond vlan per vrf

## Task

```
[
    {
        "k8s": {
            "__enabled__": true,
            "description": "ethernet",
            "items": [
                {
                    "__type__": "nncp",
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
                        }
                    ]
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "description": "bond",
            "items": [
                {
                    "__type__": "nncp",
                    "interfaces": [
                        {
                            "type": "bond",
                            "name": "bond666",
                            "state": "up",
                            "mode": "active-backup",
                            "port": "ens11f0,ens11f1"
                        }
                    ]
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "description": "vlan vrf blue",
            "items": [
                {
                    "__type__": "nncp",
                    "node": "bm1-1",
                    "interfaces": [
                        {
                            "type": "vlan",
                            "base": "bond666",
                            "state": "up",
                            "vlan": 667,
                            "ipv4": "67.67.67.10/24"
                        }
                    ]
                },
                {
                    "__type__": "nncp",
                    "node": "bm1-2",
                    "interfaces": [
                        {
                            "type": "vlan",
                            "base": "bond666",
                            "state": "up",
                            "vlan": 667,
                            "ipv4": "67.67.67.11/24"
                        }
                    ]
                },
                {
                    "__type__": "nncp",
                    "node": "bm1-3",
                    "interfaces": [
                        {
                            "type": "vlan",
                            "base": "bond666",
                            "state": "up",
                            "vlan": 667,
                            "ipv4": "67.67.67.12/24"
                        }
                    ]
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "description": "vlan vrf red",
            "items": [
                {
                    "__type__": "nncp",
                    "node": "bm1-1",
                    "interfaces": [
                        {
                            "type": "vlan",
                            "base": "bond666",
                            "state": "up",
                            "vlan": 668,
                            "ipv4": "68.68.68.10/24"
                        }
                    ]
                },
                {
                    "__type__": "nncp",
                    "node": "bm1-2",
                    "interfaces": [
                        {
                            "type": "vlan",
                            "base": "bond666",
                            "state": "up",
                            "vlan": 668,
                            "ipv4": "68.68.68.11/24"
                        }
                    ]
                },
                {
                    "__type__": "nncp",
                    "node": "bm1-3",
                    "interfaces": [
                        {
                            "type": "vlan",
                            "base": "bond666",
                            "state": "up",
                            "vlan": 668,
                            "ipv4": "68.68.68.12/24"
                        }
                    ]
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "description": "vrf",
            "items": [
                {
                    "__type__": "nncp",
                    "interfaces": [
                        {
                            "type": "vrf",
                            "name": "blue",
                            "state": "up",
                            "port": "bond666.667",
                            "table": 667
                        },
                        {
                            "type": "vrf",
                            "name": "red",
                            "state": "up",
                            "port": "bond666.668",
                            "table": 668
                        }
                    ]
                }
            ]
        }
    },
    {
        "k8s": {
            "__enabled__": true,
            "description": "route",
            "items": [
                {
                    "__type__": "nncp",
                    "routes": [
                        {
                            "destination": "67.67.0.6/32",
                            "gateway": "67.67.67.67",
                            "interface": "bond666.667",
                            "table": 667
                        },
                        {
                            "destination": "67.67.0.7/32",
                            "gateway": "67.67.67.67",
                            "interface": "bond666.667",
                            "table": 667
                        },
                        {
                            "destination": "68.68.0.6/32",
                            "gateway": "68.68.68.68",
                            "interface": "bond666.668",
                            "table": 668
                        },
                        {
                            "destination": "68.68.0.7/32",
                            "gateway": "68.68.68.68",
                            "interface": "bond666.668",
                            "table": 668
                        }
                    ]
                }
            ]
        }
    }
]
```

[[Back]](./README.md) [[CRD]](./create-nncp.md)