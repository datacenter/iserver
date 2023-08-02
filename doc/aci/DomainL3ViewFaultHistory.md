# L3 Domain

## Fault history view

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view hfault

Apic: apic21 (mode:online, cache:off)

L3 Domain - Fault Records last 10y [#0]
---------------------------------------
None
```

Developer

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view hfault

{
    "duration": 1858,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 453,
        "disconnect_time": 0,
        "mo_time": 1179,
        "total_time": 1632
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

True	453	-	connect apic21o.emea-sp.cisco.com:443
True	374	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	805	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL3.md)