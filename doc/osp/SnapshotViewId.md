# Snapshot

## Identifier (id) view

```
# iserver get osp snap --cluster pod1 -v id

Cluster: pod1

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
# iserver get osp snap --cluster pod1 -v id

{
    "duration": 3763,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 3630,
        "total_time": 3630
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

2023-11-20 17:26:05.275200	True	3630	get	snapshots
```

[[Back]](./SnapshotGet.md)