# Virtual Machine

## Filter by name

```
# iserver get osp vm --cluster pod1 --flv upf*

Cluster: pod1

Virtual Machine [#3]
--------------------

+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+-----+
| Tenant | VM          | Hypervisor       | Status | Power      | Task | Boot Source             | Flavor | Resource         | Age |
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+-----+
| smi5gc | VPC-SI-upf1 | compute-server-1 | ACTIVE | powered-up | --   | (img) qvpc-si-21.28.m15 | upf1   | C:18 M:32768 D:6 | 3d  | 
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+-----+
| smi5gc | VPC-SI-upf2 | compute-server-2 | ACTIVE | powered-up | --   | (img) qvpc-si-21.28.m15 | upf2   | C:18 M:32768 D:6 | 3d  | 
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+-----+
| smi5gc | VPC-SI-upf8 | AIO-server-3     | ACTIVE | powered-up | --   | (img) qvpc-si-21.28.m15 | upf3   | C:18 M:32768 D:6 | 3d  | 
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+-----+

Filter: name, tenant, img, flv, net, address, mac, hv
View:   state (def), id, net, all
```

Developer

```
# iserver get osp vm --cluster pod1 --flv upf*

{
    "duration": 5936,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 3517,
        "total_time": 3517
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

2023-11-20 18:37:30.259973	True	2219	get	virtual_machines
2023-11-20 18:37:31.397317	True	1106	get	tenants
2023-11-20 18:37:31.595413	True	192	get	flavors
2023-11-20 18:37:32.286055	True	0	get	images
```

[[Back]](./VirtualMachineGet.md)