# Node Protocol - CDP

## Show CDP state summary for all nodes

```
# iserver get aci proto cdp --apic apic11 --node any --view instance

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| System Name   | Admin State | CDP Version | Transmit Frequency | Hold Interval | CDP Neighbors | Active Interfaces |
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
| bl205-eu-spdc | enabled     | v2          | 60                 | 180           | 8             | 8                 | 
| bl206-eu-spdc | enabled     | v2          | 60                 | 180           | 8             | 8                 | 
| cl201-eu-spdc | enabled     | v2          | 60                 | 180           | 17            | 16                | 
| cl202-eu-spdc | enabled     | v2          | 60                 | 180           | 15            | 15                | 
| rl301-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
| rl302-eu-spdc | enabled     | v2          | 60                 | 180           | 4             | 4                 | 
| s101-eu-spdc  | enabled     | v2          | 60                 | 180           | 1             | 1                 | 
| s102-eu-spdc  | enabled     | v2          | 60                 | 180           | 1             | 1                 | 
+---------------+-------------+-------------+--------------------+---------------+---------------+-------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node any --view instance

{
    "duration": 8665,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 7857,
        "total_time": 8252
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	308	11	apic11o.emea-sp.cisco.com class fabricNode
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst
True	287	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	303	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst
True	289	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	313	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	336	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	327	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst
True	315	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	390	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	389	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	321	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	303	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	316	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	313	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	357	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	285	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)