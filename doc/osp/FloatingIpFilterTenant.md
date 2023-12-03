# Floating IP

## Filter by tenant

```
# iserver get osp fip --cluster pod1 --tenant smi5gc

Cluster: pod1

Floating IP [#4]
----------------

+--------+-------------+--------+----------+--------------+-------------------+------------+----------------+---------------+
| Status | Floating    | Tenant | Network  | Fixed        | MAC               | Network    | VM             | Router        |
+--------+-------------+--------+----------+--------------+-------------------+------------+----------------+---------------+
| ACTIVE | 10.58.28.82 | smi5gc | external | 15.100.1.36  | fa:16:3e:bb:2b:cd | management | smi5gc/esc     | smi5gc-router | 
| ACTIVE | 10.58.28.83 | smi5gc | external | 15.100.1.102 | fa:16:3e:38:40:30 | management | smi5gc/server  | smi5gc-router | 
| ACTIVE | 10.58.28.84 | smi5gc | external | 15.100.1.100 | fa:16:3e:cc:97:82 | management | smi5gc/portal  | smi5gc-router | 
| ACTIVE | 10.58.28.85 | smi5gc | external | 15.100.1.101 | fa:16:3e:c3:6b:06 | management | smi5gc/lattice | smi5gc-router | 
+--------+-------------+--------+----------+--------------+-------------------+------------+----------------+---------------+

Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp fip --cluster pod1 --tenant smi5gc

{
    "duration": 5508,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 4628,
        "total_time": 4628
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

2023-11-18 16:50:41.621483	True	1406	get	floating_ips
2023-11-18 16:50:41.944147	True	310	get	tenants
2023-11-18 16:50:42.237167	True	282	get	networks
2023-11-18 16:50:42.541649	True	271	get	routers
2023-11-18 16:50:45.523583	True	2359	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)