# L2 Domain

## Fault view

```
# iserver get aci domain l2 --apic apic21 --name infra* --view fault

Apic: apic21 (mode:online, cache:off)

L2 Domain - Faults [#0]
-----------------------
None
```

Developer

```
# iserver get aci domain l2 --apic apic21 --name infra* --view fault

{
    "duration": 1337,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 707,
        "total_time": 1151
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

True	444	-	connect apic21o.emea-sp.cisco.com:443
True	365	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	342	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./DomainL2.md)