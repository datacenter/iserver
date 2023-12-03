# Role

## State view

```
# iserver get osp role --cluster pod1

Cluster: pod1

Role [#4]
---------

+----------------------------------+----------+
| Id                               | Name     |
+----------------------------------+----------+
| 0e1937746f634c9186f1b287de3303c5 | _member_ | 
| 47151af5641149579acab097aa7b0261 | reader   | 
| e1a3fd1ec760483db25911028f585e0a | member   | 
| efe2e47cb6344c52a8e4cb2127f95bcc | admin    | 
+----------------------------------+----------+

Filter: --
View:   state (def)
```

Developer

```
# iserver get osp role --cluster pod1

{
    "duration": 1264,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1207,
        "total_time": 1207
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

2023-11-20 09:30:42.839370	True	1207	get	roles
```

[[Back]](./RoleGet.md)