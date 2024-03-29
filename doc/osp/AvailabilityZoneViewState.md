# Availability Zone

## State view

```
# iserver get osp az --cluster pod1

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

Filter: name, hv
View:   state (def), hv, all
```

Developer

```
# iserver get osp az --cluster pod1

{
    "duration": 3172,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 2632,
        "total_time": 2632
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

2023-11-18 15:33:03.600058	True	2632	get	availability_zones
```

[[Back]](./AvailabilityZoneGet.md)