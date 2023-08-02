# Node Protocol - ARP

## Event view

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view event

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

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
    --view event

{
    "duration": 1111,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 566,
        "total_time": 955
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

True	389	-	connect apic21o.emea-sp.cisco.com:443
True	273	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	293	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolArp.md)