# Node Interface - CloudSec

## All view

```
# iserver get aci intf cloudsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface CloudSec State [#0]
-----------------------------
None

Interface CloudSec - Faults [#0]
--------------------------------
None

Interface CloudSec - Fault Records last 10y [#0]
------------------------------------------------
None

Interface CloudSec - Event Logs last 10y [#0]
---------------------------------------------
None

Interface CloudSec - Audit Logs last 10y [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci intf cloudsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view all

{
    "duration": 1620,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 531,
        "disconnect_time": 0,
        "mo_time": 856,
        "total_time": 1387
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

True	531	-	connect apic21o.emea-sp.cisco.com:443
True	424	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	432	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205 query query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceCloudSec.md)