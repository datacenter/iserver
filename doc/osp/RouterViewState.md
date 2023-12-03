# Router

## State view

```
# iserver get osp rtr --cluster pod1

Cluster: pod1

Router [#1]
-----------

+---------------+--------+-------+--------+----+------+----------+------------+----------------+-------------+-------------+------+
| Name          | Tenant | Admin | Status | HA | SNAT | Network  | Subnet     | CIDR           | Gateway     | IP          | Age  |
+---------------+--------+-------+--------+----+------+----------+------------+----------------+-------------+-------------+------+
| smi5gc-router | smi5gc | V     | ACTIVE | V  | V    | external | subnet-ext | 10.58.28.80/28 | 10.58.28.94 | 10.58.28.81 | 472d | 
+---------------+--------+-------+--------+----+------+----------+------------+----------------+-------------+-------------+------+

Filter: name
View:   state (def), id, port, all
```

Developer

```
# iserver get osp rtr --cluster pod1

{
    "duration": 4266,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 3965,
        "total_time": 3965
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

2023-11-20 12:14:25.971719	True	2516	get	routers
2023-11-20 12:14:26.649335	True	654	get	tenants
2023-11-20 12:14:27.178604	True	519	get	networks
2023-11-20 12:14:27.470306	True	276	get	subnets
```

[[Back]](./RouterGet.md)