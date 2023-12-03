# Network

## Default output

```
# iserver get osp net --cluster pod1

Cluster: pod1

Network [#15]
-------------

+----------------------------------------------------+---------+-------+--------+--------+-----+-----+------+---------------------------------------------------+------------------+------+
| Name                                               | Tenant  | Admin | Status | Shared | Ext | Sec | MTU  | Subnet                                            | CIDR             | Age  |
+----------------------------------------------------+---------+-------+--------+--------+-----+-----+------+---------------------------------------------------+------------------+------+
| C8KV01_LAN01                                       | ialonso | V     | ACTIVE | X      | X   | V   | 9000 | C8KV01_LAN01                                      | 10.0.11.0/24     | 33d  | 
| C8KV_ORANGE_LAN01                                  | ialonso | V     | ACTIVE | X      | X   | V   | 9000 | C8KV_ORANGE_LAN01                                 | 10.0.21.0/24     | 26d  | 
| control-k8s                                        | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-k8s-subnet                                | 15.100.3.0/24    | 472d | 
| control-N2                                         | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-N2-subnet                                 | 15.100.5.0/24    | 472d | 
| control-N4                                         | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-N4-subnet                                 | 15.100.6.0/24    | 472d | 
| control-SBI                                        | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-SBI-subnet                                | 15.100.4.0/24    | 472d | 
| data-N3                                            | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | data-N3-subnet                                    | 15.100.7.0/24    | 472d | 
| data-N6                                            | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | data-N6-subnet                                    | 15.100.8.0/24    | 472d | 
| di-internal1                                       | smi5gc  | V     | ACTIVE | X      | X   | X   | 9000 | di-internal1-subnet                               | 172.16.0.0/18    | 457d | 
| external                                           | admin   | V     | ACTIVE | V      | V   | V   | 9000 | subnet-ext                                        | 10.58.28.80/28   | 472d | 
| HA network tenant 05b8e996f0654e4491d2e925a91c6250 | --      | V     | ACTIVE | X      | X   | V   | 9000 | HA subnet tenant 05b8e996f0654e4491d2e925a91c6250 | 169.254.192.0/18 | 472d | 
| management                                         | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | management-subnet                                 | 15.100.1.0/24    | 472d | 
| orchestration                                      | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | orchestration-subnet                              | 15.100.2.0/24    | 472d | 
| sriov0                                             | smi5gc  | V     | ACTIVE | V      | X   | V   | 9000 | sriov0-subnet                                     | 15.100.105.0/24  | 472d | 
| sriov1                                             | smi5gc  | V     | ACTIVE | V      | X   | V   | 9000 | sriov1-subnet                                     | 15.100.106.0/24  | 472d | 
+----------------------------------------------------+---------+-------+--------+--------+-----+-----+------+---------------------------------------------------+------------------+------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1

{
    "duration": 4662,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4526,
        "total_time": 4526
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

2023-11-19 13:17:13.961828	True	3592	get	networks
2023-11-19 13:17:14.532576	True	562	get	tenants
2023-11-19 13:17:14.909795	True	372	get	subnets
```

[[Back]](./NetworkGet.md)