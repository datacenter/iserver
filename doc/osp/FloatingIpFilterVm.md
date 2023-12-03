# Floating IP

## Filter by vm

```
# iserver get osp fip --cluster pod1 --vm smi5gc/portal

Cluster: pod1

Floating IP [#1]
----------------

+--------+-------------+--------+----------+--------------+-------------------+------------+---------------+---------------+
| Status | Floating    | Tenant | Network  | Fixed        | MAC               | Network    | VM            | Router        |
+--------+-------------+--------+----------+--------------+-------------------+------------+---------------+---------------+
| ACTIVE | 10.58.28.84 | smi5gc | external | 15.100.1.100 | fa:16:3e:cc:97:82 | management | smi5gc/portal | smi5gc-router | 
+--------+-------------+--------+----------+--------------+-------------------+------------+---------------+---------------+

Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp fip --cluster pod1 --vm smi5gc/portal

{
    "duration": 5109,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 4272,
        "total_time": 4272
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

2023-11-18 16:51:22.478343	True	1451	get	floating_ips
2023-11-18 16:51:22.702219	True	212	get	tenants
2023-11-18 16:51:22.990697	True	274	get	networks
2023-11-18 16:51:23.295369	True	274	get	routers
2023-11-18 16:51:25.920424	True	2061	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)