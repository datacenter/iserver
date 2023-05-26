# L2 Domain

## JSON

```
# iserver get aci domain l2 --apic apic11 -o json

[
    {
        "__Output": {},
        "dn": "uni/l2dom-VNF-mgmt_L2Dom",
        "name": "VNF-mgmt_L2Dom",
        "aaep_names": [
            "Infra_AAEP"
        ],
        "vlan": "Infra_VlanPool",
        "vlan_info": {
            "__Output": {},
            "allocMode": "static",
            "descr": "",
            "dn": "uni/infra/vlanns-[Infra_VlanPool]-static",
            "name": "Infra_VlanPool",
            "fvnsEncapBlk": [
                {
                    "__Output": {},
                    "allocMode": "inherit",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-1",
                    "name": "blk1",
                    "rn": "from-[vlan-1]-to-[vlan-1000]",
                    "role": "external",
                    "to": "vlan-1000",
                    "fromVlan": "1",
                    "toVlan": "1000",
                    "blockInfo": "[1-1000] (inherit)"
                },
                {
                    "__Output": {},
                    "allocMode": "inherit",
                    "descr": "",
                    "dn": null,
                    "from": "vlan-2000",
                    "name": "blk2",
                    "rn": "from-[vlan-2000]-to-[vlan-2000]",
                    "role": "external",
                    "to": "vlan-2000",
                    "fromVlan": "2000",
                    "toVlan": "2000",
                    "blockInfo": "[2000-2000] (inherit)"
                }
            ],
            "vlanCount": 1001,
            "epg": [],
            "epgCount": 0,
            "epgUsage": "0/1001",
            "fvnsRtVlanNs": [
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-Infra-2_L3Dom",
                    "domainName": "Infra-2_L3Dom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "physDomP",
                    "tDn": "uni/phys-Infra-2_PhysDom",
                    "domainName": "Infra-2_PhysDom"
                },
                {
                    "__Output": {},
                    "dn": null,
                    "tCl": "l3extDomP",
                    "tDn": "uni/l3dom-Infra-BGP_L3Dom",
                    "domainName": "Infra-BGP_L3Dom"
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
                    "tCl": "l2extDomP",
                    "tDn": "uni/l2dom-VNF-mgmt_L2Dom",
                    "domainName": "uni/l2dom-VNF-mgmt_L2Dom"
                }
            ]
        }
    }
]
```

[[Back]](./DomainL2.md)