# Hypervisor

## Filter by vm

```
# iserver get osp hv --cluster pod1 --vm portal -v vm

Cluster: pod1

Hypervisor - Virtual Machine [#1]
---------------------------------

+----+--------------+---------+---------------+--------+-----+-------------+-----------+
| Id | Hypervisor   | Tenant  | Name          | Status | CPU | Memory [MB] | Disk [GB] |
+----+--------------+---------+---------------+--------+-----+-------------+-----------+
| 13 | AIO-server-1 | ialonso | ORANGE-C8KV-1 | ACTIVE | 4   | 4096        | 0         | 
|    |              | ialonso | ORANGE-C8KV-2 | ACTIVE | 4   | 4096        | 0         | 
|    |              | ialonso | SDWAN-C8KV01B | ACTIVE | 4   | 4096        | 0         | 
|    |              | smi5gc  | portal        | ACTIVE | 8   | 32768       | 80        | 
|    |              | smi5gc  | VPC-SI-mme    | ACTIVE | 2   | 16384       | 4         | 
+----+--------------+---------+---------------+--------+-----+-------------+-----------+

Filter: name, address, vm
View:   state (def), vm, all
```

Developer

```
# iserver get osp hv --cluster pod1 --vm portal -v vm

{
    "duration": 7143,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 6337,
        "total_time": 6337
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

2023-11-19 09:55:10.717155	True	2739	get	hypervisors
2023-11-19 09:55:12.239150	True	1499	get	virtual_machines
2023-11-19 09:55:14.194806	True	1896	get	tenants
2023-11-19 09:55:14.403519	True	203	get	flavors
```

[[Back]](./HypervisorGet.md)