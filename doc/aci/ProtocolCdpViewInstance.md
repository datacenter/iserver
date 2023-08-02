# Node Protocol - CDP

## Inst view

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol CDP - Instance [#1]
----------------------------

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| cl201-eu-spdc | enabled     | v2          | 60                 | 180           | 19            | 18                | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view inst

{
    "duration": 2466,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 1918,
        "total_time": 2323
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

True	405	-	connect apic11o.emea-sp.cisco.com:443
True	313	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	766	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/cdp/inst
True	331	19	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	508	100	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)