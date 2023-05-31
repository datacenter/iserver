# Application Profile (AP)

## JSON

```
# iserver get aci ap --apic apic21 --name vEPC/vSFO_ANP -o json

[
    {
        "__Output": {},
        "descr": "",
        "dn": "uni/tn-vEPC/ap-vSFO_ANP",
        "name": "vSFO_ANP",
        "prio": "unspecified",
        "userdom": ":all:common:",
        "tenant": "vEPC",
        "nameTenant": "vEPC/vSFO_ANP",
        "epgs": [
            {
                "__Output": {
                    "adminUpTick": "Green",
                    "configSt": "Green",
                    "contractTick": "Green"
                },
                "annotation": "",
                "configSt": "applied",
                "descr": "",
                "dn": "uni/tn-vEPC/ap-vSFO_ANP/epg-WWW",
                "exceptionTag": "",
                "floodOnEncap": "disabled",
                "hasMcastSource": "no",
                "isAttrBasedEPg": "no",
                "matchT": "AtleastOne",
                "name": "WWW",
                "nameAlias": "",
                "pcEnfPref": "unenforced",
                "pcTag": "32771",
                "prefGrMemb": "exclude",
                "prio": "level3",
                "shutdown": "no",
                "adminUp": true,
                "adminUpTick": "\u2713",
                "tenant": "vEPC",
                "nameTenant": "vEPC/WWW",
                "application_profile": "vSFO_ANP",
                "nameApTenant": "vEPC/vSFO_ANP/WWW",
                "contractConsumed": [
                    {
                        "dn": "uni/tn-vEPC/brc-vEPC_alltraffic",
                        "tenant": "vEPC",
                        "name": "vEPC_alltraffic",
                        "nameTenant": "vEPC/vEPC_alltraffic"
                    }
                ],
                "contractProvided": [],
                "contractTick": "\u2713",
                "bd_tenant_name": "vEPC",
                "bd_name": "vSFO_BD"
            }
        ]
    }
]
```

[[Back]](./ApplicationProfile.md)