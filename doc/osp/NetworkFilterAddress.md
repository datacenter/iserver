# Network

## Filter by IP address

```
# iserver get osp net --cluster pod1 --address 15.100.3.33

Cluster: pod1

Network [#1]
------------

+-------------+--------+-------+--------+--------+-----+-----+------+--------------------+---------------+------+
| Name        | Tenant | Admin | Status | Shared | Ext | Sec | MTU  | Subnet             | CIDR          | Age  |
+-------------+--------+-------+--------+--------+-----+-----+------+--------------------+---------------+------+
| control-k8s | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-k8s-subnet | 15.100.3.0/24 | 472d | 
+-------------+--------+-------+--------+--------+-----+-----+------+--------------------+---------------+------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 --address 15.100.3.33

{
    "duration": 2639,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2520,
        "total_time": 2520
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

2023-11-19 13:15:59.873612	True	2075	get	networks
2023-11-19 13:16:00.177949	True	295	get	tenants
2023-11-19 13:16:00.331011	True	150	get	subnets
```

[[Back]](./NetworkGet.md)