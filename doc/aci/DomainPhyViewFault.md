# Physical Domain

## Fault view

```
# iserver get aci domain phy --apic apic21 --name UCSB* --view fault

Apic: apic21 (mode:online, cache:off)

Physical Domain - Faults [#0]
-----------------------------
None
```

Developer

```
# iserver get aci domain phy --apic apic21 --name UCSB* --view fault

{
    "duration": 1806,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 495,
        "disconnect_time": 0,
        "mo_time": 824,
        "total_time": 1319
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

True	495	-	connect apic21o.emea-sp.cisco.com:443
True	422	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	402	0	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./DomainPhy.md)