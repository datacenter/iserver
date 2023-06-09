# Node Protocol - BGP

## Get BGP neighbors from selected nodes

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

```
# iserver get aci proto bgp --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                      | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | idle        | 64371 | ebgp | 4   | 0               | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | idle        | 64371 | ebgp | 4   | 0               | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1      | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228    | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35      | established | 64001 | ebgp | 2   |                 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | idle        | 64371 | ebgp | 4   | 0               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | idle        | 64371 | ebgp | 4   | 0               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | overlay-1                | 15.16.3.5        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.1      | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.228    | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35      | established | 64001 | ebgp | 2   |                 | 
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl

{
    "duration": 3060,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 433,
        "disconnect_time": 0,
        "mo_time": 2272,
        "total_time": 2705
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

True	433	-	connect apic11o.emea-sp.cisco.com
True	304	13	apic11o.emea-sp.cisco.com class fabricNode
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	315	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	289	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	338	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	353	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)