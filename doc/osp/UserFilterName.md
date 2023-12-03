# User

## Filter by name

```
# iserver get osp user --cluster pod1 --name smi5gc

Cluster: pod1

User [#1]
---------

+----------------------------------+--------+---------+--------+---------+-----------------+
| Id                               | Name   | Enabled | Expiry | Domain  | Default Project |
+----------------------------------+--------+---------+--------+---------+-----------------+
| dea57460869c49e6a829ad88b5b14db1 | smi5gc | V       | --     | default | smi5gc          | 
+----------------------------------+--------+---------+--------+---------+-----------------+

Filter: name
View:   state (def)
```

Developer

```
# iserver get osp user --cluster pod1 --name smi5gc

{
    "duration": 1508,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 1446,
        "total_time": 1446
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
        "lines": 2
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 09:31:40.735608	True	1170	get	users
2023-11-20 09:31:41.021937	True	276	get	tenants
```

[[Back]](./UserGet.md)