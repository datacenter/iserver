# Router

## Default output

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
    "duration": 2432,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 2230,
        "total_time": 2230
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

2023-11-20 12:15:44.984566	True	1595	get	routers
2023-11-20 12:15:45.239046	True	239	get	tenants
2023-11-20 12:15:45.497488	True	251	get	networks
2023-11-20 12:15:45.662469	True	145	get	subnets
```

[[Back]](./RouterGet.md)