# Subnet

## Filter by mac address

```
# iserver get osp sub --cluster pod1 --mac 94eb -v port

Cluster: pod1

Subnet - Port [#1]
------------------

+-----------------------+---------------+-------------------+--------------+---------+---------------+------------------+
| Name                  | CIDR          | MAC               | IP           | Type    | VM            | HV               |
+-----------------------+---------------+-------------------+--------------+---------+---------------+------------------+
| smi5gc/data-N6-subnet | 15.100.8.0/24 | fa:16:3e:1e:37:ac | 15.100.8.1   | DHCP    | --            | AIO-server-3     | 
|                       |               | fa:16:3e:b4:94:eb | 15.100.8.102 | Compute | smi5gc/server | compute-server-1 | 
|                       |               | fa:16:3e:46:ab:b0 | 15.100.8.2   | DHCP    | --            | AIO-server-2     | 
+-----------------------+---------------+-------------------+--------------+---------+---------------+------------------+

Filter: name, tenant, address, mac, vm, hv
View:   state (def), id, port, all
```

Developer

```
# iserver get osp sub --cluster pod1 --mac 94eb -v port

{
    "duration": 7354,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 6427,
        "total_time": 6427
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

2023-11-20 18:10:08.112444	True	2757	get	subnets
2023-11-20 18:10:08.528806	True	398	get	tenants
2023-11-20 18:10:08.828427	True	295	get	networks
2023-11-20 18:10:09.254497	True	410	get	ports
2023-11-20 18:10:12.478799	True	2567	get	virtual_machines
```

[[Back]](./SubnetGet.md)