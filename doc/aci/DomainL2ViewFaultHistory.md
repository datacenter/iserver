# L2 Domain

## Fault history view

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view hfault

Apic: apic21 (mode:online, cache:off)

L2 Domain - Fault Records last 10y [#0]
---------------------------------------
None
```

Developer

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view hfault

{
    "duration": 1593,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 526,
        "disconnect_time": 0,
        "mo_time": 811,
        "total_time": 1337
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

True	526	-	connect apic21o.emea-sp.cisco.com:443
True	377	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	434	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL2.md)