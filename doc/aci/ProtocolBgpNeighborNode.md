# Node Protocol - BGP

## Get BGP neighbors from selected node

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

```
# iserver get aci proto bgp --apic apic11 --node cl201-eu-spdc

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+------------------+-------------+-------+------+-----+-----------------+
| Node                | VRF                           | Neighbor Address | BGP State   | ASN   | Type | TTL | Paths (AF IPv4) |
+---------------------+-------------------------------+------------------+-------------+-------+------+-----+-----------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.101     | established | 65100 | ebgp | 5   | 16              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.41      | established | 65101 | ebgp | 5   | 5               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.191   | established | 65066 | ebgp | 1   | 7               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.192   | established | 65066 | ebgp | 1   | 7               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.193   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.194   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.195   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.196   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.191   | established | 65066 | ebgp | 1   | 5               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.192   | established | 65066 | ebgp | 1   | 5               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.193   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.194   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.195   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.196   | idle        | 65066 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.120     | idle        | 65101 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.220     | idle        | 65101 | ebgp | 8   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.221     | idle        | 65101 | ebgp | 10  | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.101   | established | 65100 | ebgp | 5   | 16              | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.41    | idle        | 65101 | ebgp | 5   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.191   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.192   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.193   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.194   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.195   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.196   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.191   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.192   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.193   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.194   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.195   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.196   | idle        | 65069 | ebgp | 1   | 0               | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.65      | established | 50000 | ibgp | 1   |                 | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.32.65       | established | 50000 | ibgp | 1   |                 | 
+---------------------+-------------------------------+------------------+-------------+-------+------+-----+-----------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node cl201-eu-spdc

{
    "duration": 2579,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 2045,
        "total_time": 2438
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

True	393	-	connect apic11o.emea-sp.cisco.com
True	1091	11	apic11o.emea-sp.cisco.com class fabricNode
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/bgp/inst
True	300	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom
True	371	113	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)