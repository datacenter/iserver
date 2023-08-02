# Node Interface - MacSec

## Event view

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface MacSec - Event Logs last 10y [#0]
-------------------------------------------
None
```

Developer

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

{
    "duration": 3753,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 573,
        "disconnect_time": 0,
        "mo_time": 2908,
        "total_time": 3481
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

True	573	-	connect apic21o.emea-sp.cisco.com:443
True	411	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	531	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1053	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	377	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	536	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceMacSec.md)