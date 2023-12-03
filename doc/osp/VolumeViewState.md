# Volume

## State view

```
# iserver get osp vol --cluster pod1

Cluster: pod1

Volume [#6]
-----------

+-----------------------------------+--------+-----------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+
| Name                              | Tenant | Status    | Snap | Boot | Encr | Multi | Size | Type        | VM                | Device   | HV               | Age |
+-----------------------------------+--------+-----------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+
| cirros                            | admin  | available | X    | V    | X    | X     | 20   | __DEFAULT__ | --                | --       | --               | 21d | 
| migratable_C8KV_ORANGE            | admin  | available | X    | V    | X    | X     | 16   | __DEFAULT__ | --                | --       | --               | 18d | 
| migratable_c8kv                   | admin  | available | X    | V    | X    | X     | 16   | __DEFAULT__ | --                | --       | --               | 27d | 
| migratable_c8kv_vm                | admin  | available | V    | V    | X    | X     | 16   | __DEFAULT__ | --                | --       | --               | 21d | 
| my-cirros                         | admin  | available | V    | V    | X    | X     | 20   | __DEFAULT__ | --                | --       | --               | 20d | 
| volume_migratable_C8KV_ORANGE_new | admin  | in-use    | V    | V    | X    | X     | 16   | __DEFAULT__ | admin/c8koncinder | /dev/vda | compute-server-2 | 18d | 
+-----------------------------------+--------+-----------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+

Filter: name, tenant, hv, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp vol --cluster pod1

{
    "duration": 6398,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 5483,
        "total_time": 5483
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

2023-11-20 17:36:39.029049	True	1788	get	volumes.list
2023-11-20 17:36:39.436838	True	376	get	tenants
2023-11-20 17:36:43.468770	True	3319	get	virtual_machines
```

[[Back]](./VolumeGet.md)