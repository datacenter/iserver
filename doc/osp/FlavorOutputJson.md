# Flavor

## Default output

```
# iserver get osp flv --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "0d160026-5947-445a-9eb8-1dc4c076225a",
        "name": "cirros",
        "vcpus": 1,
        "ram": 2048,
        "disk": 20,
        "rxtx_factor": 1.0,
        "resource": "C:1 M:2048 D:20",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "2a27ea69-1f24-413a-a440-1bc0ca7a4951",
        "name": "esc",
        "vcpus": 2,
        "ram": 6144,
        "disk": 40,
        "rxtx_factor": 1.0,
        "resource": "C:2 M:6144 D:40",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "e86bad11-d0f6-4a7a-be57-f562e9433358",
        "name": "flavor_c8kv_4096_0_4",
        "vcpus": 4,
        "ram": 4096,
        "disk": 0,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:4096 D:0",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "7b4877fe-79e4-4b6b-a919-36b1774e607c",
        "name": "lattice",
        "vcpus": 8,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:8 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "751a9512-57a4-41c4-8a9c-c52de1955d16",
        "name": "mmesgsn",
        "vcpus": 2,
        "ram": 16384,
        "disk": 4,
        "rxtx_factor": 1.0,
        "resource": "C:2 M:16384 D:4",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "e5d37c1d-f945-4b19-9f51-d94ee48091f7",
        "name": "portal",
        "vcpus": 8,
        "ram": 32768,
        "disk": 80,
        "rxtx_factor": 1.0,
        "resource": "C:8 M:32768 D:80",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "efe7e5cd-ed6a-43a1-9799-d63ae65dffda",
        "name": "rcm",
        "vcpus": 4,
        "ram": 12228,
        "disk": 40,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:12228 D:40",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "ae3aa692-2e32-4c35-8d59-df0fddeed973",
        "name": "server",
        "vcpus": 2,
        "ram": 4096,
        "disk": 40,
        "rxtx_factor": 1.0,
        "resource": "C:2 M:4096 D:40",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "ecc69903-0a77-4d3b-b455-942290becae6",
        "name": "smi-cm",
        "vcpus": 8,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:8 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "5536b0a1-50d2-4ef0-8626-9477d9cb637a",
        "name": "smi-etcd1",
        "vcpus": 4,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "53c0dc56-d130-4448-bf6f-efcc93a60ab5",
        "name": "smi-etcd2",
        "vcpus": 4,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "2a61bf1a-7d64-4a1e-90d0-236180d67ff0",
        "name": "smi-etcd3",
        "vcpus": 4,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "6b8aaf2b-0bd2-4ba2-ad63-b3971e12966a",
        "name": "smi-master1",
        "vcpus": 4,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "bac96581-ad6e-4ddf-919e-f37ee176dc36",
        "name": "smi-master2",
        "vcpus": 4,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "1020d556-6f3d-440f-a63d-376e393d1ca0",
        "name": "smi-master3",
        "vcpus": 4,
        "ram": 32768,
        "disk": 100,
        "rxtx_factor": 1.0,
        "resource": "C:4 M:32768 D:100",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "831f8d4e-8b53-4e0a-ab6b-6ae24e8602df",
        "name": "smi-oam1",
        "vcpus": 12,
        "ram": 65536,
        "disk": 160,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:65536 D:160",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "4058f62c-ae1c-4a65-a3cc-913cfb4cce30",
        "name": "smi-oam2",
        "vcpus": 12,
        "ram": 65536,
        "disk": 160,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:65536 D:160",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "87d28126-1276-4340-abd5-98fd91885dd4",
        "name": "smi-oam3",
        "vcpus": 12,
        "ram": 65536,
        "disk": 160,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:65536 D:160",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "7577fc58-5259-43d8-9d9d-f407f94607df",
        "name": "smi-worker-protocol-1",
        "vcpus": 12,
        "ram": 32768,
        "disk": 80,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:32768 D:80",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "363c29eb-53a7-4bfb-b288-21f3ec21dab9",
        "name": "smi-worker-protocol-2",
        "vcpus": 12,
        "ram": 32768,
        "disk": 80,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:32768 D:80",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "11043fb4-3c31-4916-b866-50546a62df6e",
        "name": "smi-worker-svccdl-1",
        "vcpus": 12,
        "ram": 32768,
        "disk": 80,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:32768 D:80",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "5222fdc1-8b88-4a5b-abcb-d3c3e076a4d9",
        "name": "smi-worker-svccdl-2",
        "vcpus": 12,
        "ram": 32768,
        "disk": 80,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:32768 D:80",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "24f809c3-f3d8-4b42-9507-6dc03cf5b638",
        "name": "upf",
        "vcpus": 18,
        "ram": 32768,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:18 M:32768 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "e64aa121-041e-405d-bafa-62936198732d",
        "name": "upf1",
        "vcpus": 18,
        "ram": 32768,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:18 M:32768 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "67f4b719-f367-4191-86fb-a97fe6b0c6b3",
        "name": "upf2",
        "vcpus": 18,
        "ram": 32768,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:18 M:32768 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "1c15b1c8-edd8-441d-a799-c35939f226b4",
        "name": "upf3",
        "vcpus": 18,
        "ram": 32768,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:18 M:32768 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "72062904-0bf1-440b-9ea4-f7ac4e723c1b",
        "name": "vpc-cf",
        "vcpus": 8,
        "ram": 30720,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:8 M:30720 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "b650b041-d398-42fa-89d1-619cdb912a4f",
        "name": "vpc-sf",
        "vcpus": 12,
        "ram": 30720,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:30720 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 0
    },
    {
        "__Output": {
            "publicTick": "Green",
            "enabledTick": "Green"
        },
        "id": "f0db7ec9-0c28-4fc4-a88a-d7dc62ee0043",
        "name": "vpc-si-saegw-c",
        "vcpus": 12,
        "ram": 32768,
        "disk": 6,
        "rxtx_factor": 1.0,
        "resource": "C:12 M:32768 D:6",
        "public": true,
        "publicTick": "\u2713",
        "enabled": true,
        "enabledTick": "\u2713",
        "ephemeral": 16
    }
]
```

Developer

```
# iserver get osp flv --cluster pod1 -o json

{
    "duration": 8073,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 7578,
        "total_time": 7578
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

2023-11-19 09:27:10.808964	True	7578	get	flavors
```

[[Back]](./FlavorGet.md)