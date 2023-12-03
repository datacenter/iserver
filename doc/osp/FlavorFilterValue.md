# Flavor

## Filter by value

```
# iserver get osp flv --cluster pod1 --value 2MB -v key

Cluster: pod1

Flavor [#1]
-----------

+--------+---------+-----+-----+----------+-----------+----------+------------------------+
| Name   | Enabled | Pub | CPU | Mem [MB] | Disk [GB] | Eph [GB] | Keys                   |
+--------+---------+-----+-----+----------+-----------+----------+------------------------+
| cirros | V       | V   | 1   | 2048     | 20        | 0        | hw:mem_page_size = 2MB | 
+--------+---------+-----+-----+----------+-----------+----------+------------------------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv --cluster pod1 --value 2MB -v key

{
    "duration": 5864,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 4933,
        "total_time": 4933
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

2023-11-19 09:26:17.439821	True	2100	get	flavors
2023-11-19 09:26:20.284569	True	2833	get	flavors_keys
```

[[Back]](./FlavorGet.md)