# Virtual Machine

## Filter by image

```
# iserver get osp vm --cluster pod1 --img esc-5.6

Cluster: pod1

Virtual Machine [#1]
--------------------

+--------+-----+--------------+--------+------------+------+---------------+--------+-----------------+-----+
| Tenant | VM  | Hypervisor   | Status | Power      | Task | Boot Source   | Flavor | Resource        | Age |
+--------+-----+--------------+--------+------------+------+---------------+--------+-----------------+-----+
| smi5gc | esc | AIO-server-2 | ACTIVE | powered-up | --   | (img) esc-5.6 | esc    | C:2 M:6144 D:40 | 4d  | 
+--------+-----+--------------+--------+------------+------+---------------+--------+-----------------+-----+

Filter: name, tenant, img, flv, net, address, mac, hv
View:   state (def), id, net, all
```

Developer

```
# iserver get osp vm --cluster pod1 --img esc-5.6

{
    "duration": 7608,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 5144,
        "total_time": 5144
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
        "lines": 5
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 18:37:13.266583	True	2686	get	virtual_machines
2023-11-20 18:37:14.627476	True	1259	get	tenants
2023-11-20 18:37:14.808430	True	166	get	flavors
2023-11-20 18:37:15.566362	True	0	get	images
2023-11-20 18:37:17.495775	True	1033	get	volumes.list
```

[[Back]](./VirtualMachineGet.md)