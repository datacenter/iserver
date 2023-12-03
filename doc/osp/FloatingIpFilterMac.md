# Floating IP

## Filter by mac

```
# iserver get osp fip --cluster pod1 --mac 4030

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
# iserver get osp fip --cluster pod1 --mac 4030

{
    "duration": 6558,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 5587,
        "total_time": 5587
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

2023-11-18 16:50:08.736820	True	2484	get	floating_ips
2023-11-18 16:50:08.990147	True	245	get	tenants
2023-11-18 16:50:09.266420	True	263	get	networks
2023-11-18 16:50:09.567464	True	266	get	routers
2023-11-18 16:50:12.504620	True	2329	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)