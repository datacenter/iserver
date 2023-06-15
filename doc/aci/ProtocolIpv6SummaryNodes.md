# Node Protocol - IPv6

## Show IPv6 route table summary for selected node

```
# iserver get aci proto ipv6 --apic apic11 --node rl --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| VRF                            | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_BGP_VRF           | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_privIP_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:INT-ext_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:MPC-RDC-3_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:EU-SPDC-ERSPAN-VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:inb                       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:CU-DU-Infra_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-IN_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-Residential-R3DC_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-IN_VRF              | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-OUT_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-IN_VRF            | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| overlay-1                      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPN_IntraLab:SPN_VRF1          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| UC3-CL2023-Demo:default        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_BGP_VRF           | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_privIP_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:INT-ext_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:MPC-RDC-3_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:EU-SPDC-ERSPAN-VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:inb                       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:CU-DU-Infra_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-IN_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-Residential-R3DC_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-IN_VRF              | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-OUT_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-IN_VRF            | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| overlay-1                      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPN_IntraLab:SPN_VRF1          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| UC3-CL2023-Demo:default        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

Developer

```
# iserver get aci proto ipv6 --apic apic11 --node rl --view summary

{
    "duration": 15895,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 13826,
        "total_time": 14240
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
True	306	13	apic11o.emea-sp.cisco.com class fabricNode
True	302	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6 query query-target=children&target-subtree-class=uribv6Dom
True	324	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-black-hole query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	331	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	342	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-SPIN_InnoLab:SPIN_RDC3_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	334	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	303	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC-E:CU-DU-Infra_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	313	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC-E:MPC-E-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	314	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-management query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	306	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-UC3-CL2023-Demo:default query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	343	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	344	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	320	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	388	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC-E:MPC-Residential-R3DC_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	320	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-ECMP-demo:INT-ext_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	335	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	313	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	376	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	339	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	342	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	346	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv6/dom-ECMP-demo:MPC-RDC-3_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	336	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6 query query-target=children&target-subtree-class=uribv6Dom
True	351	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-black-hole query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	338	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	321	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC-E:CU-DU-Infra_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	350	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-SPIN_InnoLab:SPIN_RDC3_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	366	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC-E:MPC-E-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	346	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-UC3-CL2023-Demo:default query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	334	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-management query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	340	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	320	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	397	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC-E:MPC-Residential-R3DC_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-ECMP-demo:INT-ext_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	332	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	378	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	368	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	322	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-ECMP-demo:MPC-RDC-3_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	382	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv6/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
```

[[Back]](./ProtocolIpv6.md)