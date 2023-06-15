# Node Protocol - BGP

## Show IP transport related attributes of selected BGP neighbors

```
# iserver get aci proto bgp --apic apic11 --node rl --view trans

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-----------------+-------------+-------------+-------+------+-----+-------------+---------------+
| Node                | VRF                      | Neighbor Address | Router Id       | Admin State | BGP State   | ASN   | Type | TTL | Source Intf | Local IP      |
+---------------------+--------------------------+------------------+-----------------+-------------+-------------+-------+------+-----+-------------+---------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 0.0.0.0         | enabled     | idle        | 64371 | ebgp | 4   | lo9         | 0.0.0.0       | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 0.0.0.0         | enabled     | idle        | 64371 | ebgp | 4   | lo9         | 0.0.0.0       | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3      | enabled     | established | 64371 | ebgp | 4   | lo9         | 172.24.3.15   | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1        | 35.35.35.35     | enabled     | established | 64001 | ebgp | 1   | eth1/29     | 15.16.3.2     | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1      | 102.102.102.102 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.160 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228    | 101.101.101.101 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.160 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35      | 35.35.35.35     | enabled     | established | 64001 | ebgp | 2   | lo3         | 172.31.3.31   | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | 0.0.0.0         | enabled     | idle        | 64371 | ebgp | 4   | lo8         | 0.0.0.0       | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | 0.0.0.0         | enabled     | idle        | 64371 | ebgp | 4   | lo8         | 0.0.0.0       | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | 172.24.3.3      | enabled     | established | 64371 | ebgp | 4   | lo8         | 172.24.3.14   | 
| pod-1/rl302-eu-spdc | overlay-1                | 15.16.3.5        | 35.35.35.35     | enabled     | established | 64001 | ebgp | 1   | eth1/29     | 15.16.3.6     | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.1      | 102.102.102.102 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.120 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.228    | 101.101.101.101 | enabled     | established | 50000 | ibgp | 1   | lo0         | 172.16.30.120 | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35      | 35.35.35.35     | enabled     | established | 64001 | ebgp | 2   | lo3         | 172.31.3.32   | 
+---------------------+--------------------------+------------------+-----------------+-------------+-------------+-------+------+-----+-------------+---------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --view trans

{
    "duration": 2762,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 2135,
        "total_time": 2527
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

True	392	-	connect apic11o.emea-sp.cisco.com
True	338	13	apic11o.emea-sp.cisco.com class fabricNode
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	298	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	325	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	286	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	301	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)