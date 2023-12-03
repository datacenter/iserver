# Subnet

## Filter by name

```
# iserver get osp sub --cluster pod1 --name subnet-ext

Cluster: pod1

Subnet [#1]
-----------

+-------------------+----------------+-------------+------+-----------------------------+----------------+------+
| Subnet            | CIDR           | Gateway     | DHCP | Pool                        | DNS            | Age  |
+-------------------+----------------+-------------+------+-----------------------------+----------------+------+
| subnet-ext        | 10.58.28.80/28 | 10.58.28.94 | X    | [                           | 144.254.71.184 | 474d | 
| Tenant: admin     |                |             |      |   {                         |                |      | 
| Network: external |                |             |      |     "start": "10.58.28.81", |                |      | 
|                   |                |             |      |     "end": "10.58.28.93"    |                |      | 
|                   |                |             |      |   }                         |                |      | 
|                   |                |             |      | ]                           |                |      | 
+-------------------+----------------+-------------+------+-----------------------------+----------------+------+

Filter: name, tenant, address, mac, vm, hv
View:   state (def), id, port, all
```

Developer

```
# iserver get osp sub --cluster pod1 --name subnet-ext

{
    "duration": 2623,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2426,
        "total_time": 2426
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

2023-11-20 18:09:28.778108	True	1620	get	subnets
2023-11-20 18:09:29.082999	True	285	get	tenants
2023-11-20 18:09:29.609668	True	521	get	networks
```

[[Back]](./SubnetGet.md)