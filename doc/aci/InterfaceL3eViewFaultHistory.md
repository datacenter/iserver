# Node Interface - Encapsulated Routed

## Fault history view

```
# iserver get aci intf l3e
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Encapsulated Routed - Fault Records last 10y [#5]
-----------------------------------------------------------

+----------------------+------------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| Node                 | Interface  | Sev  | Code    | Cause             | Created Time                  | Lifecycle | Description                                                                    |
+----------------------+------------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | eth1/25.19 | Warn | F112128 | threshold-crossed | 2023-07-24T20:18:31.256+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 18 raised above  | 
|                      |            |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | Warn | F112128 | threshold-crossed | 2023-07-24T20:20:32.237+02:00 | raised    | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 56 raised above  | 
|                      |            |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | --   | F112128 | threshold-crossed | 2023-07-24T20:20:32.232+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below     | 
|                      |            |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | --   | F112128 | threshold-crossed | 2023-07-24T20:22:35.248+02:00 | retaining | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 8 fell below     | 
|                      |            |      |         |                   |                               |           | threshold 10                                                                   | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | --   | F112128 | threshold-crossed | 2023-07-24T21:23:01.591+02:00 |           | TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 8 fell below     | 
|                      |            |      |         |                   |                               |           | threshold 10                                                                   | 
+----------------------+------------+------+---------+-------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf l3e
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

{
    "duration": 3481,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 584,
        "disconnect_time": 0,
        "mo_time": 2430,
        "total_time": 3014
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

True	584	-	connect apic21o.emea-sp.cisco.com:443
True	394	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	381	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	1035	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
True	620	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceL3e.md)