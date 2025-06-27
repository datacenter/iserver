# ACI Fabric - Create workflow

The create workflow is launched with 'iserver create ocp cluster bm --dir [directory-name] --fabric patch' command as long as fabric.json file is in defined directory.

## Overview

iserver can fully configure ACI fabric for OpenShift bare metal cluster connectivity based on definitions (intent) in fabric.json file.

The only pre-requirement for ACI fabric is the configuration of:
- Tenant
- VRF
- L3Out

Two deployment models are supported:
- epg/bd (for non-bgp case)

![AciEpgConfigurationSummary](../images/aci_configuration_epg_summary.png)

- l3out w/external-epg (for bgp case)

![AciL3outConfigurationSummary](../images/aci_configuration_l3out_summary.png)

Objects creation rules ([data model](./fabric_aci_data_model.md)):
- object name generated based on controller.tenant, controller.domain and controller.mo_name user-provided values
- object names can be explictly defined
- object managed i.e. created and if already exists then updated
- object marked as unmanaged is not created/updated and it must exist
- object marked as disabled is not create/update/checked
- object properties can be changed by used-provided values

## Example EPG/BD

### Environment

- Single Node OpenShift (SNO) cluster with bonded interface over VLAN encapsulation.
- All ACI objects managed with generated name and default properties
- No ACI objects pre-exist besides tenant, vrf and l3out as defined in user-input

### fabric.json

```
{
    "controller": [
        {
            "type": "aci",
            "apic": "myapic",
            "domain": "main",
            "mo_name": "bm2",
            "tenant": "k8s",
            "l3out": "MyL3out",
            "vrf": "MyVrf"
        }
    ],
    "server": [
        {
            "hostname": "bm2",
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

### Workflow

Steps
- input data validation and expansion
- tenant, vrf and l3out checks
- create objects using generated names and built-in defaults

Objects
- vlan pool
- physical domain associated with vlan pool
- attachable access entity profile assisted with physical domain
- interface policy cdp, lldp, link level, l2 and port channel
- vpc policy group with policies and aaep relationships
- vpc policy group applied on server interfaces
- bridge domain with l3 configuration, vrf and l3out configurations from user input
- application profile
- epg in application profile with physical domain, static ports and bridge domain relationships

See [here](./fabric_aci_example_sno_vpc_epg.md) an example of single node openshift setup with vpc access interface.

## Example L3Out

### Environment

- Single Node OpenShift (SNO) cluster with bonded interface over VLAN encapsulation.
- All ACI objects managed with generated name and default properties
- No ACI objects pre-exist besides tenant, vrf and l3out as defined in user-input
- BGP-ready configuration for peering between kubernetes nodes and ACI leaves

### fabric.json

```
{
    "controller": [
        {
            "type": "aci",
            "apic": "myapic",
            "domain": "main",
            "mo_name": "bm2",
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
            "hostname": "bm2",
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

### Workflow

Steps
- input data validation and expansion
- tenant, vrf and l3out checks
- create objects using generated names and built-in defaults

Objects
- vlan pool
- physical domain associated with vlan pool
- l3 domain associated with vlan pool
- attachable access entity profile assisted with physical domain
- interface policy cdp, lldp, link level, l2 and port channel
- vpc policy group with policies and aaep relationships
- vpc policy group applied on server interfaces
- l3out with logical interface profile selecing server interface
- external EPG with machine network subnet

See [here](./fabric_aci_example_sno_vpc_l3out.md) an example of single node openshift setup with vpc access interface for bgp-ready configuration.

[Back](./input_data_fabric.md)