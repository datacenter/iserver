# Node Interface - MacSec

## All view

```
# iserver get aci intf macsec
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id eth1/28
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface MacSec - State [#1]
-----------------------------

+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| Node                 | Health | Faults  | Interface | Admin    | Oper | Reason     | Session         | Peers | Cepher Suite | Confid Offset | Ker Server Prio | Replay Window |
+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/28   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+

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
    --id eth1/28
    --view all

{
    "duration": 5894,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 615,
        "disconnect_time": 0,
        "mo_time": 4969,
        "total_time": 5584
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

True	615	-	connect apic21o.emea-sp.cisco.com:443
True	441	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	492	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1159	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	420	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	483	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	666	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	634	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	674	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceMacSec.md)