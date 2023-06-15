# Node Protocol - CDP

## Show CDP neighbors details for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------------+----------------------+----------------+-----------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name | Platform       | Port            | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+----------------------+----------------+-----------------+--------+------+-------------+---------------------------------------+
| pod-1/rl301-eu-spdc | eth1/29         | Berlin-35.cisco.com  | cisco NCS-5500 | TenGigE0/0/0/29 | full   | 0    |             | router                                | 
| pod-1/rl301-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454    | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B   | UCS-FI-6454    | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/41    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/29         | Berlin-35.cisco.com  | cisco NCS-5500 | TenGigE0/0/0/28 | full   | 0    |             | router                                | 
| pod-1/rl302-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454    | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B   | UCS-FI-6454    | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/42    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+----------------------+----------------+-----------------+--------+------+-------------+---------------------------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl

{
    "duration": 3270,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 495,
        "disconnect_time": 0,
        "mo_time": 2390,
        "total_time": 2885
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

True	495	-	connect apic11o.emea-sp.cisco.com
True	331	13	apic11o.emea-sp.cisco.com class fabricNode
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	315	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	335	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	357	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	366	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	367	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)