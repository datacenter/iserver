# Network

## Filter by vlan

```
# iserver get osp net --cluster pod1 --vlan 1204 -v phy

Cluster: pod1

Network - Phy [#1]
------------------

+---------------------+-------+--------+--------------+------------------+-----------------+
| Name                | Admin | Status | Network Type | Physical Network | Segmentation ID |
+---------------------+-------+--------+--------------+------------------+-----------------+
| smi5gc/di-internal1 | V     | ACTIVE | vlan         | physnet1         | 1204            | 
+---------------------+-------+--------+--------------+------------------+-----------------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 --vlan 1204 -v phy

{
    "duration": 4241,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 4140,
        "total_time": 4140
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

2023-11-19 13:17:02.536930	True	3140	get	networks
2023-11-19 13:17:03.549187	True	1000	get	tenants
```

[[Back]](./NetworkGet.md)