# Virtual Machine

## Filter by name

```
# iserver get osp vm --cluster pod1 --name portal

Cluster: pod1

Virtual Machine [#1]
--------------------

+--------+--------+--------------+--------+------------+------+--------------------------------+--------+------------------+------+
| Tenant | VM     | Hypervisor   | Status | Power      | Task | Boot Source                    | Flavor | Resource         | Age  |
+--------+--------+--------------+--------+------------+------+--------------------------------+--------+------------------+------+
| smi5gc | portal | AIO-server-1 | ACTIVE | powered-up | --   | (img) portal-snapshot-20220802 | portal | C:8 M:32768 D:80 | 473d | 
+--------+--------+--------------+--------+------------+------+--------------------------------+--------+------------------+------+

Filter: name, tenant, img, flv, net, address, mac, hv
View:   state (def), id, net, all
```

Developer

```
# iserver get osp vm --cluster pod1 --name portal

{
    "duration": 6160,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 3716,
        "total_time": 3716
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

2023-11-20 18:36:38.758203	True	2260	get	virtual_machines
2023-11-20 18:36:40.119724	True	1290	get	tenants
2023-11-20 18:36:40.298967	True	166	get	flavors
2023-11-20 18:36:40.881416	True	0	get	images
```

[[Back]](./VirtualMachineGet.md)