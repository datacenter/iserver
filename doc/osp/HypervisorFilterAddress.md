# Hypervisor

## Filter by address

```
# iserver get osp hv --cluster pod1 --address 192.168.100.13

Cluster: pod1

Hypervisor [#1]
---------------

+----+--------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+
| Id | Hypervisor   | IP             | Status  | State | VMs | CPU   | Memory                     | Disk               |
+----+--------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+
| 13 | AIO-server-1 | 192.168.100.13 | enabled | up    | 5   | 22/80 | 111,616/257,397 [MB] (43%) | 100/825 [GB] (12%) | 
+----+--------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+

Filter: name, address, vm
View:   state (def), vm, all
```

Developer

```
# iserver get osp hv --cluster pod1 --address 192.168.100.13

{
    "duration": 2719,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 2200,
        "total_time": 2200
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

2023-11-19 09:54:58.432101	True	2200	get	hypervisors
```

[[Back]](./HypervisorGet.md)