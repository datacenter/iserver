# Volume

## Filter by name

```
# iserver get osp vol --cluster pod1 --name cirros

Cluster: pod1

Volume [#1]
-----------

+--------+--------+-----------+------+------+------+-------+------+-------------+----+--------+----+-----+
| Name   | Tenant | Status    | Snap | Boot | Encr | Multi | Size | Type        | VM | Device | HV | Age |
+--------+--------+-----------+------+------+------+-------+------+-------------+----+--------+----+-----+
| cirros | admin  | available | X    | V    | X    | X     | 20   | __DEFAULT__ | -- | --     | -- | 21d | 
+--------+--------+-----------+------+------+------+-------+------+-------------+----+--------+----+-----+

Filter: name, tenant, hv, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp vol --cluster pod1 --name cirros

{
    "duration": 2271,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2130,
        "total_time": 2130
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

2023-11-20 17:37:25.941725	True	1762	get	volumes.list
2023-11-20 17:37:26.336664	True	368	get	tenants
```

[[Back]](./VolumeGet.md)