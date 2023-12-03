# Router

## Default output

```
# iserver get osp rtr --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "status": "Green",
            "adminTick": "Green"
        },
        "id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "name": "smi5gc-router",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "admin_state_up": true,
        "status": "ACTIVE",
        "availability_zones": [
            "nova"
        ],
        "ha": true,
        "routes": [],
        "created_at": "2022-08-04T13:38:50Z",
        "updated_at": "2022-08-04T13:39:13Z",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.81",
                "subnet_name": "subnet-ext",
                "gateway_ip": "10.58.28.94",
                "cidr": "10.58.28.80/28"
            }
        ],
        "snat": true,
        "adminTick": "\u2713",
        "haTick": "\u2713",
        "snatTick": "\u2713",
        "created_age": "472d",
        "updated_age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "external"
    }
]
```

Developer

```
# iserver get osp rtr --cluster pod1 -o json

{
    "duration": 2695,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 2498,
        "total_time": 2498
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 3
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 12:15:56.928790	True	1823	get	routers
2023-11-20 12:15:57.210160	True	259	get	tenants
2023-11-20 12:15:57.476896	True	251	get	networks
2023-11-20 12:15:57.652464	True	165	get	subnets
```

[[Back]](./RouterGet.md)