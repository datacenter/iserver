# Availability Zone

## Hypervisor (hv) view

```
# iserver get osp az --cluster pod1 -v hv

Cluster: pod1

Availability Zone - Hypervisor [#2]
-----------------------------------

+----------+-------+------------------+-----+-------+----------------------------+--------------------+
| AZ       | Avail | Hypervisor       | VMs | CPU   | Memory                     | Disk               |
+----------+-------+------------------+-----+-------+----------------------------+--------------------+
| ALL      | V     | AIO-server-1     | 5   | 22/80 | 111,616/257,397 [MB] (43%) | 100/825 [GB] (12%) | 
|          |       | AIO-server-2     | 2   | 14/48 | 89,088/257,405 [MB] (34%)  | 62/825 [GB] (7%)   | 
|          |       | AIO-server-3     | 2   | 30/80 | 115,712/257,398 [MB] (44%) | 44/825 [GB] (5%)   | 
|          |       | compute-server-1 | 3   | 22/92 | 66,560/257,396 [MB] (25%)  | 102/852 [GB] (11%) | 
|          |       | compute-server-2 | 5   | 35/92 | 101,376/385,412 [MB] (26%) | 142/852 [GB] (16%) | 
+----------+-------+------------------+-----+-------+----------------------------+--------------------+
| internal | V     | AIO-server-1     | 5   | 22/80 | 111,616/257,397 [MB] (43%) | 100/825 [GB] (12%) | 
|          |       | AIO-server-2     | 2   | 14/48 | 89,088/257,405 [MB] (34%)  | 62/825 [GB] (7%)   | 
|          |       | AIO-server-3     | 2   | 30/80 | 115,712/257,398 [MB] (44%) | 44/825 [GB] (5%)   | 
+----------+-------+------------------+-----+-------+----------------------------+--------------------+

Filter: name, hv
View:   state (def), hv, all
```

Developer

```
# iserver get osp az --cluster pod1 -v hv

{
    "duration": 2746,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 1913,
        "total_time": 1913
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

2023-11-18 15:33:18.443468	True	1766	get	availability_zones
2023-11-18 15:33:18.611682	True	147	get	hypervisors
```

[[Back]](./AvailabilityZoneGet.md)