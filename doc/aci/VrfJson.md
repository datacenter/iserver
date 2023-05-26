# Virtual Routing and Forwarding (VRF)

## Get vrf properties in JSON format

```
# iserver get aci vrf --apic apic21 --name Infra_VRF -o json

[
    {
        "__Output": {},
        "bdEnforcedEnable": "no",
        "descr": "",
        "dn": "uni/tn-common/ctx-Infra_VRF",
        "ipDataPlaneLearning": "enabled",
        "knwMcastAct": "permit",
        "name": "Infra_VRF",
        "pcEnfDir": "ingress",
        "pcEnfPref": "unenforced",
        "userdom": ":all:common:",
        "vrfIndex": "0",
        "tenant": "common",
        "nameTenant": "common/Infra_VRF",
        "endpointsCount": 0,
        "fvBD": [],
        "fvSubnet": [],
        "fvAEPg": [],
        "l3out": [
            {
                "__Output": {
                    "mplsEnabledTick": "Red"
                },
                "descr": "",
                "dn": "uni/tn-common/out-Infra_L3out",
                "enforceRtctrl": "export",
                "mplsEnabled": false,
                "name": "Infra_L3out",
                "targetDscp": "unspecified",
                "userdom": ":all:common:",
                "mplsEnabledTick": "\u2717",
                "tenant": "common",
                "nameTenant": "common/Infra_L3out",
                "l3extRsL3DomAtt": {
                    "__Output": {},
                    "dn": "uni/l3dom-Infra_L3Dom",
                    "name": "Infra_L3Dom"
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
                        "enabledTick": "Red"
                    },
                    "enabled": false,
                    "enabledTick": "\u2717"
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
                    "dn": "uni/tn-common/ctx-Infra_VRF",
                    "tenant": "common",
                    "name": "Infra_VRF",
                    "nameTenant": "common/Infra_VRF"
                },
                "nodeProfiles": [
                    {
                        "__Output": {},
                        "descr": "",
                        "dn": "uni/tn-common/out-Infra_L3out/lnodep-Infra_L3out_LNP",
                        "name": "Infra_L3out_LNP",
                        "targetDscp": "unspecified",
                        "userdom": ":all:common:",
                        "tenant": "common",
                        "l3out": "nfra_L3out",
                        "nodes": [
                            {
                                "rtrId": "206.206.206.206",
                                "rtrIdLoopBack": "yes",
                                "podId": "1",
                                "nodeId": "2206",
                                "nodeDn": "topology/pod-1/node-2206"
                            },
                            {
                                "rtrId": "205.205.205.205",
                                "rtrIdLoopBack": "yes",
                                "podId": "1",
                                "nodeId": "2205",
                                "nodeDn": "topology/pod-1/node-2205"
                            }
                        ]
                    }
                ],
                "l3extInstP": [
                    {
                        "__Output": {
                            "configSt": "Green"
                        },
                        "annotation": "orchestrator:terraform",
                        "configSt": "applied",
                        "descr": "",
                        "exceptionTag": "",
                        "floodOnEncap": "disabled",
                        "isSharedSrvMsiteEPg": "no",
                        "matchT": "AtleastOne",
                        "name": "Infra_L3out_ExtEPG",
                        "nameAlias": "",
                        "pcEnfPref": "unenforced",
                        "pcTag": "32779",
                        "prefGrMemb": "exclude",
                        "prio": "unspecified",
                        "rn": "instP-Infra_L3out_ExtEPG",
                        "status": "",
                        "targetDscp": "unspecified"
                    }
                ],
                "nodes": [
                    {
                        "rtrId": "206.206.206.206",
                        "rtrIdLoopBack": "yes",
                        "podId": "1",
                        "nodeId": "2206",
                        "nodeDn": "topology/pod-1/node-2206"
                    },
                    {
                        "rtrId": "205.205.205.205",
                        "rtrIdLoopBack": "yes",
                        "podId": "1",
                        "nodeId": "2205",
                        "nodeDn": "topology/pod-1/node-2205"
                    }
                ]
            }
        ]
    }
]
```

[[Back]](./Vrf.md)