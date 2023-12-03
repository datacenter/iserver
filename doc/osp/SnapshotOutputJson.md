# Snapshot

## Default output

```
# iserver get osp snap --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "status": "Green"
        },
        "id": "3ba97e1d-6544-477a-93df-8a57fc048947",
        "name": "snapshot for forklift-migration-vm-f83b1396-40b2-4dec-b336-597fc42e55d7",
        "description": null,
        "volume_id": "88b81c75-c333-45fa-be50-219e12ae5520",
        "status": "available",
        "size": 16,
        "metadata": {},
        "created_at": "2023-11-02T09:20:21.000000",
        "updated_at": "2023-11-02T09:20:22.000000",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "progress": "100%",
        "created_age": "18d",
        "updated_age": "18d",
        "tenant_name": "admin",
        "volume_name": "volume_migratable_C8KV_ORANGE_new"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "4f7bd7af-51c2-43e8-9602-139981d20bad",
        "name": "snapshot for forklift-migration-vm-f83b1396-40b2-4dec-b336-597fc42e55d7",
        "description": null,
        "volume_id": "88b81c75-c333-45fa-be50-219e12ae5520",
        "status": "available",
        "size": 16,
        "metadata": {},
        "created_at": "2023-11-02T08:59:39.000000",
        "updated_at": "2023-11-02T08:59:40.000000",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "progress": "100%",
        "created_age": "18d",
        "updated_age": "18d",
        "tenant_name": "admin",
        "volume_name": "volume_migratable_C8KV_ORANGE_new"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "ae0ae14b-4073-4279-a1e1-c0ec64935c55",
        "name": "snapshot_from_migratable_C8KV_ORANGE",
        "description": null,
        "volume_id": "1f50033c-93e8-44cd-9ad4-13b00613382f",
        "status": "available",
        "size": 16,
        "metadata": {},
        "created_at": "2023-11-02T07:53:54.000000",
        "updated_at": "2023-11-02T07:53:56.000000",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "progress": "100%",
        "created_age": "18d",
        "updated_age": "18d",
        "tenant_name": "admin",
        "volume_name": "migratable_C8KV_ORANGE"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "b99e3eaf-fee1-477b-950c-e5a009960531",
        "name": "snapshot_of_volume_migratable_C8KV_ORANGE",
        "description": null,
        "volume_id": "1f50033c-93e8-44cd-9ad4-13b00613382f",
        "status": "available",
        "size": 16,
        "metadata": {},
        "created_at": "2023-11-01T20:32:08.000000",
        "updated_at": "2023-11-01T21:39:15.000000",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "progress": "100%",
        "created_age": "18d",
        "updated_age": "18d",
        "tenant_name": "admin",
        "volume_name": "migratable_C8KV_ORANGE"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "309b0367-4ba2-415a-9213-ad47633f3caf",
        "name": "my-cirros",
        "description": null,
        "volume_id": "01ffbe45-fef6-4711-835b-6bf649e8ea90",
        "status": "available",
        "size": 20,
        "metadata": {},
        "created_at": "2023-10-30T22:03:50.000000",
        "updated_at": "2023-10-30T22:03:51.000000",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "progress": "100%",
        "created_age": "20d",
        "updated_age": "20d",
        "tenant_name": "admin",
        "volume_name": "cirros"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "38d68769-9faa-4cd1-be26-c18fccacac19",
        "name": "snapshot-migratable_c8kv",
        "description": null,
        "volume_id": "a9ee570a-e39c-424f-be5b-d2fb93de2984",
        "status": "available",
        "size": 16,
        "metadata": {},
        "created_at": "2023-10-30T14:56:48.000000",
        "updated_at": "2023-11-01T19:49:43.000000",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "progress": "100%",
        "created_age": "21d",
        "updated_age": "18d",
        "tenant_name": "admin",
        "volume_name": "migratable_c8kv"
    }
]
```

Developer

```
# iserver get osp snap --cluster pod1 -o json

{
    "duration": 2815,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2611,
        "total_time": 2611
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

2023-11-20 17:27:27.403572	True	1824	get	snapshots
2023-11-20 17:27:27.717684	True	283	get	tenants
2023-11-20 17:27:28.231742	True	504	get	volumes.list
```

[[Back]](./SnapshotGet.md)