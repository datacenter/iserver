# Floating IP

## Filter by fixed address

```
# iserver get osp fip --cluster pod1 --fixed 15.100.1.102

Cluster: pod1

Floating IP [#1]
----------------

+--------+-------------+--------+----------+--------------+-------------------+------------+---------------+---------------+
| Status | Floating    | Tenant | Network  | Fixed        | MAC               | Network    | VM            | Router        |
+--------+-------------+--------+----------+--------------+-------------------+------------+---------------+---------------+
| ACTIVE | 10.58.28.83 | smi5gc | external | 15.100.1.102 | fa:16:3e:38:40:30 | management | smi5gc/server | smi5gc-router | 
+--------+-------------+--------+----------+--------------+-------------------+------------+---------------+---------------+

Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp fip --cluster pod1 --fixed 15.100.1.102

{
    "duration": 5225,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 4353,
        "total_time": 4353
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-18 16:49:52.123124	True	1482	get	floating_ips
2023-11-18 16:49:52.480426	True	344	get	tenants
2023-11-18 16:49:52.777069	True	288	get	networks
2023-11-18 16:49:53.013583	True	214	get	routers
2023-11-18 16:49:55.654795	True	2025	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)