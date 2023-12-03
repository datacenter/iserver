# Snapshot

## State view

```
# iserver get osp snap --cluster pod1

Cluster: pod1

Volume Snapshot [#6]
--------------------

+-------------------------------------------------------------------------+--------+-----------------------------------+------+-----------+----------+-----+
| Name                                                                    | Tenant | Volume                            | Size | Status    | Progress | Age |
+-------------------------------------------------------------------------+--------+-----------------------------------+------+-----------+----------+-----+
| snapshot for forklift-migration-vm-f83b1396-40b2-4dec-b336-597fc42e55d7 | admin  | volume_migratable_C8KV_ORANGE_new | 16   | available | 100%     | 18d | 
| snapshot for forklift-migration-vm-f83b1396-40b2-4dec-b336-597fc42e55d7 | admin  | volume_migratable_C8KV_ORANGE_new | 16   | available | 100%     | 18d | 
| snapshot_from_migratable_C8KV_ORANGE                                    | admin  | migratable_C8KV_ORANGE            | 16   | available | 100%     | 18d | 
| snapshot_of_volume_migratable_C8KV_ORANGE                               | admin  | migratable_C8KV_ORANGE            | 16   | available | 100%     | 18d | 
| my-cirros                                                               | admin  | cirros                            | 20   | available | 100%     | 20d | 
| snapshot-migratable_c8kv                                                | admin  | migratable_c8kv                   | 16   | available | 100%     | 21d | 
+-------------------------------------------------------------------------+--------+-----------------------------------+------+-----------+----------+-----+

Filter: name, tenant, vol
View:   state (def), id, all
```

Developer

```
# iserver get osp snap --cluster pod1

{
    "duration": 3903,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 3708,
        "total_time": 3708
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
        "lines": 3
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 17:25:49.947763	True	2207	get	snapshots
2023-11-20 17:25:50.328119	True	356	get	tenants
2023-11-20 17:25:51.482101	True	1145	get	volumes.list
```

[[Back]](./SnapshotGet.md)