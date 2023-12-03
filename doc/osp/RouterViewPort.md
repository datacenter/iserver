# Router

## Port view

```
# iserver get osp rtr --cluster pod1 -v port

Cluster: pod1

Router - Port [#1]
------------------

+----------------------+-------------------+-------------+----------+-----------------------+
| Name                 | MAC               | IP          | Type     | VM                    |
+----------------------+-------------------+-------------+----------+-----------------------+
| smi5gc/smi5gc-router | fa:16:3e:c1:37:01 | 10.58.28.81 | Gateway  | --                    | 
|                      | fa:16:3e:f3:63:1f | 10.58.28.82 | Floating | smi5gc/esc            | 
|                      | fa:16:3e:b8:e4:f3 | 10.58.28.83 | Floating | smi5gc/server         | 
|                      | fa:16:3e:32:07:87 | 10.58.28.84 | Floating | smi5gc/portal         | 
|                      | fa:16:3e:93:e6:fe | 10.58.28.85 | Floating | smi5gc/lattice        | 
|                      | fa:16:3e:e7:04:c9 | 10.58.28.90 | Floating | ialonso/SDWAN-C8KV01B | 
|                      | fa:16:3e:7c:67:22 | 10.58.28.91 | Floating | ialonso/ORANGE-C8KV-1 | 
|                      | fa:16:3e:fc:2b:eb | 10.58.28.92 | Floating | ialonso/ORANGE-C8KV-2 | 
+----------------------+-------------------+-------------+----------+-----------------------+

Filter: name
View:   state (def), id, port, all
```

Developer

```
# iserver get osp rtr --cluster pod1 -v port

{
    "duration": 7063,
    "osp": {
        "read": true,
        "success": 6,
        "failed": 0,
        "mo": 6,
        "mo_time": 6085,
        "total_time": 6085
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

2023-11-20 12:14:53.440412	True	1915	get	routers
2023-11-20 12:14:53.988662	True	517	get	tenants
2023-11-20 12:14:54.645796	True	652	get	ports
2023-11-20 12:14:54.934893	True	214	get	floating_ips
2023-11-20 12:14:55.322375	True	378	get	networks
2023-11-20 12:14:58.270877	True	2409	get	virtual_machines
```

[[Back]](./RouterGet.md)