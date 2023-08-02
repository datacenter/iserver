# Node Interface - CloudSec

## Fault history view

```
# iserver get aci intf cloudsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface CloudSec - Fault Records last 10y [#0]
------------------------------------------------
None
```

Developer

```
# iserver get aci intf cloudsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

{
    "duration": 1489,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 537,
        "disconnect_time": 0,
        "mo_time": 808,
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

True	537	-	connect apic21o.emea-sp.cisco.com:443
True	406	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	402	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceCloudSec.md)