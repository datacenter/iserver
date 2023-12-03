# Port

## Filter by tenant

```
# iserver get osp port --cluster pod1 --tenant admin

Cluster: pod1

Port [#5]
---------

+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+
| MAC               | Admin | Status | Type    | Name       | IP             | Subnet            | Network           | Tenant | Age  |
+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+
| fa:16:3e:ae:32:44 | V     | DOWN   | Compute |            | 10.0.21.2      | C8KV_ORANGE_LAN01 | C8KV_ORANGE_LAN01 | admin  | 17d  | 
+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+
| fa:16:3e:6b:57:aa | V     | DOWN   | Compute |            | 15.100.1.117   | management-subnet | management        | admin  | 17d  | 
+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+
| fa:16:3e:0c:78:90 | V     | DOWN   | Compute |            | 15.100.1.220   | management-subnet | management        | admin  | 17d  | 
+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+
| fa:16:3e:13:75:c2 | V     | ACTIVE | Compute |            | 15.100.1.69    | management-subnet | management        | admin  | 17d  | 
+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+
| fa:16:3e:89:e6:2b | V     | ACTIVE | Compute | test-sriov | 15.100.105.245 | sriov0-subnet     | sriov0            | admin  | 202d | 
+-------------------+-------+--------+---------+------------+----------------+-------------------+-------------------+--------+------+

Filter: name, state, type, tenant, net, subnet, address, mac, hv, vm, sg
View:   state (def), id, sec, hv, all
```

Developer

```
# iserver get osp port --cluster pod1 --tenant admin

{
    "duration": 4259,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 4127,
        "total_time": 4127
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

2023-11-19 14:43:40.501463	True	3053	get	ports
2023-11-19 14:43:40.900457	True	377	get	tenants
2023-11-19 14:43:41.395532	True	490	get	networks
2023-11-19 14:43:41.615474	True	207	get	subnets
```

[[Back]](./PortGet.md)