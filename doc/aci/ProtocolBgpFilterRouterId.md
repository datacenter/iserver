# Node Protocol - BGP

## Filter by Router ID

Example: IP address

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --rtr-ip 35.35.35.35
    --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#2]
----------------------------

+---------------------+-----------+-------------+-------------+---------+-------------+-------+------+-----+----------+-------------+---------------+
| Node                | VRF       | Nbr Address | Router Id   | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP    | Conns (A/D/E) |
+---------------------+-----------+-------------+-------------+---------+-------------+-------+------+-----+----------+-------------+---------------+
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.1   | 35.35.35.35 | enabled | established | 64001 | ebgp | 1   | eth1/29  | 15.16.3.2   | 1/0/1         | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.31.3.35 | 35.35.35.35 | enabled | established | 64001 | ebgp | 2   | lo3      | 172.31.3.31 | 3/0/1         | 
+---------------------+-----------+-------------+-------------+---------+-------------+-------+------+-----+----------+-------------+---------------+
```

Example: IP subnet

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --rtr-subnet 172.24.0.0/16
    --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#3]
----------------------------

+---------------------+--------------------------+-------------+------------+---------+-------------+-------+------+-----+----------+-------------+---------------+--------------+
| Node                | VRF                      | Nbr Address | Router Id  | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP    | Conns (A/D/E) | Paths        |
+---------------------+--------------------------+-------------+------------+---------+-------------+-------+------+-----+----------+-------------+---------------+--------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1  | 172.24.3.1 | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15 | 3/0/1         | IPv4-ucast:3 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2  | 172.24.3.2 | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15 | 3/0/1         | IPv4-ucast:3 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3  | 172.24.3.3 | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15 | 3/0/1         | IPv4-ucast:3 | 
+---------------------+--------------------------+-------------+------------+---------+-------------+-------+------+-----+----------+-------------+---------------+--------------+
```

Developer

```
# iserver get aci proto bgp
    --apic apic11
    --node rl301
    --rtr-ip 35.35.35.35
    --view nei

{
    "duration": 2473,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1872,
        "total_time": 2270
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

True	398	-	connect apic11o.emea-sp.cisco.com:443
True	293	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	329	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	375	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	292	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	287	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[15.16.3.1/32]/ent-[15.16.3.1]/peerstats
True	296	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.31.3.35/32]/ent-[172.31.3.35]/peerstats
```

[[Back]](./ProtocolBgp.md)