# Quota

## Filter by name

```
# iserver get osp quota --cluster pod1 --name smi5gc

Cluster: pod1

Quota [#1]
----------

+--------+----------+------+---------+----------+-------------+----------+----------+-----------+-------+--------------+---------+-------+-----------+--------------+
| Tenant | Instance | Core | Memory  | Fixed IP | Floating IP | Key Pair | Metadata | SecGroups | Rules | ServerGroups | Members | Files | PathBytes | ContentBytes |
+--------+----------+------+---------+----------+-------------+----------+----------+-----------+-------+--------------+---------+-------+-----------+--------------+
| smi5gc | 100      | 2000 | 5120000 | -1       | 10          | 1000     | 1280     | 10        | 20    | 100          | 100     | 50    | 255       | 655360       | 
+--------+----------+------+---------+----------+-------------+----------+----------+-----------+-------+--------------+---------+-------+-----------+--------------+

Filter: name
View:   state (def)
```

Developer

```
# iserver get osp quota --cluster pod1 --name smi5gc

{
    "duration": 5586,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 5322,
        "total_time": 5322
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

2023-11-20 09:27:54.311105	True	1108	get	tenants
2023-11-20 09:27:58.730617	True	4214	get	quotas
```

[[Back]](./QuotaGet.md)