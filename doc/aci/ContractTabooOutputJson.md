# Taboo Contract

## JSON output

```
# iserver get aci contract taboo --apic apic21 --name k8s/my* -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "descr": "",
        "dn": "uni/tn-k8s/taboo-MyTabooContract",
        "name": "MyTabooContract",
        "reevaluateAll": "no",
        "scope": "context",
        "status": "",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/MyTabooContract",
        "vzFilter": [
            {
                "__Output": {
                    "faults": ":R.M.Y.G"
                },
                "descr": "",
                "dn": "uni/tn-k8s/flt-icmp",
                "name": "icmp",
                "userdom": ":all:common:",
                "tenant": "k8s",
                "nameTenant": "k8s/icmp",
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
                        "name": "icmp",
                        "prot": "icmp",
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
                "subjectName": "MyTabooSubject",
                "subjectTenant": "k8s",
                "subjectNameTenant": "k8s/MyTabooSubject"
            }
        ],
        "protectedEpg": [
            {
                "class": "fvAEPg",
                "tenant": "k8s",
                "application_profile": "k8s_ANP",
                "name": "SRIoV_A",
                "nameTenant": "k8s/SRIoV_A",
                "nameLong": "k8s/k8s_ANP/SRIoV_A"
            }
        ],
        "faults": "0 0 0 0",
        "isAnyFault": false
    }
]
```

[[Back]](./ContractTaboo.md)