# Volume

## All view

```
# iserver get osp vol --cluster pod1 -v all

Cluster: pod1

Volume [#6]
-----------

+-----------------------------------+--------+-----------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+
| Name                              | Tenant | Status    | Snap | Boot | Encr | Multi | Size | Type        | VM                | Device   | HV               | Age |
+-----------------------------------+--------+-----------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+
| cirros                            | admin  | available | X    | V    | X    | X     | 20   | __DEFAULT__ | --                | --       | --               | 21d | 
| migratable_C8KV_ORANGE            | admin  | available | X    | V    | X    | X     | 16   | __DEFAULT__ | --                | --       | --               | 18d | 
| migratable_c8kv                   | admin  | available | X    | V    | X    | X     | 16   | __DEFAULT__ | --                | --       | --               | 27d | 
| migratable_c8kv_vm                | admin  | available | V    | V    | X    | X     | 16   | __DEFAULT__ | --                | --       | --               | 21d | 
| my-cirros                         | admin  | available | V    | V    | X    | X     | 20   | __DEFAULT__ | --                | --       | --               | 20d | 
| volume_migratable_C8KV_ORANGE_new | admin  | in-use    | V    | V    | X    | X     | 16   | __DEFAULT__ | admin/c8koncinder | /dev/vda | compute-server-2 | 18d | 
+-----------------------------------+--------+-----------+------+------+------+-------+------+-------------+-------------------+----------+------------------+-----+

Volume - Indentifier [#6]
-------------------------

+-----------------------------------+--------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| Name                              | Tenant | Id                                   | Snapshot                             | Attachment                           | VM                                   |
+-----------------------------------+--------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+
| cirros                            | admin  | 01ffbe45-fef6-4711-835b-6bf649e8ea90 | --                                   | --                                   | --                                   | 
| migratable_C8KV_ORANGE            | admin  | 1f50033c-93e8-44cd-9ad4-13b00613382f | --                                   | --                                   | --                                   | 
| migratable_c8kv                   | admin  | a9ee570a-e39c-424f-be5b-d2fb93de2984 | --                                   | --                                   | --                                   | 
| migratable_c8kv_vm                | admin  | 5fa13919-8d80-4f75-96e9-bc19556781ce | 38d68769-9faa-4cd1-be26-c18fccacac19 | --                                   | --                                   | 
| my-cirros                         | admin  | bb0b41d7-798d-47bd-9e13-701f9422904a | 309b0367-4ba2-415a-9213-ad47633f3caf | --                                   | --                                   | 
| volume_migratable_C8KV_ORANGE_new | admin  | 88b81c75-c333-45fa-be50-219e12ae5520 | ae0ae14b-4073-4279-a1e1-c0ec64935c55 | 5441fe7c-32c4-4192-a8e9-d607a66e6ad3 | f83b1396-40b2-4dec-b336-597fc42e55d7 | 
+-----------------------------------+--------+--------------------------------------+--------------------------------------+--------------------------------------+--------------------------------------+

Filter: name, tenant, hv, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp vol --cluster pod1 -v all

{
    "duration": 5332,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4658,
        "total_time": 4658
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

2023-11-20 17:37:09.417031	True	1841	get	volumes.list
2023-11-20 17:37:09.712505	True	264	get	tenants
2023-11-20 17:37:12.743071	True	2553	get	virtual_machines
```

[[Back]](./VolumeGet.md)