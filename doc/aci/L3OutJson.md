# L3 Out

## JSON

```
# iserver get aci l3out --apic apic11 --name multipodL3Out -o json

[
    {
        "__Output": {
            "mplsEnabledTick": "Red"
        },
        "descr": "",
        "dn": "uni/tn-infra/out-multipodL3Out",
        "enforceRtctrl": "export",
        "mplsEnabled": false,
        "name": "multipodL3Out",
        "targetDscp": "unspecified",
        "userdom": "",
        "mplsEnabledTick": "\u2717",
        "tenant": "infra",
        "nameTenant": "infra/multipodL3Out",
        "l3extRsL3DomAtt": {
            "__Output": {},
            "dn": "uni/l3dom-multipodL3Out_RoutedDomain",
            "name": "multipodL3Out_RoutedDomain"
        },
        "bgpExtP": {
            "__Output": {
                "enabledTick": "Green"
            },
            "enabled": true,
            "enabledTick": "\u2713"
        },
        "ospfExtP": {
            "__Output": {
                "enabledTick": "Green",
                "redistributeTick": "Green",
                "summaryTick": "Green",
                "suppressTick": "Red"
            },
            "enabled": true,
            "enabledTick": "\u2713",
            "areaCost": "1",
            "areaCtrl": "redistribute,summary",
            "areaId": "backbone",
            "areaType": "regular",
            "multipodInternal": "no",
            "redistribute": true,
            "redistributeTick": "\u2713",
            "summary": true,
            "summaryTick": "\u2713",
            "suppress": false,
            "suppressTick": "\u2717"
        },
        "eigrpExtP": {
            "__Output": {
                "enabledTick": "Red"
            },
            "enabled": false,
            "enabledTick": "\u2717"
        },
        "pimExtP": {
            "__Output": {
                "enabledTick": "Red"
            },
            "enabled": false,
            "enabledTick": "\u2717"
        },
        "l3extRsEctx": {
            "__Output": {
                "enabledTick": "Green"
            },
            "enabled": true,
            "enabledTick": "\u2713",
            "dn": "uni/tn-infra/ctx-overlay-1",
            "tenant": "infra",
            "name": "overlay-1",
            "nameTenant": "infra/overlay-1"
        },
        "nodeProfiles": [
            {
                "__Output": {},
                "descr": "",
                "dn": "uni/tn-infra/out-multipodL3Out/lnodep-LNodeP_101",
                "name": "LNodeP_101",
                "targetDscp": "unspecified",
                "userdom": "",
                "tenant": "infra",
                "l3out": "multipodL3Out",
                "nodes": [
                    {
                        "rtrId": "101.101.101.101",
                        "rtrIdLoopBack": "yes",
                        "podId": "1",
                        "nodeId": "101",
                        "nodeDn": "topology/pod-1/node-101"
                    }
                ]
            },
            {
                "__Output": {},
                "descr": "",
                "dn": "uni/tn-infra/out-multipodL3Out/lnodep-LNodeP_102",
                "name": "LNodeP_102",
                "targetDscp": "unspecified",
                "userdom": "",
                "tenant": "infra",
                "l3out": "multipodL3Out",
                "nodes": [
                    {
                        "rtrId": "102.102.102.102",
                        "rtrIdLoopBack": "yes",
                        "podId": "1",
                        "nodeId": "102",
                        "nodeDn": "topology/pod-1/node-102"
                    }
                ]
            }
        ],
        "l3extInstP": [
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
                "name": "ipnInstP",
                "nameAlias": "",
                "pcEnfPref": "unenforced",
                "pcTag": "49154",
                "prefGrMemb": "exclude",
                "prio": "unspecified",
                "rn": "instP-ipnInstP",
                "status": "",
                "targetDscp": "unspecified"
            }
        ],
        "nodes": [
            {
                "rtrId": "101.101.101.101",
                "rtrIdLoopBack": "yes",
                "podId": "1",
                "nodeId": "101",
                "nodeDn": "topology/pod-1/node-101"
            },
            {
                "rtrId": "102.102.102.102",
                "rtrIdLoopBack": "yes",
                "podId": "1",
                "nodeId": "102",
                "nodeDn": "topology/pod-1/node-102"
            }
        ]
    }
]
```

[[Back]](./L3Out.md)