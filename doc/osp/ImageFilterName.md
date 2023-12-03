# Image

## Filter by name

```
# iserver get osp img --cluster pod1 --name qvpc*

Cluster: pod1

Image [#11]
-----------

+----------------------+-------+-----------+-------------+--------+------------+-----------+----------------------------------+
| Name                 | Disk  | Container | Size [B]    | Status | Visibility | Protected | Checksum                         |
+----------------------+-------+-----------+-------------+--------+------------+-----------+----------------------------------+
| qvpc-di-xf-21.28.m15 | qcow2 | bare      | 201,064,448 | active | public     | X         | d040fa8919c009318c600486f9057b77 | 
| qvpc-di-cf-21.28.m15 | qcow2 | bare      | 209,125,376 | active | public     | X         | 5ce4a218e2394987b4b48e2782f613f9 | 
| qvpc-si-21.28.m15    | qcow2 | bare      | 210,370,560 | active | public     | X         | 55e8916d3911570596ba35cd9aff8357 | 
| qvpc-si-21.28.h0     | qcow2 | bare      | 223,150,080 | active | public     | X         | dd7dc7d10849d777cdabf22d34894599 | 
| qvpc-si-21.28.2      | qcow2 | bare      | 212,074,496 | active | public     | X         | 4858ef8e164ac5fe3c8df7265122fadd | 
| qvpc-di-cf-21.28.2   | qcow2 | bare      | 210,894,848 | active | public     | X         | 0bd42ab4e337ed927639bafe778afca1 | 
| qvpc-di-xf-21.28.2   | qcow2 | bare      | 202,833,920 | active | public     | X         | 63d734d4d329406f8910c226784c02f0 | 
| qvpc-di-xf-21.27.1   | qcow2 | bare      | 201,392,128 | active | public     | X         | cd2b564b606bd46a3d2e7b2060a72225 | 
| qvpc-di-cf-21.27.1   | qcow2 | bare      | 209,518,592 | active | public     | X         | e0892942de2fb8f6fc47b72150c7e307 | 
| qvpc-si-21.27.h0     | qcow2 | bare      | 221,839,360 | active | public     | X         | 5c4eb0fb4fbd048fa01b4b91707ed20e | 
| qvpc-si-21.27.1      | qcow2 | bare      | 210,763,776 | active | public     | X         | d1f670c32c80d1282e5b24d6b190aab4 | 
+----------------------+-------+-----------+-------------+--------+------------+-----------+----------------------------------+

Filter: name, vm
View:   state (def), id, vm, all
```

Developer

```
# iserver get osp img --cluster pod1 --name qvpc*

{
    "duration": 4812,
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

2023-11-19 12:22:07.579182	True	0	get	images
```

[[Back]](./ImageGet.md)