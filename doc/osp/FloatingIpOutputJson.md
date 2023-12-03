# Floating IP

## Default output

```
# iserver get osp fip --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "status": "Green"
        },
        "id": "563cee91-6426-46c2-b659-2d1027a259b3",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "floating_ip_address": "10.58.28.82",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "c59f2ec5-017e-4c0f-9051-e64285fb5ec6",
        "fixed_ip_address": "15.100.1.36",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:bb:2b:cd",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "smi5gc/esc"
        },
        "tags": [],
        "created_at": "2023-11-16T17:03:15Z",
        "updated_at": "2023-11-16T17:03:31Z",
        "revision_number": 3,
        "project_id": "05b8e996f0654e4491d2e925a91c6250",
        "tenant_name": "smi5gc",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "030dffa5-d64b-45fd-aa51-adc6cf535e6e",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "floating_ip_address": "10.58.28.83",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "a64f6957-442b-43c5-b0f9-eb48f921b1e9",
        "fixed_ip_address": "15.100.1.102",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "server-management",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:38:40:30",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "b56451ce-e214-4484-9f35-e656a95a8328",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "smi5gc/server"
        },
        "tags": [],
        "created_at": "2022-08-04T14:02:27Z",
        "updated_at": "2023-07-05T17:19:41Z",
        "revision_number": 10,
        "project_id": "05b8e996f0654e4491d2e925a91c6250",
        "tenant_name": "smi5gc",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "95b29935-5951-49ed-a836-ba49309bab6d",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "floating_ip_address": "10.58.28.84",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "0351b0fa-7ff1-4911-9b4e-5e80d33225aa",
        "fixed_ip_address": "15.100.1.100",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "portal-management",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:cc:97:82",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "3fea1ac9-25cc-4183-976e-af79a513aa36",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "smi5gc/portal"
        },
        "tags": [],
        "created_at": "2022-08-04T13:40:22Z",
        "updated_at": "2023-07-05T17:19:42Z",
        "revision_number": 10,
        "project_id": "05b8e996f0654e4491d2e925a91c6250",
        "tenant_name": "smi5gc",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "2b60dc69-795a-4fdd-ab15-248a89cbef2b",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "floating_ip_address": "10.58.28.85",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "c3ddf85a-c27b-4ff1-aed5-575d600cac85",
        "fixed_ip_address": "15.100.1.101",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "lattice-management",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:c3:6b:06",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "smi5gc/lattice"
        },
        "tags": [],
        "created_at": "2022-08-04T14:02:36Z",
        "updated_at": "2023-07-05T17:19:42Z",
        "revision_number": 10,
        "project_id": "05b8e996f0654e4491d2e925a91c6250",
        "tenant_name": "smi5gc",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "47f497c8-678e-412f-863e-d0167a7745f0",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "floating_ip_address": "10.58.28.90",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "70c295b3-5b54-4b57-aa6f-547bd8da78ca",
        "fixed_ip_address": "15.100.1.30",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "wan-C8KV01B",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:14:7d:d0",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "1fb263d3-437c-47dc-b3a0-38168a0a9e41",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "ialonso/SDWAN-C8KV01B"
        },
        "tags": [],
        "created_at": "2023-10-23T15:19:57Z",
        "updated_at": "2023-10-23T15:20:26Z",
        "revision_number": 4,
        "project_id": "9b50a8dba82f4c14802c4554482882b8",
        "tenant_name": "ialonso",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "cebf11be-0198-4edf-8790-630093b29e8f",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "floating_ip_address": "10.58.28.91",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "725dbe0a-4da8-4bb1-9e1e-eb14dc51caec",
        "fixed_ip_address": "15.100.1.219",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "wan-SDWAN-C8KV01",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:97:c1:38",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "4e8f1b44-593d-492b-8985-094e6f88f83b",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "ialonso/ORANGE-C8KV-1"
        },
        "tags": [],
        "created_at": "2023-11-01T22:26:45Z",
        "updated_at": "2023-11-01T22:26:59Z",
        "revision_number": 3,
        "project_id": "9b50a8dba82f4c14802c4554482882b8",
        "tenant_name": "ialonso",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "id": "6bb32d9d-9756-46d1-a87b-208327864a52",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "floating_ip_address": "10.58.28.92",
        "floating_network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "router_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "port_id": "0a3f9d9e-04fe-4c3c-9e3f-9da4a86428d2",
        "fixed_ip_address": "15.100.1.179",
        "status": "ACTIVE",
        "description": "",
        "port_details": {
            "name": "wan-C8KV_ORANGE",
            "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
            "mac_address": "fa:16:3e:a4:f5:53",
            "admin_state_up": true,
            "status": "ACTIVE",
            "device_id": "0f3afdc8-8405-460a-a3cc-95944c695d4d",
            "device_owner": "compute:ALL",
            "network_name": "management",
            "vm_name": "ialonso/ORANGE-C8KV-2"
        },
        "tags": [],
        "created_at": "2023-10-24T08:11:13Z",
        "updated_at": "2023-10-24T08:11:36Z",
        "revision_number": 4,
        "project_id": "9b50a8dba82f4c14802c4554482882b8",
        "tenant_name": "ialonso",
        "floating_network_name": "external",
        "router_name": "smi5gc-router"
    }
]
```

Developer

```
# iserver get osp fip --cluster pod1 -o json

{
    "duration": 5231,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 4028,
        "total_time": 4028
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

2023-11-18 16:51:51.354848	True	1502	get	floating_ips
2023-11-18 16:51:51.660548	True	292	get	tenants
2023-11-18 16:51:51.856166	True	184	get	networks
2023-11-18 16:51:52.121586	True	223	get	routers
2023-11-18 16:51:54.871509	True	1827	get	virtual_machines
```

[[Back]](./FloatingIpGet.md)