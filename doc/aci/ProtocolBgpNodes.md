# Node Protocol - BGP

## Show BGP state summary for selected nodes

```
# iserver get aci proto bgp --apic apic11 --node rl --view node

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| Node                | Admin State | ASN   | VRF (Up/Count) | Neighbors (Up/Count) | AS Path Entries | Attribute Entries | Memory Status | SNMP Trap | Syslog Level |
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| pod-1/rl301-eu-spdc | enabled     | 50000 | 18/18          | 5/7                  | 19              | 248               | normal        | disable   | err          | 
| pod-1/rl302-eu-spdc | enabled     | 50000 | 18/18          | 5/7                  | 19              | 248               | normal        | disable   | err          | 
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --view node

{
    "duration": 2764,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 2107,
        "total_time": 2521
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

True	414	-	connect apic11o.emea-sp.cisco.com
True	308	13	apic11o.emea-sp.cisco.com class fabricNode
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	295	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	308	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	280	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	335	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)