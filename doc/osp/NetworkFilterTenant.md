# Network

## Filter by tenant

```
# iserver get osp net --cluster pod1 --tenant smi5gc

Cluster: pod1

Network [#11]
-------------

+---------------+--------+-------+--------+--------+-----+-----+------+----------------------+-----------------+------+
| Name          | Tenant | Admin | Status | Shared | Ext | Sec | MTU  | Subnet               | CIDR            | Age  |
+---------------+--------+-------+--------+--------+-----+-----+------+----------------------+-----------------+------+
| control-k8s   | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-k8s-subnet   | 15.100.3.0/24   | 472d | 
| control-N2    | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-N2-subnet    | 15.100.5.0/24   | 472d | 
| control-N4    | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-N4-subnet    | 15.100.6.0/24   | 472d | 
| control-SBI   | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | control-SBI-subnet   | 15.100.4.0/24   | 472d | 
| data-N3       | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | data-N3-subnet       | 15.100.7.0/24   | 472d | 
| data-N6       | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | data-N6-subnet       | 15.100.8.0/24   | 472d | 
| di-internal1  | smi5gc | V     | ACTIVE | X      | X   | X   | 9000 | di-internal1-subnet  | 172.16.0.0/18   | 457d | 
| management    | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | management-subnet    | 15.100.1.0/24   | 472d | 
| orchestration | smi5gc | V     | ACTIVE | X      | X   | V   | 9000 | orchestration-subnet | 15.100.2.0/24   | 472d | 
| sriov0        | smi5gc | V     | ACTIVE | V      | X   | V   | 9000 | sriov0-subnet        | 15.100.105.0/24 | 472d | 
| sriov1        | smi5gc | V     | ACTIVE | V      | X   | V   | 9000 | sriov1-subnet        | 15.100.106.0/24 | 472d | 
+---------------+--------+-------+--------+--------+-----+-----+------+----------------------+-----------------+------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 --tenant smi5gc

{
    "duration": 2953,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2836,
        "total_time": 2836
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

2023-11-19 13:15:48.605044	True	2238	get	networks
2023-11-19 13:15:48.925326	True	311	get	tenants
2023-11-19 13:15:49.215561	True	287	get	subnets
```

[[Back]](./NetworkGet.md)