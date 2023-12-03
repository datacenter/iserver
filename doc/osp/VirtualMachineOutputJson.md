# Virtual Machine

## Default output

```
# iserver get osp vm --cluster pod1 -o json

Cluster: pod1
[
    {
        "id": "f83b1396-40b2-4dec-b336-597fc42e55d7",
        "name": "c8koncinder",
        "status": "SHUTOFF",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "user_id": "a23ec81be2d9405db107acf4194f44f0",
        "metadata": {},
        "hostId": "4ef7e27924b544195c43170f5147b3976b204e6d87b744380e31aeb9",
        "image": "",
        "flavor": {
            "id": "e86bad11-d0f6-4a7a-be57-f562e9433358",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e86bad11-d0f6-4a7a-be57-f562e9433358"
                }
            ]
        },
        "created": "2023-11-02T08:55:00Z",
        "updated": "2023-11-02T09:19:57Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.220",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:0c:78:90"
                }
            ],
            "C8KV_ORANGE_LAN01": [
                {
                    "version": 4,
                    "addr": "10.0.21.2",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:ae:32:44"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/f83b1396-40b2-4dec-b336-597fc42e55d7"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/f83b1396-40b2-4dec-b336-597fc42e55d7"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-02T08:55:25.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000005e4",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "stopped",
        "OS-EXT-STS:power_state": 4,
        "os-extended-volumes:volumes_attached": [
            {
                "id": "88b81c75-c333-45fa-be50-219e12ae5520"
            }
        ],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Red"
        },
        "bootFrom": "Volume",
        "power_state": "shutdown",
        "task_state": null,
        "hypervisor": "compute-server-2",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.220",
                "type": "fixed",
                "ip_type": "15.100.1.220 (fixed)",
                "mac": "fa:16:3e:0c:78:90",
                "network_ip": "management=15.100.1.220"
            },
            {
                "network": "C8KV_ORANGE_LAN01",
                "ip": "10.0.21.2",
                "type": "fixed",
                "ip_type": "10.0.21.2 (fixed)",
                "mac": "fa:16:3e:ae:32:44",
                "network_ip": "C8KV_ORANGE_LAN01=10.0.21.2"
            }
        ],
        "age": "18d",
        "tenant_name": "admin",
        "flavor_info": {
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
        "volumes": [
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
                        "attached_at": "2023-11-02T08:55:18.000000"
                    }
                ],
                "bootableTick": "\u2713",
                "encryptedTick": "\u2717",
                "multiattachTick": "\u2717",
                "snapshotTick": "\u2713",
                "created_age": "18d",
                "updated_age": "18d"
            }
        ],
        "image_info": null,
        "bootSource": "volume_migratable_C8KV_ORANGE_new",
        "bootSourceT": "(vol) volume_migratable_C8KV_ORANGE_new"
    },
    {
        "id": "cf0d30bc-7ff5-4959-bbda-b06a803d9526",
        "name": "my-c8kv",
        "status": "SHUTOFF",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "user_id": "a23ec81be2d9405db107acf4194f44f0",
        "metadata": {},
        "hostId": "4ef7e27924b544195c43170f5147b3976b204e6d87b744380e31aeb9",
        "image": {
            "id": "06e5174d-124d-444d-9aca-8e2e82218865",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/06e5174d-124d-444d-9aca-8e2e82218865"
                }
            ]
        },
        "flavor": {
            "id": "e86bad11-d0f6-4a7a-be57-f562e9433358",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e86bad11-d0f6-4a7a-be57-f562e9433358"
                }
            ]
        },
        "created": "2023-11-01T20:02:35Z",
        "updated": "2023-11-01T21:13:57Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.117",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:6b:57:aa"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/cf0d30bc-7ff5-4959-bbda-b06a803d9526"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/cf0d30bc-7ff5-4959-bbda-b06a803d9526"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-01T20:02:45.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000005cc",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "stopped",
        "OS-EXT-STS:power_state": 4,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Red"
        },
        "bootFrom": "Image",
        "power_state": "shutdown",
        "task_state": null,
        "hypervisor": "compute-server-2",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.117",
                "type": "fixed",
                "ip_type": "15.100.1.117 (fixed)",
                "mac": "fa:16:3e:6b:57:aa",
                "network_ip": "management=15.100.1.117"
            }
        ],
        "age": "18d",
        "tenant_name": "admin",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "c8000v_17_09_01a_16G_vga",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 1860567040,
            "sizeT": "1,860,567,040",
            "virtual_size": null,
            "status": "active",
            "checksum": "3836e1c924e21eb55b54397fef415c42",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "ae47ace93c6b0699f99ead5bca646b7be098ff991ba901cb3b1dde2b83ca272aa88898ef06d12c81c60135968d106cae96f0772f31dcbf9d59f3a990dbbdad7a",
            "id": "06e5174d-124d-444d-9aca-8e2e82218865",
            "updated_at": "2023-10-16T15:22:37Z",
            "created_at": "2023-10-16T15:21:58Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/06e5174d-124d-444d-9aca-8e2e82218865/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/06e5174d-124d-444d-9aca-8e2e82218865/file"
        },
        "bootSource": "c8000v_17_09_01a_16G_vga",
        "bootSourceT": "(img) c8000v_17_09_01a_16G_vga"
    },
    {
        "id": "b75cd7b9-5154-4863-93e9-79dc651198b8",
        "name": "my-cirros-img",
        "status": "ACTIVE",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "user_id": "a23ec81be2d9405db107acf4194f44f0",
        "metadata": {},
        "hostId": "4ef7e27924b544195c43170f5147b3976b204e6d87b744380e31aeb9",
        "image": {
            "id": "f59b504b-42b7-415f-b34a-72dd53043bc0",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/f59b504b-42b7-415f-b34a-72dd53043bc0"
                }
            ]
        },
        "flavor": {
            "id": "0d160026-5947-445a-9eb8-1dc4c076225a",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/0d160026-5947-445a-9eb8-1dc4c076225a"
                }
            ]
        },
        "created": "2023-11-02T14:09:51Z",
        "updated": "2023-11-03T00:29:37Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.69",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:13:75:c2"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/b75cd7b9-5154-4863-93e9-79dc651198b8"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/b75cd7b9-5154-4863-93e9-79dc651198b8"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-02T14:09:58.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000005e7",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "compute-server-2",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.69",
                "type": "fixed",
                "ip_type": "15.100.1.69 (fixed)",
                "mac": "fa:16:3e:13:75:c2",
                "network_ip": "management=15.100.1.69"
            }
        ],
        "age": "18d",
        "tenant_name": "admin",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "cirros",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 16338944,
            "sizeT": "16,338,944",
            "virtual_size": null,
            "status": "active",
            "checksum": "1d3062cd89af34e419f7100277f38b2b",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "553d220ed58cfee7dafe003c446a9f197ab5edf8ffc09396c74187cf83873c877e7ae041cb80f3b91489acf687183adcd689b53b38e3ddd22e627e7f98a09c46",
            "id": "f59b504b-42b7-415f-b34a-72dd53043bc0",
            "updated_at": "2023-10-30T15:04:42Z",
            "created_at": "2023-10-30T15:04:41Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/f59b504b-42b7-415f-b34a-72dd53043bc0/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/f59b504b-42b7-415f-b34a-72dd53043bc0/file"
        },
        "bootSource": "cirros",
        "bootSourceT": "(img) cirros"
    },
    {
        "id": "58799272-64da-4056-bf7e-11053042423b",
        "name": "test-sriov",
        "status": "ACTIVE",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "user_id": "a23ec81be2d9405db107acf4194f44f0",
        "metadata": {},
        "hostId": "9b4c6eea4255ac34777b6b7c956163f07b1b939c903c044e4d8a4e93",
        "image": {
            "id": "273bf614-2aba-4f4f-8f0f-5c782dc90b40",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/273bf614-2aba-4f4f-8f0f-5c782dc90b40"
                }
            ]
        },
        "flavor": {
            "id": "ae3aa692-2e32-4c35-8d59-df0fddeed973",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/ae3aa692-2e32-4c35-8d59-df0fddeed973"
                }
            ]
        },
        "created": "2023-05-01T09:15:27Z",
        "updated": "2023-05-01T09:15:44Z",
        "addresses": {
            "sriov0": [
                {
                    "version": 4,
                    "addr": "15.100.105.245",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:89:e6:2b"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/58799272-64da-4056-bf7e-11053042423b"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/58799272-64da-4056-bf7e-11053042423b"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-05-01T09:15:43.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000003e9",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "compute-server-1",
        "interface": [
            {
                "network": "sriov0",
                "ip": "15.100.105.245",
                "type": "fixed",
                "ip_type": "15.100.105.245 (fixed)",
                "mac": "fa:16:3e:89:e6:2b",
                "network_ip": "sriov0=15.100.105.245"
            }
        ],
        "age": "203d",
        "tenant_name": "admin",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "ubuntu-2204-amd64",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 624361472,
            "sizeT": "624,361,472",
            "virtual_size": null,
            "status": "active",
            "checksum": "2454ccb3b986448911f6b5e99ca7d9c7",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "05b8e996f0654e4491d2e925a91c6250",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "6c9100e4fae15aab30b471daafa3850b80f6d75c9b730a038bd5f1a300ab6e3583ec4ad8716657ec434c88adbb102457e3a2346345e20ce7bec506adf7510164",
            "id": "273bf614-2aba-4f4f-8f0f-5c782dc90b40",
            "updated_at": "2022-08-04T11:03:39Z",
            "created_at": "2022-08-04T11:03:27Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/273bf614-2aba-4f4f-8f0f-5c782dc90b40/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/273bf614-2aba-4f4f-8f0f-5c782dc90b40/file"
        },
        "bootSource": "ubuntu-2204-amd64",
        "bootSourceT": "(img) ubuntu-2204-amd64"
    },
    {
        "id": "4e8f1b44-593d-492b-8985-094e6f88f83b",
        "name": "ORANGE-C8KV-1",
        "status": "ACTIVE",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "user_id": "522c200898cc4962a34e1e90cc42fd1b",
        "metadata": {},
        "hostId": "7677c3ed17790277b2f2c6ae19f5099a2f3577ec5cd7fb8605b6d7f9",
        "image": {
            "id": "06e5174d-124d-444d-9aca-8e2e82218865",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/06e5174d-124d-444d-9aca-8e2e82218865"
                }
            ]
        },
        "flavor": {
            "id": "e86bad11-d0f6-4a7a-be57-f562e9433358",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e86bad11-d0f6-4a7a-be57-f562e9433358"
                }
            ]
        },
        "created": "2023-10-23T14:55:50Z",
        "updated": "2023-11-01T22:38:33Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.219",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:97:c1:38"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.91",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:97:c1:38"
                }
            ],
            "C8KV01_LAN01": [
                {
                    "version": 4,
                    "addr": "10.0.11.1",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:5c:b7:b8"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/4e8f1b44-593d-492b-8985-094e6f88f83b"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/4e8f1b44-593d-492b-8985-094e6f88f83b"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-10-23T14:56:00.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-0000040a",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-1",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.219",
                "type": "fixed",
                "ip_type": "15.100.1.219 (fixed)",
                "mac": "fa:16:3e:97:c1:38",
                "network_ip": "management=15.100.1.219"
            },
            {
                "network": "management",
                "ip": "10.58.28.91",
                "type": "floating",
                "ip_type": "10.58.28.91 (floating)",
                "mac": "fa:16:3e:97:c1:38",
                "network_ip": "management=10.58.28.91"
            },
            {
                "network": "C8KV01_LAN01",
                "ip": "10.0.11.1",
                "type": "fixed",
                "ip_type": "10.0.11.1 (fixed)",
                "mac": "fa:16:3e:5c:b7:b8",
                "network_ip": "C8KV01_LAN01=10.0.11.1"
            }
        ],
        "age": "28d",
        "tenant_name": "ialonso",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "c8000v_17_09_01a_16G_vga",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 1860567040,
            "sizeT": "1,860,567,040",
            "virtual_size": null,
            "status": "active",
            "checksum": "3836e1c924e21eb55b54397fef415c42",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "ae47ace93c6b0699f99ead5bca646b7be098ff991ba901cb3b1dde2b83ca272aa88898ef06d12c81c60135968d106cae96f0772f31dcbf9d59f3a990dbbdad7a",
            "id": "06e5174d-124d-444d-9aca-8e2e82218865",
            "updated_at": "2023-10-16T15:22:37Z",
            "created_at": "2023-10-16T15:21:58Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/06e5174d-124d-444d-9aca-8e2e82218865/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/06e5174d-124d-444d-9aca-8e2e82218865/file"
        },
        "bootSource": "c8000v_17_09_01a_16G_vga",
        "bootSourceT": "(img) c8000v_17_09_01a_16G_vga"
    },
    {
        "id": "0f3afdc8-8405-460a-a3cc-95944c695d4d",
        "name": "ORANGE-C8KV-2",
        "status": "ACTIVE",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "user_id": "522c200898cc4962a34e1e90cc42fd1b",
        "metadata": {},
        "hostId": "7677c3ed17790277b2f2c6ae19f5099a2f3577ec5cd7fb8605b6d7f9",
        "image": {
            "id": "06e5174d-124d-444d-9aca-8e2e82218865",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/06e5174d-124d-444d-9aca-8e2e82218865"
                }
            ]
        },
        "flavor": {
            "id": "e86bad11-d0f6-4a7a-be57-f562e9433358",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e86bad11-d0f6-4a7a-be57-f562e9433358"
                }
            ]
        },
        "created": "2023-10-24T08:12:15Z",
        "updated": "2023-11-01T22:40:21Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.179",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:a4:f5:53"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.92",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:a4:f5:53"
                }
            ],
            "C8KV_ORANGE_LAN01": [
                {
                    "version": 4,
                    "addr": "10.0.21.1",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:67:1b:48"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/0f3afdc8-8405-460a-a3cc-95944c695d4d"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/0f3afdc8-8405-460a-a3cc-95944c695d4d"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-10-24T08:12:27.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-00000410",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-1",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.179",
                "type": "fixed",
                "ip_type": "15.100.1.179 (fixed)",
                "mac": "fa:16:3e:a4:f5:53",
                "network_ip": "management=15.100.1.179"
            },
            {
                "network": "management",
                "ip": "10.58.28.92",
                "type": "floating",
                "ip_type": "10.58.28.92 (floating)",
                "mac": "fa:16:3e:a4:f5:53",
                "network_ip": "management=10.58.28.92"
            },
            {
                "network": "C8KV_ORANGE_LAN01",
                "ip": "10.0.21.1",
                "type": "fixed",
                "ip_type": "10.0.21.1 (fixed)",
                "mac": "fa:16:3e:67:1b:48",
                "network_ip": "C8KV_ORANGE_LAN01=10.0.21.1"
            }
        ],
        "age": "27d",
        "tenant_name": "ialonso",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "c8000v_17_09_01a_16G_vga",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 1860567040,
            "sizeT": "1,860,567,040",
            "virtual_size": null,
            "status": "active",
            "checksum": "3836e1c924e21eb55b54397fef415c42",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "ae47ace93c6b0699f99ead5bca646b7be098ff991ba901cb3b1dde2b83ca272aa88898ef06d12c81c60135968d106cae96f0772f31dcbf9d59f3a990dbbdad7a",
            "id": "06e5174d-124d-444d-9aca-8e2e82218865",
            "updated_at": "2023-10-16T15:22:37Z",
            "created_at": "2023-10-16T15:21:58Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/06e5174d-124d-444d-9aca-8e2e82218865/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/06e5174d-124d-444d-9aca-8e2e82218865/file"
        },
        "bootSource": "c8000v_17_09_01a_16G_vga",
        "bootSourceT": "(img) c8000v_17_09_01a_16G_vga"
    },
    {
        "id": "1fb263d3-437c-47dc-b3a0-38168a0a9e41",
        "name": "SDWAN-C8KV01B",
        "status": "ACTIVE",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "user_id": "522c200898cc4962a34e1e90cc42fd1b",
        "metadata": {},
        "hostId": "7677c3ed17790277b2f2c6ae19f5099a2f3577ec5cd7fb8605b6d7f9",
        "image": {
            "id": "9095f375-3afa-46d7-9cce-a0c2a3cd0736",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/9095f375-3afa-46d7-9cce-a0c2a3cd0736"
                }
            ]
        },
        "flavor": {
            "id": "e86bad11-d0f6-4a7a-be57-f562e9433358",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e86bad11-d0f6-4a7a-be57-f562e9433358"
                }
            ]
        },
        "created": "2023-10-23T15:22:45Z",
        "updated": "2023-10-23T16:17:09Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.30",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:14:7d:d0"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.90",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:14:7d:d0"
                }
            ],
            "C8KV01_LAN01": [
                {
                    "version": 4,
                    "addr": "10.0.11.2",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:3b:d5:c6"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/1fb263d3-437c-47dc-b3a0-38168a0a9e41"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/1fb263d3-437c-47dc-b3a0-38168a0a9e41"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-10-23T15:23:17.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-0000040d",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-1",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.30",
                "type": "fixed",
                "ip_type": "15.100.1.30 (fixed)",
                "mac": "fa:16:3e:14:7d:d0",
                "network_ip": "management=15.100.1.30"
            },
            {
                "network": "management",
                "ip": "10.58.28.90",
                "type": "floating",
                "ip_type": "10.58.28.90 (floating)",
                "mac": "fa:16:3e:14:7d:d0",
                "network_ip": "management=10.58.28.90"
            },
            {
                "network": "C8KV01_LAN01",
                "ip": "10.0.11.2",
                "type": "fixed",
                "ip_type": "10.0.11.2 (fixed)",
                "mac": "fa:16:3e:3b:d5:c6",
                "network_ip": "C8KV01_LAN01=10.0.11.2"
            }
        ],
        "age": "28d",
        "tenant_name": "ialonso",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "image-SDWAN-C8KV01",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "private",
            "size": 2436956160,
            "sizeT": "2,436,956,160",
            "virtual_size": null,
            "status": "active",
            "checksum": "2d29dd6799f105375eb3ef06184a8bc0",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "9b50a8dba82f4c14802c4554482882b8",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "980d97aab820a843991a0428be655513d5547bd5037efc002ebc33ce527b186f5f4d9f5cb35efa3a030bb17670aac24ed91d6d985a4dd28361494ff891547554",
            "id": "9095f375-3afa-46d7-9cce-a0c2a3cd0736",
            "updated_at": "2023-10-23T15:17:32Z",
            "created_at": "2023-10-23T15:16:29Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/9095f375-3afa-46d7-9cce-a0c2a3cd0736/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/9095f375-3afa-46d7-9cce-a0c2a3cd0736/file"
        },
        "bootSource": "image-SDWAN-C8KV01",
        "bootSourceT": "(img) image-SDWAN-C8KV01"
    },
    {
        "id": "61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db",
        "name": "esc",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "217c1ceee07b0c4381c81b741cae8c751ea8b8dfe6ff27d62ea9dccc",
        "image": {
            "id": "969f3733-a8a7-4af1-89f7-8cc44b683550",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/969f3733-a8a7-4af1-89f7-8cc44b683550"
                }
            ]
        },
        "flavor": {
            "id": "2a27ea69-1f24-413a-a440-1bc0ca7a4951",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/2a27ea69-1f24-413a-a440-1bc0ca7a4951"
                }
            ]
        },
        "created": "2023-11-16T17:01:56Z",
        "updated": "2023-11-16T17:02:21Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.36",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:bb:2b:cd"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.82",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:bb:2b:cd"
                }
            ],
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.36",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:2d:58:f2"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-16T17:02:21.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-00000725",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "esc"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-2",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.36",
                "type": "fixed",
                "ip_type": "15.100.1.36 (fixed)",
                "mac": "fa:16:3e:bb:2b:cd",
                "network_ip": "management=15.100.1.36"
            },
            {
                "network": "management",
                "ip": "10.58.28.82",
                "type": "floating",
                "ip_type": "10.58.28.82 (floating)",
                "mac": "fa:16:3e:bb:2b:cd",
                "network_ip": "management=10.58.28.82"
            },
            {
                "network": "orchestration",
                "ip": "15.100.2.36",
                "type": "fixed",
                "ip_type": "15.100.2.36 (fixed)",
                "mac": "fa:16:3e:2d:58:f2",
                "network_ip": "orchestration=15.100.2.36"
            }
        ],
        "age": "4d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "esc-5.6",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 1451753472,
            "sizeT": "1,451,753,472",
            "virtual_size": null,
            "status": "active",
            "checksum": "67c062ee700b9ccf6bb2adb7e9be52b9",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "05b8e996f0654e4491d2e925a91c6250",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "ffbc995d43e7b9ee50a491a04d11d0c97cbd98e444e3d2f119d657223a97c484f90ca93aaec80aea31cdc6860b47827cd1b0c83cb71bb77d000d787b19ab831c",
            "id": "969f3733-a8a7-4af1-89f7-8cc44b683550",
            "updated_at": "2022-08-04T11:01:20Z",
            "created_at": "2022-08-04T11:00:47Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/969f3733-a8a7-4af1-89f7-8cc44b683550/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/969f3733-a8a7-4af1-89f7-8cc44b683550/file"
        },
        "bootSource": "esc-5.6",
        "bootSourceT": "(img) esc-5.6"
    },
    {
        "id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
        "name": "lattice",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "bf36d1eb55b3d52eb91d1b3817f0d9f25fd3885d8ec3b23fcca2841b",
        "image": {
            "id": "407ac7cc-2757-4fe3-abf5-9a29925aa639",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/407ac7cc-2757-4fe3-abf5-9a29925aa639"
                }
            ]
        },
        "flavor": {
            "id": "7b4877fe-79e4-4b6b-a919-36b1774e607c",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/7b4877fe-79e4-4b6b-a919-36b1774e607c"
                }
            ]
        },
        "created": "2022-08-04T11:27:09Z",
        "updated": "2023-11-02T11:16:19Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.101",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:c3:6b:06"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.85",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:c3:6b:06"
                }
            ],
            "control-SBI": [
                {
                    "version": 4,
                    "addr": "15.100.4.101",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:cc:7f:24"
                }
            ],
            "control-N2": [
                {
                    "version": 4,
                    "addr": "15.100.5.101",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:63:7d:aa"
                }
            ],
            "data-N3": [
                {
                    "version": 4,
                    "addr": "15.100.7.101",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:70:4d:85"
                }
            ],
            "control-N4": [
                {
                    "version": 4,
                    "addr": "15.100.6.101",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:fe:4d:de"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/53e7b6fe-e33e-4d83-8936-ab8fe9b26d60"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/53e7b6fe-e33e-4d83-8936-ab8fe9b26d60"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": "5gc_key",
        "OS-SRV-USG:launched_at": "2022-08-04T11:30:32.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-0000000d",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "compute-server-2",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.101",
                "type": "fixed",
                "ip_type": "15.100.1.101 (fixed)",
                "mac": "fa:16:3e:c3:6b:06",
                "network_ip": "management=15.100.1.101"
            },
            {
                "network": "management",
                "ip": "10.58.28.85",
                "type": "floating",
                "ip_type": "10.58.28.85 (floating)",
                "mac": "fa:16:3e:c3:6b:06",
                "network_ip": "management=10.58.28.85"
            },
            {
                "network": "control-SBI",
                "ip": "15.100.4.101",
                "type": "fixed",
                "ip_type": "15.100.4.101 (fixed)",
                "mac": "fa:16:3e:cc:7f:24",
                "network_ip": "control-SBI=15.100.4.101"
            },
            {
                "network": "control-N2",
                "ip": "15.100.5.101",
                "type": "fixed",
                "ip_type": "15.100.5.101 (fixed)",
                "mac": "fa:16:3e:63:7d:aa",
                "network_ip": "control-N2=15.100.5.101"
            },
            {
                "network": "data-N3",
                "ip": "15.100.7.101",
                "type": "fixed",
                "ip_type": "15.100.7.101 (fixed)",
                "mac": "fa:16:3e:70:4d:85",
                "network_ip": "data-N3=15.100.7.101"
            },
            {
                "network": "control-N4",
                "ip": "15.100.6.101",
                "type": "fixed",
                "ip_type": "15.100.6.101 (fixed)",
                "mac": "fa:16:3e:fe:4d:de",
                "network_ip": "control-N4=15.100.6.101"
            }
        ],
        "age": "473d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "lattice-snapshot-20220802",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 23308992512,
            "sizeT": "23,308,992,512",
            "virtual_size": null,
            "status": "active",
            "checksum": "114e9ea949c75b47e937b80a3a85f05c",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "05b8e996f0654e4491d2e925a91c6250",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "2e59e984b157533dbed16c95e099d80b7be5ed89cb74e2fd089182a21181dca9d9b4a307780092ea44f1c02e538ffbc890c0f00277701bb5094b7696221470a8",
            "id": "407ac7cc-2757-4fe3-abf5-9a29925aa639",
            "updated_at": "2022-08-04T11:24:40Z",
            "created_at": "2022-08-04T11:16:34Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/407ac7cc-2757-4fe3-abf5-9a29925aa639/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/407ac7cc-2757-4fe3-abf5-9a29925aa639/file"
        },
        "bootSource": "lattice-snapshot-20220802",
        "bootSourceT": "(img) lattice-snapshot-20220802"
    },
    {
        "id": "3fea1ac9-25cc-4183-976e-af79a513aa36",
        "name": "portal",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "35d1efdb2dfb3225b1a54a87e70b9c3b679680850b5aa7399b1eeeef",
        "image": {
            "id": "f7ba2608-75f2-4a4a-b6e7-41566665f52f",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/f7ba2608-75f2-4a4a-b6e7-41566665f52f"
                }
            ]
        },
        "flavor": {
            "id": "e5d37c1d-f945-4b19-9f51-d94ee48091f7",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e5d37c1d-f945-4b19-9f51-d94ee48091f7"
                }
            ]
        },
        "created": "2022-08-04T14:23:08Z",
        "updated": "2022-08-04T14:23:16Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.100",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:cc:97:82"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.84",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:cc:97:82"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/3fea1ac9-25cc-4183-976e-af79a513aa36"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/3fea1ac9-25cc-4183-976e-af79a513aa36"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": "5gc_key",
        "OS-SRV-USG:launched_at": "2022-08-04T14:23:16.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-0000001f",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "portal"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-1",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.100",
                "type": "fixed",
                "ip_type": "15.100.1.100 (fixed)",
                "mac": "fa:16:3e:cc:97:82",
                "network_ip": "management=15.100.1.100"
            },
            {
                "network": "management",
                "ip": "10.58.28.84",
                "type": "floating",
                "ip_type": "10.58.28.84 (floating)",
                "mac": "fa:16:3e:cc:97:82",
                "network_ip": "management=10.58.28.84"
            }
        ],
        "age": "473d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "portal-snapshot-20220802",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 80702210048,
            "sizeT": "80,702,210,048",
            "virtual_size": null,
            "status": "active",
            "checksum": "06668115973408eaf8950f2d0eeff560",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "05b8e996f0654e4491d2e925a91c6250",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "86819cd81df75e97e98a0ff891e7cc39a7a214a9fee56b5fc8fb1c666b0f2e9ded66b85962580a55a52b1896606f1bae85d2de915a5aa1294b0fdff9b8fcc620",
            "id": "f7ba2608-75f2-4a4a-b6e7-41566665f52f",
            "updated_at": "2022-08-04T11:59:34Z",
            "created_at": "2022-08-04T11:32:08Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/f7ba2608-75f2-4a4a-b6e7-41566665f52f/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/f7ba2608-75f2-4a4a-b6e7-41566665f52f/file"
        },
        "bootSource": "portal-snapshot-20220802",
        "bootSourceT": "(img) portal-snapshot-20220802"
    },
    {
        "id": "b56451ce-e214-4484-9f35-e656a95a8328",
        "name": "server",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "35d5cf7473ef5154b856cbe0f258c9042720f36973a0e69f30db8f9b",
        "image": {
            "id": "b659442c-b5e8-4bdf-a15e-a6c43695c317",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/b659442c-b5e8-4bdf-a15e-a6c43695c317"
                }
            ]
        },
        "flavor": {
            "id": "ae3aa692-2e32-4c35-8d59-df0fddeed973",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/ae3aa692-2e32-4c35-8d59-df0fddeed973"
                }
            ]
        },
        "created": "2022-08-04T11:20:17Z",
        "updated": "2022-08-04T11:20:31Z",
        "addresses": {
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.102",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:38:40:30"
                },
                {
                    "version": 4,
                    "addr": "10.58.28.83",
                    "OS-EXT-IPS:type": "floating",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:38:40:30"
                }
            ],
            "data-N6": [
                {
                    "version": 4,
                    "addr": "15.100.8.102",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:b4:94:eb"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/b56451ce-e214-4484-9f35-e656a95a8328"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/b56451ce-e214-4484-9f35-e656a95a8328"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "",
        "key_name": "5gc_key",
        "OS-SRV-USG:launched_at": "2022-08-04T11:20:31.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-0000000a",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "compute-server-1",
        "interface": [
            {
                "network": "management",
                "ip": "15.100.1.102",
                "type": "fixed",
                "ip_type": "15.100.1.102 (fixed)",
                "mac": "fa:16:3e:38:40:30",
                "network_ip": "management=15.100.1.102"
            },
            {
                "network": "management",
                "ip": "10.58.28.83",
                "type": "floating",
                "ip_type": "10.58.28.83 (floating)",
                "mac": "fa:16:3e:38:40:30",
                "network_ip": "management=10.58.28.83"
            },
            {
                "network": "data-N6",
                "ip": "15.100.8.102",
                "type": "fixed",
                "ip_type": "15.100.8.102 (fixed)",
                "mac": "fa:16:3e:b4:94:eb",
                "network_ip": "data-N6=15.100.8.102"
            }
        ],
        "age": "473d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "ubuntu-1804-i386",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 351797248,
            "sizeT": "351,797,248",
            "virtual_size": null,
            "status": "active",
            "checksum": "cec3dec44f5437a087b70403df7e6487",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "05b8e996f0654e4491d2e925a91c6250",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "e379b78914b68ac5bc8e31e244c675c23fab25400a09944af60fbd1d4d9f1192e01b3686ae6de4188ed82d721de5053dd6ba348be5d9376c3a0048c4b8b8cb34",
            "id": "b659442c-b5e8-4bdf-a15e-a6c43695c317",
            "updated_at": "2022-08-04T11:03:55Z",
            "created_at": "2022-08-04T11:03:43Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/b659442c-b5e8-4bdf-a15e-a6c43695c317/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/b659442c-b5e8-4bdf-a15e-a6c43695c317/file"
        },
        "bootSource": "ubuntu-1804-i386",
        "bootSourceT": "(img) ubuntu-1804-i386"
    },
    {
        "id": "a898461f-20f2-454f-82e9-3ff1905f399e",
        "name": "VPC-SI-mme",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "35d1efdb2dfb3225b1a54a87e70b9c3b679680850b5aa7399b1eeeef",
        "image": {
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/fd4c408c-8860-4111-8ec0-dba64266cdbf"
                }
            ]
        },
        "flavor": {
            "id": "751a9512-57a4-41c4-8a9c-c52de1955d16",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/751a9512-57a4-41c4-8a9c-c52de1955d16"
                }
            ]
        },
        "created": "2023-11-17T18:27:28Z",
        "updated": "2023-11-17T18:27:40Z",
        "addresses": {
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.103",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:88:5f:dd"
                }
            ],
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.103",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:22:8e:23"
                }
            ],
            "data-N3": [
                {
                    "version": 4,
                    "addr": "15.100.7.41",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:7c:ff:47"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/a898461f-20f2-454f-82e9-3ff1905f399e"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/a898461f-20f2-454f-82e9-3ff1905f399e"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-17T18:27:40.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-0000079d",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-1",
        "interface": [
            {
                "network": "orchestration",
                "ip": "15.100.2.103",
                "type": "fixed",
                "ip_type": "15.100.2.103 (fixed)",
                "mac": "fa:16:3e:88:5f:dd",
                "network_ip": "orchestration=15.100.2.103"
            },
            {
                "network": "management",
                "ip": "15.100.1.103",
                "type": "fixed",
                "ip_type": "15.100.1.103 (fixed)",
                "mac": "fa:16:3e:22:8e:23",
                "network_ip": "management=15.100.1.103"
            },
            {
                "network": "data-N3",
                "ip": "15.100.7.41",
                "type": "fixed",
                "ip_type": "15.100.7.41 (fixed)",
                "mac": "fa:16:3e:7c:ff:47",
                "network_ip": "data-N3=15.100.7.41"
            }
        ],
        "age": "3d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "qvpc-si-21.28.m15",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 210370560,
            "sizeT": "210,370,560",
            "virtual_size": null,
            "status": "active",
            "checksum": "55e8916d3911570596ba35cd9aff8357",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "updated_at": "2023-10-25T10:03:24Z",
            "created_at": "2023-10-25T10:03:19Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
        },
        "bootSource": "qvpc-si-21.28.m15",
        "bootSourceT": "(img) qvpc-si-21.28.m15"
    },
    {
        "id": "b698f08c-71bd-430c-b966-8c16230c824d",
        "name": "VPC-SI-saegw1",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "85ecfbe38613c3f7360a3cc4ae2063302d2b9327006c5f84517245ca",
        "image": {
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/fd4c408c-8860-4111-8ec0-dba64266cdbf"
                }
            ]
        },
        "flavor": {
            "id": "f0db7ec9-0c28-4fc4-a88a-d7dc62ee0043",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/f0db7ec9-0c28-4fc4-a88a-d7dc62ee0043"
                }
            ]
        },
        "created": "2023-11-17T18:28:25Z",
        "updated": "2023-11-17T18:28:54Z",
        "addresses": {
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.51",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:6f:c4:6a"
                }
            ],
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.51",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:15:b1:7f"
                }
            ],
            "sriov0": [
                {
                    "version": 4,
                    "addr": "15.100.105.151",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:dd:d2:9d"
                },
                {
                    "version": 4,
                    "addr": "15.100.105.51",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:c3:ad:0b"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/b698f08c-71bd-430c-b966-8c16230c824d"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/b698f08c-71bd-430c-b966-8c16230c824d"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-17T18:28:54.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-3",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000007a0",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-3",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-3",
        "interface": [
            {
                "network": "orchestration",
                "ip": "15.100.2.51",
                "type": "fixed",
                "ip_type": "15.100.2.51 (fixed)",
                "mac": "fa:16:3e:6f:c4:6a",
                "network_ip": "orchestration=15.100.2.51"
            },
            {
                "network": "management",
                "ip": "15.100.1.51",
                "type": "fixed",
                "ip_type": "15.100.1.51 (fixed)",
                "mac": "fa:16:3e:15:b1:7f",
                "network_ip": "management=15.100.1.51"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.151",
                "type": "fixed",
                "ip_type": "15.100.105.151 (fixed)",
                "mac": "fa:16:3e:dd:d2:9d",
                "network_ip": "sriov0=15.100.105.151"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.51",
                "type": "fixed",
                "ip_type": "15.100.105.51 (fixed)",
                "mac": "fa:16:3e:c3:ad:0b",
                "network_ip": "sriov0=15.100.105.51"
            }
        ],
        "age": "3d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        },
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "qvpc-si-21.28.m15",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 210370560,
            "sizeT": "210,370,560",
            "virtual_size": null,
            "status": "active",
            "checksum": "55e8916d3911570596ba35cd9aff8357",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "updated_at": "2023-10-25T10:03:24Z",
            "created_at": "2023-10-25T10:03:19Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
        },
        "bootSource": "qvpc-si-21.28.m15",
        "bootSourceT": "(img) qvpc-si-21.28.m15"
    },
    {
        "id": "0b7905f8-d572-42c6-91ad-b24b21f4cade",
        "name": "VPC-SI-saegw2",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "217c1ceee07b0c4381c81b741cae8c751ea8b8dfe6ff27d62ea9dccc",
        "image": {
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/fd4c408c-8860-4111-8ec0-dba64266cdbf"
                }
            ]
        },
        "flavor": {
            "id": "f0db7ec9-0c28-4fc4-a88a-d7dc62ee0043",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/f0db7ec9-0c28-4fc4-a88a-d7dc62ee0043"
                }
            ]
        },
        "created": "2023-11-17T18:28:50Z",
        "updated": "2023-11-17T18:29:35Z",
        "addresses": {
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.52",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:92:89:86"
                }
            ],
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.52",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:57:23:38"
                }
            ],
            "sriov0": [
                {
                    "version": 4,
                    "addr": "15.100.105.152",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:18:11:ba"
                },
                {
                    "version": 4,
                    "addr": "15.100.105.52",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:1e:c2:e6"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/0b7905f8-d572-42c6-91ad-b24b21f4cade"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/0b7905f8-d572-42c6-91ad-b24b21f4cade"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-17T18:29:35.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000007ac",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-2",
        "interface": [
            {
                "network": "orchestration",
                "ip": "15.100.2.52",
                "type": "fixed",
                "ip_type": "15.100.2.52 (fixed)",
                "mac": "fa:16:3e:92:89:86",
                "network_ip": "orchestration=15.100.2.52"
            },
            {
                "network": "management",
                "ip": "15.100.1.52",
                "type": "fixed",
                "ip_type": "15.100.1.52 (fixed)",
                "mac": "fa:16:3e:57:23:38",
                "network_ip": "management=15.100.1.52"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.152",
                "type": "fixed",
                "ip_type": "15.100.105.152 (fixed)",
                "mac": "fa:16:3e:18:11:ba",
                "network_ip": "sriov0=15.100.105.152"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.52",
                "type": "fixed",
                "ip_type": "15.100.105.52 (fixed)",
                "mac": "fa:16:3e:1e:c2:e6",
                "network_ip": "sriov0=15.100.105.52"
            }
        ],
        "age": "3d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        },
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "qvpc-si-21.28.m15",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 210370560,
            "sizeT": "210,370,560",
            "virtual_size": null,
            "status": "active",
            "checksum": "55e8916d3911570596ba35cd9aff8357",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "updated_at": "2023-10-25T10:03:24Z",
            "created_at": "2023-10-25T10:03:19Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
        },
        "bootSource": "qvpc-si-21.28.m15",
        "bootSourceT": "(img) qvpc-si-21.28.m15"
    },
    {
        "id": "40133dad-7c09-4846-9f4e-f5db7872a1ea",
        "name": "VPC-SI-upf1",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "35d5cf7473ef5154b856cbe0f258c9042720f36973a0e69f30db8f9b",
        "image": {
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/fd4c408c-8860-4111-8ec0-dba64266cdbf"
                }
            ]
        },
        "flavor": {
            "id": "e64aa121-041e-405d-bafa-62936198732d",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/e64aa121-041e-405d-bafa-62936198732d"
                }
            ]
        },
        "created": "2023-11-17T18:28:32Z",
        "updated": "2023-11-17T19:10:58Z",
        "addresses": {
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.191",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:cf:4b:b5"
                }
            ],
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.191",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:22:9c:e2"
                }
            ],
            "sriov0": [
                {
                    "version": 4,
                    "addr": "15.100.105.191",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:e8:f1:d5"
                },
                {
                    "version": 4,
                    "addr": "15.100.105.91",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:e7:65:c7"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/40133dad-7c09-4846-9f4e-f5db7872a1ea"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/40133dad-7c09-4846-9f4e-f5db7872a1ea"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-17T18:28:55.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-1",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000007a6",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-1",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "compute-server-1",
        "interface": [
            {
                "network": "orchestration",
                "ip": "15.100.2.191",
                "type": "fixed",
                "ip_type": "15.100.2.191 (fixed)",
                "mac": "fa:16:3e:cf:4b:b5",
                "network_ip": "orchestration=15.100.2.191"
            },
            {
                "network": "management",
                "ip": "15.100.1.191",
                "type": "fixed",
                "ip_type": "15.100.1.191 (fixed)",
                "mac": "fa:16:3e:22:9c:e2",
                "network_ip": "management=15.100.1.191"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.191",
                "type": "fixed",
                "ip_type": "15.100.105.191 (fixed)",
                "mac": "fa:16:3e:e8:f1:d5",
                "network_ip": "sriov0=15.100.105.191"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.91",
                "type": "fixed",
                "ip_type": "15.100.105.91 (fixed)",
                "mac": "fa:16:3e:e7:65:c7",
                "network_ip": "sriov0=15.100.105.91"
            }
        ],
        "age": "3d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "qvpc-si-21.28.m15",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 210370560,
            "sizeT": "210,370,560",
            "virtual_size": null,
            "status": "active",
            "checksum": "55e8916d3911570596ba35cd9aff8357",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "updated_at": "2023-10-25T10:03:24Z",
            "created_at": "2023-10-25T10:03:19Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
        },
        "bootSource": "qvpc-si-21.28.m15",
        "bootSourceT": "(img) qvpc-si-21.28.m15"
    },
    {
        "id": "f9d17afa-36bb-4b8e-9448-77e61dfc2552",
        "name": "VPC-SI-upf2",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "bf36d1eb55b3d52eb91d1b3817f0d9f25fd3885d8ec3b23fcca2841b",
        "image": {
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/fd4c408c-8860-4111-8ec0-dba64266cdbf"
                }
            ]
        },
        "flavor": {
            "id": "67f4b719-f367-4191-86fb-a97fe6b0c6b3",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/67f4b719-f367-4191-86fb-a97fe6b0c6b3"
                }
            ]
        },
        "created": "2023-11-17T18:28:27Z",
        "updated": "2023-11-17T19:11:02Z",
        "addresses": {
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.192",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:d8:3b:77"
                }
            ],
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.192",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:01:17:1c"
                }
            ],
            "sriov0": [
                {
                    "version": 4,
                    "addr": "15.100.105.192",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:48:32:31"
                },
                {
                    "version": 4,
                    "addr": "15.100.105.92",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:74:59:71"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/f9d17afa-36bb-4b8e-9448-77e61dfc2552"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/f9d17afa-36bb-4b8e-9448-77e61dfc2552"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-17T18:28:53.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "compute-server-2",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000007a3",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "compute-server-2",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "compute-server-2",
        "interface": [
            {
                "network": "orchestration",
                "ip": "15.100.2.192",
                "type": "fixed",
                "ip_type": "15.100.2.192 (fixed)",
                "mac": "fa:16:3e:d8:3b:77",
                "network_ip": "orchestration=15.100.2.192"
            },
            {
                "network": "management",
                "ip": "15.100.1.192",
                "type": "fixed",
                "ip_type": "15.100.1.192 (fixed)",
                "mac": "fa:16:3e:01:17:1c",
                "network_ip": "management=15.100.1.192"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.192",
                "type": "fixed",
                "ip_type": "15.100.105.192 (fixed)",
                "mac": "fa:16:3e:48:32:31",
                "network_ip": "sriov0=15.100.105.192"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.92",
                "type": "fixed",
                "ip_type": "15.100.105.92 (fixed)",
                "mac": "fa:16:3e:74:59:71",
                "network_ip": "sriov0=15.100.105.92"
            }
        ],
        "age": "3d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "qvpc-si-21.28.m15",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 210370560,
            "sizeT": "210,370,560",
            "virtual_size": null,
            "status": "active",
            "checksum": "55e8916d3911570596ba35cd9aff8357",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "updated_at": "2023-10-25T10:03:24Z",
            "created_at": "2023-10-25T10:03:19Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
        },
        "bootSource": "qvpc-si-21.28.m15",
        "bootSourceT": "(img) qvpc-si-21.28.m15"
    },
    {
        "id": "38e93240-4d5d-476b-b5f9-362c5d2b508a",
        "name": "VPC-SI-upf8",
        "status": "ACTIVE",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "user_id": "dea57460869c49e6a829ad88b5b14db1",
        "metadata": {},
        "hostId": "85ecfbe38613c3f7360a3cc4ae2063302d2b9327006c5f84517245ca",
        "image": {
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/images/fd4c408c-8860-4111-8ec0-dba64266cdbf"
                }
            ]
        },
        "flavor": {
            "id": "1c15b1c8-edd8-441d-a799-c35939f226b4",
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/flavors/1c15b1c8-edd8-441d-a799-c35939f226b4"
                }
            ]
        },
        "created": "2023-11-17T18:28:45Z",
        "updated": "2023-11-17T18:29:09Z",
        "addresses": {
            "orchestration": [
                {
                    "version": 4,
                    "addr": "15.100.2.198",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8f:e0:92"
                }
            ],
            "management": [
                {
                    "version": 4,
                    "addr": "15.100.1.198",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8f:6a:55"
                }
            ],
            "sriov0": [
                {
                    "version": 4,
                    "addr": "15.100.105.198",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:fc:e6:60"
                },
                {
                    "version": 4,
                    "addr": "15.100.105.98",
                    "OS-EXT-IPS:type": "fixed",
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:7d:a2:a1"
                }
            ]
        },
        "accessIPv4": "",
        "accessIPv6": "",
        "links": [
            {
                "rel": "self",
                "href": "https://10.58.28.113:8774/v2.1/2cced286b74c45ea95c83cc2e5d3b413/servers/38e93240-4d5d-476b-b5f9-362c5d2b508a"
            },
            {
                "rel": "bookmark",
                "href": "https://10.58.28.113:8774/2cced286b74c45ea95c83cc2e5d3b413/servers/38e93240-4d5d-476b-b5f9-362c5d2b508a"
            }
        ],
        "OS-DCF:diskConfig": "MANUAL",
        "progress": 0,
        "OS-EXT-AZ:availability_zone": "ALL",
        "config_drive": "True",
        "key_name": null,
        "OS-SRV-USG:launched_at": "2023-11-17T18:29:09.000000",
        "OS-SRV-USG:terminated_at": null,
        "OS-EXT-SRV-ATTR:host": "AIO-server-3",
        "OS-EXT-SRV-ATTR:instance_name": "instance-000007a9",
        "OS-EXT-SRV-ATTR:hypervisor_hostname": "AIO-server-3",
        "OS-EXT-STS:task_state": null,
        "OS-EXT-STS:vm_state": "active",
        "OS-EXT-STS:power_state": 1,
        "os-extended-volumes:volumes_attached": [],
        "security_groups": [
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            },
            {
                "name": "default"
            }
        ],
        "__Output": {
            "status": "Green"
        },
        "bootFrom": "Image",
        "power_state": "powered-up",
        "task_state": null,
        "hypervisor": "AIO-server-3",
        "interface": [
            {
                "network": "orchestration",
                "ip": "15.100.2.198",
                "type": "fixed",
                "ip_type": "15.100.2.198 (fixed)",
                "mac": "fa:16:3e:8f:e0:92",
                "network_ip": "orchestration=15.100.2.198"
            },
            {
                "network": "management",
                "ip": "15.100.1.198",
                "type": "fixed",
                "ip_type": "15.100.1.198 (fixed)",
                "mac": "fa:16:3e:8f:6a:55",
                "network_ip": "management=15.100.1.198"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.198",
                "type": "fixed",
                "ip_type": "15.100.105.198 (fixed)",
                "mac": "fa:16:3e:fc:e6:60",
                "network_ip": "sriov0=15.100.105.198"
            },
            {
                "network": "sriov0",
                "ip": "15.100.105.98",
                "type": "fixed",
                "ip_type": "15.100.105.98 (fixed)",
                "mac": "fa:16:3e:7d:a2:a1",
                "network_ip": "sriov0=15.100.105.98"
            }
        ],
        "age": "3d",
        "tenant_name": "smi5gc",
        "flavor_info": {
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
        "volumes": [],
        "image_info": {
            "__Output": {
                "status": "Green"
            },
            "name": "qvpc-si-21.28.m15",
            "disk_format": "qcow2",
            "container_format": "bare",
            "visibility": "public",
            "size": 210370560,
            "sizeT": "210,370,560",
            "virtual_size": null,
            "status": "active",
            "checksum": "55e8916d3911570596ba35cd9aff8357",
            "protected": false,
            "protectedTick": "\u2717",
            "min_ram": 0,
            "min_disk": 0,
            "owner": "2cced286b74c45ea95c83cc2e5d3b413",
            "os_hidden": false,
            "os_hash_algo": "sha512",
            "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
            "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
            "updated_at": "2023-10-25T10:03:24Z",
            "created_at": "2023-10-25T10:03:19Z",
            "locations": [
                {
                    "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                    "metadata": {}
                }
            ],
            "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
        },
        "bootSource": "qvpc-si-21.28.m15",
        "bootSourceT": "(img) qvpc-si-21.28.m15"
    }
]
```

Developer

```
# iserver get osp vm --cluster pod1 -o json

{
    "duration": 8428,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 5729,
        "total_time": 5729
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
        "lines": 5
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 18:39:28.406850	True	3555	get	virtual_machines
2023-11-20 18:39:29.700643	True	1246	get	tenants
2023-11-20 18:39:29.886045	True	171	get	flavors
2023-11-20 18:39:30.616482	True	0	get	images
2023-11-20 18:39:32.264714	True	757	get	volumes.list
```

[[Back]](./VirtualMachineGet.md)