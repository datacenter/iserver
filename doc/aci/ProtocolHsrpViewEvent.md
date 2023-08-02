# Node Protocol - HSRP

## Event view

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view event
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

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
    --view event
    --when 90d

{
    "duration": 1309,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 428,
        "disconnect_time": 0,
        "mo_time": 730,
        "total_time": 1158
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

True	428	-	connect apic11o.emea-sp.cisco.com:443
True	337	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	393	3	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolHsrp.md)