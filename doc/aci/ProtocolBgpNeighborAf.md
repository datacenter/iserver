# Node Protocol - BGP

## Show Address Family related attributes of selected BGP neighbors

```
# iserver get aci proto bgp --apic apic11 --node rl --view af

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+------------------+-------------+-------+------+-----+---------+----------+----------+
| Node                | VRF                      | Neighbor Address | BGP State   | ASN   | Type | TTL | AF IPv4 | AF VPNv4 | AF VPNv6 |
+---------------------+--------------------------+------------------+-------------+-------+------+-----+---------+----------+----------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | established | 64371 | ebgp | 4   | 3       |          |          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | established | 64371 | ebgp | 4   | 3       |          |          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3       |          |          | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1        | established | 64001 | ebgp | 1   | 0       |          |          | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1      | established | 50000 | ibgp | 1   |         | 357      | 0        | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228    | established | 50000 | ibgp | 1   |         | 357      | 0        | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35      | established | 64001 | ebgp | 2   |         |          |          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1       | established | 64371 | ebgp | 4   | 3       |          |          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2       | established | 64371 | ebgp | 4   | 3       |          |          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3       | established | 64371 | ebgp | 4   | 3       |          |          | 
| pod-1/rl302-eu-spdc | overlay-1                | 15.16.3.5        | established | 64001 | ebgp | 1   | 0       |          |          | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.1      | established | 50000 | ibgp | 1   |         | 357      | 0        | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.16.11.228    | established | 50000 | ibgp | 1   |         | 357      | 0        | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35      | established | 64001 | ebgp | 2   |         |          |          | 
+---------------------+--------------------------+------------------+-------------+-------+------+-----+---------+----------+----------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --view af

{
    "duration": 2708,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 2109,
        "total_time": 2501
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

True	392	-	connect apic11o.emea-sp.cisco.com
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	282	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	296	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	294	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	308	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)