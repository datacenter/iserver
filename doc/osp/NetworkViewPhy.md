# Network

## Phy view

```
# iserver get osp net --cluster pod1 -v id

Cluster: pod1

Network - Identifier [#15]
--------------------------

+--------------------------------------+----------------------------------------------------+----------------------------------+--------------------------------------+
| Id                                   | Name                                               | Tenant                           | Subnet                               |
+--------------------------------------+----------------------------------------------------+----------------------------------+--------------------------------------+
| d6a76040-e0f7-47d2-a4b8-542e896cc2ec | C8KV01_LAN01                                       | 9b50a8dba82f4c14802c4554482882b8 | db2b80bf-65d0-4836-9eb3-929eefb8fff0 | 
| 15c99bd1-25e1-445b-8c97-daf8eb5c66f2 | C8KV_ORANGE_LAN01                                  | 9b50a8dba82f4c14802c4554482882b8 | afd52863-ee94-4880-80be-fc6fd7788f6e | 
| a4fe3f25-a010-4cad-a945-0e36256b3783 | control-k8s                                        | 05b8e996f0654e4491d2e925a91c6250 | 4299410e-e562-46d6-93b0-d839669a5bca | 
| 25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43 | control-N2                                         | 05b8e996f0654e4491d2e925a91c6250 | 1786aa38-3ab1-4a86-9966-f4dae5411bab | 
| 0d6676b5-6fbc-4b51-bf29-1380cef97fcd | control-N4                                         | 05b8e996f0654e4491d2e925a91c6250 | ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a | 
| 02c949a8-1b9c-4162-a8ad-f8941a8f37d1 | control-SBI                                        | 05b8e996f0654e4491d2e925a91c6250 | 84b1de29-b4be-4508-8ad9-6c68c930dac5 | 
| bb3bf0cd-6361-4d79-8764-92eaa9de7880 | data-N3                                            | 05b8e996f0654e4491d2e925a91c6250 | addec922-7181-4039-be79-4da3d88d2c0a | 
| 10885efc-c3cf-41cf-b5ec-264996f1d78c | data-N6                                            | 05b8e996f0654e4491d2e925a91c6250 | ba7cff90-beb1-4061-ba6c-5c223ed56586 | 
| 4510e325-db2f-48ce-8e93-c1dcd6065825 | di-internal1                                       | 05b8e996f0654e4491d2e925a91c6250 | 4f59eb25-f662-490a-8e08-c427478857c1 | 
| e7474314-438a-43f6-9ddf-319f0578ca30 | external                                           | 2cced286b74c45ea95c83cc2e5d3b413 | 379bd679-fea7-4aa6-b8c3-0368ab2790a9 | 
| 68a6f31c-a4a1-4990-8654-3d00c6e9115e | HA network tenant 05b8e996f0654e4491d2e925a91c6250 |                                  | e122cda4-5250-467e-ba83-1e4fcfeb0b1b | 
| fe1e3247-64b8-45ae-aa40-468a9a768954 | management                                         | 05b8e996f0654e4491d2e925a91c6250 | 14b5c631-8d81-46b9-b3d9-abbb4acc0191 | 
| 3065667d-94c9-442c-87c1-bec9cffa0d50 | orchestration                                      | 05b8e996f0654e4491d2e925a91c6250 | 3ab58791-ba30-45a9-b185-d9f3809f2556 | 
| 7fa67775-1f5f-4dca-baaa-15ea5b55c4e2 | sriov0                                             | 05b8e996f0654e4491d2e925a91c6250 | 195953ed-add3-4c59-b81a-ee372dcd7838 | 
| cd63e7ec-39b2-4f47-9f46-df5d3e25c967 | sriov1                                             | 05b8e996f0654e4491d2e925a91c6250 | 1cbf95c8-b46c-4684-92da-7199481236c3 | 
+--------------------------------------+----------------------------------------------------+----------------------------------+--------------------------------------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 -v id

{
    "duration": 3417,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 3272,
        "total_time": 3272
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

2023-11-19 13:15:10.549796	True	3272	get	networks
```

[[Back]](./NetworkGet.md)