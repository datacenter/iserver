# Volume

## Filter by tenant

```
# iserver get osp vol --cluster pod1 --tenant admin

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
# iserver get osp vol --cluster pod1 --tenant admin

{
    "duration": 5335,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4356,
        "total_time": 4356
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

2023-11-20 17:37:41.701497	True	1793	get	volumes.list
2023-11-20 17:37:42.107226	True	346	get	tenants
2023-11-20 17:37:45.058160	True	2217	get	virtual_machines
```

[[Back]](./VolumeGet.md)