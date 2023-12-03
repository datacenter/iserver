# Hypervisor

## Filter by name

```
# iserver get osp hv --cluster pod1 --name compute-server-1

Cluster: pod1

Hypervisor [#1]
---------------

+----+------------------+----------------+---------+-------+-----+-------+---------------------------+--------------------+
| Id | Hypervisor       | IP             | Status  | State | VMs | CPU   | Memory                    | Disk               |
+----+------------------+----------------+---------+-------+-----+-------+---------------------------+--------------------+
| 1  | compute-server-1 | 192.168.100.11 | enabled | up    | 3   | 22/92 | 66,560/257,396 [MB] (25%) | 102/852 [GB] (11%) | 
+----+------------------+----------------+---------+-------+-----+-------+---------------------------+--------------------+

Filter: name, address, vm
View:   state (def), vm, all
```

Developer

```
# iserver get osp hv --cluster pod1 --name compute-server-1

{
    "duration": 3275,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 2800,
        "total_time": 2800
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
        "lines": 2
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 09:54:46.665646	True	2800	get	hypervisors
```

[[Back]](./HypervisorGet.md)