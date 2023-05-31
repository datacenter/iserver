# Node Protocol - BGP

## Filter BGP neighbors by source interface

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

```
# iserver get aci proto bgp --apic apic11 --node any --intf lo9 --view trans

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

+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| Node                | VRF                      | Neighbor Address | Router Id  | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP    |
+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 172.24.3.1 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 172.24.3.2 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any --intf lo9 --view trans

{
    "duration": 8407,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 380,
        "disconnect_time": 0,
        "mo_time": 7615,
        "total_time": 7995
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

True	380	-	connect apic11o.emea-sp.cisco.com
True	290	11	apic11o.emea-sp.cisco.com class fabricNode
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	288	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	317	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	276	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	285	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	322	78	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	318	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	318	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	303	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	326	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	298	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	338	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	339	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	294	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	314	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	293	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	277	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	292	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)