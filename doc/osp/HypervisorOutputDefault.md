# Hypervisor

## Default output

```
# iserver get osp hv --cluster pod1

Cluster: pod1

Hypervisor [#5]
---------------

+----+------------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+
| Id | Hypervisor       | IP             | Status  | State | VMs | CPU   | Memory                     | Disk               |
+----+------------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+
| 13 | AIO-server-1     | 192.168.100.13 | enabled | up    | 5   | 22/80 | 111,616/257,397 [MB] (43%) | 100/825 [GB] (12%) | 
| 7  | AIO-server-2     | 192.168.100.12 | enabled | up    | 2   | 14/48 | 89,088/257,405 [MB] (34%)  | 62/825 [GB] (7%)   | 
| 10 | AIO-server-3     | 192.168.100.14 | enabled | up    | 2   | 30/80 | 115,712/257,398 [MB] (44%) | 44/825 [GB] (5%)   | 
| 1  | compute-server-1 | 192.168.100.11 | enabled | up    | 3   | 22/92 | 66,560/257,396 [MB] (25%)  | 102/852 [GB] (11%) | 
| 4  | compute-server-2 | 192.168.100.10 | enabled | up    | 5   | 35/92 | 101,376/385,412 [MB] (26%) | 142/852 [GB] (16%) | 
+----+------------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+

Filter: name, address, vm
View:   state (def), vm, all
```

Developer

```
# iserver get osp hv --cluster pod1

{
    "duration": 3343,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 2540,
        "total_time": 2540
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

2023-11-19 09:55:28.331995	True	2540	get	hypervisors
```

[[Back]](./HypervisorGet.md)