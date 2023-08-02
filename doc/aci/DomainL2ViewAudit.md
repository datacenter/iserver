# L2 Domain

## Audit view

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view audit

Apic: apic21 (mode:online, cache:off)

L2 Domain - Audit Logs last 10y [#0]
------------------------------------
None
```

Developer

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view audit

{
    "duration": 1473,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 477,
        "disconnect_time": 0,
        "mo_time": 759,
        "total_time": 1236
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

True	477	-	connect apic21o.emea-sp.cisco.com:443
True	347	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	412	5	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL2.md)