# Node Interface - CloudSec

## Fault view

```
# iserver get aci intf cloudsec --apic apic21 --node bl2205-eu-spdc --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface CloudSec - Faults [#0]
--------------------------------
None
```

Developer

```
# iserver get aci intf cloudsec --apic apic21 --node bl2205-eu-spdc --view fault

{
    "duration": 1501,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 528,
        "disconnect_time": 0,
        "mo_time": 788,
        "total_time": 1316
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

True	528	-	connect apic21o.emea-sp.cisco.com:443
True	410	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	378	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceCloudSec.md)