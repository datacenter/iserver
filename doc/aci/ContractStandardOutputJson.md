# Standard Contract

## JSON output

```
# iserver get aci contract standard --apic apic21 --name k8s/k8s_tn_bm -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "descr": "",
        "dn": "uni/tn-k8s/brc-k8s_tn_bm",
        "intent": "install",
        "name": "k8s_tn_bm",
        "scope": "global",
        "targetDscp": "unspecified",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/k8s_tn_bm",
        "vzFilter": [
            {
                "__Output": {
                    "faults": ":R.M.Y.G"
                },
                "descr": "",
                "dn": "uni/tn-common/flt-any",
                "name": "any",
                "userdom": ":all:common:",
                "tenant": "common",
                "nameTenant": "common/any",
                "vzEntry": [
                    {
                        "__Output": {},
                        "applyToFrag": "no",
                        "arpOpc": "",
                        "dFromPort": "unspecified",
                        "dToPort": "unspecified",
                        "descr": "",
                        "etherT": "ipv4",
                        "icmpv4T": "unspecified",
                        "icmpv6T": "unspecified",
                        "matchDscp": "unspecified",
                        "name": "any",
                        "prot": "",
                        "sFromPort": "unspecified",
                        "sToPort": "unspecified",
                        "stateful": "no",
                        "status": "",
                        "tcpRules": "",
                        "source": "",
                        "destination": ""
                    }
                ],
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "subjectName": "k8s_tn_vm",
                "subjectTenant": "k8s",
                "subjectNameTenant": "k8s/k8s_tn_vm"
            }
        ],
        "consumerEpg": [],
        "providerEpg": [
            {
                "class": "l3extInstP",
                "tenant": "k8s",
                "l3out": "bml3_k8s",
                "name": "bml3_k8s_ExtEPG",
                "nameTenant": "k8s/bml3_k8s_ExtEPG",
                "nameLong": "k8s/bml3_k8s/bml3_k8s_ExtEPG"
            }
        ],
        "faults": "0 0 0 0",
        "isAnyFault": false
    }
]
```

[[Back]](./ContractStandard.md)