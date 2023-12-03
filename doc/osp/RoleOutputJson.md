# Role

## Default output

```
# iserver get osp role --cluster pod1 -o json

Cluster: pod1
[
    {
        "id": "0e1937746f634c9186f1b287de3303c5",
        "name": "_member_",
        "domain_id": null,
        "description": null,
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/roles/0e1937746f634c9186f1b287de3303c5"
        },
        "__Output": {}
    },
    {
        "id": "47151af5641149579acab097aa7b0261",
        "name": "reader",
        "domain_id": null,
        "description": null,
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/roles/47151af5641149579acab097aa7b0261"
        },
        "__Output": {}
    },
    {
        "id": "e1a3fd1ec760483db25911028f585e0a",
        "name": "member",
        "domain_id": null,
        "description": null,
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/roles/e1a3fd1ec760483db25911028f585e0a"
        },
        "__Output": {}
    },
    {
        "id": "efe2e47cb6344c52a8e4cb2127f95bcc",
        "name": "admin",
        "domain_id": null,
        "description": null,
        "options": {},
        "links": {
            "self": "https://10.58.28.113:5000/v3/roles/efe2e47cb6344c52a8e4cb2127f95bcc"
        },
        "__Output": {}
    }
]
```

Developer

```
# iserver get osp role --cluster pod1 -o json

{
    "duration": 1273,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1218,
        "total_time": 1218
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

2023-11-20 09:30:57.412053	True	1218	get	roles
```

[[Back]](./RoleGet.md)