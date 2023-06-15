# Node Protocol - BGP

## Show BGP state summary for all nodes

```
# iserver get aci proto bgp --apic apic11 --node any --view node

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

+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| Node                | Admin State | ASN   | VRF (Up/Count) | Neighbors (Up/Count) | AS Path Entries | Attribute Entries | Memory Status | SNMP Trap | Syslog Level |
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| pod-1/bl205-eu-spdc | enabled     | 50000 | 27/27          | 13/20                | 18              | 293               | normal        | disable   | err          | 
| pod-1/bl206-eu-spdc | enabled     | 50000 | 26/26          | 13/20                | 18              | 292               | normal        | disable   | err          | 
| pod-1/cl201-eu-spdc | enabled     | 50000 | 30/30          | 2/33                 | 15              | 299               | normal        | disable   | err          | 
| pod-1/cl202-eu-spdc | enabled     | 50000 | 30/30          | 2/33                 | 15              | 299               | normal        | disable   | err          | 
| pod-1/cl209-eu-spdc | enabled     | 50000 | 1/1            | 2/2                  | 0               | 1                 | normal        | disable   | err          | 
| pod-1/cl210-eu-spdc | enabled     | 50000 | 1/1            | 2/2                  | 0               | 3                 | normal        | disable   | err          | 
| pod-1/rl301-eu-spdc | enabled     | 50000 | 18/18          | 5/7                  | 19              | 248               | normal        | disable   | err          | 
| pod-1/rl302-eu-spdc | enabled     | 50000 | 18/18          | 5/7                  | 19              | 248               | normal        | disable   | err          | 
| pod-1/s101-eu-spdc  | enabled     | 50000 | 3/3            | 10/10                | 20              | 92                | normal        | disable   | err          | 
| pod-1/s102-eu-spdc  | enabled     | 50000 | 3/3            | 10/10                | 20              | 92                | normal        | disable   | err          | 
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any --view node

{
    "duration": 12161,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 485,
        "disconnect_time": 0,
        "mo_time": 10537,
        "total_time": 11022
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

True	485	-	connect apic11o.emea-sp.cisco.com
True	333	13	apic11o.emea-sp.cisco.com class fabricNode
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	343	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	367	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	296	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	340	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	335	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	341	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	349	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	390	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bgp/inst
True	356	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/bgpDom
True	361	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bgp/inst
True	352	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/bgpDom
True	334	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	394	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	408	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	396	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	357	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	344	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	377	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	308	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	318	41	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	289	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	305	41	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)