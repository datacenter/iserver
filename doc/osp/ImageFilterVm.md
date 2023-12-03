# Image

## Filter by vm

```
# iserver get osp img --cluster pod1 --vm portal -v vm

Cluster: pod1

Image - Virtual Machine [#1]
----------------------------

+--------------------------+-------+-----------+----------------+--------+-----------------+
| Name                     | Disk  | Container | Size [B]       | Status | Virtual Machine |
+--------------------------+-------+-----------+----------------+--------+-----------------+
| portal-snapshot-20220802 | qcow2 | bare      | 80,702,210,048 | active | smi5gc/portal   | 
+--------------------------+-------+-----------+----------------+--------+-----------------+

Filter: name, vm
View:   state (def), id, vm, all
```

Developer

```
# iserver get osp img --cluster pod1 --vm portal -v vm

{
    "duration": 8376,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4332,
        "total_time": 4332
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

2023-11-19 12:22:20.624527	True	0	get	images
2023-11-19 12:22:26.371945	True	3941	get	virtual_machines
2023-11-19 12:22:26.820657	True	391	get	tenants
```

[[Back]](./ImageGet.md)