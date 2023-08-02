# Node Protocol - BGP

## Filter by source interface

```
# iserver get aci proto bgp --apic apic11 --node any --intf lo17 --view nei

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
# iserver get aci proto bgp --apic apic11 --node any --intf lo17 --view nei

{
    "duration": 11323,
    "apic": {
        "read": true,
        "success": 35,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 34,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 10442,
        "total_time": 10837
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

True	395	-	connect apic11o.emea-sp.cisco.com:443
True	296	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	287	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	366	26	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	380	66	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	269	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	351	25	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-206/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	291	66	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-206/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	279	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	364	29	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	310	117	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	379	29	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-202/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	357	117	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-202/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	309	3	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-209/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	279	10	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-209/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	280	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	284	3	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-210/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	283	10	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-210/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	343	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	306	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	299	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
True	290	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	286	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
True	284	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	334	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-302/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	303	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	321	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	302	3	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-101/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	297	35	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-101/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	293	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	297	3	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-102/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	286	35	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-102/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)