# Tenant

## Default output

```
# iserver get osp tenant --cluster pod1

Cluster: pod1

Tenant [#5]
-----------

+----------------------------------+-----------------+
| Id                               | Name            |
+----------------------------------+-----------------+
| 05b8e996f0654e4491d2e925a91c6250 | smi5gc          | 
| 2cced286b74c45ea95c83cc2e5d3b413 | admin           | 
| 9b50a8dba82f4c14802c4554482882b8 | ialonso         | 
| c4a93dc9499e40f78e32a83d914e6a87 | service         | 
| ece266e361054538b965ceebea009241 | cinder-internal | 
+----------------------------------+-----------------+

Filter: --
View:   state (def)
```

Developer

```
# iserver get osp tenant --cluster pod1

{
    "duration": 1156,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1092,
        "total_time": 1092
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

2023-11-20 09:33:12.641802	True	1092	get	tenants
```

[[Back]](./TenantGet.md)