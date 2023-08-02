# Node Protocol - HSRP

## Diag view

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view diag
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Event Logs [#0]
-------------------------------
None

Protocol HSRP - Event Logs [#0]
-------------------------------
None

Protocol HSRP - Event Logs [#1]
-------------------------------

+---------------------+------+----------+--------------------+-------------------------------+------------------------------------+-----------------------------------+
| Node                | Sev  | Code     | Cause              | Created Time                  | Description                        | Affected                          |
+---------------------+------+----------+--------------------+-------------------------------+------------------------------------+-----------------------------------+
| pod-1/cl201-eu-spdc | Info | E4210476 | admin-state-change | 2023-05-31T23:11:11.462+02:00 | HSRP instance is administratively  | topology/pod-1/node-201/sys/hsrp/ | 
|                     |      |          |                    |                               | Enabled                            | inst-default                      | 
+---------------------+------+----------+--------------------+-------------------------------+------------------------------------+-----------------------------------+
```

Developer

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view diag
    --when 90d

{
    "duration": 1956,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 1402,
        "total_time": 1796
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

True	394	-	connect apic11o.emea-sp.cisco.com:443
True	288	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	320	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=faults,no-scoped,subtree
True	400	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	394	3	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolHsrp.md)