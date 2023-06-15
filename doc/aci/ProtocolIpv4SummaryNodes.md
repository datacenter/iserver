# Node Protocol - IPv4

## Show IPv4 route table summary for selected node

```
# iserver get aci proto ipv4 --apic apic11 --node rl --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| Node                | VRF                            | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+---------------------+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| pod-1/rl301-eu-spdc | black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | common:Infra_BGP_VRF           | up    | 51     | True    | 0      | 5     | 35  | 35   | 0    | 
| pod-1/rl301-eu-spdc | common:Infra_privIP_VRF        | up    | 28     | True    | 0      | 1     | 26  | 26   | 0    | 
| pod-1/rl301-eu-spdc | ECMP-demo:INT-ext_VRF          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | mgmt:inb                       | up    | 38     | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/rl301-eu-spdc | MPC-E:CU-DU-Infra_VRF          | up    | 8      | False   | 0      | 1     | 6   | 0    | 6    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | up    | 19     | True    | 3      | 10    | 2   | 2    | 0    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 16     | True    | 3      | 5     | 6   | 5    | 1    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | up    | 9      | True    | 3      | 5     | 2   | 1    | 1    | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-IN_VRF              | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-OUT_VRF             | up    | 7      | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/rl301-eu-spdc | MPC:MPC-sPBR-IN_VRF            | up    | 17     | True    | 0      | 5     | 7   | 7    | 0    | 
| pod-1/rl301-eu-spdc | overlay-1                      | up    | 79     | False   | 10     | 12    | 1   | 0    | 1    | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 9      | True    | 3      | 5     | 3   | 1    | 2    | 
| pod-1/rl301-eu-spdc | SPN_IntraLab:SPN_VRF1          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | UC3-CL2023-Demo:default        | up    | 7      | True    | 0      | 0     | 7   | 7    | 0    | 
| pod-1/rl302-eu-spdc | black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | common:Infra_BGP_VRF           | up    | 51     | True    | 0      | 5     | 35  | 35   | 0    | 
| pod-1/rl302-eu-spdc | common:Infra_privIP_VRF        | up    | 28     | True    | 0      | 1     | 26  | 26   | 0    | 
| pod-1/rl302-eu-spdc | ECMP-demo:INT-ext_VRF          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | mgmt:inb                       | up    | 38     | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/rl302-eu-spdc | MPC-E:CU-DU-Infra_VRF          | up    | 8      | False   | 0      | 1     | 6   | 0    | 6    | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | up    | 19     | True    | 3      | 10    | 2   | 2    | 0    | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 16     | True    | 3      | 5     | 6   | 5    | 1    | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | up    | 9      | True    | 3      | 5     | 2   | 1    | 1    | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-IN_VRF              | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-OUT_VRF             | up    | 7      | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/rl302-eu-spdc | MPC:MPC-sPBR-IN_VRF            | up    | 17     | True    | 0      | 5     | 7   | 7    | 0    | 
| pod-1/rl302-eu-spdc | overlay-1                      | up    | 79     | False   | 10     | 12    | 1   | 0    | 1    | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 9      | True    | 3      | 5     | 3   | 1    | 2    | 
| pod-1/rl302-eu-spdc | SPN_IntraLab:SPN_VRF1          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | UC3-CL2023-Demo:default        | up    | 7      | True    | 0      | 0     | 7   | 7    | 0    | 
+---------------------+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node rl --view summary

{
    "duration": 15140,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 13240,
        "total_time": 13654
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

True	414	-	connect apic11o.emea-sp.cisco.com
True	337	13	apic11o.emea-sp.cisco.com class fabricNode
True	295	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	318	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	374	290	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	301	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-SPIN_InnoLab:SPIN_RDC3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	328	36	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	312	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:CU-DU-Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	317	41	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	294	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	292	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-UC3-CL2023-Demo:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	308	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	547	133	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	328	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	310	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-Residential-R3DC_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	304	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-ECMP-demo:INT-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	333	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	305	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	287	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	306	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	309	78	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	282	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-ECMP-demo:MPC-RDC-3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	292	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	314	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	350	290	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	324	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:CU-DU-Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	335	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-SPIN_InnoLab:SPIN_RDC3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	311	36	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	284	41	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-E-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	290	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-UC3-CL2023-Demo:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	312	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	394	133	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	315	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	334	23	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-Residential-R3DC_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	341	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-ECMP-demo:INT-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	297	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	325	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	361	78	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	295	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-ECMP-demo:MPC-RDC-3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	351	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)