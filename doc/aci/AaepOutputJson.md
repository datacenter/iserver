# Attachable Access Entity Profile (AAEP)

## JSON

```
# iserver get aci aaep --apic apic11 --name UCSB1_AAEP -o json

[
    {
        "__Output": {
            "infraVlanEnabledTick": "Red"
        },
        "descr": "",
        "dn": "uni/infra/attentp-UCSB1_AAEP",
        "name": "UCSB1_AAEP",
        "infraRtAttEntP": [
            {
                "__Output": {},
                "dn": "uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp",
                "type": "infraAccBndlGrp",
                "typeName": "PC/VPC Interface",
                "name": "UCSB1-FI-A_PolGrp"
            },
            {
                "__Output": {},
                "dn": "uni/infra/funcprof/accbundle-UCSB1-FI-B_PolGrp",
                "type": "infraAccBndlGrp",
                "typeName": "PC/VPC Interface",
                "name": "UCSB1-FI-B_PolGrp"
            }
        ],
        "infraRsDomP": [
            {
                "__Output": {},
                "forceResolve": "yes",
                "state": "formed",
                "tCl": "vmmDomP",
                "tDn": "uni/vmmp-VMware/dom-EU-SPDC-CDC",
                "domainType": "VMM",
                "domainName": "EU-SPDC-CDC"
            },
            {
                "__Output": {},
                "forceResolve": "yes",
                "state": "formed",
                "tCl": "l3extDomP",
                "tDn": "uni/l3dom-Infra_L3Dom",
                "domainType": "L3",
                "domainName": "Infra_L3Dom"
            },
            {
                "__Output": {},
                "forceResolve": "yes",
                "state": "formed",
                "tCl": "l3extDomP",
                "tDn": "uni/l3dom-UCSB1_L3Dom",
                "domainType": "L3",
                "domainName": "UCSB1_L3Dom"
            },
            {
                "__Output": {},
                "forceResolve": "yes",
                "state": "formed",
                "tCl": "physDomP",
                "tDn": "uni/phys-UCSB1_PhysDom",
                "domainType": "Physical",
                "domainName": "UCSB1_PhysDom"
            }
        ],
        "infraVlanEnabled": false,
        "infraVlanEnabledTick": "\u2717"
    }
]
```

[[Back]](./Aaep.md)