# Fabric

## Problem statement

When OpenShift cluster is defined and installed, there are several definitions that assume desired network state such as:
- bonding
- vlan encapsulation
- IP address
- default gateway
- ntp and dns servers reachability
- internet reachability

The network fabric must be aligned with OpenShift cluster configuration, otherwise installation or operations should fail.

## Overview

iserver supports three different fabric workflows i.e. check, create, delete; triggered with 'iserver create ocp bm' and 'iserver delete ocp bm' commands.

Fabric Type | Data Model | Check | Create | Delete
--- | ---| --- | --- | ---
ACI | [Link](./fabric_aci_data_model.md) | [Link](./fabric_aci_check.md) | [Link](./fabric_aci_create.md) | [Link](./fabric_aci_delete.md)
NDFC | --- | --- | --- | ---
IOS-XR | --- | --- | --- | ---

## fabric.json

All workflows act upon the same single fabric.json file
- common structure
- different mandatory vs. optional requirements depending on the workflow
- fabric.json for create/delete workflows are same and contain complete fabric configuration information
- fabric.json for check workflow may have subset of information provided in create/delete workflows

Complete fabric.json can be used in check workflow. The more information is provided, the more complete checks are.

```
{
    "controller": [...],
    "server": [...]
}
```

Controller
- defines the desired network configuration e.g. policies
- controller type dependant
- every defined controller configuration is annotated with 'domain' attribute

Server
- defines servers' interfaces connectivity to the fabric (device/interface), bonding and vlan encapsulation
- 'domain' value per interface attaches the interface to the fabric configuration at controller level
- server definition is controller type independent

### Template 1

```
{
    "controller": [
        {
            "type": "<controller-type>"
            "apic": "<connector-name>",
            "domain": "<domain-name>",
            ...
        }
    ],
    "server": [
        {
            "hostname": "<hostname>",
            "interface": [
                {
                    "domain": "<domain-name>",
                    ...
                }
            ]
        }
    ]
}
```

### Template 2

```
{
    "controller": [
        {
            "type": "<controller-type1>"
            "apic": "<connector-name1>",
            "domain": "<domain-name1>",
            ...
        },
        {
            "type": "<controller-type2>"
            "apic": "<connector-name2>",
            "domain": "<domain-name2>",
            ...
        }
    ],
    "server": [
        {
            "hostname": "<hostname>",
            "interface": [
                {
                    "domain": "<domain-name1>",
                    ...
                },
                {
                    "domain": "<domain-name1>",
                    ...
                },
                {
                    "domain": "<domain-name2>",
                    ...
                },
                {
                    "domain": "<domain-name2>",
                    ...
                }
                ]
        }
    ]
}
```

[Back](../BareMetalCluster.md)
