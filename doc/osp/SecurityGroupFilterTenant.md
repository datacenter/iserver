# Security Group

## Filter by tenant

```
# iserver get osp sg --cluster pod1 --tenant admin

Cluster: pod1

Security Group [#1]
-------------------

+--------+---------+------------+--------+--------+
| Tenant | Name    | Rule Count | Create | Update |
+--------+---------+------------+--------+--------+
| admin  | default | 4          | 474d   | 474d   | 
+--------+---------+------------+--------+--------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1 --tenant admin

{
    "duration": 2502,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2226,
        "total_time": 2226
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

2023-11-20 18:23:42.941428	True	1840	get	security_groups
2023-11-20 18:23:43.369230	True	386	get	tenants
```

[[Back]](./SecurityGroupGet.md)