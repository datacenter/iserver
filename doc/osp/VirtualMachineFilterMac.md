# Virtual Machine

## Filter by mac address

```
# iserver get osp vm --cluster pod1 --mac 5971 -v net

Cluster: pod1

Virtual Machine - Networking [#1]
---------------------------------

+--------+-------------+---------------+-------------------+------------------------+-----------------+
| Tenant | VM          | Network       | MAC               | IP                     | Subnet          |
+--------+-------------+---------------+-------------------+------------------------+-----------------+
| smi5gc | VPC-SI-upf2 | orchestration | fa:16:3e:d8:3b:77 | 15.100.2.192 (fixed)   | 15.100.2.0/24   | 
|        |             | management    | fa:16:3e:01:17:1c | 15.100.1.192 (fixed)   | 15.100.1.0/24   | 
|        |             | sriov0        | fa:16:3e:48:32:31 | 15.100.105.192 (fixed) | 15.100.105.0/24 | 
|        |             | sriov0        | fa:16:3e:74:59:71 | 15.100.105.92 (fixed)  | 15.100.105.0/24 | 
+--------+-------------+---------------+-------------------+------------------------+-----------------+

Filter: name, tenant, img, flv, net, address, mac, hv
View:   state (def), id, net, all
```

Developer

```
# iserver get osp vm --cluster pod1 --mac 5971 -v net

{
    "duration": 5064,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 4383,
        "total_time": 4383
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

2023-11-20 18:38:36.193363	True	2137	get	virtual_machines
2023-11-20 18:38:37.570061	True	1316	get	tenants
2023-11-20 18:38:38.389307	True	772	get	networks
2023-11-20 18:38:38.566604	True	158	get	subnets
```

[[Back]](./VirtualMachineGet.md)