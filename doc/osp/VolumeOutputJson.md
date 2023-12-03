# Volume

## Default output

```
# iserver get osp vol --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "status": "Green"
        },
        "id": "01ffbe45-fef6-4711-835b-6bf649e8ea90",
        "status": "available",
        "size": 20,
        "availability_zone": "nova",
        "created_at": "2023-10-30T15:26:38.000000",
        "updated_at": "2023-11-02T14:06:52.000000",
        "name": "cirros",
        "description": null,
        "volume_type": "__DEFAULT__",
        "snapshot_id": null,
        "bootable": "true",
        "encrypted": false,
        "multiattach": false,
        "volume_image_metadata": {
            "signature_verified": "False",
            "image_id": "f59b504b-42b7-415f-b34a-72dd53043bc0",
            "image_name": "cirros",
            "checksum": "1d3062cd89af34e419f7100277f38b2b",
            "container_format": "bare",
            "disk_format": "qcow2",
            "min_disk": "0",
            "min_ram": "0",
            "size": "16338944"
        },
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "attachment": [],
        "bootableTick": "\u2713",
        "encryptedTick": "\u2717",
        "multiattachTick": "\u2717",
        "snapshotTick": "\u2717",
        "created_age": "21d",
        "updated_age": "18d",
        "tenant_name": "admin"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "1f50033c-93e8-44cd-9ad4-13b00613382f",
        "status": "available",
        "size": 16,
        "availability_zone": "nova",
        "created_at": "2023-11-01T20:26:03.000000",
        "updated_at": "2023-11-01T20:27:05.000000",
        "name": "migratable_C8KV_ORANGE",
        "description": null,
        "volume_type": "__DEFAULT__",
        "snapshot_id": null,
        "bootable": "true",
        "encrypted": false,
        "multiattach": false,
        "volume_image_metadata": {
            "signature_verified": "False",
            "base_image_ref": "06e5174d-124d-444d-9aca-8e2e82218865",
            "boot_roles": "member,reader,admin",
            "image_location": "snapshot",
            "image_state": "available",
            "image_type": "snapshot",
            "instance_uuid": "0f3afdc8-8405-460a-a3cc-95944c695d4d",
            "owner_id": "9b50a8dba82f4c14802c4554482882b8",
            "owner_project_name": "ialonso",
            "owner_user_name": "ialonso",
            "user_id": "a23ec81be2d9405db107acf4194f44f0",
            "image_id": "e8a4ea55-c142-48c9-bc58-455389c3324a",
            "image_name": "SNAPSHOT_IMAGE_C8KV_ORANGE",
            "checksum": "0beddedeaeb5e236b5778482dedc1040",
            "container_format": "bare",
            "disk_format": "qcow2",
            "min_disk": "0",
            "min_ram": "0",
            "size": "2591752192"
        },
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "attachment": [],
        "bootableTick": "\u2713",
        "encryptedTick": "\u2717",
        "multiattachTick": "\u2717",
        "snapshotTick": "\u2717",
        "created_age": "18d",
        "updated_age": "18d",
        "tenant_name": "admin"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "a9ee570a-e39c-424f-be5b-d2fb93de2984",
        "status": "available",
        "size": 16,
        "availability_zone": "nova",
        "created_at": "2023-10-24T09:04:12.000000",
        "updated_at": "2023-11-01T19:46:19.000000",
        "name": "migratable_c8kv",
        "description": null,
        "volume_type": "__DEFAULT__",
        "snapshot_id": null,
        "bootable": "true",
        "encrypted": false,
        "multiattach": false,
        "volume_image_metadata": {
            "signature_verified": "False",
            "base_image_ref": "06e5174d-124d-444d-9aca-8e2e82218865",
            "boot_roles": "member,reader,admin",
            "image_location": "snapshot",
            "image_state": "available",
            "image_type": "snapshot",
            "instance_uuid": "4e8f1b44-593d-492b-8985-094e6f88f83b",
            "owner_id": "9b50a8dba82f4c14802c4554482882b8",
            "owner_project_name": "ialonso",
            "owner_user_name": "ialonso",
            "user_id": "a23ec81be2d9405db107acf4194f44f0",
            "image_id": "cf8915eb-473c-438c-a55c-3b13e8e34c9d",
            "image_name": "SNAPSHOT_OCT24_SDWAN_C8KV01",
            "checksum": "70899bfbaecf33d0f2c2871c79000f50",
            "container_format": "bare",
            "disk_format": "qcow2",
            "min_disk": "0",
            "min_ram": "0",
            "size": "2557214720"
        },
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "attachment": [],
        "bootableTick": "\u2713",
        "encryptedTick": "\u2717",
        "multiattachTick": "\u2717",
        "snapshotTick": "\u2717",
        "created_age": "27d",
        "updated_age": "18d",
        "tenant_name": "admin"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "5fa13919-8d80-4f75-96e9-bc19556781ce",
        "status": "available",
        "size": 16,
        "availability_zone": "nova",
        "created_at": "2023-10-30T14:58:14.000000",
        "updated_at": "2023-11-01T19:21:35.000000",
        "name": "migratable_c8kv_vm",
        "description": null,
        "volume_type": "__DEFAULT__",
        "snapshot_id": "38d68769-9faa-4cd1-be26-c18fccacac19",
        "bootable": "true",
        "encrypted": false,
        "multiattach": false,
        "volume_image_metadata": {
            "signature_verified": "False",
            "base_image_ref": "06e5174d-124d-444d-9aca-8e2e82218865",
            "boot_roles": "member,reader,admin",
            "image_location": "snapshot",
            "image_state": "available",
            "image_type": "snapshot",
            "instance_uuid": "4e8f1b44-593d-492b-8985-094e6f88f83b",
            "owner_id": "9b50a8dba82f4c14802c4554482882b8",
            "owner_project_name": "ialonso",
            "owner_user_name": "ialonso",
            "user_id": "a23ec81be2d9405db107acf4194f44f0",
            "image_id": "cf8915eb-473c-438c-a55c-3b13e8e34c9d",
            "image_name": "SNAPSHOT_OCT24_SDWAN_C8KV01",
            "checksum": "70899bfbaecf33d0f2c2871c79000f50",
            "container_format": "bare",
            "disk_format": "qcow2",
            "min_disk": "0",
            "min_ram": "0",
            "size": "2557214720"
        },
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "attachment": [],
        "bootableTick": "\u2713",
        "encryptedTick": "\u2717",
        "multiattachTick": "\u2717",
        "snapshotTick": "\u2713",
        "created_age": "21d",
        "updated_age": "18d",
        "tenant_name": "admin"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "bb0b41d7-798d-47bd-9e13-701f9422904a",
        "status": "available",
        "size": 20,
        "availability_zone": "nova",
        "created_at": "2023-10-30T22:05:37.000000",
        "updated_at": "2023-10-30T22:10:45.000000",
        "name": "my-cirros",
        "description": null,
        "volume_type": "__DEFAULT__",
        "snapshot_id": "309b0367-4ba2-415a-9213-ad47633f3caf",
        "bootable": "true",
        "encrypted": false,
        "multiattach": false,
        "volume_image_metadata": {
            "signature_verified": "False",
            "image_id": "f59b504b-42b7-415f-b34a-72dd53043bc0",
            "image_name": "cirros",
            "checksum": "1d3062cd89af34e419f7100277f38b2b",
            "container_format": "bare",
            "disk_format": "qcow2",
            "min_disk": "0",
            "min_ram": "0",
            "size": "16338944"
        },
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "attachment": [],
        "bootableTick": "\u2713",
        "encryptedTick": "\u2717",
        "multiattachTick": "\u2717",
        "snapshotTick": "\u2713",
        "created_age": "20d",
        "updated_age": "20d",
        "tenant_name": "admin"
    },
    {
        "__Output": {
            "status": "Red"
        },
        "id": "88b81c75-c333-45fa-be50-219e12ae5520",
        "status": "in-use",
        "size": 16,
        "availability_zone": "nova",
        "created_at": "2023-11-02T07:58:50.000000",
        "updated_at": "2023-11-02T08:55:19.000000",
        "name": "volume_migratable_C8KV_ORANGE_new",
        "description": null,
        "volume_type": "__DEFAULT__",
        "snapshot_id": "ae0ae14b-4073-4279-a1e1-c0ec64935c55",
        "bootable": "true",
        "encrypted": false,
        "multiattach": false,
        "volume_image_metadata": {
            "signature_verified": "False",
            "base_image_ref": "06e5174d-124d-444d-9aca-8e2e82218865",
            "boot_roles": "member,reader,admin",
            "image_location": "snapshot",
            "image_state": "available",
            "image_type": "snapshot",
            "instance_uuid": "0f3afdc8-8405-460a-a3cc-95944c695d4d",
            "owner_id": "9b50a8dba82f4c14802c4554482882b8",
            "owner_project_name": "ialonso",
            "owner_user_name": "ialonso",
            "user_id": "a23ec81be2d9405db107acf4194f44f0",
            "image_id": "e8a4ea55-c142-48c9-bc58-455389c3324a",
            "image_name": "SNAPSHOT_IMAGE_C8KV_ORANGE",
            "checksum": "0beddedeaeb5e236b5778482dedc1040",
            "container_format": "bare",
            "disk_format": "qcow2",
            "min_disk": "0",
            "min_ram": "0",
            "size": "2591752192"
        },
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "attachment": [
            {
                "attachment_id": "5441fe7c-32c4-4192-a8e9-d607a66e6ad3",
                "server_id": "f83b1396-40b2-4dec-b336-597fc42e55d7",
                "host_name": "compute-server-2",
                "device": "/dev/vda",
                "attached_at": "2023-11-02T08:55:18.000000",
                "vm_tenant_name": "admin/c8koncinder"
            }
        ],
        "bootableTick": "\u2713",
        "encryptedTick": "\u2717",
        "multiattachTick": "\u2717",
        "snapshotTick": "\u2713",
        "created_age": "18d",
        "updated_age": "18d",
        "tenant_name": "admin"
    }
]
```

Developer

```
# iserver get osp vol --cluster pod1 -o json

{
    "duration": 5206,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 4650,
        "total_time": 4650
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 17:38:44.263481	True	1766	get	volumes.list
2023-11-20 17:38:44.640066	True	340	get	tenants
2023-11-20 17:38:47.599158	True	2544	get	virtual_machines
```

[[Back]](./VolumeGet.md)