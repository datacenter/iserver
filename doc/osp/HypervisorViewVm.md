# Hypervisor

## Virtual machine (vm) view

```
# iserver get osp hv --cluster pod1 -v vm

Cluster: pod1

Hypervisor - Virtual Machine [#5]
---------------------------------

+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| Id | Hypervisor       | Tenant  | Name          | Status  | CPU | Memory [MB] | Disk [GB] |
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 13 | AIO-server-1     | ialonso | ORANGE-C8KV-1 | ACTIVE  | 4   | 4096        | 0         | 
|    |                  | ialonso | ORANGE-C8KV-2 | ACTIVE  | 4   | 4096        | 0         | 
|    |                  | ialonso | SDWAN-C8KV01B | ACTIVE  | 4   | 4096        | 0         | 
|    |                  | smi5gc  | portal        | ACTIVE  | 8   | 32768       | 80        | 
|    |                  | smi5gc  | VPC-SI-mme    | ACTIVE  | 2   | 16384       | 4         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 7  | AIO-server-2     | smi5gc  | esc           | ACTIVE  | 2   | 6144        | 40        | 
|    |                  | smi5gc  | VPC-SI-saegw2 | ACTIVE  | 12  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 10 | AIO-server-3     | smi5gc  | VPC-SI-saegw1 | ACTIVE  | 12  | 32768       | 6         | 
|    |                  | smi5gc  | VPC-SI-upf8   | ACTIVE  | 18  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 1  | compute-server-1 | admin   | test-sriov    | ACTIVE  | 2   | 4096        | 40        | 
|    |                  | smi5gc  | server        | ACTIVE  | 2   | 4096        | 40        | 
|    |                  | smi5gc  | VPC-SI-upf1   | ACTIVE  | 18  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 4  | compute-server-2 | admin   | c8koncinder   | SHUTOFF | 4   | 4096        | 0         | 
|    |                  | admin   | my-c8kv       | SHUTOFF | 4   | 4096        | 0         | 
|    |                  | admin   | my-cirros-img | ACTIVE  | 1   | 2048        | 20        | 
|    |                  | smi5gc  | lattice       | ACTIVE  | 8   | 32768       | 100       | 
|    |                  | smi5gc  | VPC-SI-upf2   | ACTIVE  | 18  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+

Filter: name, address, vm
View:   state (def), vm, all
```

Developer

```
# iserver get osp hv --cluster pod1 -v vm

{
    "duration": 11844,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 11083,
        "total_time": 11083
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

2023-11-19 09:54:08.046985	True	5639	get	hypervisors
2023-11-19 09:54:09.736385	True	1685	get	virtual_machines
2023-11-19 09:54:13.267054	True	3506	get	tenants
2023-11-19 09:54:13.530767	True	253	get	flavors
```

[[Back]](./HypervisorGet.md)