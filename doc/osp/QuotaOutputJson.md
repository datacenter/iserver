# Quota

## Default output

```
# iserver get osp quota --cluster pod1 -o json

Cluster: pod1
[
    {
        "id": "2cced286b74c45ea95c83cc2e5d3b413",
        "cores": 20,
        "fixed_ips": -1,
        "floating_ips": 10,
        "injected_file_content_bytes": 65536,
        "injected_file_path_bytes": 255,
        "injected_files": 5,
        "instances": 10,
        "key_pairs": 100,
        "metadata_items": 128,
        "ram": 51200,
        "security_group_rules": 20,
        "security_groups": 10,
        "server_group_members": 10,
        "server_groups": 10,
        "__Output": {},
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "tenant_name": "admin"
    },
    {
        "id": "ece266e361054538b965ceebea009241",
        "cores": 20,
        "fixed_ips": -1,
        "floating_ips": 10,
        "injected_file_content_bytes": 65536,
        "injected_file_path_bytes": 255,
        "injected_files": 5,
        "instances": 10,
        "key_pairs": 100,
        "metadata_items": 128,
        "ram": 51200,
        "security_group_rules": 20,
        "security_groups": 10,
        "server_group_members": 10,
        "server_groups": 10,
        "__Output": {},
        "tenant_id": "ece266e361054538b965ceebea009241",
        "tenant_name": "cinder-internal"
    },
    {
        "id": "9b50a8dba82f4c14802c4554482882b8",
        "cores": 20,
        "fixed_ips": -1,
        "floating_ips": 10,
        "injected_file_content_bytes": 200000,
        "injected_file_path_bytes": 255,
        "injected_files": 5,
        "instances": 10,
        "key_pairs": 100,
        "metadata_items": 128,
        "ram": 204800,
        "security_group_rules": 20,
        "security_groups": 10,
        "server_group_members": 10,
        "server_groups": 10,
        "__Output": {},
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "tenant_name": "ialonso"
    },
    {
        "id": "c4a93dc9499e40f78e32a83d914e6a87",
        "cores": 20,
        "fixed_ips": -1,
        "floating_ips": 10,
        "injected_file_content_bytes": 65536,
        "injected_file_path_bytes": 255,
        "injected_files": 5,
        "instances": 10,
        "key_pairs": 100,
        "metadata_items": 128,
        "ram": 51200,
        "security_group_rules": 20,
        "security_groups": 10,
        "server_group_members": 10,
        "server_groups": 10,
        "__Output": {},
        "tenant_id": "c4a93dc9499e40f78e32a83d914e6a87",
        "tenant_name": "service"
    },
    {
        "id": "05b8e996f0654e4491d2e925a91c6250",
        "cores": 2000,
        "fixed_ips": -1,
        "floating_ips": 10,
        "injected_file_content_bytes": 655360,
        "injected_file_path_bytes": 255,
        "injected_files": 50,
        "instances": 100,
        "key_pairs": 1000,
        "metadata_items": 1280,
        "ram": 5120000,
        "security_group_rules": 20,
        "security_groups": 10,
        "server_group_members": 100,
        "server_groups": 100,
        "__Output": {},
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "tenant_name": "smi5gc"
    }
]
```

Developer

```
# iserver get osp quota --cluster pod1 -o json

{
    "duration": 5476,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 5203,
        "total_time": 5203
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

2023-11-20 09:28:17.085631	True	1126	get	tenants
2023-11-20 09:28:21.379632	True	4077	get	quotas
```

[[Back]](./QuotaGet.md)