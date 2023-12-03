# Port

## Filter by security group

```
# iserver get osp port --cluster pod1 --sg smi5gc/portal -v sec

Cluster: pod1

Port - Security [#1]
--------------------

+-------------------+-------+--------+---------+--------------+---------------+----------------------+---------------+----------------+
| MAC               | Admin | Status | Type    | IP           | VM            | Allowed Access Pairs | Port Security | Security Group |
+-------------------+-------+--------+---------+--------------+---------------+----------------------+---------------+----------------+
| fa:16:3e:cc:97:82 | V     | ACTIVE | Compute | 15.100.1.100 | smi5gc/portal |                      | V             | smi5gc/portal  | 
+-------------------+-------+--------+---------+--------------+---------------+----------------------+---------------+----------------+

Filter: name, state, type, tenant, net, subnet, address, mac, hv, vm, sg
View:   state (def), id, sec, hv, all
```

Developer

```
# iserver get osp port --cluster pod1 --sg smi5gc/portal -v sec

{
    "duration": 9035,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 8708,
        "total_time": 8708
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

2023-11-19 14:44:48.254171	True	1902	get	ports
2023-11-19 14:44:48.846754	True	570	get	security_groups
2023-11-19 14:44:49.343080	True	487	get	tenants
2023-11-19 14:44:55.297607	True	5749	get	virtual_machines
```

[[Back]](./PortGet.md)