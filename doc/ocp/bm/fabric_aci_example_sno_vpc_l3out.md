# ACI Fabric - Create workflow

![AciEpgConfigurationSummary](../images/aci_configuration_l3out_summary.png)

## Input Data

```
{
    "controller": [
        {
            "type": "aci",
            "apic": "myapic",
            "domain": "main",
            "mo_name": "bm1",
            "tenant": "k8s",
            "l3out": "MyL3out",
            "vrf": "MyVrf",
            "bgp": {
                "leaf_A": {
                    "id": "100",
                    "ip": "10.4.4.13",
                    "loopback": "100.100.100.100"
                },
                "leaf_B": {
                    "id": "200",
                    "ip": "10.4.4.14",
                    "loopback": "200.200.200.200"
                },
                "asn": "64666"
            }
        }
    ],
    "server": [
        {
            "hostname": "bm1",
            "interface": [
                {
                    "domain": "main",
                    "ip": "10.4.4.1",
                    "gateway": "10.4.4.15/28",
                    "mac": "aa:aa:aa:aa:aa:aa",
                    "bond": true,
                    "trunk": true,
                    "vlan": 666,
                    "node": "100",
                    "port": "1/1/1"
                },
                {
                    "domain": "main",
                    "ip": "10.4.4.1",
                    "gateway": "10.4.4.15/28",
                    "mac": "bb:bb:bb:bb:bb:bb",
                    "bond": true,
                    "trunk": true,
                    "vlan": 666,
                    "node": "200",
                    "port": "1/1/1"
                }
            ]
        }
    ]
}
```

## Validated and Expanded Data

```
{
    "type": "aci",
    "apic": "myapic",
    "domain": "main",
    "mo_name": "bm1",
    "tenant": "k8s",
    "l3out": "MyL3out",
    "vrf": "MyVrf",
    "port_channel": {
        "mode": "active",
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "min": 1,
        "max": 16,
        "lb": "static",
        "suspend": true,
        "graceful": true,
        "fast": true,
        "symmetric": false,
        "hash": null
    },
    "bgp": {
        "leaf_A": {
            "id": "100",
            "ip": "10.4.4.13",
            "loopback": "100.100.100.100",
            "cidr": "10.4.4.0/28",
            "pod": "1"
        },
        "leaf_B": {
            "id": "200",
            "ip": "10.4.4.13",
            "loopback": "200.200.200.200",
            "cidr": "10.4.4.13/28",
            "pod": "1"
        },
        "asn": 64666,
        "enabled": true,
        "managed": true,
        "shared": false,
        "name": "bm1",
        "type": "svi",
        "gateway": "10.4.4.15/28",
        "ttl": 5,
        "l3out": {
            "name": "bm1"
        },
        "epg": {
            "name": "bm1",
            "subnet": [
                {
                    "ip": "10.58.24.96/28",
                    "scope": [
                        "import-security"
                    ]
                }
            ]
        },
        "lnp": {
            "name": "100_200",
            "lip": "bm1"
        }
    },
    "ap": {
        "enabled": false
    },
    "epg": {
        "enabled": false
    },
    "bd": {
        "enabled": false,
        "gateway": "10.4.4.15/28"
    },
    "vlan_pool": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "vlan": "666",
        "mode": "static"
    },
    "physical_domain": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main"
    },
    "aaep": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main"
    },
    "policy_group": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "type": "vpc",
        "encap": "vlan-666",
        "immediacy": "immediate"
    },
    "l3_domain": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main"
    },
    "cdp": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "cdp_enabled": true
    },
    "lldp": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "lldp_receive": true,
        "lldp_transmit": true
    },
    "link_level": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "auto": "on",
        "media": "auto",
        "debounce": 100,
        "delay": 0,
        "emi": false
    },
    "l2": {
        "managed": true,
        "enabled": true,
        "shared": false,
        "name": "k8s-bm1-main",
        "qinq": "disabled",
        "relay": false,
        "vlan": "local"
    },
    "l3out_tenant": "common",
    "external_epg": "MyL3out_ExtEPG"
}

Validated and resolved servers connectivity layout
[
    {
        "hostname": "bm1",
        "interface": [
            {
                "domain": "main",
                "ip": "10.4.4.1",
                "gateway": "10.4.4.15/28",
                "mac": "aa:aa:aa:aa:aa:aa",
                "bond": true,
                "trunk": true,
                "vlan": "666",
                "node": "100",
                "port": "1/1/1",
                "mtu": "1500",
                "pod": "1"
            },
            {
                "domain": "main",
                "ip": "10.4.4.1",
                "gateway": "10.4.4.15/28",
                "mac": "bb:bb:bb:bb:bb:bb",
                "bond": true,
                "trunk": true,
                "vlan": "666",
                "node": "200",
                "port": "1/1/1",
                "mtu": "1500",
                "pod": "1"
            }
        ]
    }
]
```

