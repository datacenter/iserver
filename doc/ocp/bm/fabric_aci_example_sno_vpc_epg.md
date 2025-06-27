# ACI Fabric - Create workflow

![AciEpgConfigurationSummary](../images/aci_configuration_epg_summary.png)

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
            "vrf": "MyVrf"
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
    "controller": [
        {
            "type": "aci",
            "apic": "myapic",
            "domain": "main",
            "mo_name": "bm1",
            "tenant": "k8s",
            "l3out": "MyL3out",
            "vrf": "MyVrf"
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
            "ap": {
                "managed": true,
                "enabled": true,
                "shared": false,
                "name": "bm1"
            },
            "epg": {
                "managed": true,
                "enabled": true,
                "shared": false,
                "name": "k8s/bm1/main"
            },
            "bd": {
                "managed": true,
                "enabled": true,
                "shared": false,
                "name": "bm1-main",
                "gateway": "10.4.4.15/28"
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
            "port_channel": {
                "managed": true,
                "enabled": true,
                "shared": false,
                "name": "k8s-bm1-main",
                "mode": "on",
                "min": 1,
                "max": 16,
                "lb": "static",
                "suspend": true,
                "graceful": true,
                "fast": true,
                "symmetric": false,
                "hash": null
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
                    "port": "1/1/1",
                    "pod": "1"
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
                    "port": "1/1/1",
                    "pod": "1"
                }
            ]
        }
    ]
}
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

### Step: Attachable Access Entity Profile

- create attachable access entity profile with 'k8s-bm1-main' name
- associate aaep with physical domain 'k8s-bm1-main'

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

### Step: Bridge Domain

- create bridge domain with 'bm1-main' name in tenant 'k8s'
- L3 gateway 10.4.4.15/28
- vrf 'MyVrf'
- l3out 'MyL3out'

Reference: [data model](./fabric_aci_data_model_bridge_domain.md)

### Step: Application Profile

- create application profile 'bm1' in tenant 'k8s'

Reference: [data model](./fabric_aci_data_model_application_profile.md)

### Step: EPG

- create epg 'main' in application profile 'bm1' and tenant 'k8s'
- associate epg with bridge domain 'k8s/bm1-main'
- associate epg with physical domain 'k8s-bm1-main'
- add static port to vpc policy group 'k8s-bm1-main' with vlan-666 encapsulation

Reference: [data model](./fabric_aci_data_model_epg.md)

[Back](./fabric_aci_create.md)