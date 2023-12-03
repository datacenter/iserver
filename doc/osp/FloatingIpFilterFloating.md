# Floating IP

## Filter by floating address

```
# iserver get osp fip --cluster pod1 --floating 10.58.28.82

Cluster: pod1

Floating IP [#1]
----------------

+--------+-------------+--------+----------+-------------+-------------------+------------+------------+---------------+
| Status | Floating    | Tenant | Network  | Fixed       | MAC               | Network    | VM         | Router        |
+--------+-------------+--------+----------+-------------+-------------------+------------+------------+---------------+
| ACTIVE | 10.58.28.82 | smi5gc | external | 15.100.1.36 | fa:16:3e:bb:2b:cd | management | smi5gc/esc | smi5gc-router | 
+--------+-------------+--------+----------+-------------+-------------------+------------+------------+---------------+

Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp fip --cluster pod1 --floating 10.58.28.82

{
    "duration": 5461,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 4557,
        "total_time": 4557
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

2023-11-18 16:49:35.001393	True	1422	get	floating_ips
2023-11-18 16:49:35.252219	True	236	get	tenants
2023-11-18 16:49:35.459488	True	200	get	networks
2023-11-18 16:49:35.877550	True	368	get	routers
2023-11-18 16:49:38.815280	True	2331	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)