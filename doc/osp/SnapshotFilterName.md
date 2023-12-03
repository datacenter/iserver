# Snapshot

## Filter by name

```
# iserver get osp snap --cluster pod1 --name my-cirros

Cluster: pod1

Volume Snapshot [#1]
--------------------

+-----------+--------+--------+------+-----------+----------+-----+
| Name      | Tenant | Volume | Size | Status    | Progress | Age |
+-----------+--------+--------+------+-----------+----------+-----+
| my-cirros | admin  | cirros | 20   | available | 100%     | 20d | 
+-----------+--------+--------+------+-----------+----------+-----+

Filter: name, tenant, vol
View:   state (def), id, all
```

Developer

```
# iserver get osp snap --cluster pod1 --name my-cirros

{
    "duration": 3467,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 3320,
        "total_time": 3320
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

2023-11-20 17:26:32.181502	True	2306	get	snapshots
2023-11-20 17:26:32.618025	True	410	get	tenants
2023-11-20 17:26:33.231943	True	604	get	volumes.list
```

[[Back]](./SnapshotGet.md)