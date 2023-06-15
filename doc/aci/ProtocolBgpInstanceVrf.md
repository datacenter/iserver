# Node Protocol - BGP

## Show BGP selected VRF domains for selected nodes

```
# iserver get aci proto bgp --apic apic11 --node any --vrf overlay-1 --view vrf

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

+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
| Node                | VRF       | BGP State | Mode   | Router ID       | RD                  | Neighbors | Established |
+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
| pod-1/bl205-eu-spdc | overlay-1 | up        | fabric | 125.125.125.125 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/bl206-eu-spdc | overlay-1 | up        | fabric | 126.126.126.126 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/cl201-eu-spdc | overlay-1 | up        | fabric | 10.3.192.67     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/cl202-eu-spdc | overlay-1 | up        | fabric | 10.3.192.68     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/cl209-eu-spdc | overlay-1 | up        | fabric | 10.3.136.64     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/cl210-eu-spdc | overlay-1 | up        | fabric | 10.3.136.65     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/rl301-eu-spdc | overlay-1 | up        | fabric | 131.131.131.131 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/rl302-eu-spdc | overlay-1 | up        | fabric | 132.132.132.132 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/s101-eu-spdc  | overlay-1 | up        | fabric | 101.101.101.101 | unknown:unknown:0:0 | 10        | 10          | 
| pod-1/s102-eu-spdc  | overlay-1 | up        | fabric | 102.102.102.102 | unknown:unknown:0:0 | 10        | 10          | 
+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any --vrf overlay-1 --view vrf

{
    "duration": 11569,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 449,
        "disconnect_time": 0,
        "mo_time": 10201,
        "total_time": 10650
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

True	449	-	connect apic11o.emea-sp.cisco.com
True	327	13	apic11o.emea-sp.cisco.com class fabricNode
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	317	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	341	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	300	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	311	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	319	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	354	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	306	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	322	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bgp/inst
True	607	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/bgpDom
True	298	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bgp/inst
True	373	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/bgpDom
True	304	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	305	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	347	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	335	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	297	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	293	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	306	41	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	386	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	294	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	327	41	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)