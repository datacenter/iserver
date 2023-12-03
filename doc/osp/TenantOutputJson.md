# Tenant

## Default output

```
# iserver get osp tenant --cluster pod1 -o json

Cluster: pod1
[
    {
        "id": "05b8e996f0654e4491d2e925a91c6250",
        "name": "smi5gc",
        "domain_id": "default",
        "description": "",
        "enabled": true,
        "parent_id": "default",
        "is_domain": false,
        "tags": [],
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/projects/05b8e996f0654e4491d2e925a91c6250"
        },
        "__Output": {}
    },
    {
        "id": "2cced286b74c45ea95c83cc2e5d3b413",
        "name": "admin",
        "domain_id": "default",
        "description": "Bootstrap project for initializing the cloud.",
        "enabled": true,
        "parent_id": "default",
        "is_domain": false,
        "tags": [],
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/projects/2cced286b74c45ea95c83cc2e5d3b413"
        },
        "__Output": {}
    },
    {
        "id": "9b50a8dba82f4c14802c4554482882b8",
        "name": "ialonso",
        "domain_id": "default",
        "description": "",
        "enabled": true,
        "parent_id": "default",
        "is_domain": false,
        "tags": [],
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/projects/9b50a8dba82f4c14802c4554482882b8"
        },
        "__Output": {}
    },
    {
        "id": "c4a93dc9499e40f78e32a83d914e6a87",
        "name": "service",
        "domain_id": "default",
        "description": "",
        "enabled": true,
        "parent_id": "default",
        "is_domain": false,
        "tags": [],
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/projects/c4a93dc9499e40f78e32a83d914e6a87"
        },
        "__Output": {}
    },
    {
        "id": "ece266e361054538b965ceebea009241",
        "name": "cinder-internal",
        "domain_id": "default",
        "description": "",
        "enabled": true,
        "parent_id": "default",
        "is_domain": false,
        "tags": [],
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/projects/ece266e361054538b965ceebea009241"
        },
        "__Output": {}
    }
]
```

Developer

```
# iserver get osp tenant --cluster pod1 -o json

{
    "duration": 1272,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1224,
        "total_time": 1224
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

2023-11-20 09:33:21.060796	True	1224	get	tenants
```

[[Back]](./TenantGet.md)