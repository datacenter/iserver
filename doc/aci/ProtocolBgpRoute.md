# Node Protocol - BGP

Show IP route table BGP-sourced entries learnt by selected nodes and neighbors.

```
# iserver get aci proto bgp --apic apic11 --node rl --view route

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+----------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| Node                | VRF                      | Prefix         | Next Hop      | Type | Source    | NH VRF                   | MPLS Label | Active | Preference |
+---------------------+--------------------------+----------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.0.0/22   | 172.24.3.1/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.4.0/22   | 172.24.3.2/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22   | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35/32 | 15.16.3.1/32  | ebgp | bgp-50000 | overlay-1                | 3          | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.0.0/22   | 172.24.3.1/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.4.0/22   | 172.24.3.2/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22   | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35/32 | 15.16.3.5/32  | ebgp | bgp-50000 | overlay-1                | 3          | yes    | 20         | 
+---------------------+--------------------------+----------------+---------------+------+-----------+--------------------------+------------+--------+------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --view route

{
    "duration": 9149,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 7564,
        "total_time": 7983
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

True	419	-	connect apic11o.emea-sp.cisco.com
True	314	11	apic11o.emea-sp.cisco.com class fabricNode
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	285	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	288	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	273	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.228/32]/ent-[172.16.11.228]/peerstats
True	405	294	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.1/32]/ent-[172.16.11.1]/peerstats
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.31.3.35/32]/ent-[172.31.3.35]/peerstats
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[15.16.3.1/32]/ent-[15.16.3.1]/peerstats
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
True	317	44	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	284	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	298	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	267	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.228/32]/ent-[172.16.11.228]/peerstats
True	355	294	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	276	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.1/32]/ent-[172.16.11.1]/peerstats
True	276	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-overlay-1/peer-[172.31.3.35/32]/ent-[172.31.3.35]/peerstats
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-overlay-1/peer-[15.16.3.5/32]/ent-[15.16.3.5]/peerstats
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	321	44	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
```

[[Back]](./ProtocolBgp.md)