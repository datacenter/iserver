# L2 Domain

## Event view

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view event

Apic: apic21 (mode:online, cache:off)

L2 Domain - Event Logs last 10y [#0]
------------------------------------
None
```

Developer

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view event

{
    "duration": 1471,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 460,
        "disconnect_time": 0,
        "mo_time": 780,
        "total_time": 1240
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

True	460	-	connect apic21o.emea-sp.cisco.com:443
True	367	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	413	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL2.md)