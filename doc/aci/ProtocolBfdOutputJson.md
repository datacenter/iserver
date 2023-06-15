# Node Protocol - BFD

## JSON

```
# iserver get aci proto bfd --apic apic11 --node cl201-eu-spdc -o json

[
    {
        "instance": {
            "__Output": {
                "adminSt": "Green",
                "sessionSummary": "Green"
            },
            "adminSt": "enabled",
            "childAction": "",
            "ctrl": "",
            "dn": "topology/pod-1/node-201/sys/bfd/inst",
            "echoIf": "unspecified",
            "lcOwn": "local",
            "maxLimitReached": "no",
            "modTs": "2023-06-12T09:12:18.104+02:00",
            "monPolDn": "uni/fabric/monfab-default",
            "name": "",
            "operErr": "",
            "status": "",
            "unsupportedTimersForScale": "no",
            "pod_node_name": "pod-1/cl201-eu-spdc",
            "sessionSummary": "0/0"
        },
        "sessions": [],
        "interfaces": []
    }
]
```

[[Back]](./ProtocolBfd.md)