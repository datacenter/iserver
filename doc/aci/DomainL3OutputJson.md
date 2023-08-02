# L3 Domain

## JSON output

```
# iserver get aci domain l3 --apic apic21 -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l3dom-Infra_L3Dom",
        "name": "Infra_L3Dom",
        "aaep_names": [
            "TEST-AAP",
            "Infra_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-TEST-AAP",
                "type": "AAEP",
                "name": "TEST-AAP"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-Infra_AAEP",
                "type": "AAEP",
                "name": "Infra_AAEP"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-mgmt/out-INB_L3out",
                "type": "L3 Out",
                "name": "mgmt/INB_L3out"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-common/out-Infra_privIP_L3out",
                "type": "L3 Out",
                "name": "common/Infra_privIP_L3out"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-Ericsson_PACO/out-DUMMY",
                "type": "L3 Out",
                "name": "Ericsson_PACO/DUMMY"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-k8s/out-vl3_k8s",
                "type": "L3 Out",
                "name": "k8s/vl3_k8s"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-vEPC/out-vSFO_L3out",
                "type": "L3 Out",
                "name": "vEPC/vSFO_L3out"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-k8s/out-bml3_k8s",
                "type": "L3 Out",
                "name": "k8s/bml3_k8s"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-common/out-Infra_L3out",
                "type": "L3 Out",
                "name": "common/Infra_L3out"
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
        "dn": "uni/l3dom-k8s_phys_L3Dom",
        "name": "k8s_phys_L3Dom",
        "aaep_names": [
            "k8s_phys_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-k8s_phys_AAEP",
                "type": "AAEP",
                "name": "k8s_phys_AAEP"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-Ericsson_PACO/out-RAN",
                "type": "L3 Out",
                "name": "Ericsson_PACO/RAN"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-Ericsson_PACO/out-PDN",
                "type": "L3 Out",
                "name": "Ericsson_PACO/PDN"
            }
        ],
        "vlan": "k8s_phys_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "static",
            "descr": "Managed by Terraform",
            "dn": "uni/infra/vlanns-[k8s_phys_VlanPool]-static",
            "name": "k8s_phys_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "Managed by Terraform",
                    "dn": null,
                    "from": "vlan-800",
                    "name": "",
                    "rn": "from-[vlan-800]-to-[vlan-809]",
                    "role": "external",
                    "to": "vlan-809",
                    "fromVlan": "800",
                    "toVlan": "809",
                    "blockInfo": "[800-809] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "Used for Ericsson 5GC. Manual config.",
                    "dn": null,
                    "from": "vlan-810",
                    "name": "",
                    "rn": "from-[vlan-810]-to-[vlan-813]",
                    "role": "external",
                    "to": "vlan-813",
                    "fromVlan": "810",
                    "toVlan": "813",
                    "blockInfo": "[810-813] (static)"
                }
            ],
            "vlanCount": 14,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-k8s_phys_L3Dom",
                    "domainName": "k8s_phys_L3Dom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-k8s_phys_PhysDom",
                    "domainName": "k8s_phys_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "800-809",
            "810-813"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l3dom-L3_Domain_vsfo",
        "name": "L3_Domain_vsfo",
        "aaep_names": [],
        "reln": [],
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
        "dn": "uni/l3dom-multipodL3out_L3Dom",
        "name": "multipodL3out_L3Dom",
        "aaep_names": [
            "multipodL3out_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-multipodL3out_AAEP",
                "type": "AAEP",
                "name": "multipodL3out_AAEP"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-infra/out-intersite",
                "type": "L3 Out",
                "name": "infra/intersite"
            }
        ],
        "vlan": "multipodL3out_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[multipodL3out_VlanPool]-dynamic",
            "name": "multipodL3out_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-4",
                    "name": "",
                    "rn": "from-[vlan-4]-to-[vlan-4]",
                    "role": "external",
                    "to": "vlan-4",
                    "fromVlan": "4",
                    "toVlan": "4",
                    "blockInfo": "[4-4] (dynamic)"
                }
            ],
            "vlanCount": 1,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-multipodL3out_L3Dom",
                    "domainName": "multipodL3out_L3Dom"
                }
            ]
        },
        "vlan_block": [
            "4-4"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l3dom-RL-L3Out_RoutedDomain",
        "name": "RL-L3Out_RoutedDomain",
        "aaep_names": [
            "RL-L3Out_EntityProfile"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-RL-L3Out_EntityProfile",
                "type": "AAEP",
                "name": "RL-L3Out_EntityProfile"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-infra/out-RL-L3Out",
                "type": "L3 Out",
                "name": "infra/RL-L3Out"
            }
        ],
        "vlan": "RL-L3Out_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[RL-L3Out_VlanPool]-dynamic",
            "name": "RL-L3Out_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-4",
                    "name": "",
                    "rn": "from-[vlan-4]-to-[vlan-4]",
                    "role": "external",
                    "to": "vlan-4",
                    "fromVlan": "4",
                    "toVlan": "4",
                    "blockInfo": "[4-4] (dynamic)"
                }
            ],
            "vlanCount": 1,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-RL-L3Out_RoutedDomain",
                    "domainName": "RL-L3Out_RoutedDomain"
                }
            ]
        },
        "vlan_block": [
            "4-4"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l3dom-UCSB1_L3Dom",
        "name": "UCSB1_L3Dom",
        "aaep_names": [
            "UCSB1_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-UCSB1_AAEP",
                "type": "AAEP",
                "name": "UCSB1_AAEP"
            }
        ],
        "vlan": "UCSB1_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[UCSB1_VlanPool]-dynamic",
            "name": "UCSB1_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2",
                    "name": "blk1",
                    "rn": "from-[vlan-2]-to-[vlan-100]",
                    "role": "external",
                    "to": "vlan-100",
                    "fromVlan": "2",
                    "toVlan": "100",
                    "blockInfo": "[2-100] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-3701",
                    "name": "blk2",
                    "rn": "from-[vlan-3701]-to-[vlan-4000]",
                    "role": "external",
                    "to": "vlan-4000",
                    "fromVlan": "3701",
                    "toVlan": "4000",
                    "blockInfo": "[3701-4000] (dynamic)"
                }
            ],
            "vlanCount": 399,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-UCSB1_L3Dom",
                    "domainName": "UCSB1_L3Dom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-UCSB1_PhysDom",
                    "domainName": "UCSB1_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "2-100",
            "3701-4000"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/l3dom-vEPC_ESX",
        "name": "vEPC_ESX",
        "aaep_names": [
            "ESX-CDC-22_AAEP",
            "vEPC-ESX21-22_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-ESX-CDC-22_AAEP",
                "type": "AAEP",
                "name": "ESX-CDC-22_AAEP"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-vEPC-ESX21-22_AAEP",
                "type": "AAEP",
                "name": "vEPC-ESX21-22_AAEP"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-vEPC_demo/out-ACC_L3out",
                "type": "L3 Out",
                "name": "vEPC_demo/ACC_L3out"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-vEPC_demo/out-SX_L3out",
                "type": "L3 Out",
                "name": "vEPC_demo/SX_L3out"
            },
            {
                "tCl": "l3extOut",
                "tDn": "uni/tn-vEPC_demo/out-INT_L3out",
                "type": "L3 Out",
                "name": "vEPC_demo/INT_L3out"
            }
        ],
        "vlan": "ESX-CDC-22_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[ESX-CDC-22_VlanPool]-dynamic",
            "name": "ESX-CDC-22_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2501",
                    "name": "blk1",
                    "rn": "from-[vlan-2501]-to-[vlan-2502]",
                    "role": "external",
                    "to": "vlan-2502",
                    "fromVlan": "2501",
                    "toVlan": "2502",
                    "blockInfo": "[2501-2502] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2503",
                    "name": "blk2",
                    "rn": "from-[vlan-2503]-to-[vlan-2509]",
                    "role": "external",
                    "to": "vlan-2509",
                    "fromVlan": "2503",
                    "toVlan": "2509",
                    "blockInfo": "[2503-2509] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "Non overlapping range with ACI1 Fabric",
                    "dn": null,
                    "from": "vlan-2700",
                    "name": "blk3",
                    "rn": "from-[vlan-2700]-to-[vlan-2999]",
                    "role": "external",
                    "to": "vlan-2999",
                    "fromVlan": "2700",
                    "toVlan": "2999",
                    "blockInfo": "[2700-2999] (dynamic)"
                }
            ],
            "vlanCount": 309,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-ESX-CDC-22_PhysDom",
                    "domainName": "ESX-CDC-22_PhysDom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "vmmDomP",
                    "tDn": "uni/vmmp-VMware/dom-EU-SPDC-CDC-22",
                    "domainName": "EU-SPDC-CDC-22"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-vEPC_ESX",
                    "domainName": "vEPC_ESX"
                }
            ]
        },
        "vlan_block": [
            "2501-2502",
            "2503-2509",
            "2700-2999"
        ]
    }
]
```

[[Back]](./DomainL3.md)