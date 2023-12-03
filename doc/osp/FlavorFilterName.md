# Flavor

## Filter by name

```
# iserver get osp flv --cluster pod1 --name portal

Cluster: pod1

Flavor [#1]
-----------

+--------+---------+-----+-----+----------+-----------+----------+
| Name   | Enabled | Pub | CPU | Mem [MB] | Disk [GB] | Eph [GB] |
+--------+---------+-----+-----+----------+-----------+----------+
| portal | V       | V   | 8   | 32768    | 80        | 0        | 
+--------+---------+-----+-----+----------+-----------+----------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv --cluster pod1 --name portal

{
    "duration": 3336,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 2558,
        "total_time": 2558
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

2023-11-19 09:25:48.580925	True	2558	get	flavors
```

[[Back]](./FlavorGet.md)