# Volume

## Filter by hypervisor (hv)

```
# iserver get osp vol --cluster pod1 --hv compute-server-2

Cluster: pod1

Volume [#1]
-----------

+-----------------------------------+--------+--------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+
| Name                              | Tenant | Status | Snap | Boot | Encr | Multi | Size | Type        | VM                | Device   | HV               | Age |
+-----------------------------------+--------+--------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+
| volume_migratable_C8KV_ORANGE_new | admin  | in-use | V    | V    | X    | X     | 16   | __DEFAULT__ | admin/c8koncinder | /dev/vda | compute-server-2 | 18d | 
+-----------------------------------+--------+--------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+

Filter: name, tenant, hv, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp vol --cluster pod1 --hv compute-server-2

{
    "duration": 5619,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4904,
        "total_time": 4904
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

2023-11-20 17:37:58.082373	True	1762	get	volumes.list
2023-11-20 17:37:58.489396	True	385	get	tenants
2023-11-20 17:38:01.837776	True	2757	get	virtual_machines
```

[[Back]](./VolumeGet.md)