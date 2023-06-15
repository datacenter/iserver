# Node Protocol - CDP

## Filter CDP neighbors by neighbor's advertised capabilities

```
# iserver get aci proto cdp --apic apic11 --node rl --cap *switch*

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------------+----------------------+----------------+--------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name | Platform       | Port         | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+----------------------+----------------+--------------+--------+------+-------------+---------------------------------------+
| pod-1/rl301-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454    | Ethernet1/46 | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B   | UCS-FI-6454    | Ethernet1/46 | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/41 | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454    | Ethernet1/45 | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B   | UCS-FI-6454    | Ethernet1/45 | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/42 | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+----------------------+----------------+--------------+--------+------+-------------+---------------------------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl --cap *switch*

{
    "duration": 3515,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 489,
        "disconnect_time": 0,
        "mo_time": 2479,
        "total_time": 2968
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

True	489	-	connect apic11o.emea-sp.cisco.com
True	326	13	apic11o.emea-sp.cisco.com class fabricNode
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	359	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	361	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	355	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	382	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)