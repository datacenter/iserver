# Security Group

## Default output

```
# iserver get osp sg --cluster pod1

Cluster: pod1

Security Group [#7]
-------------------

+---------+---------+------------+--------+--------+
| Tenant  | Name    | Rule Count | Create | Update |
+---------+---------+------------+--------+--------+
| --      | default | 4          | 474d   | 474d   | 
| admin   | default | 4          | 474d   | 474d   | 
| ialonso | default | 5          | 35d    | 28d    | 
| service | default | 4          | 474d   | 474d   | 
| smi5gc  | default | 39         | 473d   | 473d   | 
| smi5gc  | esc     | 7          | 4d     | 4d     | 
| smi5gc  | portal  | 20         | 473d   | 473d   | 
+---------+---------+------------+--------+--------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1

{
    "duration": 2313,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2094,
        "total_time": 2094
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

2023-11-20 18:24:34.907694	True	1808	get	security_groups
2023-11-20 18:24:35.231259	True	286	get	tenants
```

[[Back]](./SecurityGroupGet.md)