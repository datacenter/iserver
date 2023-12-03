# Security Group

## State view

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
    "duration": 2882,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2497,
        "total_time": 2497
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

2023-11-20 18:22:09.831641	True	2148	get	security_groups
2023-11-20 18:22:10.233315	True	349	get	tenants
```

[[Back]](./SecurityGroupGet.md)