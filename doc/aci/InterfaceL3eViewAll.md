# Node Interface - Encapsulated Routed

## All view

```
# iserver get aci intf l3e
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id eth1/35*
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+--------+---------+-----------+-------+------+--------+---------+------+--------------------+-------+-------------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf | Delay | Router MAC        |
+----------------------+--------+---------+-----------+-------+------+--------+---------+------+--------------------+-------+-------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/35.9 | up    | up   | vlan-2 | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
+----------------------+--------+---------+-----------+-------+------+--------+---------+------+--------------------+-------+-------------------+

Interface Encapsulated Routed - Faults [#0]
-------------------------------------------
None

Interface Encapsulated Routed - Fault Records last 10y [#0]
-----------------------------------------------------------
None

Interface Encapsulated Routed - Event Logs last 10y [#0]
--------------------------------------------------------
None

Interface Encapsulated Routed - Audit Logs last 10y [#0]
--------------------------------------------------------
None
```

Developer

```
# iserver get aci intf l3e
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id eth1/35*
    --view all

{
    "duration": 3920,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 509,
        "disconnect_time": 0,
        "mo_time": 3054,
        "total_time": 3563
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

True	509	-	connect apic21o.emea-sp.cisco.com:443
True	502	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	419	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	416	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
True	419	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	459	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	426	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	413	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceL3e.md)