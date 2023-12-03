# Flavor

## Filter by vm

```
# iserver get osp flv --cluster pod1 --vm esc -v vm

Cluster: pod1

Flavor - Virtual Machine Usage [#1]
-----------------------------------

+------+-----+----------+-----------+----------+------------+
| Name | CPU | Mem [MB] | Disk [GB] | Eph [GB] | VM         |
+------+-----+----------+-----------+----------+------------+
| esc  | 2   | 6144     | 40        | 0        | smi5gc/esc | 
+------+-----+----------+-----------+----------+------------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv --cluster pod1 --vm esc -v vm

{
    "duration": 8304,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 7780,
        "total_time": 7780
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

2023-11-19 09:26:34.859841	True	2977	get	flavors
2023-11-19 09:26:37.401103	True	2510	get	virtual_machines
2023-11-19 09:26:39.727560	True	2293	get	tenants
```

[[Back]](./FlavorGet.md)