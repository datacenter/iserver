# Subnet

## Filter by tenant

```
# iserver get osp sub --cluster pod1 --tenant smi5gc

Cluster: pod1

Subnet [#11]
------------

+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| Subnet                 | CIDR            | Gateway      | DHCP | Pool                         | DNS            | Age  |
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| management-subnet      | 15.100.1.0/24   | 15.100.1.254 | V    | [                            | 144.254.71.184 | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: management    |                 |              |      |     "start": "15.100.1.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.1.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| control-N2-subnet      | 15.100.5.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: control-N2    |                 |              |      |     "start": "15.100.5.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.5.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| sriov0-subnet          | 15.100.105.0/24 | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: sriov0        |                 |              |      |     "start": "15.100.105.1", |                |      | 
|                        |                 |              |      |     "end": "15.100.105.253"  |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| sriov1-subnet          | 15.100.106.0/24 | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: sriov1        |                 |              |      |     "start": "15.100.106.1", |                |      | 
|                        |                 |              |      |     "end": "15.100.106.253"  |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| orchestration-subnet   | 15.100.2.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: orchestration |                 |              |      |     "start": "15.100.2.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.2.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| control-k8s-subnet     | 15.100.3.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: control-k8s   |                 |              |      |     "start": "15.100.3.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.3.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| di-internal1-subnet    | 172.16.0.0/18   | --           | X    | [                            | --             | 458d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: di-internal1  |                 |              |      |     "start": "172.16.0.1",   |                |      | 
|                        |                 |              |      |     "end": "172.16.63.254"   |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| control-SBI-subnet     | 15.100.4.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: control-SBI   |                 |              |      |     "start": "15.100.4.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.4.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| control-N4-subnet      | 15.100.6.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: control-N4    |                 |              |      |     "start": "15.100.6.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.6.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| data-N3-subnet         | 15.100.7.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: data-N3       |                 |              |      |     "start": "15.100.7.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.7.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+
| data-N6-subnet         | 15.100.8.0/24   | --           | V    | [                            | --             | 473d | 
| Tenant: smi5gc         |                 |              |      |   {                          |                |      | 
| Network: data-N6       |                 |              |      |     "start": "15.100.8.1",   |                |      | 
|                        |                 |              |      |     "end": "15.100.8.253"    |                |      | 
|                        |                 |              |      |   }                          |                |      | 
|                        |                 |              |      | ]                            |                |      | 
+------------------------+-----------------+--------------+------+------------------------------+----------------+------+

Filter: name, tenant, address, mac, vm, hv
View:   state (def), id, port, all
```

Developer

```
# iserver get osp sub --cluster pod1 --tenant smi5gc

{
    "duration": 2716,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2352,
        "total_time": 2352
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

2023-11-20 18:09:40.470920	True	1607	get	subnets
2023-11-20 18:09:40.974818	True	475	get	tenants
2023-11-20 18:09:41.254743	True	270	get	networks
```

[[Back]](./SubnetGet.md)