# Node Protocol - CDP

## Show CDP state summary for all nodes

```
# iserver get aci proto cdp --apic apic11 --node any --view instance

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
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
| cl209-eu-spdc | enabled     | v2          | 60                 | 180           | 0             | 0                 | 
| cl210-eu-spdc | enabled     | v2          | 60                 | 180           | 0             | 0                 | 
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
    "duration": 11774,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 418,
        "disconnect_time": 0,
        "mo_time": 10263,
        "total_time": 10681
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

True	418	-	connect apic11o.emea-sp.cisco.com
True	311	13	apic11o.emea-sp.cisco.com class fabricNode
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst
True	292	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	280	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst
True	288	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	309	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	322	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	331	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst
True	337	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	333	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst
True	370	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	433	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	378	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	357	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	346	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	393	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	309	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	354	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	328	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	329	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)