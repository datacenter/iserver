# VLAN Pool

## Fault history view

```
# iserver get aci pool vlan --apic apic21 --when any --view hfault

Apic: apic21 (mode:online, cache:off)

Pool VLAN - Fault Records last 10y [#0]
---------------------------------------
None
```

Developer

```
# iserver get aci pool vlan --apic apic21 --when any --view hfault

{
    "duration": 1552,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 381,
        "disconnect_time": 0,
        "mo_time": 964,
        "total_time": 1345
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

True	381	-	connect apic21o.emea-sp.cisco.com:443
True	317	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	647	0	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./PoolVlan.md)