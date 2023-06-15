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

+---------------------+-------------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| Node                | VRF                           | Neighbor Address | Router Id  | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP    |
+---------------------+-------------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1       | 0.0.0.0    | enabled     | idle        | 64271 | ebgp | 4   | lo9         | 0.0.0.0     | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.101     | 0.0.0.0    | enabled     | idle        | 65100 | ebgp | 5   | lo9         | 0.0.0.0     | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.41      | 0.0.0.0    | enabled     | idle        | 65101 | ebgp | 5   | lo9         | 0.0.0.0     | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.1       | 0.0.0.0    | enabled     | idle        | 64371 | ebgp | 4   | lo9         | 0.0.0.0     | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.2       | 0.0.0.0    | enabled     | idle        | 64371 | ebgp | 4   | lo9         | 0.0.0.0     | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.3       | 172.24.3.3 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.15 | 
+---------------------+-------------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node any --intf lo9 --view trans

{
    "duration": 11987,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 10337,
        "total_time": 10749
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

True	412	-	connect apic11o.emea-sp.cisco.com
True	337	13	apic11o.emea-sp.cisco.com class fabricNode
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/bgp/inst
True	319	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom
True	355	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/bgp/inst
True	337	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom
True	325	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	338	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	385	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/bgp/inst
True	374	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom
True	395	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/bgp/inst
True	317	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/bgpDom
True	284	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/bgp/inst
True	304	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/bgpDom
True	317	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	331	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	348	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	330	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	302	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/bgp/inst
True	398	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom
True	344	41	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/bgp/inst
True	344	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom
True	339	41	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)