# Node Interface - MacSec

## Fault history view

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface MacSec - Fault Records last 10y [#0]
----------------------------------------------
None
```

Developer

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

{
    "duration": 5214,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 569,
        "disconnect_time": 0,
        "mo_time": 3242,
        "total_time": 3811
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

True	569	-	connect apic21o.emea-sp.cisco.com:443
True	388	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	640	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1201	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	482	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	531	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceMacSec.md)