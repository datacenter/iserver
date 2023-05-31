# Node Protocol - BGP

## Filter BGP neighbors by neighbor IP Address

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: IP address

```
# iserver get aci proto bgp --apic apic11 --node rl --nbr-ip 172.24.3.3

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                      | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
```

Example: IP subnet

```
# iserver get aci proto bgp --apic apic11 --node rl --nbr-subnet 15.0.0.0/8

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF       | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+-----------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.1        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.5        | established | 64001 | ebgp | 1   | 0               | 
+---------------------+-----------+------------------+-------------+-------+------+-----+-----------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --nbr-ip 172.24.3.3

{
    "duration": 2686,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 2114,
        "total_time": 2508
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

True	394	-	connect apic11o.emea-sp.cisco.com
True	328	11	apic11o.emea-sp.cisco.com class fabricNode
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	286	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	298	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	299	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	337	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)