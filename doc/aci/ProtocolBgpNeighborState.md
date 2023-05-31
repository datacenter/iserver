# Node Protocol - BGP

## Filter BGP neighbors by state (established|idle)

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: established (up)

```
# iserver get aci proto bgp --apic apic11 --node rl --state up

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                      | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1      | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228    | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35      | established | 64001 | ebgp | 2   |                 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3               | 
| pod-1/rl302-eu-spdc | overlay-1                | 15.16.3.5        | established | 64001 | ebgp | 1   | 0               | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.1      | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.228    | established | 50000 | ibgp | 1   |                 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35      | established | 64001 | ebgp | 2   |                 | 
+---------------------+--------------------------+------------------+-------------+-------+------+-----+-----------------+
```

Example: idle (down)

```
# iserver get aci proto bgp --apic apic11 --node any --state down

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

+---------------------+-------------------------------+------------------+-----------+-------+------+-----+-----------------+
| Node                | VRF                           | Neighbor Address | BGP State | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+-------------------------------+------------------+-----------+-------+------+-----+-----------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1       | idle      | 64271 | ebgp | 4   | 3               | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1       | idle      | 64271 | ebgp | 4   | 3               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.193   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.194   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.195   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.196   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.193   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.194   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.195   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.196   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120     | idle      | 65101 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220     | idle      | 65101 | ebgp | 8   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221     | idle      | 65101 | ebgp | 10  | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.41    | idle      | 65101 | ebgp | 5   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.191   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.192   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.193   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.194   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.195   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.196   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.191   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.192   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.193   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.194   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.195   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.196   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.41      | idle      | 65101 | ebgp | 5   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.193   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.194   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.195   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.196   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.193   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.194   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.195   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.196   | idle      | 65066 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120     | idle      | 65101 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220     | idle      | 65101 | ebgp | 8   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221     | idle      | 65101 | ebgp | 10  | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.41    | idle      | 65101 | ebgp | 5   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.191   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.193   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.194   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.195   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.191   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.192   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.193   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.194   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.195   | idle      | 65069 | ebgp | 1   | 0               | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.196   | idle      | 65069 | ebgp | 1   | 0               | 
+---------------------+-------------------------------+------------------+-----------+-------+------+-----+-----------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --state up

{
    "duration": 2599,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 2025,
        "total_time": 2420
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	290	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	290	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	290	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	287	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)