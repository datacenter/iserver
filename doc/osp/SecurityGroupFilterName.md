# Security Group

## Filter by name

```
# iserver get osp sg --cluster pod1 --name portal

Cluster: pod1

Security Group [#1]
-------------------

+--------+--------+------------+--------+--------+
| Tenant | Name   | Rule Count | Create | Update |
+--------+--------+------------+--------+--------+
| smi5gc | portal | 20         | 473d   | 473d   | 
+--------+--------+------------+--------+--------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1 --name portal

{
    "duration": 2316,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2090,
        "total_time": 2090
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

2023-11-20 18:23:28.587993	True	1844	get	security_groups
2023-11-20 18:23:28.885730	True	246	get	tenants
```

[[Back]](./SecurityGroupGet.md)