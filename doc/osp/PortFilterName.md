# Port

## Filter by name

```
# iserver get osp port --cluster pod1 --name lattice*

Cluster: pod1

Port [#5]
---------

+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+
| MAC               | Admin | Status | Type    | Name               | IP           | Subnet             | Network     | Tenant | Age  |
+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+
| fa:16:3e:c3:6b:06 | V     | ACTIVE | Compute | lattice-management | 15.100.1.101 | management-subnet  | management  | smi5gc | 472d | 
+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+
| fa:16:3e:cc:7f:24 | V     | ACTIVE | Compute | lattice-sbi        | 15.100.4.101 | control-SBI-subnet | control-SBI | smi5gc | 472d | 
+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+
| fa:16:3e:63:7d:aa | V     | ACTIVE | Compute | lattice-n2         | 15.100.5.101 | control-N2-subnet  | control-N2  | smi5gc | 472d | 
+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+
| fa:16:3e:fe:4d:de | V     | ACTIVE | Compute | lattice-n4         | 15.100.6.101 | control-N4-subnet  | control-N4  | smi5gc | 472d | 
+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+
| fa:16:3e:70:4d:85 | V     | ACTIVE | Compute | lattice-n3         | 15.100.7.101 | data-N3-subnet     | data-N3     | smi5gc | 472d | 
+-------------------+-------+--------+---------+--------------------+--------------+--------------------+-------------+--------+------+

Filter: name, state, type, tenant, net, subnet, address, mac, hv, vm, sg
View:   state (def), id, sec, hv, all
```

Developer

```
# iserver get osp port --cluster pod1 --name lattice*

{
    "duration": 9688,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 9565,
        "total_time": 9565
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

2023-11-19 14:43:13.073939	True	7093	get	ports
2023-11-19 14:43:14.629632	True	1538	get	tenants
2023-11-19 14:43:15.384908	True	750	get	networks
2023-11-19 14:43:15.579801	True	184	get	subnets
```

[[Back]](./PortGet.md)