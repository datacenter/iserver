# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[CRD]](./create-nncp.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- no vlan encapsulation
- route to leaf loopback interface via bond

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
                    "node": "bm1-1",
                    "interfaces": [
                        {
                            "type": "bond",
                            "name": "bond666",
                            "state": "up",
                            "mode": "active-backup",
                            "port": "ens11f0,ens11f1",
                            "ipv4": "66.66.66.10/24"
                        }
                    ]
                },
                {
                    "__type__": "nncp",
                    "node": "bm1-2",
                    "interfaces": [
                        {
                            "type": "bond",
                            "name": "bond666",
                            "state": "up",
                            "mode": "active-backup",
                            "port": "ens11f0,ens11f1",
                            "ipv4": "66.66.66.11/24"
                        }
                    ]
                },
                {
                    "__type__": "nncp",
                    "node": "bm1-3",
                    "interfaces": [
                        {
                            "type": "bond",
                            "name": "bond666",
                            "state": "up",
                            "mode": "active-backup",
                            "port": "ens11f0,ens11f1",
                            "ipv4": "66.66.66.12/24"
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

[[Back]](./README.md) [[CRD]](./create-nncp.md)