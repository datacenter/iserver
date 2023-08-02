# Node Protocol - HSRP

## Intf view

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Interface [#0]
------------------------------
None
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view intf

{
    "duration": 1101,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 575,
        "total_time": 970
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	395	-	connect apic11o.emea-sp.cisco.com:443
True	303	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	272	0	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolHsrp.md)