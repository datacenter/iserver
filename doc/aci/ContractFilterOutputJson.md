# Contract Filter

## JSON output

```
# iserver get aci contract filter --apic apic21 --name k8s/icmp -o json

[
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
        "isAnyFault": false
    }
]
```

[[Back]](./ContractFilter.md)