# Node Protocol - CDP

## Show CDP state summary for selected node

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view instance

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| cl201-eu-spdc | enabled     | v2          | 60                 | 180           | 17            | 16                | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view instance

{
    "duration": 1994,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1292,
        "total_time": 1728
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

True	436	-	connect apic11o.emea-sp.cisco.com
True	328	13	apic11o.emea-sp.cisco.com class fabricNode
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	323	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	353	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)