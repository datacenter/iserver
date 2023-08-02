# Node Protocol - ARP

## Diag view

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view diag

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Faults [#0]
--------------------------
None

Protocol ARP - Fault Records last 10y [#0]
------------------------------------------
None

Protocol ARP - Event Logs last 10y [#2]
---------------------------------------

+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
| Node                 | Sev  | Code     | Cause              | Created Time                  | Description                       | Affected                              |
+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
| pod-1/bl2205-eu-spdc | Info | E4208089 | admin-state-change | 2023-06-12T09:51:01.479+02:00 | ARP instance is administratively  | topology/pod-1/node-2205/sys/arp/inst | 
|                      |      |          |                    |                               | Enabled                           |                                       | 
+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
| pod-1/bl2205-eu-spdc | Info | E4208089 | admin-state-change | 2023-06-18T09:37:07.519+02:00 | ARP instance is administratively  | topology/pod-1/node-2205/sys/arp/inst | 
|                      |      |          |                    |                               | Enabled                           |                                       | 
+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
```

Developer

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view diag

{
    "duration": 1758,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 1105,
        "total_time": 1532
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

True	427	-	connect apic21o.emea-sp.cisco.com:443
True	276	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	261	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=faults,no-scoped,subtree
True	286	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	282	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolArp.md)