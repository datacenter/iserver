# Node Protocol - BGP

## Filter by VRF

```
# iserver get aci proto bgp --apic apic11 --node rl301 --vrf *mpc* --view nei

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
# iserver get aci proto bgp --apic apic11 --node rl301 --vrf *mpc* --view nei

{
    "duration": 2714,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 383,
        "disconnect_time": 0,
        "mo_time": 2122,
        "total_time": 2505
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

True	383	-	connect apic11o.emea-sp.cisco.com:443
True	295	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	291	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	370	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	300	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	286	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
True	294	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	286	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
```

[[Back]](./ProtocolBgp.md)