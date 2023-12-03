# User

## Default output

```
# iserver get osp user --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "a23ec81be2d9405db107acf4194f44f0",
        "name": "admin",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "76ad41b7b7654c0d805d7ced89dfb696",
        "name": "cinder",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "673f6e73b12b464fba269d143e26bb7f",
        "name": "cinder-internal",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "d50e3108321749d38684eb58012dc644",
        "name": "cloudpulse",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "2adb20226c1f4906bf93a8f78e88bb77",
        "name": "glance",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "522c200898cc4962a34e1e90cc42fd1b",
        "name": "ialonso",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": "9b50a8dba82f4c14802c4554482882b8",
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": "ialonso"
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "80104c72e8e44713b7e01a15132de806",
        "name": "neutron",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "0f2080e6a4144a7882117dbd9cedd233",
        "name": "nova",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "36b87303c47a4e4893db28743135b8db",
        "name": "placement",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": null,
        "ignore_change_password_upon_first_use": true,
        "ignore_password_expiry": true,
        "ignore_lockout_failure_attempts": true,
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": null
    },
    {
        "__Output": {
            "enabledTick": "Green"
        },
        "id": "dea57460869c49e6a829ad88b5b14db1",
        "name": "smi5gc",
        "domain_id": "default",
        "enabled": true,
        "password_expires_at": null,
        "default_project_id": "05b8e996f0654e4491d2e925a91c6250",
        "enabledTick": "\u2713",
        "expiresTick": "--",
        "default_project_name": "smi5gc"
    }
]
```

Developer

```
# iserver get osp user --cluster pod1 -o json

{
    "duration": 1564,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 1392,
        "total_time": 1392
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

2023-11-20 09:31:55.505821	True	1114	get	users
2023-11-20 09:31:55.790966	True	278	get	tenants
```

[[Back]](./UserGet.md)