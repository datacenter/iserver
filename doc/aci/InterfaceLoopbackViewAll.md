# Node Interface - Loopback

## All view

```
# iserver get aci intf lb
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id lo8
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                 | Health | Faults  | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+

Interface Loopback - Faults [#0]
--------------------------------
None

Interface Loopback - Fault Records last 10y [#0]
------------------------------------------------
None

Interface Loopback - Event Logs last 10y [#0]
---------------------------------------------
None

Interface Loopback - Audit Logs last 10y [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci intf lb
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id lo8
    --view all

{
    "duration": 4464,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 597,
        "disconnect_time": 0,
        "mo_time": 3421,
        "total_time": 4018
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

True	597	-	connect apic21o.emea-sp.cisco.com:443
True	509	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	417	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	411	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	496	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	586	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	536	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	466	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceLoopback.md)