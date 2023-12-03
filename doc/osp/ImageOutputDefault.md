# Image

## Default output

```
# iserver get osp img --cluster pod1

Cluster: pod1

Image [#30]
-----------

+--------------------------------------+-------+-----------+----------------+--------+------------+-----------+----------------------------------+
| Name                                 | Disk  | Container | Size [B]       | Status | Visibility | Protected | Checksum                         |
+--------------------------------------+-------+-----------+----------------+--------+------------+-----------+----------------------------------+
| esc-5.10                             | qcow2 | bare      | 1,467,678,720  | active | public     | X         | 8024dd4edff3b5facd633580f1710f75 | 
| migrate-81288fe18055                 | qcow2 | bare      | 216,596,480    | active | private    | X         | bf3e50a15fd2fd5caf9835d21f88162c | 
| 7d8bb8b5-f286-4466-a583-b493b3084efe | raw   | bare      | 17,179,869,184 | active | private    | X         | d4a7872bebf404b37a8776cf14062531 | 
| final-before-migration-c8kv-orange   | qcow2 | bare      | 2,343,763,968  | active | private    | X         | ad42e085b954f5a2214c71c38e2f05ca | 
| my-cirros                            | qcow2 | bare      | 26,351,104     | active | private    | X         | acbba3dc308c003078ff3af371827a4e | 
| cirros                               | qcow2 | bare      | 16,338,944     | active | public     | X         | 1d3062cd89af34e419f7100277f38b2b | 
| rcm-21.28.m15                        | qcow2 | bare      | 4,415,356,928  | active | public     | X         | 209e798809cc6e09fc8d07f632cf09d6 | 
| esc-6.0                              | qcow2 | bare      | 2,036,203,520  | active | public     | X         | 24e27098c80de99b112a574a62f1a259 | 
| qvpc-di-xf-21.28.m15                 | qcow2 | bare      | 201,064,448    | active | public     | X         | d040fa8919c009318c600486f9057b77 | 
| qvpc-di-cf-21.28.m15                 | qcow2 | bare      | 209,125,376    | active | public     | X         | 5ce4a218e2394987b4b48e2782f613f9 | 
| qvpc-si-21.28.m15                    | qcow2 | bare      | 210,370,560    | active | public     | X         | 55e8916d3911570596ba35cd9aff8357 | 
| image-SDWAN-C8KV01                   | qcow2 | bare      | 2,436,956,160  | active | private    | X         | 2d29dd6799f105375eb3ef06184a8bc0 | 
| c8000v_17_09_01a_16G_vga             | qcow2 | bare      | 1,860,567,040  | active | public     | X         | 3836e1c924e21eb55b54397fef415c42 | 
| rcm-21.28.2                          | qcow2 | bare      | 4,064,215,040  | active | public     | X         | 14617b2ec8249200dd458f6228b0ce1b | 
| qvpc-si-21.28.h0                     | qcow2 | bare      | 223,150,080    | active | public     | X         | dd7dc7d10849d777cdabf22d34894599 | 
| qvpc-si-21.28.2                      | qcow2 | bare      | 212,074,496    | active | public     | X         | 4858ef8e164ac5fe3c8df7265122fadd | 
| qvpc-di-cf-21.28.2                   | qcow2 | bare      | 210,894,848    | active | public     | X         | 0bd42ab4e337ed927639bafe778afca1 | 
| qvpc-di-xf-21.28.2                   | qcow2 | bare      | 202,833,920    | active | public     | X         | 63d734d4d329406f8910c226784c02f0 | 
| smi-install-disk.20211122            | raw   | bare      | 443,547,648    | active | public     | X         | 5c076926d5c741e57a1b64cfe222dd72 | 
| qvpc-di-xf-21.27.1                   | qcow2 | bare      | 201,392,128    | active | public     | X         | cd2b564b606bd46a3d2e7b2060a72225 | 
| qvpc-di-cf-21.27.1                   | qcow2 | bare      | 209,518,592    | active | public     | X         | e0892942de2fb8f6fc47b72150c7e307 | 
| qvpc-si-21.27.h0                     | qcow2 | bare      | 221,839,360    | active | public     | X         | 5c4eb0fb4fbd048fa01b4b91707ed20e | 
| rcm-21.27.1                          | qcow2 | bare      | 3,726,704,640  | active | public     | X         | 904d622f8c15e3e41200de718d509559 | 
| portal-snapshot-20220802             | qcow2 | bare      | 80,702,210,048 | active | public     | X         | 06668115973408eaf8950f2d0eeff560 | 
| lattice-snapshot-20220802            | qcow2 | bare      | 23,308,992,512 | active | public     | X         | 114e9ea949c75b47e937b80a3a85f05c | 
| ubuntu-1804-i386                     | qcow2 | bare      | 351,797,248    | active | public     | X         | cec3dec44f5437a087b70403df7e6487 | 
| ubuntu-2204-amd64                    | qcow2 | bare      | 624,361,472    | active | public     | X         | 2454ccb3b986448911f6b5e99ca7d9c7 | 
| qvpc-si-21.27.1                      | qcow2 | bare      | 210,763,776    | active | public     | X         | d1f670c32c80d1282e5b24d6b190aab4 | 
| esc-5.6                              | qcow2 | bare      | 1,451,753,472  | active | public     | X         | 67c062ee700b9ccf6bb2adb7e9be52b9 | 
| RHEL-guest-image                     | qcow2 | bare      | 1,196,818,432  | active | shared     | X         | f0b3efae6e9eb9e2d500ed78b2544755 | 
+--------------------------------------+-------+-----------+----------------+--------+------------+-----------+----------------------------------+

Filter: name, vm
View:   state (def), id, vm, all
```

Developer

```
# iserver get osp img --cluster pod1

{
    "duration": 5128,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 0,
        "total_time": 0
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

2023-11-19 12:22:40.752874	True	0	get	images
```

[[Back]](./ImageGet.md)