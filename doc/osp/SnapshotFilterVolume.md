# Snapshot

## Filter by name

```
# iserver get osp snap --cluster pod1 --vol cirros

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
# iserver get osp snap --cluster pod1 --vol cirros

{
    "duration": 2800,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2624,
        "total_time": 2624
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

2023-11-20 17:26:59.960194	True	1633	get	snapshots
2023-11-20 17:27:00.471407	True	485	get	tenants
2023-11-20 17:27:00.984218	True	506	get	volumes.list
```

[[Back]](./SnapshotGet.md)