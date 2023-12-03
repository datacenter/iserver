# Snapshot

## All view

```
# iserver get osp snap --cluster pod1 -v all

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

Volume Snapshot - Identifier [#6]
---------------------------------

+--------------------------------------+-------------------------------------------------------------------------+
| Id                                   | Name                                                                    |
+--------------------------------------+-------------------------------------------------------------------------+
| 3ba97e1d-6544-477a-93df-8a57fc048947 | snapshot for forklift-migration-vm-f83b1396-40b2-4dec-b336-597fc42e55d7 | 
| 4f7bd7af-51c2-43e8-9602-139981d20bad | snapshot for forklift-migration-vm-f83b1396-40b2-4dec-b336-597fc42e55d7 | 
| ae0ae14b-4073-4279-a1e1-c0ec64935c55 | snapshot_from_migratable_C8KV_ORANGE                                    | 
| b99e3eaf-fee1-477b-950c-e5a009960531 | snapshot_of_volume_migratable_C8KV_ORANGE                               | 
| 309b0367-4ba2-415a-9213-ad47633f3caf | my-cirros                                                               | 
| 38d68769-9faa-4cd1-be26-c18fccacac19 | snapshot-migratable_c8kv                                                | 
+--------------------------------------+-------------------------------------------------------------------------+

Filter: name, tenant, vol
View:   state (def), id, all
```

Developer

```
# iserver get osp snap --cluster pod1 -v all

{
    "duration": 4259,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4086,
        "total_time": 4086
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

2023-11-20 17:26:18.179267	True	2268	get	snapshots
2023-11-20 17:26:18.587452	True	389	get	tenants
2023-11-20 17:26:20.022546	True	1429	get	volumes.list
```

[[Back]](./SnapshotGet.md)