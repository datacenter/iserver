# Port

## Default output

```
# iserver get osp port --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "20ff3eb6-5c97-403a-839e-24b19da9578c",
        "name": "lan-C8KV01",
        "network_id": "d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:5c:b7:b8",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "4e8f1b44-593d-492b-8985-094e6f88f83b",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "db2b80bf-65d0-4836-9eb3-929eefb8fff0",
                "ip_address": "10.0.11.1",
                "subnet_name": "C8KV01_LAN01"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:5c:b7:b8",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "92b851c1-a79b-48ea-8784-3c3bc3adba8e"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-23T14:29:49Z",
        "updated_at": "2023-11-01T22:34:11Z",
        "ips": "10.0.11.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "27d",
        "tenant_name": "ialonso",
        "network_name": "C8KV01_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "e314506b-aa5f-4b21-9655-d2a3c254670e",
        "name": "lan-C8KV01B",
        "network_id": "d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:3b:d5:c6",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "1fb263d3-437c-47dc-b3a0-38168a0a9e41",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "db2b80bf-65d0-4836-9eb3-929eefb8fff0",
                "ip_address": "10.0.11.2",
                "subnet_name": "C8KV01_LAN01"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:3b:d5:c6",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "92b851c1-a79b-48ea-8784-3c3bc3adba8e"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-23T15:20:31Z",
        "updated_at": "2023-10-23T16:17:11Z",
        "ips": "10.0.11.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "27d",
        "tenant_name": "ialonso",
        "network_name": "C8KV01_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "75058109-acc1-41c0-9268-0cb32231d2e3",
        "name": "",
        "network_id": "d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:79:74:6e",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "db2b80bf-65d0-4836-9eb3-929eefb8fff0",
                "ip_address": "10.0.11.5",
                "subnet_name": "C8KV01_LAN01"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-16T15:30:05Z",
        "updated_at": "2023-10-16T15:30:09Z",
        "ips": "10.0.11.5",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "34d",
        "tenant_name": "ialonso",
        "network_name": "C8KV01_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "55dcc954-bb54-489d-931c-c12dc8dbf535",
        "name": "",
        "network_id": "d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:91:2f:04",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "db2b80bf-65d0-4836-9eb3-929eefb8fff0",
                "ip_address": "10.0.11.6",
                "subnet_name": "C8KV01_LAN01"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-16T15:30:06Z",
        "updated_at": "2023-10-16T15:30:08Z",
        "ips": "10.0.11.6",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "34d",
        "tenant_name": "ialonso",
        "network_name": "C8KV01_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "0d99d989-7de5-49e8-8b9b-3981ebb6be56",
        "name": "lan-C8KV_ORANGE",
        "network_id": "15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:67:1b:48",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "0f3afdc8-8405-460a-a3cc-95944c695d4d",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "afd52863-ee94-4880-80be-fc6fd7788f6e",
                "ip_address": "10.0.21.1",
                "subnet_name": "C8KV_ORANGE_LAN01"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:67:1b:48",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "92b851c1-a79b-48ea-8784-3c3bc3adba8e"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-24T08:11:50Z",
        "updated_at": "2023-11-01T22:40:24Z",
        "ips": "10.0.21.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "26d",
        "tenant_name": "ialonso",
        "network_name": "C8KV_ORANGE_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "a99c45e4-4935-41a8-8a15-d64e0406efdd",
        "name": "",
        "network_id": "15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "mac_address": "fa:16:3e:ae:32:44",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "f83b1396-40b2-4dec-b336-597fc42e55d7",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "afd52863-ee94-4880-80be-fc6fd7788f6e",
                "ip_address": "10.0.21.2",
                "subnet_name": "C8KV_ORANGE_LAN01"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "64b47d51-b1bc-4142-a2f0-b321d85a3291"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-02T08:55:06Z",
        "updated_at": "2023-11-02T09:19:58Z",
        "ips": "10.0.21.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "DOWN",
        "type": "Compute",
        "age": "17d",
        "tenant_name": "admin",
        "network_name": "C8KV_ORANGE_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "82109a20-a4f5-4862-86c4-8f81130f8889",
        "name": "",
        "network_id": "15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:db:b8:4b",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "afd52863-ee94-4880-80be-fc6fd7788f6e",
                "ip_address": "10.0.21.5",
                "subnet_name": "C8KV_ORANGE_LAN01"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-24T08:09:28Z",
        "updated_at": "2023-10-24T08:09:31Z",
        "ips": "10.0.21.5",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "26d",
        "tenant_name": "ialonso",
        "network_name": "C8KV_ORANGE_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "79b347fb-c909-457e-a121-3953c69967b0",
        "name": "",
        "network_id": "15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:d6:0f:0c",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "afd52863-ee94-4880-80be-fc6fd7788f6e",
                "ip_address": "10.0.21.6",
                "subnet_name": "C8KV_ORANGE_LAN01"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-24T08:09:29Z",
        "updated_at": "2023-10-24T08:09:32Z",
        "ips": "10.0.21.6",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "26d",
        "tenant_name": "ialonso",
        "network_name": "C8KV_ORANGE_LAN01"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "6a4556a4-fad4-4d29-b3fe-eda3b156e9ab",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "",
        "mac_address": "fa:16:3e:c1:37:01",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "device_owner": "network:router_gateway",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.81",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T13:39:00Z",
        "updated_at": "2023-07-05T17:17:36Z",
        "ips": "10.58.28.81",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "Gateway",
        "age": "472d",
        "tenant_name": null,
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "0a2f3401-c61f-45d4-abc7-094f5d9d4f67",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:f3:63:1f",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "563cee91-6426-46c2-b659-2d1027a259b3",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.82",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-16T17:03:14Z",
        "updated_at": "2023-11-16T17:03:17Z",
        "ips": "10.58.28.82",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "2d",
        "tenant_name": "smi5gc",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "e4eed45c-950a-46d5-9996-7ef50254a948",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:b8:e4:f3",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "030dffa5-d64b-45fd-aa51-adc6cf535e6e",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.83",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T14:02:26Z",
        "updated_at": "2022-08-04T14:02:28Z",
        "ips": "10.58.28.83",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "29296900-ec71-4783-b5ff-96a0f86b516e",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:32:07:87",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "95b29935-5951-49ed-a836-ba49309bab6d",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.84",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T13:40:21Z",
        "updated_at": "2022-08-04T13:40:23Z",
        "ips": "10.58.28.84",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "63f97b42-828f-40eb-ac14-b3652dd9309c",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:93:e6:fe",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "2b60dc69-795a-4fdd-ab15-248a89cbef2b",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.85",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T14:02:36Z",
        "updated_at": "2022-08-04T14:02:37Z",
        "ips": "10.58.28.85",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "2db8f699-c218-46c1-8c25-08a6ea53e867",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:e7:04:c9",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "47f497c8-678e-412f-863e-d0167a7745f0",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.90",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-23T15:19:56Z",
        "updated_at": "2023-10-23T15:19:58Z",
        "ips": "10.58.28.90",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "27d",
        "tenant_name": "ialonso",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "057b63ca-e72d-456a-8171-5ae37e1c79d9",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:7c:67:22",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "cebf11be-0198-4edf-8790-630093b29e8f",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.91",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-01T22:26:42Z",
        "updated_at": "2023-11-01T22:26:48Z",
        "ips": "10.58.28.91",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "17d",
        "tenant_name": "ialonso",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green"
        },
        "id": "1111fc66-5479-41f1-b50b-02fa36a6b39f",
        "name": "",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:fc:2b:eb",
        "admin_state_up": true,
        "status": "N/A",
        "device_id": "6bb32d9d-9756-46d1-a87b-208327864a52",
        "device_owner": "network:floatingip",
        "fixed_ips": [
            {
                "subnet_id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
                "ip_address": "10.58.28.92",
                "subnet_name": "subnet-ext"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-24T08:11:12Z",
        "updated_at": "2023-10-24T08:11:13Z",
        "ips": "10.58.28.92",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "--",
        "type": "Floating",
        "age": "26d",
        "tenant_name": "ialonso",
        "network_name": "external"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "3a6f7317-15b9-4778-badb-60653168f75e",
        "name": "",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:d3:81:f1",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-fe1e3247-64b8-45ae-aa40-468a9a768954",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.1",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:12Z",
        "updated_at": "2022-08-04T10:57:14Z",
        "ips": "15.100.1.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "0351b0fa-7ff1-4911-9b4e-5e80d33225aa",
        "name": "portal-management",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:cc:97:82",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "3fea1ac9-25cc-4183-976e-af79a513aa36",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.100",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "6208a2c8-c27c-49f8-9c19-625d79221b2b"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T12:43:59Z",
        "updated_at": "2022-08-04T14:23:14Z",
        "ips": "15.100.1.100",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c3ddf85a-c27b-4ff1-aed5-575d600cac85",
        "name": "lattice-management",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:c3:6b:06",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.101",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:14Z",
        "updated_at": "2023-11-02T11:16:21Z",
        "ips": "15.100.1.101",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "a64f6957-442b-43c5-b0f9-eb48f921b1e9",
        "name": "server-management",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:38:40:30",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b56451ce-e214-4484-9f35-e656a95a8328",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.102",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:06Z",
        "updated_at": "2022-08-04T11:20:28Z",
        "ips": "15.100.1.102",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "63e28384-5a73-4741-9058-e2fbe460aca3",
        "name": "VPC-SI-mme-nic1",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:22:8e:23",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "a898461f-20f2-454f-82e9-3ff1905f399e",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.103",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:26:37Z",
        "updated_at": "2023-11-17T18:27:37Z",
        "ips": "15.100.1.103",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "140a1aaa-affc-4eca-932f-79b7734d5f01",
        "name": "",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "mac_address": "fa:16:3e:6b:57:aa",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "cf0d30bc-7ff5-4959-bbda-b06a803d9526",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.117",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "64b47d51-b1bc-4142-a2f0-b321d85a3291"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-01T20:02:40Z",
        "updated_at": "2023-11-01T20:25:02Z",
        "ips": "15.100.1.117",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "DOWN",
        "type": "Compute",
        "age": "17d",
        "tenant_name": "admin",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "0a3f9d9e-04fe-4c3c-9e3f-9da4a86428d2",
        "name": "wan-C8KV_ORANGE",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:a4:f5:53",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "0f3afdc8-8405-460a-a3cc-95944c695d4d",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.179",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:a4:f5:53",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "92b851c1-a79b-48ea-8784-3c3bc3adba8e"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-24T08:09:40Z",
        "updated_at": "2023-11-01T22:40:22Z",
        "ips": "15.100.1.179",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "26d",
        "tenant_name": "ialonso",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "00f08d24-2d92-4058-bc8a-db3cbec560f6",
        "name": "VPC-SI-upf1-nic1",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:22:9c:e2",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "40133dad-7c09-4846-9f4e-f5db7872a1ea",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.191",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:23Z",
        "updated_at": "2023-11-17T19:10:58Z",
        "ips": "15.100.1.191",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "03b89215-7752-447a-8a2a-1d40fadb61a8",
        "name": "VPC-SI-upf2-nic1",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:01:17:1c",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "f9d17afa-36bb-4b8e-9448-77e61dfc2552",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.192",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:15Z",
        "updated_at": "2023-11-17T19:11:07Z",
        "ips": "15.100.1.192",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "8c2dfb97-4280-474b-b8bb-914d37ed78a8",
        "name": "VPC-SI-upf8-nic1",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:8f:6a:55",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "38e93240-4d5d-476b-b5f9-362c5d2b508a",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.198",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:29Z",
        "updated_at": "2023-11-17T18:29:00Z",
        "ips": "15.100.1.198",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "86052387-6b5f-4b53-9661-1f2edee14191",
        "name": "",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:2e:aa:e4",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-fe1e3247-64b8-45ae-aa40-468a9a768954",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.2",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:13Z",
        "updated_at": "2022-08-04T10:57:16Z",
        "ips": "15.100.1.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "f6ec692e-e0c1-4134-a35b-2e4136589aef",
        "name": "master-vip",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:b3:23:ae",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "",
        "device_owner": "",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.201",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:04:31Z",
        "updated_at": "2022-08-04T11:04:31Z",
        "ips": "15.100.1.201",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "",
        "binding_vif_type": "unbound",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "DOWN",
        "type": null,
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "725dbe0a-4da8-4bb1-9e1e-eb14dc51caec",
        "name": "wan-SDWAN-C8KV01",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:97:c1:38",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "4e8f1b44-593d-492b-8985-094e6f88f83b",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.219",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:97:c1:38",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "92b851c1-a79b-48ea-8784-3c3bc3adba8e"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-23T14:29:12Z",
        "updated_at": "2023-11-01T22:14:56Z",
        "ips": "15.100.1.219",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "27d",
        "tenant_name": "ialonso",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "3db9c359-07c6-4cd7-a68d-331ede87953b",
        "name": "",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "mac_address": "fa:16:3e:0c:78:90",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "f83b1396-40b2-4dec-b336-597fc42e55d7",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.220",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "64b47d51-b1bc-4142-a2f0-b321d85a3291"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-02T08:55:05Z",
        "updated_at": "2023-11-02T09:19:58Z",
        "ips": "15.100.1.220",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "DOWN",
        "type": "Compute",
        "age": "17d",
        "tenant_name": "admin",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "9bfbcef9-462d-4413-bbd3-c989ead917b1",
        "name": "smi5gc-router-management",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:78:dd:45",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "device_owner": "network:ha_router_replicated_interface",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.254",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T13:39:08Z",
        "updated_at": "2023-07-05T17:17:37Z",
        "ips": "15.100.1.254",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "HA",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "70c295b3-5b54-4b57-aa6f-547bd8da78ca",
        "name": "wan-C8KV01B",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "mac_address": "fa:16:3e:14:7d:d0",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "1fb263d3-437c-47dc-b3a0-38168a0a9e41",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.30",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:14:7d:d0",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "92b851c1-a79b-48ea-8784-3c3bc3adba8e"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-10-23T15:19:35Z",
        "updated_at": "2023-10-23T16:17:10Z",
        "ips": "15.100.1.30",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "27d",
        "tenant_name": "ialonso",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c59f2ec5-017e-4c0f-9051-e64285fb5ec6",
        "name": "",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:bb:2b:cd",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.36",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "5df0520b-674e-422b-abb4-b25d645d9aba",
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-16T17:02:00Z",
        "updated_at": "2023-11-16T17:06:39Z",
        "ips": "15.100.1.36",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "2d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "d8a106f7-6fcd-4141-b542-e471a269f049",
        "name": "VPC-SI-saegw1-nic1",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:15:b1:7f",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b698f08c-71bd-430c-b966-8c16230c824d",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.51",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:02Z",
        "updated_at": "2023-11-17T18:28:43Z",
        "ips": "15.100.1.51",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "f15000ee-b812-4456-8fa0-6ab5551f3ba3",
        "name": "VPC-SI-saegw2-nic1",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:57:23:38",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "0b7905f8-d572-42c6-91ad-b24b21f4cade",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.52",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:27Z",
        "updated_at": "2023-11-17T18:29:29Z",
        "ips": "15.100.1.52",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "7d8c1304-18ea-4988-a779-d59040972a8d",
        "name": "",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "mac_address": "fa:16:3e:13:75:c2",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b75cd7b9-5154-4863-93e9-79dc651198b8",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
                "ip_address": "15.100.1.69",
                "subnet_name": "management-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "64b47d51-b1bc-4142-a2f0-b321d85a3291"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-02T14:09:54Z",
        "updated_at": "2023-11-03T00:29:39Z",
        "ips": "15.100.1.69",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "17d",
        "tenant_name": "admin",
        "network_name": "management"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "cff62f6e-bd60-4850-81fa-f3803df4ba83",
        "name": "",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:51:c2:e3",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.1",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:39Z",
        "updated_at": "2023-07-05T17:19:26Z",
        "ips": "15.100.105.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "binding_failed",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "DOWN",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c265c00c-f5a6-4afd-9835-3d246887c1ed",
        "name": "VPC-SI-saegw1-nic2",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:dd:d2:9d",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b698f08c-71bd-430c-b966-8c16230c824d",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.151",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:dd:d2:9d",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:25Z",
        "updated_at": "2023-11-17T18:28:50Z",
        "ips": "15.100.105.151",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.7",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "0621bfa3-5e19-4307-8a64-cd9e4f2f3cf2",
        "name": "VPC-SI-saegw2-nic2",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:18:11:ba",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "0b7905f8-d572-42c6-91ad-b24b21f4cade",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.152",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:18:11:ba",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:48Z",
        "updated_at": "2023-11-17T18:29:33Z",
        "ips": "15.100.105.152",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.7",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "64c5e030-ccee-4e8f-a3db-78c3a551981d",
        "name": "VPC-SI-upf1-nic2",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:e8:f1:d5",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "40133dad-7c09-4846-9f4e-f5db7872a1ea",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.191",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:e8:f1:d5",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:38Z",
        "updated_at": "2023-11-17T18:28:52Z",
        "ips": "15.100.105.191",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.7",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "aa3cb08f-f99c-400e-a8eb-fec8104c97a3",
        "name": "VPC-SI-upf2-nic2",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:48:32:31",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "f9d17afa-36bb-4b8e-9448-77e61dfc2552",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.192",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:48:32:31",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:29Z",
        "updated_at": "2023-11-17T18:28:50Z",
        "ips": "15.100.105.192",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.7",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "1147a955-ab01-4297-9585-0382770bad45",
        "name": "VPC-SI-upf8-nic2",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:fc:e6:60",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "38e93240-4d5d-476b-b5f9-362c5d2b508a",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.198",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:fc:e6:60",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:51Z",
        "updated_at": "2023-11-17T18:29:07Z",
        "ips": "15.100.105.198",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.5",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "9d06a0d9-e801-4f69-b40b-258b0d46fb2c",
        "name": "",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:15:37:ec",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.2",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:40Z",
        "updated_at": "2023-07-05T17:20:45Z",
        "ips": "15.100.105.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "binding_failed",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "DOWN",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c85ec143-f671-47b6-8c4a-4032e750b2fd",
        "name": "test-sriov",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "mac_address": "fa:16:3e:89:e6:2b",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "58799272-64da-4056-bf7e-11053042423b",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.245",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "64b47d51-b1bc-4142-a2f0-b321d85a3291"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-05-01T09:13:42Z",
        "updated_at": "2023-07-05T17:19:12Z",
        "ips": "15.100.105.245",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.6",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "202d",
        "tenant_name": "admin",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "404158b3-e275-4cb6-b5f4-da615488c6de",
        "name": "VPC-SI-saegw1-nic3",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:c3:ad:0b",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b698f08c-71bd-430c-b966-8c16230c824d",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.51",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:c3:ad:0b",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:45Z",
        "updated_at": "2023-11-17T18:28:52Z",
        "ips": "15.100.105.51",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.6",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "b69931ac-b78b-45d8-a4f6-cc62a7d615cc",
        "name": "VPC-SI-saegw2-nic3",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:1e:c2:e6",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "0b7905f8-d572-42c6-91ad-b24b21f4cade",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.52",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:1e:c2:e6",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:28:16Z",
        "updated_at": "2023-11-17T18:29:33Z",
        "ips": "15.100.105.52",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.6",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "e8124da8-c459-4d4f-afbc-3b32ba3901e7",
        "name": "VPC-SI-upf1-nic3",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:e7:65:c7",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "40133dad-7c09-4846-9f4e-f5db7872a1ea",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.91",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:e7:65:c7",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:28:13Z",
        "updated_at": "2023-11-17T18:28:53Z",
        "ips": "15.100.105.91",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.2",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c3228e48-6c31-448b-b80f-7e7718373ce8",
        "name": "VPC-SI-upf2-nic3",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:74:59:71",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "f9d17afa-36bb-4b8e-9448-77e61dfc2552",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.92",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:74:59:71",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:58Z",
        "updated_at": "2023-11-17T18:28:51Z",
        "ips": "15.100.105.92",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.4",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "d0ea273f-eb63-4283-8267-57fa9ac11220",
        "name": "VPC-SI-upf8-nic3",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:7d:a2:a1",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "38e93240-4d5d-476b-b5f9-362c5d2b508a",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "195953ed-add3-4c59-b81a-ee372dcd7838",
                "ip_address": "15.100.105.98",
                "subnet_name": "sriov0-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:7d:a2:a1",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:28:16Z",
        "updated_at": "2023-11-17T18:29:07Z",
        "ips": "15.100.105.98",
        "binding_vnic_type": "direct",
        "binding_profile": {
            "pci_vendor_info": "8086:154c",
            "pci_slot": "0000:5e:0b.4",
            "physical_network": "phys_sriov0"
        },
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "hw_veb",
        "binding_vif_details": {
            "port_filter": false,
            "connectivity": "l2",
            "vlan": "0"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "f4feb13c-87d7-4a64-b468-2dca5a717f00",
        "name": "",
        "network_id": "cd63e7ec-39b2-4f47-9f46-df5d3e25c967",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:8e:cf:5c",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-cd63e7ec-39b2-4f47-9f46-df5d3e25c967",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "1cbf95c8-b46c-4684-92da-7199481236c3",
                "ip_address": "15.100.106.1",
                "subnet_name": "sriov1-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:43Z",
        "updated_at": "2023-07-05T17:20:46Z",
        "ips": "15.100.106.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "binding_failed",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "DOWN",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "sriov1"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Red"
        },
        "id": "dd59111e-96a7-4617-984c-72b1b6f09a89",
        "name": "",
        "network_id": "cd63e7ec-39b2-4f47-9f46-df5d3e25c967",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:ac:78:eb",
        "admin_state_up": true,
        "status": "DOWN",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-cd63e7ec-39b2-4f47-9f46-df5d3e25c967",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "1cbf95c8-b46c-4684-92da-7199481236c3",
                "ip_address": "15.100.106.2",
                "subnet_name": "sriov1-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:44Z",
        "updated_at": "2023-07-05T17:15:47Z",
        "ips": "15.100.106.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "binding_failed",
        "binding_vif_details": {},
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "DOWN",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "sriov1"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "a7f2630a-8948-4dab-8328-d424246b078f",
        "name": "",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:e2:ff:72",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-3065667d-94c9-442c-87c1-bec9cffa0d50",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.1",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:15Z",
        "updated_at": "2022-08-04T10:57:18Z",
        "ips": "15.100.2.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "b730b869-d322-4868-993d-c25115065004",
        "name": "VPC-SI-mme-nic0",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:88:5f:dd",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "a898461f-20f2-454f-82e9-3ff1905f399e",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.103",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:26:30Z",
        "updated_at": "2023-11-17T18:27:38Z",
        "ips": "15.100.2.103",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "d276f181-4281-4f70-8af9-464b1f22b2b5",
        "name": "VPC-SI-upf1-nic0",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:cf:4b:b5",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "40133dad-7c09-4846-9f4e-f5db7872a1ea",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.191",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:14Z",
        "updated_at": "2023-11-17T19:10:57Z",
        "ips": "15.100.2.191",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "b52c7c0f-6a0c-41bd-b587-ae4dfec406b5",
        "name": "VPC-SI-upf2-nic0",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:d8:3b:77",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "f9d17afa-36bb-4b8e-9448-77e61dfc2552",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.192",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:26:58Z",
        "updated_at": "2023-11-17T19:11:03Z",
        "ips": "15.100.2.192",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "2f1dd34f-446c-4f45-b7b9-9859da1efe58",
        "name": "VPC-SI-upf8-nic0",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:8f:e0:92",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "38e93240-4d5d-476b-b5f9-362c5d2b508a",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.198",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:26Z",
        "updated_at": "2023-11-17T18:29:01Z",
        "ips": "15.100.2.198",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c9d7b037-d284-4c29-a4b2-1dc5fe1155e2",
        "name": "",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:9e:96:65",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-3065667d-94c9-442c-87c1-bec9cffa0d50",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.2",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:16Z",
        "updated_at": "2022-08-04T10:57:20Z",
        "ips": "15.100.2.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "48686396-417d-433c-8088-e2c845ade262",
        "name": "",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:2d:58:f2",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "61aed3ca-ca27-4ec4-a7ea-9a5cf8da94db",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.36",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-16T17:02:03Z",
        "updated_at": "2023-11-16T17:02:19Z",
        "ips": "15.100.2.36",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "2d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "5db647c6-4822-4057-afb5-76bdc978ef7c",
        "name": "VPC-SI-saegw1-nic0",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:6f:c4:6a",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b698f08c-71bd-430c-b966-8c16230c824d",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.51",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:26:48Z",
        "updated_at": "2023-11-17T18:28:49Z",
        "ips": "15.100.2.51",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "d2704fbf-137c-4add-bf28-c197083c3407",
        "name": "VPC-SI-saegw2-nic0",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:92:89:86",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "0b7905f8-d572-42c6-91ad-b24b21f4cade",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
                "ip_address": "15.100.2.52",
                "subnet_name": "orchestration-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:27:22Z",
        "updated_at": "2023-11-17T18:29:29Z",
        "ips": "15.100.2.52",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "75584da5-6d87-4523-a900-795a03f7b435",
        "name": "",
        "network_id": "a4fe3f25-a010-4cad-a945-0e36256b3783",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:ea:51:30",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-a4fe3f25-a010-4cad-a945-0e36256b3783",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "4299410e-e562-46d6-93b0-d839669a5bca",
                "ip_address": "15.100.3.1",
                "subnet_name": "control-k8s-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:19Z",
        "updated_at": "2022-08-04T10:57:22Z",
        "ips": "15.100.3.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-k8s"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c8059be0-eb60-4a9f-aeb9-9a6767222672",
        "name": "",
        "network_id": "a4fe3f25-a010-4cad-a945-0e36256b3783",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:5b:72:42",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-a4fe3f25-a010-4cad-a945-0e36256b3783",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "4299410e-e562-46d6-93b0-d839669a5bca",
                "ip_address": "15.100.3.2",
                "subnet_name": "control-k8s-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:20Z",
        "updated_at": "2022-08-04T10:57:23Z",
        "ips": "15.100.3.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-k8s"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "832a46f2-ee2a-4f90-b374-cd6f916ec788",
        "name": "",
        "network_id": "02c949a8-1b9c-4162-a8ad-f8941a8f37d1",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:9b:b6:b0",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-02c949a8-1b9c-4162-a8ad-f8941a8f37d1",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "84b1de29-b4be-4508-8ad9-6c68c930dac5",
                "ip_address": "15.100.4.1",
                "subnet_name": "control-SBI-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:22Z",
        "updated_at": "2022-08-04T10:57:25Z",
        "ips": "15.100.4.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-SBI"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "c449bed2-dd2d-488d-a457-8cd4d9530579",
        "name": "lattice-sbi",
        "network_id": "02c949a8-1b9c-4162-a8ad-f8941a8f37d1",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:cc:7f:24",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "84b1de29-b4be-4508-8ad9-6c68c930dac5",
                "ip_address": "15.100.4.101",
                "subnet_name": "control-SBI-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:cc:7f:24",
                "ip_address": "15.100.0.0/24"
            },
            {
                "mac_address": "fa:16:3e:cc:7f:24",
                "ip_address": "15.100.4.0/24"
            },
            {
                "mac_address": "fa:16:3e:cc:7f:24",
                "ip_address": "15.100.4.106"
            },
            {
                "mac_address": "fa:16:3e:cc:7f:24",
                "ip_address": "15.100.4.107"
            },
            {
                "mac_address": "fa:16:3e:cc:7f:24",
                "ip_address": "15.100.4.108"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:22Z",
        "updated_at": "2023-11-02T11:16:20Z",
        "ips": "15.100.4.101",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-SBI"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "42fb3ad1-8ef5-4f91-94cf-f70770191bdf",
        "name": "",
        "network_id": "02c949a8-1b9c-4162-a8ad-f8941a8f37d1",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:77:f7:73",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-02c949a8-1b9c-4162-a8ad-f8941a8f37d1",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "84b1de29-b4be-4508-8ad9-6c68c930dac5",
                "ip_address": "15.100.4.2",
                "subnet_name": "control-SBI-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:23Z",
        "updated_at": "2022-08-04T10:57:25Z",
        "ips": "15.100.4.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-SBI"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "0926323f-9871-4849-b6e5-cb48e052909a",
        "name": "",
        "network_id": "25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:c9:c1:51",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "1786aa38-3ab1-4a86-9966-f4dae5411bab",
                "ip_address": "15.100.5.1",
                "subnet_name": "control-N2-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:25Z",
        "updated_at": "2022-08-04T10:57:28Z",
        "ips": "15.100.5.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-N2"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "ca51098d-b807-4060-ac89-398f2c256084",
        "name": "lattice-n2",
        "network_id": "25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:63:7d:aa",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "1786aa38-3ab1-4a86-9966-f4dae5411bab",
                "ip_address": "15.100.5.101",
                "subnet_name": "control-N2-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:63:7d:aa",
                "ip_address": "15.100.5.0/24"
            },
            {
                "mac_address": "fa:16:3e:63:7d:aa",
                "ip_address": "15.100.5.102"
            },
            {
                "mac_address": "fa:16:3e:63:7d:aa",
                "ip_address": "15.100.5.103"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:25Z",
        "updated_at": "2023-11-02T11:16:21Z",
        "ips": "15.100.5.101",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-N2"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "977dbe25-bb58-4604-94cb-72d71ae2fdd1",
        "name": "",
        "network_id": "25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:8b:2c:b8",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "1786aa38-3ab1-4a86-9966-f4dae5411bab",
                "ip_address": "15.100.5.2",
                "subnet_name": "control-N2-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:26Z",
        "updated_at": "2022-08-04T10:57:28Z",
        "ips": "15.100.5.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-N2"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "1aa3305f-2a3f-4e6d-9558-05da2761269d",
        "name": "",
        "network_id": "0d6676b5-6fbc-4b51-bf29-1380cef97fcd",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:6b:5b:ab",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-0d6676b5-6fbc-4b51-bf29-1380cef97fcd",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a",
                "ip_address": "15.100.6.1",
                "subnet_name": "control-N4-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:29Z",
        "updated_at": "2022-08-04T10:57:32Z",
        "ips": "15.100.6.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-N4"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "4169299e-d680-4ae4-ada3-645fa068908a",
        "name": "lattice-n4",
        "network_id": "0d6676b5-6fbc-4b51-bf29-1380cef97fcd",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:fe:4d:de",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a",
                "ip_address": "15.100.6.101",
                "subnet_name": "control-N4-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:29Z",
        "updated_at": "2023-11-02T11:16:20Z",
        "ips": "15.100.6.101",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-N4"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "0d8bf7a4-e7ef-480e-8056-5aad9751691f",
        "name": "",
        "network_id": "0d6676b5-6fbc-4b51-bf29-1380cef97fcd",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:6f:c6:b7",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-0d6676b5-6fbc-4b51-bf29-1380cef97fcd",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a",
                "ip_address": "15.100.6.2",
                "subnet_name": "control-N4-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:30Z",
        "updated_at": "2022-08-04T10:57:32Z",
        "ips": "15.100.6.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "control-N4"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "a468a80e-633f-4652-b908-2ba2e5008d30",
        "name": "",
        "network_id": "bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:8b:39:88",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp8925cffa-c5bf-5be1-ac3d-17918b07ed38-bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "addec922-7181-4039-be79-4da3d88d2c0a",
                "ip_address": "15.100.7.1",
                "subnet_name": "data-N3-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:32Z",
        "updated_at": "2022-08-04T10:57:35Z",
        "ips": "15.100.7.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "data-N3"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "1c4dcd74-41cb-4e4b-a85d-52bcae5b7c05",
        "name": "lattice-n3",
        "network_id": "bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:70:4d:85",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "53e7b6fe-e33e-4d83-8936-ab8fe9b26d60",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "addec922-7181-4039-be79-4da3d88d2c0a",
                "ip_address": "15.100.7.101",
                "subnet_name": "data-N3-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:70:4d:85",
                "ip_address": "15.100.0.0/24"
            },
            {
                "mac_address": "fa:16:3e:70:4d:85",
                "ip_address": "15.100.7.0/24"
            },
            {
                "mac_address": "fa:16:3e:70:4d:85",
                "ip_address": "15.100.7.102"
            },
            {
                "mac_address": "fa:16:3e:70:4d:85",
                "ip_address": "15.100.7.103"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:18Z",
        "updated_at": "2023-11-02T11:16:22Z",
        "ips": "15.100.7.101",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "data-N3"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "fab47754-c286-4d7d-9208-12a1a5683a92",
        "name": "",
        "network_id": "bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:00:0b:d6",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "addec922-7181-4039-be79-4da3d88d2c0a",
                "ip_address": "15.100.7.2",
                "subnet_name": "data-N3-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:33Z",
        "updated_at": "2022-08-04T10:57:36Z",
        "ips": "15.100.7.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "data-N3"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "be95b80b-3648-46ec-ae51-4fe280ca76db",
        "name": "VPC-SI-mme-nic2",
        "network_id": "bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:7c:ff:47",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "a898461f-20f2-454f-82e9-3ff1905f399e",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "addec922-7181-4039-be79-4da3d88d2c0a",
                "ip_address": "15.100.7.41",
                "subnet_name": "data-N3-subnet"
            }
        ],
        "allowed_address_pairs": [
            {
                "mac_address": "fa:16:3e:7c:ff:47",
                "ip_address": "0.0.0.0/0"
            }
        ],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2023-11-17T18:26:59Z",
        "updated_at": "2023-11-17T18:27:38Z",
        "ips": "15.100.7.41",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "1d",
        "tenant_name": "smi5gc",
        "network_name": "data-N3"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "febe1821-2ce3-4ed8-b75a-a4a6e63a6cd4",
        "name": "",
        "network_id": "10885efc-c3cf-41cf-b5ec-264996f1d78c",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:1e:37:ac",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp54d8dde4-ad3c-5240-9345-0d1a33148699-10885efc-c3cf-41cf-b5ec-264996f1d78c",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "ba7cff90-beb1-4061-ba6c-5c223ed56586",
                "ip_address": "15.100.8.1",
                "subnet_name": "data-N6-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:35Z",
        "updated_at": "2022-08-04T10:57:38Z",
        "ips": "15.100.8.1",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "data-N6"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "94dc5816-8f48-4565-92ac-638ea45fd224",
        "name": "server-n6",
        "network_id": "10885efc-c3cf-41cf-b5ec-264996f1d78c",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:b4:94:eb",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "b56451ce-e214-4484-9f35-e656a95a8328",
        "device_owner": "compute:ALL",
        "fixed_ips": [
            {
                "subnet_id": "ba7cff90-beb1-4061-ba6c-5c223ed56586",
                "ip_address": "15.100.8.102",
                "subnet_name": "data-N6-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [
            "af18d38b-4d02-44c0-a2c2-66d1a37ee807"
        ],
        "port_security_enabled": true,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T11:19:10Z",
        "updated_at": "2022-08-04T11:20:27Z",
        "ips": "15.100.8.102",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "compute-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "\u2713",
        "statusT": "ACTIVE",
        "type": "Compute",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "data-N6"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "55c7a226-16a1-4fb4-9750-0b0a56937ef2",
        "name": "",
        "network_id": "10885efc-c3cf-41cf-b5ec-264996f1d78c",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "mac_address": "fa:16:3e:46:ab:b0",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "dhcp1da37a13-ca17-5ddf-aa68-adb99a981d73-10885efc-c3cf-41cf-b5ec-264996f1d78c",
        "device_owner": "network:dhcp",
        "fixed_ips": [
            {
                "subnet_id": "ba7cff90-beb1-4061-ba6c-5c223ed56586",
                "ip_address": "15.100.8.2",
                "subnet_name": "data-N6-subnet"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T10:57:36Z",
        "updated_at": "2022-08-04T10:57:38Z",
        "ips": "15.100.8.2",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "DHCP",
        "age": "472d",
        "tenant_name": "smi5gc",
        "network_name": "data-N6"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "8cdf2e22-e6bc-438c-a084-08fa17b219eb",
        "name": "HA port tenant 05b8e996f0654e4491d2e925a91c6250",
        "network_id": "68a6f31c-a4a1-4990-8654-3d00c6e9115e",
        "tenant_id": "",
        "mac_address": "fa:16:3e:10:57:8d",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "device_owner": "network:router_ha_interface",
        "fixed_ips": [
            {
                "subnet_id": "e122cda4-5250-467e-ba83-1e4fcfeb0b1b",
                "ip_address": "169.254.192.170",
                "subnet_name": "HA subnet tenant 05b8e996f0654e4491d2e925a91c6250"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T13:38:51Z",
        "updated_at": "2023-07-05T17:17:05Z",
        "ips": "169.254.192.170",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-3",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "HA",
        "age": "472d",
        "tenant_name": null,
        "network_name": "HA network tenant 05b8e996f0654e4491d2e925a91c6250"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "d738d124-4800-43a4-a062-bef2eef3409e",
        "name": "HA port tenant 05b8e996f0654e4491d2e925a91c6250",
        "network_id": "68a6f31c-a4a1-4990-8654-3d00c6e9115e",
        "tenant_id": "",
        "mac_address": "fa:16:3e:c4:3b:0f",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "device_owner": "network:router_ha_interface",
        "fixed_ips": [
            {
                "subnet_id": "e122cda4-5250-467e-ba83-1e4fcfeb0b1b",
                "ip_address": "169.254.192.5",
                "subnet_name": "HA subnet tenant 05b8e996f0654e4491d2e925a91c6250"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T13:38:52Z",
        "updated_at": "2023-07-05T17:20:53Z",
        "ips": "169.254.192.5",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-1",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "HA",
        "age": "472d",
        "tenant_name": null,
        "network_name": "HA network tenant 05b8e996f0654e4491d2e925a91c6250"
    },
    {
        "__Output": {
            "adminTick": "Green",
            "statusT": "Green"
        },
        "id": "b9a38003-6372-4232-8027-f045535b4b94",
        "name": "HA port tenant 05b8e996f0654e4491d2e925a91c6250",
        "network_id": "68a6f31c-a4a1-4990-8654-3d00c6e9115e",
        "tenant_id": "",
        "mac_address": "fa:16:3e:c2:ed:bb",
        "admin_state_up": true,
        "status": "ACTIVE",
        "device_id": "424d1cba-254f-47af-9b42-a05465be1d97",
        "device_owner": "network:router_ha_interface",
        "fixed_ips": [
            {
                "subnet_id": "e122cda4-5250-467e-ba83-1e4fcfeb0b1b",
                "ip_address": "169.254.193.193",
                "subnet_name": "HA subnet tenant 05b8e996f0654e4491d2e925a91c6250"
            }
        ],
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "security_groups": [],
        "port_security_enabled": false,
        "propagate_uplink_status": true,
        "tags": [],
        "created_at": "2022-08-04T13:38:52Z",
        "updated_at": "2023-07-05T17:19:39Z",
        "ips": "169.254.193.193",
        "binding_vnic_type": "normal",
        "binding_profile": {},
        "binding_host_id": "AIO-server-2",
        "binding_vif_type": "ovs",
        "binding_vif_details": {
            "connectivity": "l2",
            "port_filter": true,
            "ovs_hybrid_plug": false,
            "datapath_type": "system",
            "bridge_name": "br-int"
        },
        "adminTick": "\u2713",
        "port_security_enabledTick": "",
        "statusT": "ACTIVE",
        "type": "HA",
        "age": "472d",
        "tenant_name": null,
        "network_name": "HA network tenant 05b8e996f0654e4491d2e925a91c6250"
    }
]
```

Developer

```
# iserver get osp port --cluster pod1 -o json

{
    "duration": 4343,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 4187,
        "total_time": 4187
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

2023-11-19 14:45:17.199923	True	2789	get	ports
2023-11-19 14:45:17.581069	True	349	get	tenants
2023-11-19 14:45:18.247032	True	657	get	networks
2023-11-19 14:45:18.650690	True	392	get	subnets
```

[[Back]](./PortGet.md)