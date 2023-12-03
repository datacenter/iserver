# Availability Zone

## Filter by name

```
# iserver get osp az --cluster pod1 --name all

Cluster: pod1

Availability Zone [#1]
----------------------

+-----+-------+------------------+-----------------------+
| AZ  | Avail | Hypervisor       | Service Name [Active] |
+-----+-------+------------------+-----------------------+
| ALL | V     | AIO-server-1     | nova-compute [V]      | 
|     |       | AIO-server-2     | nova-compute [V]      | 
|     |       | AIO-server-3     | nova-compute [V]      | 
|     |       | compute-server-1 | nova-compute [V]      | 
|     |       | compute-server-2 | nova-compute [V]      | 
+-----+-------+------------------+-----------------------+

Filter: name, hv
View:   state (def), hv, all
```

Developer

```
# iserver get osp az --cluster pod1 --name all

{
    "duration": 2243,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1707,
        "total_time": 1707
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

2023-11-18 15:33:45.793180	True	1707	get	availability_zones
```

[[Back]](./AvailabilityZoneGet.md)