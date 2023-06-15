# Node Interface - Physical

## Attachable Access Entity Profile (AAEP) focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view aaep

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| Node                | Interface | Oper | Type | Policy Group Name       | Attached Entity Profile | Domain Type | Domain Name       |
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | leaf | UCSB1-FI-A_PolGrp       | UCSB1_AAEP              | VMM         | EU-SPDC-CDC       | 
|                     |           |      |      |                         |                         | L3          | Infra_L3Dom       | 
|                     |           |      |      |                         |                         | L3          | UCSB1_L3Dom       | 
|                     |           |      |      |                         |                         | Physical    | UCSB1_PhysDom     | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/2       | up   | leaf | UCSB1-FI-B_PolGrp       | UCSB1_AAEP              | VMM         | EU-SPDC-CDC       | 
|                     |           |      |      |                         |                         | L3          | Infra_L3Dom       | 
|                     |           |      |      |                         |                         | L3          | UCSB1_L3Dom       | 
|                     |           |      |      |                         |                         | Physical    | UCSB1_PhysDom     | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/3       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/4       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/5       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/6       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/7       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/8       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/9       | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/10      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/11      | up   | leaf | HX1-FI-A_PolGrp         | HX1_AAEP                | Physical    | HX1_PhysDom       | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/12      | up   | leaf | HX1-FI-B_PolGrp         | HX1_AAEP                | Physical    | HX1_PhysDom       | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/13      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/14      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | leaf | P5G-CU-PCIe1-A_PolGrp   | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/16      | up   | leaf | P5G-CU-PCIe2-A_PolGrp   | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/17      | down | leaf | P5G-Core-PCIe1-A_PolGrp | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/18      | down | leaf | P5G-Core-PCIe2-A_PolGrp | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/19      | up   | leaf | P5G-Core-MLOM-1_PolGrp  | Private5G_AAEP          | Physical    | Private5G_PhysDom | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/20      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/21      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/22      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/23      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/24      | up   | leaf | Infra-BGP_PolGrp        | Infra_L3_AAEP           | L3          | Infra-BGP_L3Dom   | 
|                     |           |      |      |                         |                         | L3          | Infra_L3Dom       | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/25      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/26      | down | leaf |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/27      | up   | leaf | SPN_PolGrp              | SPN_AAEP                | L3          | Infra_L3Dom       | 
|                     |           |      |      |                         |                         | Physical    | SPN_PhysDom       | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/28      | up   | leaf | SR-Demo-CDC-2-vlan      | DC                      |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/29      | down | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/30      | down | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/31      | down | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/32      | down | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/33      | down | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/34      | down | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/35      | up   | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
| pod-1/bl205-eu-spdc | 1/36      | up   | fab  |                         |                         |             |                   | 
+---------------------+-----------+------+------+-------------------------+-------------------------+-------------+-------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view aaep

{
    "duration": 6998,
    "apic": {
        "read": true,
        "success": 20,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 19,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 6105,
        "total_time": 6520
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

True	415	-	connect apic11o.emea-sp.cisco.com
True	295	13	apic11o.emea-sp.cisco.com class fabricNode
True	300	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	304	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	289	12	apic11o.emea-sp.cisco.com mo uni/infra/nodecfgcont/node-205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	282	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	283	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-PCIe1-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	289	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-HX1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	286	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-SR-Demo-CDC-2 query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	299	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-SPN_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	276	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-HX1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	284	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-MLOM-1_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	286	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-Infra-BGP_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	294	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-CU-PCIe1-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	290	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-PCIe2-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	297	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-CU-PCIe2-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	314	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	552	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	369	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	516	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
```

[[Back]](./InterfacePhy.md)