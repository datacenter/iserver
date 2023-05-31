# Node Protocol - CDP

## Show CDP state summary for selected node

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
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
    "duration": 1792,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 1281,
        "total_time": 1663
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
    }
}

Log: apic
----------

True	382	-	connect apic11o.emea-sp.cisco.com
True	312	11	apic11o.emea-sp.cisco.com class fabricNode
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	311	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	367	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)