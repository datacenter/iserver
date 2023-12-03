# Subnet

## Default output

```
# iserver get osp sub --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {},
        "id": "14b5c631-8d81-46b9-b3d9-abbb4acc0191",
        "name": "management-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "fe1e3247-64b8-45ae-aa40-468a9a768954",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": "15.100.1.254",
        "cidr": "15.100.1.0/24",
        "allocation_pools": [
            {
                "start": "15.100.1.1",
                "end": "15.100.1.253"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [
            "144.254.71.184"
        ],
        "created_at": "2022-08-04T10:57:11Z",
        "updated_at": "2022-08-19T10:28:42Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "458d",
        "tenant_name": "smi5gc",
        "network_name": "management"
    },
    {
        "__Output": {},
        "id": "1786aa38-3ab1-4a86-9966-f4dae5411bab",
        "name": "control-N2-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.5.0/24",
        "allocation_pools": [
            {
                "start": "15.100.5.1",
                "end": "15.100.5.253"
            }
        ],
        "host_routes": [
            {
                "destination": "15.100.0.194/32",
                "nexthop": "15.100.5.254"
            }
        ],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:24Z",
        "updated_at": "2022-08-23T14:11:46Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "454d",
        "tenant_name": "smi5gc",
        "network_name": "control-N2"
    },
    {
        "__Output": {},
        "id": "195953ed-add3-4c59-b81a-ee372dcd7838",
        "name": "sriov0-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "7fa67775-1f5f-4dca-baaa-15ea5b55c4e2",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.105.0/24",
        "allocation_pools": [
            {
                "start": "15.100.105.1",
                "end": "15.100.105.253"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:38Z",
        "updated_at": "2022-08-04T10:57:38Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "473d",
        "tenant_name": "smi5gc",
        "network_name": "sriov0"
    },
    {
        "__Output": {},
        "id": "1cbf95c8-b46c-4684-92da-7199481236c3",
        "name": "sriov1-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "cd63e7ec-39b2-4f47-9f46-df5d3e25c967",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.106.0/24",
        "allocation_pools": [
            {
                "start": "15.100.106.1",
                "end": "15.100.106.253"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:41Z",
        "updated_at": "2022-08-04T10:57:41Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "473d",
        "tenant_name": "smi5gc",
        "network_name": "sriov1"
    },
    {
        "__Output": {},
        "id": "379bd679-fea7-4aa6-b8c3-0368ab2790a9",
        "name": "subnet-ext",
        "tenant_id": "2cced286b74c45ea95c83cc2e5d3b413",
        "network_id": "e7474314-438a-43f6-9ddf-319f0578ca30",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": false,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": "10.58.28.94",
        "cidr": "10.58.28.80/28",
        "allocation_pools": [
            {
                "start": "10.58.28.81",
                "end": "10.58.28.93"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [
            "144.254.71.184"
        ],
        "created_at": "2022-08-03T15:49:56Z",
        "updated_at": "2022-08-03T15:49:56Z",
        "dhcpTick": "\u2717",
        "created_age": "474d",
        "updated_age": "474d",
        "tenant_name": "admin",
        "network_name": "external"
    },
    {
        "__Output": {},
        "id": "3ab58791-ba30-45a9-b185-d9f3809f2556",
        "name": "orchestration-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "3065667d-94c9-442c-87c1-bec9cffa0d50",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.2.0/24",
        "allocation_pools": [
            {
                "start": "15.100.2.1",
                "end": "15.100.2.253"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:14Z",
        "updated_at": "2022-08-04T10:57:14Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "473d",
        "tenant_name": "smi5gc",
        "network_name": "orchestration"
    },
    {
        "__Output": {},
        "id": "4299410e-e562-46d6-93b0-d839669a5bca",
        "name": "control-k8s-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "a4fe3f25-a010-4cad-a945-0e36256b3783",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.3.0/24",
        "allocation_pools": [
            {
                "start": "15.100.3.1",
                "end": "15.100.3.253"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:17Z",
        "updated_at": "2022-08-04T10:57:17Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "473d",
        "tenant_name": "smi5gc",
        "network_name": "control-k8s"
    },
    {
        "__Output": {},
        "id": "4f59eb25-f662-490a-8e08-c427478857c1",
        "name": "di-internal1-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "4510e325-db2f-48ce-8e93-c1dcd6065825",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": false,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "172.16.0.0/18",
        "allocation_pools": [
            {
                "start": "172.16.0.1",
                "end": "172.16.63.254"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [],
        "created_at": "2022-08-19T09:10:37Z",
        "updated_at": "2022-08-19T16:42:27Z",
        "dhcpTick": "\u2717",
        "created_age": "458d",
        "updated_age": "458d",
        "tenant_name": "smi5gc",
        "network_name": "di-internal1"
    },
    {
        "__Output": {},
        "id": "84b1de29-b4be-4508-8ad9-6c68c930dac5",
        "name": "control-SBI-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "02c949a8-1b9c-4162-a8ad-f8941a8f37d1",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.4.0/24",
        "allocation_pools": [
            {
                "start": "15.100.4.1",
                "end": "15.100.4.253"
            }
        ],
        "host_routes": [
            {
                "destination": "15.100.100.0/24",
                "nexthop": "15.100.4.254"
            },
            {
                "destination": "15.254.101.8/32",
                "nexthop": "15.100.4.254"
            },
            {
                "destination": "15.254.101.9/32",
                "nexthop": "15.100.4.254"
            }
        ],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:21Z",
        "updated_at": "2022-08-23T14:45:10Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "454d",
        "tenant_name": "smi5gc",
        "network_name": "control-SBI"
    },
    {
        "__Output": {},
        "id": "ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a",
        "name": "control-N4-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "0d6676b5-6fbc-4b51-bf29-1380cef97fcd",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.6.0/24",
        "allocation_pools": [
            {
                "start": "15.100.6.1",
                "end": "15.100.6.253"
            }
        ],
        "host_routes": [
            {
                "destination": "15.100.0.10/32",
                "nexthop": "15.100.6.254"
            },
            {
                "destination": "15.100.0.18/32",
                "nexthop": "15.100.6.254"
            },
            {
                "destination": "15.100.0.2/32",
                "nexthop": "15.100.6.254"
            },
            {
                "destination": "15.100.0.34/32",
                "nexthop": "15.100.6.254"
            },
            {
                "destination": "15.100.0.42/32",
                "nexthop": "15.100.6.254"
            }
        ],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:28Z",
        "updated_at": "2022-08-23T14:10:56Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "454d",
        "tenant_name": "smi5gc",
        "network_name": "control-N4"
    },
    {
        "__Output": {},
        "id": "addec922-7181-4039-be79-4da3d88d2c0a",
        "name": "data-N3-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "bb3bf0cd-6361-4d79-8764-92eaa9de7880",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.7.0/24",
        "allocation_pools": [
            {
                "start": "15.100.7.1",
                "end": "15.100.7.253"
            }
        ],
        "host_routes": [
            {
                "destination": "15.100.0.1/32",
                "nexthop": "15.100.7.254"
            },
            {
                "destination": "15.100.0.17/32",
                "nexthop": "15.100.7.254"
            },
            {
                "destination": "15.100.0.214/32",
                "nexthop": "15.100.7.254"
            },
            {
                "destination": "15.100.0.215/32",
                "nexthop": "15.100.7.254"
            },
            {
                "destination": "15.100.0.216/32",
                "nexthop": "15.100.7.254"
            },
            {
                "destination": "15.100.0.9/32",
                "nexthop": "15.100.7.254"
            }
        ],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:31Z",
        "updated_at": "2022-08-19T13:26:36Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "458d",
        "tenant_name": "smi5gc",
        "network_name": "data-N3"
    },
    {
        "__Output": {},
        "id": "afd52863-ee94-4880-80be-fc6fd7788f6e",
        "name": "C8KV_ORANGE_LAN01",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "network_id": "15c99bd1-25e1-445b-8c97-daf8eb5c66f2",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": "10.0.21.1",
        "cidr": "10.0.21.0/24",
        "allocation_pools": [
            {
                "start": "10.0.21.5",
                "end": "10.0.21.100"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [
            "8.8.8.8"
        ],
        "created_at": "2023-10-24T08:09:27Z",
        "updated_at": "2023-10-24T08:09:27Z",
        "dhcpTick": "\u2713",
        "created_age": "27d",
        "updated_age": "27d",
        "tenant_name": "ialonso",
        "network_name": "C8KV_ORANGE_LAN01"
    },
    {
        "__Output": {},
        "id": "ba7cff90-beb1-4061-ba6c-5c223ed56586",
        "name": "data-N6-subnet",
        "tenant_id": "05b8e996f0654e4491d2e925a91c6250",
        "network_id": "10885efc-c3cf-41cf-b5ec-264996f1d78c",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "15.100.8.0/24",
        "allocation_pools": [
            {
                "start": "15.100.8.1",
                "end": "15.100.8.253"
            }
        ],
        "host_routes": [
            {
                "destination": "100.64.0.0/10",
                "nexthop": "15.100.8.254"
            },
            {
                "destination": "15.100.0.11/32",
                "nexthop": "15.100.8.254"
            },
            {
                "destination": "15.100.0.19/32",
                "nexthop": "15.100.8.254"
            },
            {
                "destination": "15.100.0.3/32",
                "nexthop": "15.100.8.254"
            },
            {
                "destination": "192.168.0.0/16",
                "nexthop": "15.100.8.254"
            }
        ],
        "dns_nameservers": [],
        "created_at": "2022-08-04T10:57:34Z",
        "updated_at": "2022-08-19T08:52:36Z",
        "dhcpTick": "\u2713",
        "created_age": "473d",
        "updated_age": "458d",
        "tenant_name": "smi5gc",
        "network_name": "data-N6"
    },
    {
        "__Output": {},
        "id": "db2b80bf-65d0-4836-9eb3-929eefb8fff0",
        "name": "C8KV01_LAN01",
        "tenant_id": "9b50a8dba82f4c14802c4554482882b8",
        "network_id": "d6a76040-e0f7-47d2-a4b8-542e896cc2ec",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": true,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": "10.0.11.1",
        "cidr": "10.0.11.0/24",
        "allocation_pools": [
            {
                "start": "10.0.11.5",
                "end": "10.0.11.100"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [
            "8.8.8.8"
        ],
        "created_at": "2023-10-16T15:30:04Z",
        "updated_at": "2023-10-16T15:30:04Z",
        "dhcpTick": "\u2713",
        "created_age": "35d",
        "updated_age": "35d",
        "tenant_name": "ialonso",
        "network_name": "C8KV01_LAN01"
    },
    {
        "__Output": {},
        "id": "e122cda4-5250-467e-ba83-1e4fcfeb0b1b",
        "name": "HA subnet tenant 05b8e996f0654e4491d2e925a91c6250",
        "tenant_id": "",
        "network_id": "68a6f31c-a4a1-4990-8654-3d00c6e9115e",
        "ip_version": 4,
        "subnetpool_id": null,
        "enable_dhcp": false,
        "ipv6_ra_mode": null,
        "ipv6_address_mode": null,
        "gateway_ip": null,
        "cidr": "169.254.192.0/18",
        "allocation_pools": [
            {
                "start": "169.254.192.1",
                "end": "169.254.255.254"
            }
        ],
        "host_routes": [],
        "dns_nameservers": [],
        "created_at": "2022-08-04T13:38:50Z",
        "updated_at": "2022-08-04T13:38:50Z",
        "dhcpTick": "\u2717",
        "created_age": "473d",
        "updated_age": "473d",
        "tenant_name": null,
        "network_name": "HA network tenant 05b8e996f0654e4491d2e925a91c6250"
    }
]
```

Developer

```
# iserver get osp sub --cluster pod1 -o json

{
    "duration": 2569,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 2353,
        "total_time": 2353
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

2023-11-20 18:11:17.236844	True	1421	get	subnets
2023-11-20 18:11:17.688645	True	391	get	tenants
2023-11-20 18:11:18.239314	True	541	get	networks
```

[[Back]](./SubnetGet.md)