# Volume

## Identifier (id) view

```
# iserver get osp vol --cluster pod1 -v id

Cluster: pod1

Volume - Indentifier [#6]
-------------------------

+-----------------------------------+--------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Name                              | Tenant | Id                                   | Snapshot                             | Attachment                           | VM                                   |
+-----------------------------------+--------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| cirros                            |        | 01ffbe45-fef6-4711-835b-6bf649e8ea90 | --                                   | --                                   | --                                   | 
| migratable_C8KV_ORANGE            |        | 1f50033c-93e8-44cd-9ad4-13b00613382f | --                                   | --                                   | --                                   | 
| migratable_c8kv                   |        | a9ee570a-e39c-424f-be5b-d2fb93de2984 | --                                   | --                                   | --                                   | 
| migratable_c8kv_vm                |        | 5fa13919-8d80-4f75-96e9-bc19556781ce | 38d68769-9faa-4cd1-be26-c18fccacac19 | --                                   | --                                   | 
| my-cirros                         |        | bb0b41d7-798d-47bd-9e13-701f9422904a | 309b0367-4ba2-415a-9213-ad47633f3caf | --                                   | --                                   | 
| volume_migratable_C8KV_ORANGE_new |        | 88b81c75-c333-45fa-be50-219e12ae5520 | ae0ae14b-4073-4279-a1e1-c0ec64935c55 | 5441fe7c-32c4-4192-a8e9-d607a66e6ad3 | f83b1396-40b2-4dec-b336-597fc42e55d7 | 
+-----------------------------------+--------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+

Filter: name, tenant, hv, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp vol --cluster pod1 -v id

{
    "duration": 1954,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1792,
        "total_time": 1792
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

2023-11-20 17:36:56.646413	True	1792	get	volumes.list
```

[[Back]](./VolumeGet.md)