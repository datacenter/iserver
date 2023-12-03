# Router

## Identifier (id) view

```
# iserver get osp rtr --cluster pod1 -v id

Cluster: pod1

Router - Identifier [#1]
------------------------

+---------------+--------------------------------------+----------------------------------+--------------------------------------+--------------------------------------+
| Name          | Id                                   | Tenant                           | Network                              | Subnet                               |
+---------------+--------------------------------------+----------------------------------+--------------------------------------+--------------------------------------+
| smi5gc-router | 424d1cba-254f-47af-9b42-a05465be1d97 | 05b8e996f0654e4491d2e925a91c6250 | e7474314-438a-43f6-9ddf-319f0578ca30 | 379bd679-fea7-4aa6-b8c3-0368ab2790a9 | 
+---------------+--------------------------------------+----------------------------------+--------------------------------------+--------------------------------------+

Filter: name
View:   state (def), id, port, all
```

Developer

```
# iserver get osp rtr --cluster pod1 -v id

{
    "duration": 2025,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1886,
        "total_time": 1886
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

2023-11-20 12:14:40.881408	True	1886	get	routers
```

[[Back]](./RouterGet.md)