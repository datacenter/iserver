# Node Protocol - CDP

## Filter CDP neighbors by neighbor's system name

```
# iserver get aci proto cdp --apic apic11 --node rl --sys *r23*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------------+----------------------+----------------+--------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name | Platform       | Port         | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+----------------------+----------------+--------------+--------+------+-------------+---------------------------------------+
| pod-1/rl301-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/41 | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/42 | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+----------------------+----------------+--------------+--------+------+-------------+---------------------------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl --sys *r23*

{
    "duration": 2816,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 2245,
        "total_time": 2666
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

True	421	-	connect apic11o.emea-sp.cisco.com
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
True	366	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	304	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	311	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	296	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	302	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)