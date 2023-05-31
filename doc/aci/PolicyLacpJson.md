# Policy - Port Channel

## JSON

```
# iserver get aci policy lacp --apic apic11 --name default -o json

[
    {
        "__Output": {},
        "annotation": "",
        "ctrl": "fast-sel-hot-stdby,graceful-conv,susp-individual",
        "dn": "uni/infra/lacplagp-default",
        "maxLinks": "16",
        "minLinks": "1",
        "mode": "off",
        "name": "default",
        "relnFrom": [
            {
                "class": "lacpLagPol",
                "rn": "rtresLacpLagPol",
                "tCl": "infraInfra",
                "tDn": "uni/infra",
                "policyType": "Access Infra",
                "policyName": "infra"
            },
            {
                "class": "lacpLagPol",
                "rn": "rtvmmDefaultLacpLagPol-[uni/vmmp-VMware/dom-EU-SPDC-CDC]",
                "tCl": "vmmDomP",
                "tDn": "uni/vmmp-VMware/dom-EU-SPDC-CDC",
                "policyType": "VMM Domain",
                "policyName": "EU-SPDC-CDC"
            },
            {
                "class": "lacpLagPol",
                "rn": "rtvmmDefaultLacpLagPol-[uni/vmmp-VMware/dom-EU-SPDC-R3DC]",
                "tCl": "vmmDomP",
                "tDn": "uni/vmmp-VMware/dom-EU-SPDC-R3DC",
                "policyType": "VMM Domain",
                "policyName": "EU-SPDC-R3DC"
            }
        ],
        "tf": false,
        "tfTick": "",
        "ctrlT": [
            "Fast Select Hot Standby Ports",
            "Graceful Convergence",
            "Suspend Individual Ports"
        ],
        "references": 3,
        "l1RsLacpIfPolCons": [],
        "interfaces": 0,
        "nodeInterfaces": []
    }
]
```

[[Back]](./PolicyLacp.md)