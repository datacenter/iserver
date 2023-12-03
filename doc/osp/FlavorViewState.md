# Flavor

## State view

```
# iserver get osp flv --cluster pod1

Cluster: pod1

Flavor [#29]
------------

+-----------------------+---------+-----+-----+----------+-----------+----------+
| Name                  | Enabled | Pub | CPU | Mem [MB] | Disk [GB] | Eph [GB] |
+-----------------------+---------+-----+-----+----------+-----------+----------+
| cirros                | V       | V   | 1   | 2048     | 20        | 0        | 
| esc                   | V       | V   | 2   | 6144     | 40        | 0        | 
| flavor_c8kv_4096_0_4  | V       | V   | 4   | 4096     | 0         | 0        | 
| lattice               | V       | V   | 8   | 32768    | 100       | 0        | 
| mmesgsn               | V       | V   | 2   | 16384    | 4         | 16       | 
| portal                | V       | V   | 8   | 32768    | 80        | 0        | 
| rcm                   | V       | V   | 4   | 12228    | 40        | 0        | 
| server                | V       | V   | 2   | 4096     | 40        | 0        | 
| smi-cm                | V       | V   | 8   | 32768    | 100       | 0        | 
| smi-etcd1             | V       | V   | 4   | 32768    | 100       | 0        | 
| smi-etcd2             | V       | V   | 4   | 32768    | 100       | 0        | 
| smi-etcd3             | V       | V   | 4   | 32768    | 100       | 0        | 
| smi-master1           | V       | V   | 4   | 32768    | 100       | 0        | 
| smi-master2           | V       | V   | 4   | 32768    | 100       | 0        | 
| smi-master3           | V       | V   | 4   | 32768    | 100       | 0        | 
| smi-oam1              | V       | V   | 12  | 65536    | 160       | 0        | 
| smi-oam2              | V       | V   | 12  | 65536    | 160       | 0        | 
| smi-oam3              | V       | V   | 12  | 65536    | 160       | 0        | 
| smi-worker-protocol-1 | V       | V   | 12  | 32768    | 80        | 0        | 
| smi-worker-protocol-2 | V       | V   | 12  | 32768    | 80        | 0        | 
| smi-worker-svccdl-1   | V       | V   | 12  | 32768    | 80        | 0        | 
| smi-worker-svccdl-2   | V       | V   | 12  | 32768    | 80        | 0        | 
| upf                   | V       | V   | 18  | 32768    | 6         | 16       | 
| upf1                  | V       | V   | 18  | 32768    | 6         | 16       | 
| upf2                  | V       | V   | 18  | 32768    | 6         | 16       | 
| upf3                  | V       | V   | 18  | 32768    | 6         | 16       | 
| vpc-cf                | V       | V   | 8   | 30720    | 6         | 16       | 
| vpc-sf                | V       | V   | 12  | 30720    | 6         | 0        | 
| vpc-si-saegw-c        | V       | V   | 12  | 32768    | 6         | 16       | 
+-----------------------+---------+-----+-----+----------+-----------+----------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv --cluster pod1

{
    "duration": 2872,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1930,
        "total_time": 1930
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

2023-11-19 09:24:24.403704	True	1930	get	flavors
```

[[Back]](./FlavorGet.md)