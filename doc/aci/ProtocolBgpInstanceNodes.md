# Node Protocol - BGP

## Show BGP VRF domains for selected nodes

```
# iserver get aci proto bgp --apic apic11 --node rl --view vrf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+-----------+--------+-----------------+------------------------+-----------+-------------+
| Node                | VRF                            | BGP State | Mode   | Router ID       | RD                     | Neighbors | Established |
+---------------------+--------------------------------+-----------+--------+-----------------+------------------------+-----------+-------------+
| pod-1/rl301-eu-spdc | common:Infra_BGP_VRF           | up        | fabric | 10.58.27.126    | rd:as2-nn4:301:2424848 | 0         | 0           | 
| pod-1/rl301-eu-spdc | common:Infra_privIP_VRF        | up        | fabric | 15.100.161.126  | rd:as2-nn4:301:2097161 | 0         | 0           | 
| pod-1/rl301-eu-spdc | ECMP-demo:INT-ext_VRF          | up        | fabric | 15.101.3.254    | rd:as2-nn4:301:2621448 | 0         | 0           | 
| pod-1/rl301-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | up        | fabric | 15.3.203.254    | rd:as2-nn4:301:2326531 | 0         | 0           | 
| pod-1/rl301-eu-spdc | management                     | up        | fabric | 0.0.0.0         | rd:as2-nn4:301:2752512 | 0         | 0           | 
| pod-1/rl301-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | up        | fabric | 99.99.99.254    | rd:as2-nn4:301:2555904 | 0         | 0           | 
| pod-1/rl301-eu-spdc | mgmt:inb                       | up        | fabric | 10.58.28.190    | rd:as2-nn4:301:2818048 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-E:CU-DU-Infra_VRF          | up        | fabric | 192.168.20.1    | rd:as2-nn4:301:2981889 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | up        | fabric | 131.131.131.131 | rd:as2-nn4:301:2097155 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | up        | fabric | 131.131.131.131 | rd:as2-nn4:301:2981888 | 3         | 1           | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | up        | fabric | 131.131.131.131 | rd:as2-nn4:301:2818053 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-IN_VRF              | up        | fabric | 15.2.64.254     | rd:as2-nn4:301:2162693 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-OUT_VRF             | up        | fabric | 15.2.10.254     | rd:as2-nn4:301:2523139 | 0         | 0           | 
| pod-1/rl301-eu-spdc | MPC:MPC-sPBR-IN_VRF            | up        | fabric | 15.2.6.254      | rd:as2-nn4:301:2490372 | 0         | 0           | 
| pod-1/rl301-eu-spdc | overlay-1                      | up        | fabric | 131.131.131.131 | unknown:unknown:0:0    | 4         | 4           | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | up        | fabric | 1.1.1.3         | rd:as2-nn4:301:2949120 | 0         | 0           | 
| pod-1/rl301-eu-spdc | SPN_IntraLab:SPN_VRF1          | up        | fabric | 192.168.0.254   | rd:as2-nn4:301:2883591 | 0         | 0           | 
| pod-1/rl301-eu-spdc | UC3-CL2023-Demo:default        | up        | fabric | 0.0.0.0         | rd:as2-nn4:301:3014663 | 0         | 0           | 
| pod-1/rl302-eu-spdc | common:Infra_BGP_VRF           | up        | fabric | 10.58.239.254   | rd:as2-nn4:302:2424848 | 0         | 0           | 
| pod-1/rl302-eu-spdc | common:Infra_privIP_VRF        | up        | fabric | 15.100.161.126  | rd:as2-nn4:302:2097161 | 0         | 0           | 
| pod-1/rl302-eu-spdc | ECMP-demo:INT-ext_VRF          | up        | fabric | 15.101.3.254    | rd:as2-nn4:302:2621448 | 0         | 0           | 
| pod-1/rl302-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | up        | fabric | 15.3.203.254    | rd:as2-nn4:302:2326531 | 0         | 0           | 
| pod-1/rl302-eu-spdc | management                     | up        | fabric | 0.0.0.0         | rd:as2-nn4:302:2752512 | 0         | 0           | 
| pod-1/rl302-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | up        | fabric | 99.99.99.254    | rd:as2-nn4:302:2555904 | 0         | 0           | 
| pod-1/rl302-eu-spdc | mgmt:inb                       | up        | fabric | 10.58.28.190    | rd:as2-nn4:302:2818048 | 0         | 0           | 
| pod-1/rl302-eu-spdc | MPC-E:CU-DU-Infra_VRF          | up        | fabric | 192.168.20.1    | rd:as2-nn4:302:2981889 | 0         | 0           | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | up        | fabric | 132.132.132.132 | rd:as2-nn4:302:2097155 | 0         | 0           | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | up        | fabric | 132.132.132.132 | rd:as2-nn4:302:2981888 | 3         | 1           | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | up        | fabric | 132.132.132.132 | rd:as2-nn4:302:2818053 | 0         | 0           | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-IN_VRF              | up        | fabric | 15.2.64.254     | rd:as2-nn4:302:2162693 | 0         | 0           | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-OUT_VRF             | up        | fabric | 15.2.10.254     | rd:as2-nn4:302:2523139 | 0         | 0           | 
| pod-1/rl302-eu-spdc | MPC:MPC-sPBR-IN_VRF            | up        | fabric | 15.2.64.254     | rd:as2-nn4:302:2490372 | 0         | 0           | 
| pod-1/rl302-eu-spdc | overlay-1                      | up        | fabric | 132.132.132.132 | unknown:unknown:0:0    | 4         | 4           | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | up        | fabric | 1.1.1.4         | rd:as2-nn4:302:2949120 | 0         | 0           | 
| pod-1/rl302-eu-spdc | SPN_IntraLab:SPN_VRF1          | up        | fabric | 192.168.0.254   | rd:as2-nn4:302:2883591 | 0         | 0           | 
| pod-1/rl302-eu-spdc | UC3-CL2023-Demo:default        | up        | fabric | 0.0.0.0         | rd:as2-nn4:302:3014663 | 0         | 0           | 
+---------------------+--------------------------------+-----------+--------+-----------------+------------------------+-----------+-------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl --view vrf

{
    "duration": 3231,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 435,
        "disconnect_time": 0,
        "mo_time": 2340,
        "total_time": 2775
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

True	435	-	connect apic11o.emea-sp.cisco.com
True	330	13	apic11o.emea-sp.cisco.com class fabricNode
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/bgp/inst
True	331	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom
True	340	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/bgp/inst
True	327	18	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom
True	356	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
```

[[Back]](./ProtocolBgp.md)