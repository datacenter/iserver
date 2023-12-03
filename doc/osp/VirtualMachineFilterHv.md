# Virtual Machine

## Filter by hypervisor (hv)

```
# iserver get osp vm --cluster pod1 --hv compute-server-1

Cluster: pod1

Virtual Machine [#3]
--------------------

+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+------+
| Tenant | VM          | Hypervisor       | Status | Power      | Task | Boot Source             | Flavor | Resource         | Age  |
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+------+
| admin  | test-sriov  | compute-server-1 | ACTIVE | powered-up | --   | (img) ubuntu-2204-amd64 | server | C:2 M:4096 D:40  | 203d | 
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+------+
| smi5gc | server      | compute-server-1 | ACTIVE | powered-up | --   | (img) ubuntu-1804-i386  | server | C:2 M:4096 D:40  | 473d | 
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+------+
| smi5gc | VPC-SI-upf1 | compute-server-1 | ACTIVE | powered-up | --   | (img) qvpc-si-21.28.m15 | upf1   | C:18 M:32768 D:6 | 3d   | 
+--------+-------------+------------------+--------+------------+------+-------------------------+--------+------------------+------+

Filter: name, tenant, img, flv, net, address, mac, hv
View:   state (def), id, net, all
```

Developer

```
# iserver get osp vm --cluster pod1 --hv compute-server-1

{
    "duration": 6653,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 3888,
        "total_time": 3888
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

2023-11-20 18:38:51.124473	True	2301	get	virtual_machines
2023-11-20 18:38:52.624293	True	1418	get	tenants
2023-11-20 18:38:52.809204	True	169	get	flavors
2023-11-20 18:38:53.862456	True	0	get	images
```

[[Back]](./VirtualMachineGet.md)