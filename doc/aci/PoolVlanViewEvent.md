# VLAN Pool

## Event view

```
# iserver get aci pool vlan --apic apic21 --when any --view event

Apic: apic21 (mode:online, cache:off)

Pool VLAN - Event Logs last 10y [#0]
------------------------------------
None
```

Developer

```
# iserver get aci pool vlan --apic apic21 --when any --view event

{
    "duration": 1406,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 370,
        "disconnect_time": 0,
        "mo_time": 929,
        "total_time": 1299
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

True	370	-	connect apic21o.emea-sp.cisco.com:443
True	305	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	624	0	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./PoolVlan.md)