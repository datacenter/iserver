# L2Out

## JSON output

```
# iserver get aci l2out --apic apic21 --name Test -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "descr": "",
        "dn": "uni/tn-k8s/l2out-Test",
        "name": "Test",
        "targetDscp": "unspecified",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/Test",
        "fvBD": {
            "dn": "uni/tn-k8s/BD-Test",
            "tenant": "k8s",
            "name": "Test",
            "encap": "vlan-666",
            "nameTenant": "k8s/Test"
        },
        "l2extDomP": {
            "dn": "uni/l2dom-Infra_L2dom",
            "name": "Infra_L2dom"
        },
        "l2extInstP": [
            {
                "__Output": {
                    "configSt": "Green"
                },
                "annotation": "",
                "configSt": "applied",
                "descr": "",
                "exceptionTag": "",
                "floodOnEncap": "disabled",
                "isSharedSrvMsiteEPg": "no",
                "matchT": "AtleastOne",
                "name": "L2Out-ext-epg",
                "nameAlias": "",
                "pcEnfPref": "unenforced",
                "pcTag": "49160",
                "prefGrMemb": "exclude",
                "prio": "unspecified",
                "rn": "instP-L2Out-ext-epg",
                "targetDscp": "unspecified"
            }
        ],
        "faults": "0 0 3 0",
        "isAnyFault": true,
        "path": [
            "topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp]",
            "topology/pod-1/paths-2207/pathep-[eth1/30]"
        ]
    }
]
```

[[Back]](./L2Out.md)