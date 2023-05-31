# Node Protocol - BGP

## Filter BGP neighbors by Router ID

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: IP address

```
# iserver get aci proto bgp
    --apic apic11
    --node rl
    --rtr-ip 35.35.35.35
    --view trans

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+------------------+-------------+-------------+-------------+-------+------+-----+-------------+-------------+
| Node                | VRF       | Neighbor Address | Router Id   | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP    |
+---------------------+-----------+------------------+-------------+-------------+-------------+-------+------+-----+-------------+-------------+
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.1        | 35.35.35.35 | enabled     | established | 64001 | ebgp | 1   | eth1/29     | 15.16.3.2   | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.31.3.35      | 35.35.35.35 | enabled     | established | 64001 | ebgp | 2   | lo4         | 172.31.3.31 | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.5        | 35.35.35.35 | enabled     | established | 64001 | ebgp | 1   | eth1/29     | 15.16.3.6   | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.31.3.35      | 35.35.35.35 | enabled     | established | 64001 | ebgp | 2   | lo4         | 172.31.3.32 | 
+---------------------+-----------+------------------+-------------+-------------+-------------+-------+------+-----+-------------+-------------+
```

Example: IP subnet

```
# iserver get aci proto bgp
    --apic apic11
    --node rl
    --rtr-subnet 172.24.0.0/16
    --view trans

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| Node                | VRF                      | Neighbor Address | Router Id  | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP    |
+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 172.24.3.1 | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.15 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 172.24.3.2 | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.15 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3 | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.15 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 172.24.3.1 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 172.24.3.2 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3 | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.14 | 
+---------------------+--------------------------+------------------+------------+-------------+-------------+-------+------+-----+-------------+-------------+
```

Developer

```
# iserver get aci proto bgp
    --apic apic11
    --node rl
    --rtr-ip 35.35.35.35
    --view trans

{
    "duration": 2635,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 2050,
        "total_time": 2470
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

True	420	-	connect apic11o.emea-sp.cisco.com
True	295	11	apic11o.emea-sp.cisco.com class fabricNode
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	298	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	297	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	275	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	318	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)