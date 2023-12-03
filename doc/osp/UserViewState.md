# User

## State view

```
# iserver get osp user --cluster pod1

Cluster: pod1

User [#10]
----------

+----------------------------------+-----------------+---------+--------+---------+-----------------+
| Id                               | Name            | Enabled | Expiry | Domain  | Default Project |
+----------------------------------+-----------------+---------+--------+---------+-----------------+
| a23ec81be2d9405db107acf4194f44f0 | admin           | V       | --     | default | --              | 
| 76ad41b7b7654c0d805d7ced89dfb696 | cinder          | V       | --     | default | --              | 
| 673f6e73b12b464fba269d143e26bb7f | cinder-internal | V       | --     | default | --              | 
| d50e3108321749d38684eb58012dc644 | cloudpulse      | V       | --     | default | --              | 
| 2adb20226c1f4906bf93a8f78e88bb77 | glance          | V       | --     | default | --              | 
| 522c200898cc4962a34e1e90cc42fd1b | ialonso         | V       | --     | default | ialonso         | 
| 80104c72e8e44713b7e01a15132de806 | neutron         | V       | --     | default | --              | 
| 0f2080e6a4144a7882117dbd9cedd233 | nova            | V       | --     | default | --              | 
| 36b87303c47a4e4893db28743135b8db | placement       | V       | --     | default | --              | 
| dea57460869c49e6a829ad88b5b14db1 | smi5gc          | V       | --     | default | smi5gc          | 
+----------------------------------+-----------------+---------+--------+---------+-----------------+

Filter: name
View:   state (def)
```

Developer

```
# iserver get osp user --cluster pod1

{
    "duration": 1404,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 1327,
        "total_time": 1327
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
        "lines": 2
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 09:31:33.830051	True	1086	get	users
2023-11-20 09:31:34.083472	True	241	get	tenants
```

[[Back]](./UserGet.md)