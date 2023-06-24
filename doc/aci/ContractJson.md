# Contract

## JSON

```
# iserver get aci contract --apic apic21 --type filter --name k8s/* -o json

[
    {
        "__Output": {},
        "descr": "",
        "dn": "uni/tn-k8s/flt-alltraffic",
        "name": "alltraffic",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/alltraffic",
        "vzEntry": [
            {
                "__Output": {},
                "applyToFrag": "no",
                "arpOpc": "",
                "dFromPort": "unspecified",
                "dToPort": "unspecified",
                "descr": "",
                "etherT": "",
                "icmpv4T": "unspecified",
                "icmpv6T": "unspecified",
                "matchDscp": "unspecified",
                "name": "alltraffic",
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
        "subjectName": "Any",
        "subjectTenant": "k8s",
        "subjectNameTenant": "k8s/Any",
        "taboo": [],
        "contract": [
            "k8s/BT-Demo"
        ]
    },
    {
        "__Output": {},
        "descr": "",
        "dn": "uni/tn-k8s/flt-http",
        "name": "http",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/http",
        "vzEntry": [
            {
                "__Output": {},
                "applyToFrag": "no",
                "arpOpc": "",
                "dFromPort": "http",
                "dToPort": "http",
                "descr": "",
                "etherT": "ipv4",
                "icmpv4T": "unspecified",
                "icmpv6T": "unspecified",
                "matchDscp": "unspecified",
                "name": "http",
                "prot": "tcp",
                "sFromPort": "unspecified",
                "sToPort": "unspecified",
                "stateful": "no",
                "status": "",
                "tcpRules": "",
                "source": "",
                "destination": "http - http"
            }
        ],
        "taboo": [],
        "contract": []
    },
    {
        "__Output": {},
        "descr": "",
        "dn": "uni/tn-k8s/flt-https",
        "name": "https",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/https",
        "vzEntry": [
            {
                "__Output": {},
                "applyToFrag": "no",
                "arpOpc": "",
                "dFromPort": "https",
                "dToPort": "https",
                "descr": "",
                "etherT": "ipv4",
                "icmpv4T": "unspecified",
                "icmpv6T": "unspecified",
                "matchDscp": "unspecified",
                "name": "https",
                "prot": "tcp",
                "sFromPort": "unspecified",
                "sToPort": "unspecified",
                "stateful": "no",
                "status": "",
                "tcpRules": "",
                "source": "",
                "destination": "https - https"
            }
        ],
        "taboo": [],
        "contract": []
    },
    {
        "__Output": {},
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
        "subjectName": "MyTabooSubject",
        "subjectTenant": "k8s",
        "subjectNameTenant": "k8s/MyTabooSubject",
        "taboo": [
            "k8s/MyTabooContract"
        ],
        "contract": []
    },
    {
        "__Output": {},
        "descr": "",
        "dn": "uni/tn-k8s/flt-ssh",
        "name": "ssh",
        "userdom": ":all:common:",
        "tenant": "k8s",
        "nameTenant": "k8s/ssh",
        "vzEntry": [
            {
                "__Output": {},
                "applyToFrag": "no",
                "arpOpc": "",
                "dFromPort": "ssh",
                "dToPort": "ssh",
                "descr": "",
                "etherT": "ipv4",
                "icmpv4T": "unspecified",
                "icmpv6T": "unspecified",
                "matchDscp": "unspecified",
                "name": "ssh",
                "prot": "tcp",
                "sFromPort": "unspecified",
                "sToPort": "unspecified",
                "stateful": "no",
                "status": "",
                "tcpRules": "",
                "source": "",
                "destination": "ssh - ssh"
            }
        ],
        "taboo": [],
        "contract": []
    }
]
```

[[Back]](./Contract.md)