## Create Workflow

### Step: Checks

- tenant 'k8s' must exist
- vrf 'MyVrf' must exist in tenant 'k8s' or tenant 'common'
- vrf 'MyL3out' must exist in tenant 'k8s' or tenant 'common'

### Step: VLAN Pool

- create VLAN pool with 'k8s-bm1-main' name
- type 'static'
- member vlan: 666

Reference: [data model](./fabric_aci_data_model_vlan_pool.md)

### Step: Physical Domain

- create physical domain with 'k8s-bm1-main' name
- associate physical domain with VLAN pool 'k8s-bm1-main'

Reference: [data model](./fabric_aci_data_model_physical_domain.md)

### Step: L3 Domain

- create l3 domain with 'k8s-bm1-main' name
- associate l3 domain with VLAN pool 'k8s-bm1-main'

Reference: [data model](./fabric_aci_data_model_physical_domain.md)

### Step: Attachable Access Entity Profile

- create attachable access entity profile with 'k8s-bm1-main' name
- associate aaep with physical domain 'k8s-bm1-main'
- associate aaep with l3 domain 'k8s-bm1-main'

Reference: [data model](./fabric_aci_data_model_aaep.md)

### Step: Interface Policy CDP

- create interface policy cdp with 'k8s-bm1-main' name
- cdp enabled

Reference: [data model](./fabric_aci_data_model_cdp.md)

### Step: Interface Policy LLDP

- create interface policy lldp with 'k8s-bm1-main' name
- lldp enabled in receive and transmit directions

Reference: [data model](./fabric_aci_data_model_lldp.md)

### Step: Interface Policy Link Level

- create interface policy link level with 'k8s-bm1-main' name
- auto-negotiation enabled

Reference: [data model](./fabric_aci_data_model_link_level.md)

### Step: Interface Policy L2

- create interface policy l2 with 'k8s-bm1-main' name
- vlan local scope

Reference: [data model](./fabric_aci_data_model_l2.md)

### Step: Interface Policy Port Channel

- create interface policy port channel with 'k8s-bm1-main' name
- mode: static channel - mode on

Reference: [data model](./fabric_aci_data_model_port_channel.md)

### Step: Policy Group

In this example single vpc policy group is created
- name k8s-bm1-main
- associated with aaep 'k8s-bm1-main'
- includes all policies created in previous steps

Reference: [data model](./fabric_aci_data_model_policy_group.md)

### Step: Access Interface Configuration

- configure policy group on every server interface in the domain

```
Policy Group on access interface [bm1]
        Policy [k8s-bm1-main]
        - not configured on any interface
        Checking interface pod [1] node [100] interface [1/1/1]
        - no configuration
        - policy [k8s-bm1-main] configured on interface
        Checking interface pod [1] node [200] interface [1/1/1]
        - no configuration
        - policy [k8s-bm1-main] configured on interface
```

### Step: L3out

- create l3out

Reference: [data model](./fabric_aci_data_model_bgp.md)

### Step: External EPG

- add subnet to L3Out external epg

Reference: [data model](./fabric_aci_data_model_external_epg.md)

[Back](./fabric_aci_create.md)