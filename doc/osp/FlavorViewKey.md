# Flavor

## Key view

```
# iserver get osp flv --cluster pod1 -v key

Cluster: pod1

Flavor [#29]
------------

+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| Name                  | Enabled | Pub | CPU | Mem [MB] | Disk [GB] | Eph [GB] | Keys                                                       |
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| cirros                | V       | V   | 1   | 2048     | 20        | 0        | hw:mem_page_size = 2MB                                     | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| esc                   | V       | V   | 2   | 6144     | 40        | 0        | aggregate_instance_extra_specs:esc = true                  | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| flavor_c8kv_4096_0_4  | V       | V   | 4   | 4096     | 0         | 0        | hw:mem_page_size = 2048                                    | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| lattice               | V       | V   | 8   | 32768    | 100       | 0        | aggregate_instance_extra_specs:lattice = true              | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| mmesgsn               | V       | V   | 2   | 16384    | 4         | 16       | aggregate_instance_extra_specs:mmesgsn = true              | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| portal                | V       | V   | 8   | 32768    | 80        | 0        | aggregate_instance_extra_specs:portal = true               | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| rcm                   | V       | V   | 4   | 12228    | 40        | 0        | aggregate_instance_extra_specs:rcm = true                  | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| server                | V       | V   | 2   | 4096     | 40        | 0        | aggregate_instance_extra_specs:server = true               | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-cm                | V       | V   | 8   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-cm = true               | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-etcd1             | V       | V   | 4   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-etcd1 = true            | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-etcd2             | V       | V   | 4   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-etcd2 = true            | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-etcd3             | V       | V   | 4   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-etcd3 = true            | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-master1           | V       | V   | 4   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-master1 = true          | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-master2           | V       | V   | 4   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-master2 = true          | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-master3           | V       | V   | 4   | 32768    | 100       | 0        | aggregate_instance_extra_specs:smi-master3 = true          | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-oam1              | V       | V   | 12  | 65536    | 160       | 0        | aggregate_instance_extra_specs:smi-oam1 = true             | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-oam2              | V       | V   | 12  | 65536    | 160       | 0        | aggregate_instance_extra_specs:smi-oam2 = true             | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-oam3              | V       | V   | 12  | 65536    | 160       | 0        | aggregate_instance_extra_specs:smi-oam3 = true             | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-worker-protocol-1 | V       | V   | 12  | 32768    | 80        | 0        | aggregate_instance_extra_specs:smi-protocol-worker1 = true | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-worker-protocol-2 | V       | V   | 12  | 32768    | 80        | 0        | aggregate_instance_extra_specs:smi-protocol-worker2 = true | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-worker-svccdl-1   | V       | V   | 12  | 32768    | 80        | 0        | aggregate_instance_extra_specs:smi-svccdl-worker1 = true   | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:pin_to_numa = 1                                         | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| smi-worker-svccdl-2   | V       | V   | 12  | 32768    | 80        | 0        | aggregate_instance_extra_specs:smi-svccdl-worker2 = true   | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:pin_to_numa = 1                                         | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| upf                   | V       | V   | 18  | 32768    | 6         | 16       | aggregate_instance_extra_specs:upf = true                  | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| upf1                  | V       | V   | 18  | 32768    | 6         | 16       | aggregate_instance_extra_specs:upf1 = true                 | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| upf2                  | V       | V   | 18  | 32768    | 6         | 16       | aggregate_instance_extra_specs:upf2 = true                 | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| upf3                  | V       | V   | 18  | 32768    | 6         | 16       | aggregate_instance_extra_specs:upf3 = true                 | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| vpc-cf                | V       | V   | 8   | 30720    | 6         | 16       | aggregate_instance_extra_specs:vpc-cf = true               | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| vpc-sf                | V       | V   | 12  | 30720    | 6         | 0        | aggregate_instance_extra_specs:vpc-sf = true               | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+
| vpc-si-saegw-c        | V       | V   | 12  | 32768    | 6         | 16       | aggregate_instance_extra_specs:vpc-si-saegw-c = true       | 
|                       |         |     |     |          |           |          | hw:cpu_policy = dedicated                                  | 
|                       |         |     |     |          |           |          | hw:mem_page_size = large                                   | 
|                       |         |     |     |          |           |          | hw:numa_nodes = 1                                          | 
+-----------------------+---------+-----+-----+----------+-----------+----------+------------------------------------------------------------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv --cluster pod1 -v key

{
    "duration": 5484,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 4268,
        "total_time": 4268
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

2023-11-19 09:24:55.117097	True	1769	get	flavors
2023-11-19 09:24:57.640606	True	2499	get	flavors_keys
```

[[Back]](./FlavorGet.md)