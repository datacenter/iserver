# Floating IP

## All view

```
# iserver get osp fip --cluster pod1 -v all

Cluster: pod1

Floating IP [#7]
----------------

+--------+-------------+---------+----------+--------------+-------------------+------------+-----------------------+---------------+
| Status | Floating    | Tenant  | Network  | Fixed        | MAC               | Network    | VM                    | Router        |
+--------+-------------+---------+----------+--------------+-------------------+------------+-----------------------+---------------+
| ACTIVE | 10.58.28.82 | smi5gc  | external | 15.100.1.36  | fa:16:3e:bb:2b:cd | management | smi5gc/esc            | smi5gc-router | 
| ACTIVE | 10.58.28.83 | smi5gc  | external | 15.100.1.102 | fa:16:3e:38:40:30 | management | smi5gc/server         | smi5gc-router | 
| ACTIVE | 10.58.28.84 | smi5gc  | external | 15.100.1.100 | fa:16:3e:cc:97:82 | management | smi5gc/portal         | smi5gc-router | 
| ACTIVE | 10.58.28.85 | smi5gc  | external | 15.100.1.101 | fa:16:3e:c3:6b:06 | management | smi5gc/lattice        | smi5gc-router | 
| ACTIVE | 10.58.28.90 | ialonso | external | 15.100.1.30  | fa:16:3e:14:7d:d0 | management | ialonso/SDWAN-C8KV01B | smi5gc-router | 
| ACTIVE | 10.58.28.91 | ialonso | external | 15.100.1.219 | fa:16:3e:97:c1:38 | management | ialonso/ORANGE-C8KV-1 | smi5gc-router | 
| ACTIVE | 10.58.28.92 | ialonso | external | 15.100.1.179 | fa:16:3e:a4:f5:53 | management | ialonso/ORANGE-C8KV-2 | smi5gc-router | 
+--------+-------------+---------+----------+--------------+-------------------+------------+-----------------------+---------------+

Floating IP - Identifiers[#7]
-----------------------------

+--------+-------------+--------------------------------------+--------------+--------------------------------------+--------------------------------------+--------------------------------------+----------------------------------+
| Status | Floating    | Network                              | Fixed        | Network                              | VM                                   | Router                               | Tenant                           |
+--------+-------------+--------------------------------------+--------------+--------------------------------------+--------------------------------------+--------------------------------------+----------------------------------+
| ACTIVE | 10.58.28.82 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.36  | fe1e3247-64b8-45ae-aa40-468a9a768954 | 61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db | 424d1cba-254f-47af-9b42-a05465be1d97 | 05b8e996f0654e4491d2e925a91c6250 | 
| ACTIVE | 10.58.28.83 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.102 | fe1e3247-64b8-45ae-aa40-468a9a768954 | b56451ce-e214-4484-9f35-e656a95a8328 | 424d1cba-254f-47af-9b42-a05465be1d97 | 05b8e996f0654e4491d2e925a91c6250 | 
| ACTIVE | 10.58.28.84 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.100 | fe1e3247-64b8-45ae-aa40-468a9a768954 | 3fea1ac9-25cc-4183-976e-af79a513aa36 | 424d1cba-254f-47af-9b42-a05465be1d97 | 05b8e996f0654e4491d2e925a91c6250 | 
| ACTIVE | 10.58.28.85 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.101 | fe1e3247-64b8-45ae-aa40-468a9a768954 | 53e7b6fe-e33e-4d83-8936-ab8fe9b26d60 | 424d1cba-254f-47af-9b42-a05465be1d97 | 05b8e996f0654e4491d2e925a91c6250 | 
| ACTIVE | 10.58.28.90 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.30  | fe1e3247-64b8-45ae-aa40-468a9a768954 | 1fb263d3-437c-47dc-b3a0-38168a0a9e41 | 424d1cba-254f-47af-9b42-a05465be1d97 | 9b50a8dba82f4c14802c4554482882b8 | 
| ACTIVE | 10.58.28.91 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.219 | fe1e3247-64b8-45ae-aa40-468a9a768954 | 4e8f1b44-593d-492b-8985-094e6f88f83b | 424d1cba-254f-47af-9b42-a05465be1d97 | 9b50a8dba82f4c14802c4554482882b8 | 
| ACTIVE | 10.58.28.92 | e7474314-438a-43f6-9ddf-319f0578ca30 | 15.100.1.179 | fe1e3247-64b8-45ae-aa40-468a9a768954 | 0f3afdc8-8405-460a-a3cc-95944c695d4d | 424d1cba-254f-47af-9b42-a05465be1d97 | 9b50a8dba82f4c14802c4554482882b8 | 
+--------+-------------+--------------------------------------+--------------+--------------------------------------+--------------------------------------+--------------------------------------+----------------------------------+

Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm
View:   state (def), id, all
```

Developer

```
# iserver get osp fip --cluster pod1 -v all

{
    "duration": 7244,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 5843,
        "total_time": 5843
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

2023-11-18 16:49:16.353447	True	2287	get	floating_ips
2023-11-18 16:49:16.731895	True	360	get	tenants
2023-11-18 16:49:17.097394	True	351	get	networks
2023-11-18 16:49:17.451327	True	317	get	routers
2023-11-18 16:49:20.900666	True	2528	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)