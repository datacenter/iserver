# Floating IP

## Filter by floating network

```
# iserver get osp fip --cluster pod1 --floating-net external

Cluster: pod1

Floating IP [#7]
----------------

+--------+-------------+---------+----------+--------------+-------------------+------------+-----------------------+---------------+
| Status | Floating    | Tenant  | Network  | Fixed        | MAC               | Network    | VM                    | Router        |
+--------+-------------+---------+----------+--------------+-------------------+------------+-----------------------+---------------+
| ACTIVE | 10.58.28.82 | smi5gc  | external | 15.100.1.36  | fa:16:3e:bb:2b:cd | management | smi5gc/esc            | smi5gc-router | 
| ACTIVE | 10.58.28.83 | smi5gc  | external | 15.100.1.102 | fa:16:3e:38:40:30 | management | smi5gc/server         | smi5gc-router | 
| ACTIVE | 10.58.28.84 | smi5gc  | external | 15.100.1.100 | fa:16:3e:cc:97:82 | management | smi5gc/portal         | smi5gc-router | 
| ACTIVE | 10.58.28.85 | smi5gc  | external | 15.100.1.101 | fa:16:3e:c3:6b:06 | management | smi5gc/lattice        | smi5gc-router | 
| ACTIVE | 10.58.28.90 | ialonso | external | 15.100.1.30  | fa:16:3e:14:7d:d0 | management | ialonso/SDWAN-C8KV01B | smi5gc-router | 
| ACTIVE | 10.58.28.91 | ialonso | external | 15.100.1.219 | fa:16:3e:97:c1:38 | management | ialonso/ORANGE-C8KV-1 | smi5gc-router | 
| ACTIVE | 10.58.28.92 | ialonso | external | 15.100.1.179 | fa:16:3e:a4:f5:53 | management | ialonso/ORANGE-C8KV-2 | smi5gc-router | 
+--------+-------------+---------+----------+--------------+-------------------+------------+-----------------------+---------------+

Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp fip --cluster pod1 --floating-net external

{
    "duration": 5422,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 4535,
        "total_time": 4535
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

2023-11-18 16:50:55.365536	True	1498	get	floating_ips
2023-11-18 16:50:55.646762	True	267	get	tenants
2023-11-18 16:50:56.263655	True	616	get	networks
2023-11-18 16:50:56.506907	True	226	get	routers
2023-11-18 16:50:59.086549	True	1928	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)