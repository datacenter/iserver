# L3 Domain

## Fault view

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --view fault

Apic: apic21 (mode:online, cache:off)

L3 Domain - Faults [#0]
-----------------------
None
```

Developer

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --view fault

{
    "duration": 1389,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 443,
        "disconnect_time": 0,
        "mo_time": 739,
        "total_time": 1182
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

True	443	-	connect apic21o.emea-sp.cisco.com:443
True	376	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	363	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./DomainL3.md)