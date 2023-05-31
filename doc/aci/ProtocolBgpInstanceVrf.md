# Node Protocol - BGP

## Show BGP selected VRF domains for selected nodes

```
# iserver get aci proto bgp --apic apic11 --node any --vrf overlay-1 --view vrf

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

+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
| Node                | VRF       | BGP State | Mode   | Router ID       | RD                  | Neighbors | Established |
+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
| pod-1/bl205-eu-spdc | overlay-1 | up        | fabric | 125.125.125.125 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/bl206-eu-spdc | overlay-1 | up        | fabric | 126.126.126.126 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/cl201-eu-spdc | overlay-1 | up        | fabric | 10.3.192.67     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/cl202-eu-spdc | overlay-1 | up        | fabric | 10.3.192.68     | unknown:unknown:0:0 | 2         | 2           | 
| pod-1/rl301-eu-spdc | overlay-1 | up        | fabric | 131.131.131.131 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/rl302-eu-spdc | overlay-1 | up        | fabric | 132.132.132.132 | unknown:unknown:0:0 | 4         | 4           | 
| pod-1/s101-eu-spdc  | overlay-1 | up        | fabric | 101.101.101.101 | unknown:unknown:0:0 | 8         | 8           | 
| pod-1/s102-eu-spdc  | overlay-1 | up        | fabric | 102.102.102.102 | unknown:unknown:0:0 | 8         | 8           | 
+---------------------+-----------+-----------+--------+-----------------+---------------------+-----------+-------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any --vrf overlay-1 --view vrf

{
    "duration": 9185,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 8395,
        "total_time": 8784
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

True	389	-	connect apic11o.emea-sp.cisco.com
True	1114	11	apic11o.emea-sp.cisco.com class fabricNode
True	274	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	292	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	305	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	281	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	303	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	308	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	321	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	338	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	282	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	358	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	297	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	301	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	290	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	294	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	301	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	320	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	279	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	295	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)