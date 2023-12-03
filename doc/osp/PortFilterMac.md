# Port

## Filter by mac address

```
# iserver get osp port --cluster pod1 --mac e660

Cluster: pod1

Port [#1]
---------

+-------------------+-------+--------+---------+------------------+----------------+---------------+---------+--------+-----+
| MAC               | Admin | Status | Type    | Name             | IP             | Subnet        | Network | Tenant | Age |
+-------------------+-------+--------+---------+------------------+----------------+---------------+---------+--------+-----+
| fa:16:3e:fc:e6:60 | V     | ACTIVE | Compute | VPC-SI-upf8-nic2 | 15.100.105.198 | sriov0-subnet | sriov0  | smi5gc | 1d  | 
+-------------------+-------+--------+---------+------------------+----------------+---------------+---------+--------+-----+

Filter: name, state, type, tenant, net, subnet, address, mac, hv, vm, sg
View:   state (def), id, sec, hv, all
```

Developer

```
# iserver get osp port --cluster pod1 --mac e660

{
    "duration": 3645,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 3523,
        "total_time": 3523
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

2023-11-19 14:44:18.277295	True	2111	get	ports
2023-11-19 14:44:18.970142	True	672	get	tenants
2023-11-19 14:44:19.522064	True	545	get	networks
2023-11-19 14:44:19.725184	True	195	get	subnets
```

[[Back]](./PortGet.md)