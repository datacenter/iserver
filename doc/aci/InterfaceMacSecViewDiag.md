# Node Interface - MacSec

## Diag view

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view diag

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface MacSec - Faults [#0]
------------------------------
None

Interface MacSec - Fault Records last 10y [#0]
----------------------------------------------
None

Interface MacSec - Event Logs last 10y [#0]
-------------------------------------------
None

Interface MacSec - Audit Logs last 10y [#0]
-------------------------------------------
None
```

Developer

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view diag

{
    "duration": 5714,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 503,
        "disconnect_time": 0,
        "mo_time": 4862,
        "total_time": 5365
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

True	503	-	connect apic21o.emea-sp.cisco.com:443
True	391	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	457	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1285	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	457	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	503	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	619	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	547	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	603	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceMacSec.md)