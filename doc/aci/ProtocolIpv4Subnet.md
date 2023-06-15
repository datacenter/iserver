# Node Protocol - IPv4

## Filter IPv4 route table based on IP subnet

Example: Equal IP subnet

```
# iserver get aci proto ipv4 --apic apic11 --node rl --subnet 172.16.21.0/24

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+----------------+------------------+------------+-----------------+-----------+-----------+------------+--------+------------+
| Node                | VRF       | Prefix         | Next Hop         | Type       | Source          | Interface | NH VRF    | MPLS Label | Active | Preference |
+---------------------+-----------+----------------+------------------+------------+-----------------+-----------+-----------+------------+--------+------------+
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.31.2/32  | ospf-type2 | ospf-default    | eth1/36.6 | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/33.7 | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/34.8 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.32.2/32  | ospf-type2 | ospf-default    | eth1/36.6 | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/33.7 | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/34.8 | overlay-1 | 0          | no     | 250        | 
+---------------------+-----------+----------------+------------------+------------+-----------------+-----------+-----------+------------+--------+------------+

IPv4 Routes Summary
-------------------
- Routes  : 2
- Default : False
- Direct  : 0
- Local   : 0
- BGP     : 0
- iBGP    : 0
- eBGP    : 0
```

Example: Contain IP subnet

```
# iserver get aci proto ipv4
    --apic apic11
    --node rl
    --subnet 172.16.21.16/28
    --longer

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+----------------+------------------+------------+-----------------+-----------+-----------+------------+--------+------------+
| Node                | VRF       | Prefix         | Next Hop         | Type       | Source          | Interface | NH VRF    | MPLS Label | Active | Preference |
+---------------------+-----------+----------------+------------------+------------+-----------------+-----------+-----------+------------+--------+------------+
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.31.2/32  | ospf-type2 | ospf-default    | eth1/36.6 | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/33.7 | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/34.8 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.0/24 | 192.168.32.2/32  | ospf-type2 | ospf-default    | eth1/36.6 | overlay-1 | 0          | yes    | 110        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/33.7 | overlay-1 | 0          | no     | 250        | 
|                     |           |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/34.8 | overlay-1 | 0          | no     | 250        | 
+---------------------+-----------+----------------+------------------+------------+-----------------+-----------+-----------+------------+--------+------------+

IPv4 Routes Summary
-------------------
- Routes  : 2
- Default : False
- Direct  : 0
- Local   : 0
- BGP     : 0
- iBGP    : 0
- eBGP    : 0
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node rl --subnet 172.16.21.0/24

{
    "duration": 16928,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 490,
        "disconnect_time": 0,
        "mo_time": 14537,
        "total_time": 15027
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

True	490	-	connect apic11o.emea-sp.cisco.com
True	350	13	apic11o.emea-sp.cisco.com class fabricNode
True	366	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	339	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	360	133	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	355	78	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	364	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-ECMP-demo:INT-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	322	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-ECMP-demo:MPC-RDC-3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	329	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	346	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	352	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	319	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:CU-DU-Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	334	41	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	594	36	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	335	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-E:MPC-Residential-R3DC_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	337	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	339	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	400	290	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	329	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-SPIN_InnoLab:SPIN_RDC3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	332	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	332	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4/dom-UC3-CL2023-Demo:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	332	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	331	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	380	133	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	317	78	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	381	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-ECMP-demo:INT-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	324	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-ECMP-demo:MPC-RDC-3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	371	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	326	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	454	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	349	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:CU-DU-Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	337	41	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-E-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	312	36	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	339	23	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-E:MPC-Residential-R3DC_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	331	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	361	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	331	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	390	290	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	388	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-SPIN_InnoLab:SPIN_RDC3_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	363	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	372	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4/dom-UC3-CL2023-Demo:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)