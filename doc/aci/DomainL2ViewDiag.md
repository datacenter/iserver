# L2 Domain

## Diag view

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view diag

Apic: apic21 (mode:online, cache:off)

L2 Domain - Faults [#0]
-----------------------
None

L2 Domain - Fault Records last 10y [#0]
---------------------------------------
None

L2 Domain - Event Logs last 10y [#0]
------------------------------------
None

L2 Domain - Audit Logs last 10y [#0]
------------------------------------
None
```

Developer

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view diag

{
    "duration": 3210,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 815,
        "disconnect_time": 0,
        "mo_time": 1986,
        "total_time": 2801
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

True	815	-	connect apic21o.emea-sp.cisco.com:443
True	374	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	368	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=faults,no-scoped,subtree
True	416	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	420	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	408	5	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL2.md)