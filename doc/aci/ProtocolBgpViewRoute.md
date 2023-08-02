# Node Protocol - BGP

## Route view

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view route

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

+---------------------+--------------------------+----------------+--------+---------+---------------+------+-----------+--------------------------+------------+--------+------------+
| Node                | VRF                      | Prefix         | Health | Faults  | Next Hop      | Type | Source    | NH VRF                   | MPLS Label | Active | Preference |
+---------------------+--------------------------+----------------+--------+---------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.0.0/22   | 100    | 0 0 0 0 | 172.24.3.1/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
+---------------------+--------------------------+----------------+--------+---------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.4.0/22   | 100    | 0 0 0 0 | 172.24.3.2/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
+---------------------+--------------------------+----------------+--------+---------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22   | 100    | 0 0 0 0 | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
+---------------------+--------------------------+----------------+--------+---------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35/32 | 100    | 0 0 0 0 | 15.16.3.1/32  | ebgp | bgp-50000 | overlay-1                | 3          | yes    | 20         | 
+---------------------+--------------------------+----------------+--------+---------+---------------+------+-----------+--------------------------+------------+--------+------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view route

{
    "duration": 4494,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 381,
        "disconnect_time": 0,
        "mo_time": 3796,
        "total_time": 4177
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

True	381	-	connect apic11o.emea-sp.cisco.com:443
True	292	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	282	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	322	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	271	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	270	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[15.16.3.1/32]/ent-[15.16.3.1]/peerstats
True	394	286	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/uribv4/dom-overlay-1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	289	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.31.3.35/32]/ent-[172.31.3.35]/peerstats
True	269	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.228/32]/ent-[172.16.11.228]/peerstats
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.1/32]/ent-[172.16.11.1]/peerstats
True	276	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
True	294	44	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	273	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	283	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
```

[[Back]](./ProtocolBgp.md)