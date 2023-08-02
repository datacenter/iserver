# Node Protocol - BGP

## Inst view

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view dom

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Domain (VRF) [#18]
---------------------------------

+---------------------+--------------------------------+--------+---------+-----------+--------+-----------------+------------------------+-----------+-------------+
| Node                | Domain (VRF)                   | Health | Faults  | BGP State | Mode   | Router ID       | RD                     | Neighbors | Established |
+---------------------+--------------------------------+--------+---------+-----------+--------+-----------------+------------------------+-----------+-------------+
| pod-1/rl301-eu-spdc | common:Infra_BGP_VRF           | 100    | 0 0 0 0 | up        | fabric | 10.58.27.126    | rd:as2-nn4:301:2424848 | 0         | 0           | 
| pod-1/rl301-eu-spdc | common:Infra_privIP_VRF        | 100    | 0 0 0 0 | up        | fabric | 15.100.161.126  | rd:as2-nn4:301:2097161 | 0         | 0           | 
| pod-1/rl301-eu-spdc | ECMP-demo:INT-ext_VRF          | 100    | 0 0 0 0 | up        | fabric | 15.101.3.254    | rd:as2-nn4:301:2621448 | 0         | 0           | 
| pod-1/rl301-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | 100    | 0 0 0 0 | up        | fabric | 15.3.203.254    | rd:as2-nn4:301:2326531 | 0         | 0           | 
| pod-1/rl301-eu-spdc | management                     | 100    | 0 0 0 0 | up        | fabric | 0.0.0.0         | rd:as2-nn4:301:2752512 | 0         | 0           | 
| pod-1/rl301-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | 100    | 0 0 0 0 | up        | fabric | 99.99.99.254    | rd:as2-nn4:301:2555904 | 0         | 0           | 
| pod-1/rl301-eu-spdc | mgmt:inb                       | 100    | 0 0 0 0 | up        | fabric | 10.58.28.190    | rd:as2-nn4:301:2818048 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-E:CU-DU-Infra_VRF          | 100    | 0 0 0 0 | up        | fabric | 192.168.20.1    | rd:as2-nn4:301:2981890 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 100    | 0 0 0 0 | up        | fabric | 131.131.131.131 | rd:as2-nn4:301:3112968 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 100    | 0 0 0 0 | up        | fabric | 131.131.131.131 | rd:as2-nn4:301:3014665 | 3         | 3           | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 100    | 0 0 0 0 | up        | fabric | 131.131.131.131 | rd:as2-nn4:301:2293769 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-IN_VRF              | 100    | 0 0 0 0 | up        | fabric | 15.2.64.254     | rd:as2-nn4:301:2162693 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-OUT_VRF             | 100    | 0 0 0 0 | up        | fabric | 15.2.10.254     | rd:as2-nn4:301:2523139 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 100    | 0 0 0 0 | up        | fabric | 15.2.62.254     | rd:as2-nn4:301:2293768 | 0         | 0           | 
| pod-1/rl301-eu-spdc | overlay-1                      | 100    | 0 0 0 0 | up        | fabric | 131.131.131.131 | unknown:unknown:0:0    | 4         | 4           | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 100    | 0 0 0 0 | up        | fabric | 1.1.1.3         | rd:as2-nn4:301:2949120 | 0         | 0           | 
| pod-1/rl301-eu-spdc | SPN_IntraLab:SPN_VRF1          | 100    | 0 0 0 0 | up        | fabric | 192.168.0.254   | rd:as2-nn4:301:2883591 | 0         | 0           | 
| pod-1/rl301-eu-spdc | UC3-CL2023-Demo:default        | 100    | 0 0 0 0 | up        | fabric | 0.0.0.0         | rd:as2-nn4:301:3014663 | 0         | 0           | 
+---------------------+--------------------------------+--------+---------+-----------+--------+-----------------+------------------------+-----------+-------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view dom

{
    "duration": 1737,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 1185,
        "total_time": 1581
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

True	396	-	connect apic11o.emea-sp.cisco.com:443
True	293	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	286	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	322	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	284	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)