# Flavor

## Identifier (id) view

```
# iserver get osp flv --cluster pod1 -v id

Cluster: pod1

Flavor - Identifiers [#29]
--------------------------

+--------------------------------------+-----------------------+
| Id                                   | Name                  |
+--------------------------------------+-----------------------+
| 0d160026-5947-445a-9eb8-1dc4c076225a | cirros                | 
| 2a27ea69-1f24-413a-a440-1bc0ca7a4951 | esc                   | 
| e86bad11-d0f6-4a7a-be57-f562e9433358 | flavor_c8kv_4096_0_4  | 
| 7b4877fe-79e4-4b6b-a919-36b1774e607c | lattice               | 
| 751a9512-57a4-41c4-8a9c-c52de1955d16 | mmesgsn               | 
| e5d37c1d-f945-4b19-9f51-d94ee48091f7 | portal                | 
| efe7e5cd-ed6a-43a1-9799-d63ae65dffda | rcm                   | 
| ae3aa692-2e32-4c35-8d59-df0fddeed973 | server                | 
| ecc69903-0a77-4d3b-b455-942290becae6 | smi-cm                | 
| 5536b0a1-50d2-4ef0-8626-9477d9cb637a | smi-etcd1             | 
| 53c0dc56-d130-4448-bf6f-efcc93a60ab5 | smi-etcd2             | 
| 2a61bf1a-7d64-4a1e-90d0-236180d67ff0 | smi-etcd3             | 
| 6b8aaf2b-0bd2-4ba2-ad63-b3971e12966a | smi-master1           | 
| bac96581-ad6e-4ddf-919e-f37ee176dc36 | smi-master2           | 
| 1020d556-6f3d-440f-a63d-376e393d1ca0 | smi-master3           | 
| 831f8d4e-8b53-4e0a-ab6b-6ae24e8602df | smi-oam1              | 
| 4058f62c-ae1c-4a65-a3cc-913cfb4cce30 | smi-oam2              | 
| 87d28126-1276-4340-abd5-98fd91885dd4 | smi-oam3              | 
| 7577fc58-5259-43d8-9d9d-f407f94607df | smi-worker-protocol-1 | 
| 363c29eb-53a7-4bfb-b288-21f3ec21dab9 | smi-worker-protocol-2 | 
| 11043fb4-3c31-4916-b866-50546a62df6e | smi-worker-svccdl-1   | 
| 5222fdc1-8b88-4a5b-abcb-d3c3e076a4d9 | smi-worker-svccdl-2   | 
| 24f809c3-f3d8-4b42-9507-6dc03cf5b638 | upf                   | 
| e64aa121-041e-405d-bafa-62936198732d | upf1                  | 
| 67f4b719-f367-4191-86fb-a97fe6b0c6b3 | upf2                  | 
| 1c15b1c8-edd8-441d-a799-c35939f226b4 | upf3                  | 
| 72062904-0bf1-440b-9ea4-f7ac4e723c1b | vpc-cf                | 
| b650b041-d398-42fa-89d1-619cdb912a4f | vpc-sf                | 
| f0db7ec9-0c28-4fc4-a88a-d7dc62ee0043 | vpc-si-saegw-c        | 
+--------------------------------------+-----------------------+

Filter: name, vm, key, value
View:   state (def), id, key, vm, all
```

Developer

```
# iserver get osp flv --cluster pod1 -v id

{
    "duration": 3416,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 2366,
        "total_time": 2366
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

2023-11-19 09:24:41.930438	True	2366	get	flavors
```

[[Back]](./FlavorGet.md)