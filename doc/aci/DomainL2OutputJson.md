# L2 Domain

## JSON output

```
# iserver get aci domain l2 --apic apic21 -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l2dom-Infra_L2dom",
        "name": "Infra_L2dom",
        "aaep_names": [
            "Infra_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-Infra_AAEP",
                "type": "AAEP",
                "name": "Infra_AAEP"
            },
            {
                "tCl": "l2extOut",
                "tDn": "uni/tn-k8s/l2out-Test",
                "type": "L2 Out",
                "name": "k8s/Test"
            }
        ],
        "vlan": "Infra_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "static",
            "descr": "",
            "dn": "uni/infra/vlanns-[Infra_VlanPool]-static",
            "name": "Infra_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-1",
                    "name": "blk1",
                    "rn": "from-[vlan-1]-to-[vlan-1000]",
                    "role": "external",
                    "to": "vlan-1000",
                    "fromVlan": "1",
                    "toVlan": "1000",
                    "blockInfo": "[1-1000] (static)"
                }
            ],
            "vlanCount": 1000,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l2extDomP",
                    "tDn": "uni/l2dom-Infra_L2dom",
                    "domainName": "Infra_L2dom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-Infra_L3Dom",
                    "domainName": "Infra_L3Dom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-Infra_PhysDom",
                    "domainName": "Infra_PhysDom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-L3_Domain_vsfo",
                    "domainName": "L3_Domain_vsfo"
                }
            ]
        },
        "vlan_block": [
            "1-1000"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l2dom-test",
        "name": "test",
        "aaep_names": [
            "nidemo"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-nidemo",
                "type": "AAEP",
                "name": "nidemo"
            }
        ],
        "vlan": "nidemo-3000-3001",
        "aaaDomain": [
            "UCSB1_SecDom"
        ],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "static",
            "descr": "VANNIEW temporary demo feel free to destroy",
            "dn": "uni/infra/vlanns-[nidemo-3000-3001]-static",
            "name": "nidemo-3000-3001",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "VANNIEW temporary demo feel free to destroy",
                    "dn": null,
                    "from": "vlan-3000",
                    "name": "",
                    "rn": "from-[vlan-3000]-to-[vlan-3001]",
                    "role": "external",
                    "to": "vlan-3001",
                    "fromVlan": "3000",
                    "toVlan": "3001",
                    "blockInfo": "[3000-3001] (static)"
                }
            ],
            "vlanCount": 2,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-nidemo",
                    "domainName": "nidemo"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l2extDomP",
                    "tDn": "uni/l2dom-test",
                    "domainName": "test"
                }
            ]
        },
        "vlan_block": [
            "3000-3001"
        ]
    }
]
```

[[Back]](./DomainL2.md)