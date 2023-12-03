# Flavor

## Filter by key

```
# iserver get osp flv
    --cluster pod1
    --key aggregate_instance_extra_specs:portal -v key

Cluster: pod1

Flavor [#1]
-----------

+--------+---------+-----+-----+----------+-----------+----------+----------------------------------------------+
| Name   | Enabled | Pub | CPU | Mem [MB] | Disk [GB] | Eph [GB] | Keys                                         |
+--------+---------+-----+-----+----------+-----------+----------+----------------------------------------------+
| portal | V       | V   | 8   | 32768    | 80        | 0        | aggregate_instance_extra_specs:portal = true | 
|        |         |     |     |          |           |          | hw:cpu_policy = dedicated                    | 
|        |         |     |     |          |           |          | hw:mem_page_size = large                     | 
|        |         |     |     |          |           |          | hw:numa_nodes = 1                            | 
+--------+---------+-----+-----+----------+-----------+----------+----------------------------------------------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv
    --cluster pod1
    --key aggregate_instance_extra_specs:portal -v key

{
    "duration": 7047,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 6495,
        "total_time": 6495
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

2023-11-19 09:26:01.071702	True	2520	get	flavors
2023-11-19 09:26:05.074565	True	3975	get	flavors_keys
```

[[Back]](./FlavorGet.md)