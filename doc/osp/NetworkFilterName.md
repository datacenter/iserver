# Network

## Filter by name

```
# iserver get osp net --cluster pod1 --name smi5gc/control*

Cluster: pod1

Network [#4]
------------

+-------------+--------+-------+--------+--------+-----+-----+------+--------------------+---------------+------+
| Name        | Tenant | Admin | Status | Shared | Ext | Sec | MTU  | Subnet             | CIDR          | Age  |
+-------------+--------+-------+--------+--------+-----+-----+------+--------------------+---------------+------+
| control-k8s | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-k8s-subnet | 15.100.3.0/24 | 472d | 
| control-N2  | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-N2-subnet  | 15.100.5.0/24 | 472d | 
| control-N4  | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-N4-subnet  | 15.100.6.0/24 | 472d | 
| control-SBI | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-SBI-subnet | 15.100.4.0/24 | 472d | 
+-------------+--------+-------+--------+--------+-----+-----+------+--------------------+---------------+------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 --name smi5gc/control*

{
    "duration": 3108,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2996,
        "total_time": 2996
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

2023-11-19 13:15:38.192090	True	2145	get	networks
2023-11-19 13:15:38.681160	True	480	get	tenants
2023-11-19 13:15:39.059146	True	371	get	subnets
```

[[Back]](./NetworkGet.md)