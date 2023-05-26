# Application Profile (AP)

## JSON

```
# iserver get aci ap --apic apic21 --name *sfo* -o json

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
                "fvBD": {
                    "__Output": {
                        "mcastAllowTick": "Red",
                        "ipv6McastAllowTick": "Red"
                    },
                    "arpFlood": "yes",
                    "bcastP": "225.1.139.96",
                    "descr": "",
                    "dn": "uni/tn-vEPC/BD-vSFO_BD",
                    "epClear": "no",
                    "epMoveDetectMode": "",
                    "hostBasedRouting": "no",
                    "intersiteBumTrafficAllow": "no",
                    "intersiteL2Stretch": "no",
                    "ipLearning": "yes",
                    "ipv6McastAllow": "no",
                    "limitIpLearnToSubnets": "yes",
                    "llAddr": "::",
                    "mac": "00:22:BD:F8:19:FF",
                    "mcastARPDrop": "no",
                    "mcastAllow": "no",
                    "mtu": "inherit",
                    "multiDstPktAct": "bd-flood",
                    "name": "vSFO_BD",
                    "seg": "16613251",
                    "type": "regular",
                    "unicastRoute": "yes",
                    "unkMacUcastAct": "proxy",
                    "unkMcastAct": "flood",
                    "v6unkMcastAct": "flood",
                    "vmac": "",
                    "tenant": "vEPC",
                    "nameTenant": "vEPC/vSFO_BD",
                    "mcastAllowTick": "\u2717",
                    "ipv6McastAllowTick": "\u2717",
                    "health": {
                        "__Output": {
                            "score": "Green"
                        },
                        "score": "100"
                    },
                    "fvSubnet": [
                        {
                            "__Output": {},
                            "ip": "15.16.132.254/24",
                            "ipDPLearning": "enabled",
                            "preferred": "no",
                            "rn": "subnet-[15.16.132.254/24]",
                            "scope": "public,shared",
                            "virtual": "no",
                            "network": "15.16.132.0/24",
                            "gateway": "15.16.132.254",
                            "size": 254
                        }
                    ],
                    "fvSubnetCount": 1,
                    "fvSubnets": "15.16.132.254/24",
                    "fvRsCtx": {
                        "__Output": {},
                        "dn": "uni/tn-vEPC/ctx-VSFO",
                        "tenant": "vEPC",
                        "name": "VSFO",
                        "nameTenant": "vEPC/VSFO"
                    },
                    "fvRsBDToOut": [
                        {
                            "__Output": {},
                            "tenant": "vEPC",
                            "name": "vSFO_L3out",
                            "nameTenant": "vEPC/vSFO_L3out"
                        }
                    ],
                    "l3OutCount": 1,
                    "fvRsIgmpsn": {
                        "__Output": {},
                        "tenant": "common",
                        "configuredPolicyName": "",
                        "actualPolicyName": "default",
                        "name": "default",
                        "nameTenant": "common/default"
                    },
                    "fvRsMldsn": {
                        "__Output": {},
                        "tenant": "common",
                        "configuredPolicyName": "",
                        "actualPolicyName": "default",
                        "name": "default",
                        "nameTenant": "common/default"
                    }
                }
            }
        ]
    }
]
```

[[Back]](./ApplicationProfile.md)