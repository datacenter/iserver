# Node Protocol - CDP

## Show CDP state summary for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node rl --view instance

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| rl301-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
| rl302-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl --view instance

{
    "duration": 2939,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 2213,
        "total_time": 2657
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

True	444	-	connect apic11o.emea-sp.cisco.com
True	362	13	apic11o.emea-sp.cisco.com class fabricNode
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	316	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	343	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	315	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	317	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)