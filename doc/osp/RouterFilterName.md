# Router

## Filter by name

```
# iserver get osp rtr --cluster pod1 --name smi5gc-router

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
# iserver get osp rtr --cluster pod1 --name smi5gc-router

{
    "duration": 2657,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 2377,
        "total_time": 2377
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

2023-11-20 12:15:29.933909	True	1553	get	routers
2023-11-20 12:15:30.340055	True	368	get	tenants
2023-11-20 12:15:30.649588	True	303	get	networks
2023-11-20 12:15:30.819984	True	153	get	subnets
```

[[Back]](./RouterGet.md)