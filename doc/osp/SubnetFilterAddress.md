# Subnet

## Filter by address

```
# iserver get osp sub --cluster pod1 --address 15.100.106.10 -v port

Cluster: pod1

Subnet - Port [#1]
------------------

+----------------------+-----------------+-------------------+--------------+------+----+--------------+
| Name                 | CIDR            | MAC               | IP           | Type | VM | HV           |
+----------------------+-----------------+-------------------+--------------+------+----+--------------+
| smi5gc/sriov1-subnet | 15.100.106.0/24 | fa:16:3e:8e:cf:5c | 15.100.106.1 | DHCP | -- | AIO-server-1 | 
|                      |                 | fa:16:3e:ac:78:eb | 15.100.106.2 | DHCP | -- | AIO-server-3 | 
+----------------------+-----------------+-------------------+--------------+------+----+--------------+

Filter: name, tenant, address, mac, vm, hv
View:   state (def), id, port, all
```

Developer

```
# iserver get osp sub --cluster pod1 --address 15.100.106.10 -v port

{
    "duration": 2896,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 2660,
        "total_time": 2660
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

2023-11-20 18:09:53.981099	True	1775	get	subnets
2023-11-20 18:09:54.286921	True	279	get	tenants
2023-11-20 18:09:54.524506	True	230	get	networks
2023-11-20 18:09:54.914454	True	376	get	ports
```

[[Back]](./SubnetGet.md)