# Physical Domain

## JSON output

```
# iserver get aci domain phy --apic apic21 -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-ESX-CDC-22_PhysDom",
        "name": "ESX-CDC-22_PhysDom",
        "aaep_names": [
            "ESX-CDC-22_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-common/ap-Test_ANP/epg-Test_EPG",
                "type": "Application EPG",
                "name": "common/Test_ANP/Test_EPG"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-ESX-CDC-22_AAEP",
                "type": "AAEP",
                "name": "ESX-CDC-22_AAEP"
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
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-ESX-R7DC_PhysDom",
        "name": "ESX-R7DC_PhysDom",
        "aaep_names": [
            "ESX-R7DC_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-ESX-R7DC_AAEP",
                "type": "AAEP",
                "name": "ESX-R7DC_AAEP"
            }
        ],
        "vlan": "ESX-R7DC_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[ESX-R7DC_VlanPool]-dynamic",
            "name": "ESX-R7DC_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-3701",
                    "name": "blk1",
                    "rn": "from-[vlan-3701]-to-[vlan-3800]",
                    "role": "external",
                    "to": "vlan-3800",
                    "fromVlan": "3701",
                    "toVlan": "3800",
                    "blockInfo": "[3701-3800] (dynamic)"
                }
            ],
            "vlanCount": 100,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-ESX-R7DC_PhysDom",
                    "domainName": "ESX-R7DC_PhysDom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "vmmDomP",
                    "tDn": "uni/vmmp-VMware/dom-EU-SPDC-R7DC",
                    "domainName": "EU-SPDC-R7DC"
                }
            ]
        },
        "vlan_block": [
            "3701-3800"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-HX1_PhysDom",
        "name": "HX1_PhysDom",
        "aaep_names": [
            "HX1_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT",
                "type": "Application EPG",
                "name": "vEPC_demo/vEPG_ANP/vEPG_MGMT"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-HX1_AAEP",
                "type": "AAEP",
                "name": "HX1_AAEP"
            }
        ],
        "vlan": "HX1_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "static",
            "descr": "",
            "dn": "uni/infra/vlanns-[HX1_VlanPool]-static",
            "name": "HX1_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "IWE Usage",
                    "dn": null,
                    "from": "vlan-70",
                    "name": "blk1",
                    "rn": "from-[vlan-70]-to-[vlan-79]",
                    "role": "external",
                    "to": "vlan-79",
                    "fromVlan": "70",
                    "toVlan": "79",
                    "blockInfo": "[70-79] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "HX1-eu-spdc VLAN pool",
                    "dn": null,
                    "from": "vlan-1000",
                    "name": "blk2",
                    "rn": "from-[vlan-1000]-to-[vlan-4048]",
                    "role": "external",
                    "to": "vlan-4048",
                    "fromVlan": "1000",
                    "toVlan": "4048",
                    "blockInfo": "[1000-4048] (static)"
                }
            ],
            "vlanCount": 3059,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-HX1_PhysDom",
                    "domainName": "HX1_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "70-79",
            "1000-4048"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-Infra_PhysDom",
        "name": "Infra_PhysDom",
        "aaep_names": [
            "vEPC-ESX21-22_AAEP",
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
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-vEPC-ESX21-22_AAEP",
                "type": "AAEP",
                "name": "vEPC-ESX21-22_AAEP"
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
        "dn": "uni/phys-k8s_esx_PhysDom",
        "name": "k8s_esx_PhysDom",
        "aaep_names": [
            "k8s_esx_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-MGMT",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/MGMT"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-SRIoV_A",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/SRIoV_A"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-SRIoV_B",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/SRIoV_B"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-backbone1",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/backbone1"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_prov",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/bmk8s_prov"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-csr1_lan",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/csr1_lan"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-csr2_lan",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/csr2_lan"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-csr_b2b",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/csr_b2b"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-site1_lan",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/site1_lan"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-site1_pe",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/site1_pe"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-site2_lan",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/site2_lan"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-site2_pe",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/site2_pe"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/vk8s_1"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_2",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/vk8s_2"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/vk8s_3"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/vk8s_4"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-k8s_esx_AAEP",
                "type": "AAEP",
                "name": "k8s_esx_AAEP"
            }
        ],
        "vlan": "k8s_esx_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "Managed by Terraform",
            "dn": "uni/infra/vlanns-[k8s_esx_VlanPool]-dynamic",
            "name": "k8s_esx_VlanPool",
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
                    "allocMode": "dynamic",
                    "descr": "Managed by Terraform",
                    "dn": null,
                    "from": "vlan-1300",
                    "name": "",
                    "rn": "from-[vlan-1300]-to-[vlan-1499]",
                    "role": "external",
                    "to": "vlan-1499",
                    "fromVlan": "1300",
                    "toVlan": "1499",
                    "blockInfo": "[1300-1499] (dynamic)"
                }
            ],
            "vlanCount": 210,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "vmmDomP",
                    "tDn": "uni/vmmp-VMware/dom-EU-SPDC-POD2B",
                    "domainName": "EU-SPDC-POD2B"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-k8s_esx_PhysDom",
                    "domainName": "k8s_esx_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "800-809",
            "1300-1499"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-k8s_phys_PhysDom",
        "name": "k8s_phys_PhysDom",
        "aaep_names": [
            "k8s_phys_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-SRIoV_A",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/SRIoV_A"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-SRIoV_B",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/SRIoV_B"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_1",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/bmk8s_1"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_2",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/bmk8s_2"
            },
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_prov",
                "type": "Application EPG",
                "name": "k8s/k8s_ANP/bmk8s_prov"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-k8s_phys_AAEP",
                "type": "AAEP",
                "name": "k8s_phys_AAEP"
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
        "dn": "uni/phys-nidemo",
        "name": "nidemo",
        "aaep_names": [
            "nidemo"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-nidemo/ap-streamz/epg-database",
                "type": "Application EPG",
                "name": "nidemo/streamz/database"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-nidemo",
                "type": "AAEP",
                "name": "nidemo"
            }
        ],
        "vlan": "nidemo-3000-3001",
        "aaaDomain": [],
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
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-SPN_PhysDom",
        "name": "SPN_PhysDom",
        "aaep_names": [
            "SPN_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-SPN_IntraLab/ap-SPN_Connect_ANP/epg-TEST2",
                "type": "Application EPG",
                "name": "SPN_IntraLab/SPN_Connect_ANP/TEST2"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-SPN_AAEP",
                "type": "AAEP",
                "name": "SPN_AAEP"
            }
        ],
        "vlan": "SPN_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "static",
            "descr": "",
            "dn": "uni/infra/vlanns-[SPN_VlanPool]-static",
            "name": "SPN_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2600",
                    "name": "blk1",
                    "rn": "from-[vlan-2600]-to-[vlan-2699]",
                    "role": "external",
                    "to": "vlan-2699",
                    "fromVlan": "2600",
                    "toVlan": "2699",
                    "blockInfo": "[2600-2699] (static)"
                }
            ],
            "vlanCount": 100,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-SPN_PhysDom",
                    "domainName": "SPN_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "2600-2699"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-UCSB1-R7DC_PhysDom",
        "name": "UCSB1-R7DC_PhysDom",
        "aaep_names": [
            "UCSB1-R7DC_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-UCSB1-R7DC_AAEP",
                "type": "AAEP",
                "name": "UCSB1-R7DC_AAEP"
            }
        ],
        "vlan": "UCSB1-R7DC_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[UCSB1-R7DC_VlanPool]-dynamic",
            "name": "UCSB1-R7DC_VlanPool",
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
                    "from": "vlan-1701",
                    "name": "blk2",
                    "rn": "from-[vlan-1701]-to-[vlan-1899]",
                    "role": "external",
                    "to": "vlan-1899",
                    "fromVlan": "1701",
                    "toVlan": "1899",
                    "blockInfo": "[1701-1899] (dynamic)"
                }
            ],
            "vlanCount": 298,
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-UCSB1-R7DC_PhysDom",
                    "domainName": "UCSB1-R7DC_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "2-100",
            "1701-1899"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-UCSB1_PhysDom",
        "name": "UCSB1_PhysDom",
        "aaep_names": [
            "UCSB1_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT",
                "type": "Application EPG",
                "name": "vEPC_demo/vEPG_ANP/vEPG_MGMT"
            },
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
        "dn": "uni/phys-vEPC-ESX20_PhysDom",
        "name": "vEPC-ESX20_PhysDom",
        "aaep_names": [
            "vEPC-ESX21-22_AAEP"
        ],
        "reln": [
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-vEPC-ESX21-22_AAEP",
                "type": "AAEP",
                "name": "vEPC-ESX21-22_AAEP"
            }
        ],
        "vlan": "vEPC-ESX21-22_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[vEPC-ESX21-22_VlanPool]-dynamic",
            "name": "vEPC-ESX21-22_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2501",
                    "name": "blk1",
                    "rn": "from-[vlan-2501]-to-[vlan-2509]",
                    "role": "external",
                    "to": "vlan-2509",
                    "fromVlan": "2501",
                    "toVlan": "2509",
                    "blockInfo": "[2501-2509] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2700",
                    "name": "blk2",
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
                    "tCl": "vmmDomP",
                    "tDn": "uni/vmmp-VMware/dom-vEPC-Dataplane",
                    "domainName": "vEPC-Dataplane"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-vEPC-ESX20_PhysDom",
                    "domainName": "vEPC-ESX20_PhysDom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-vEPC-ESX21-22_PhysDom",
                    "domainName": "vEPC-ESX21-22_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "2501-2509",
            "2700-2999"
        ]
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "dn": "uni/phys-vEPC-ESX21-22_PhysDom",
        "name": "vEPC-ESX21-22_PhysDom",
        "aaep_names": [
            "vEPC-ESX21-22_AAEP"
        ],
        "reln": [
            {
                "tCl": "fvAEPg",
                "tDn": "uni/tn-vEPC_demo/ap-vEPG_ANP/epg-vEPG_MGMT",
                "type": "Application EPG",
                "name": "vEPC_demo/vEPG_ANP/vEPG_MGMT"
            },
            {
                "tCl": "infraAttEntityP",
                "tDn": "uni/infra/attentp-vEPC-ESX21-22_AAEP",
                "type": "AAEP",
                "name": "vEPC-ESX21-22_AAEP"
            }
        ],
        "vlan": "vEPC-ESX21-22_VlanPool",
        "aaaDomain": [],
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "vlan_info": {
            "__Output": {},
            "allocMode": "dynamic",
            "descr": "",
            "dn": "uni/infra/vlanns-[vEPC-ESX21-22_VlanPool]-dynamic",
            "name": "vEPC-ESX21-22_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "static",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2501",
                    "name": "blk1",
                    "rn": "from-[vlan-2501]-to-[vlan-2509]",
                    "role": "external",
                    "to": "vlan-2509",
                    "fromVlan": "2501",
                    "toVlan": "2509",
                    "blockInfo": "[2501-2509] (static)"
                },
                {
                    "__Output": {},
                    "allocMode": "dynamic",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2700",
                    "name": "blk2",
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
                    "tCl": "vmmDomP",
                    "tDn": "uni/vmmp-VMware/dom-vEPC-Dataplane",
                    "domainName": "vEPC-Dataplane"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-vEPC-ESX20_PhysDom",
                    "domainName": "vEPC-ESX20_PhysDom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-vEPC-ESX21-22_PhysDom",
                    "domainName": "vEPC-ESX21-22_PhysDom"
                }
            ]
        },
        "vlan_block": [
            "2501-2509",
            "2700-2999"
        ]
    }
]
```

[[Back]](./DomainPhy.md)