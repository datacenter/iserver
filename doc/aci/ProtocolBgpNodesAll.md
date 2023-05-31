# Node Protocol - BGP

## Show BGP state summary for all nodes

```
# iserver get aci proto bgp --apic apic11 --node any --view node

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

+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| Node                | Admin State | ASN   | VRF (Up/Count) | Neighbors (Up/Count) | AS Path Entries | Attribute Entries | Memory Status | SNMP Trap | Syslog Level |
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| pod-1/bl205-eu-spdc | enabled     | 50000 | 27/27          | 25/26                | 27              | 336               | normal        | disable   | err          | 
| pod-1/bl206-eu-spdc | enabled     | 50000 | 26/26          | 25/26                | 27              | 336               | normal        | disable   | err          | 
| pod-1/cl201-eu-spdc | enabled     | 50000 | 30/30          | 9/33                 | 23              | 333               | normal        | disable   | err          | 
| pod-1/cl202-eu-spdc | enabled     | 50000 | 30/30          | 8/33                 | 23              | 334               | normal        | disable   | err          | 
| pod-1/rl301-eu-spdc | enabled     | 50000 | 18/18          | 7/7                  | 25              | 274               | normal        | disable   | err          | 
| pod-1/rl302-eu-spdc | enabled     | 50000 | 18/18          | 7/7                  | 25              | 276               | normal        | disable   | err          | 
| pod-1/s101-eu-spdc  | enabled     | 50000 | 3/3            | 8/8                  | 29              | 116               | normal        | disable   | err          | 
| pod-1/s102-eu-spdc  | enabled     | 50000 | 3/3            | 8/8                  | 29              | 116               | normal        | disable   | err          | 
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any --view node

{
    "duration": 8199,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 418,
        "disconnect_time": 0,
        "mo_time": 7401,
        "total_time": 7819
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

True	418	-	connect apic11o.emea-sp.cisco.com
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
True	281	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	284	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	317	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	300	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	302	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	295	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	312	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	269	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	299	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	305	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	293	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	293	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	306	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	293	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	285	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	312	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	281	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	293	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)