# Node Protocol - CDP

## Show CDP neighbors details for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node rl

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
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
    "duration": 2734,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 2183,
        "total_time": 2600
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

True	417	-	connect apic11o.emea-sp.cisco.com
True	305	11	apic11o.emea-sp.cisco.com class fabricNode
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	293	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	307	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	325	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	308	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)