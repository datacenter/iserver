# Network

## Filter by mac address

```
# iserver get osp net --cluster pod1 --mac d5c6 -v port

Cluster: pod1

Network - Port [#1]
-------------------

+----------------------+--------------+-------------------+-----------+---------+-----------------------+--------------+
| Name                 | CIDR         | MAC               | IP        | Type    | VM                    | HV           |
+----------------------+--------------+-------------------+-----------+---------+-----------------------+--------------+
| ialonso/C8KV01_LAN01 | 10.0.11.0/24 | fa:16:3e:5c:b7:b8 | 10.0.11.1 | Compute | ialonso/ORANGE-C8KV-1 | AIO-server-1 | 
|                      |              | fa:16:3e:3b:d5:c6 | 10.0.11.2 | Compute | ialonso/SDWAN-C8KV01B | AIO-server-1 | 
|                      |              | fa:16:3e:79:74:6e | 10.0.11.5 | DHCP    | --                    | AIO-server-1 | 
|                      |              | fa:16:3e:91:2f:04 | 10.0.11.6 | DHCP    | --                    | AIO-server-3 | 
+----------------------+--------------+-------------------+-----------+---------+-----------------------+--------------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 --mac d5c6 -v port

{
    "duration": 9144,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 8692,
        "total_time": 8692
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 13:16:14.006712	True	5006	get	networks
2023-11-19 13:16:14.440061	True	423	get	tenants
2023-11-19 13:16:14.676703	True	231	get	subnets
2023-11-19 13:16:15.166547	True	478	get	ports
2023-11-19 13:16:18.007057	True	2554	get	virtual_machines
```

[[Back]](./NetworkGet.md)