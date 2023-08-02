# Physical Domain

## Event view

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view event

Apic: apic21 (mode:online, cache:off)

Physical Domain - Event Logs last 10y [#0]
------------------------------------------
None
```

Developer

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view event

{
    "duration": 2413,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 488,
        "disconnect_time": 0,
        "mo_time": 1162,
        "total_time": 1650
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

True	488	-	connect apic21o.emea-sp.cisco.com:443
True	381	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	781	0	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./DomainPhy.md)