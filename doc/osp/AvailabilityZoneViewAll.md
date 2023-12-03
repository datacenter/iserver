# Availability Zone

## All view

```
# iserver get osp az --cluster pod1 -v all

Cluster: pod1

Availability Zone [#2]
----------------------

+----------+-------+------------------+----------------------------------------+
| AZ       | Avail | Hypervisor       | Service Name [Active]                  |
+----------+-------+------------------+----------------------------------------+
| ALL      | V     | AIO-server-1     | nova-compute [V]                       | 
|          |       | AIO-server-2     | nova-compute [V]                       | 
|          |       | AIO-server-3     | nova-compute [V]                       | 
|          |       | compute-server-1 | nova-compute [V]                       | 
|          |       | compute-server-2 | nova-compute [V]                       | 
+----------+-------+------------------+----------------------------------------+
| internal | V     | AIO-server-1     | nova-conductor [V], nova-scheduler [V] | 
|          |       | AIO-server-2     | nova-conductor [V], nova-scheduler [V] | 
|          |       | AIO-server-3     | nova-conductor [V], nova-scheduler [V] | 
+----------+-------+------------------+----------------------------------------+

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
# iserver get osp az --cluster pod1 -v all

{
    "duration": 2678,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2017,
        "total_time": 2017
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

2023-11-18 15:33:32.074229	True	1843	get	availability_zones
2023-11-18 15:33:32.300473	True	174	get	hypervisors
```

[[Back]](./AvailabilityZoneGet.md)