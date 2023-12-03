# Subnet

## Identifier (id) view

```
# iserver get osp sub --cluster pod1 -v id

Cluster: pod1

Subnet - Identifier [#15]
-------------------------

+--------------------------------------+---------------------------------------------------+----------------------------------+
| Id                                   | Name                                              | Tenant                           |
+--------------------------------------+---------------------------------------------------+----------------------------------+
| 14b5c631-8d81-46b9-b3d9-abbb4acc0191 | management-subnet                                 | 05b8e996f0654e4491d2e925a91c6250 | 
| 1786aa38-3ab1-4a86-9966-f4dae5411bab | control-N2-subnet                                 | 05b8e996f0654e4491d2e925a91c6250 | 
| 195953ed-add3-4c59-b81a-ee372dcd7838 | sriov0-subnet                                     | 05b8e996f0654e4491d2e925a91c6250 | 
| 1cbf95c8-b46c-4684-92da-7199481236c3 | sriov1-subnet                                     | 05b8e996f0654e4491d2e925a91c6250 | 
| 379bd679-fea7-4aa6-b8c3-0368ab2790a9 | subnet-ext                                        | 2cced286b74c45ea95c83cc2e5d3b413 | 
| 3ab58791-ba30-45a9-b185-d9f3809f2556 | orchestration-subnet                              | 05b8e996f0654e4491d2e925a91c6250 | 
| 4299410e-e562-46d6-93b0-d839669a5bca | control-k8s-subnet                                | 05b8e996f0654e4491d2e925a91c6250 | 
| 4f59eb25-f662-490a-8e08-c427478857c1 | di-internal1-subnet                               | 05b8e996f0654e4491d2e925a91c6250 | 
| 84b1de29-b4be-4508-8ad9-6c68c930dac5 | control-SBI-subnet                                | 05b8e996f0654e4491d2e925a91c6250 | 
| ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a | control-N4-subnet                                 | 05b8e996f0654e4491d2e925a91c6250 | 
| addec922-7181-4039-be79-4da3d88d2c0a | data-N3-subnet                                    | 05b8e996f0654e4491d2e925a91c6250 | 
| afd52863-ee94-4880-80be-fc6fd7788f6e | C8KV_ORANGE_LAN01                                 | 9b50a8dba82f4c14802c4554482882b8 | 
| ba7cff90-beb1-4061-ba6c-5c223ed56586 | data-N6-subnet                                    | 05b8e996f0654e4491d2e925a91c6250 | 
| db2b80bf-65d0-4836-9eb3-929eefb8fff0 | C8KV01_LAN01                                      | 9b50a8dba82f4c14802c4554482882b8 | 
| e122cda4-5250-467e-ba83-1e4fcfeb0b1b | HA subnet tenant 05b8e996f0654e4491d2e925a91c6250 |                                  | 
+--------------------------------------+---------------------------------------------------+----------------------------------+

Filter: name, tenant, address, mac, vm, hv
View:   state (def), id, port, all
```

Developer

```
# iserver get osp sub --cluster pod1 -v id

{
    "duration": 1934,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1739,
        "total_time": 1739
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

2023-11-20 18:08:38.670812	True	1739	get	subnets
```

[[Back]](./SubnetGet.md)