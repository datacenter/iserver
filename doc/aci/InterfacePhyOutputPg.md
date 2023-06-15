# Node Interface - Physical

## Policy Group focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view pg

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+------+--------------------------+-------------------------+-------------------+-------------------------+-------------------------+
| Node                | Interface | Oper | Type | Leaf Interface Profile   | Interface Selector      | Policy Group Type | Policy Group Name       | Attached Entity Profile |
+---------------------+-----------+------+------+--------------------------+-------------------------+-------------------+-------------------------+-------------------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | leaf | UCSB1-FI-A_IntProf       | UCSB1-FI-A_IntSel       | PC/VPC            | UCSB1-FI-A_PolGrp       | UCSB1_AAEP              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | leaf | UCSB1-FI-B_IntProf       | UCSB1-FI-B_IntSel       | PC/VPC            | UCSB1-FI-B_PolGrp       | UCSB1_AAEP              | 
| pod-1/bl205-eu-spdc | 1/3       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/4       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/5       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/6       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/7       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/8       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/9       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/10      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/11      | up   | leaf | HX1-FI-A_IntProf         | HX1-FI-A_IntSel         | PC/VPC            | HX1-FI-A_PolGrp         | HX1_AAEP                | 
| pod-1/bl205-eu-spdc | 1/12      | up   | leaf | HX1-FI-B_IntProf         | HX1-FI-B_IntSel         | PC/VPC            | HX1-FI-B_PolGrp         | HX1_AAEP                | 
| pod-1/bl205-eu-spdc | 1/13      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/14      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/15      | up   | leaf | P5G-CU-PCIe1-A_IntProf   | P5G-CU-PCIe1-A_IntSel   | Access            | P5G-CU-PCIe1-A_PolGrp   | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/16      | up   | leaf | P5G-CU-PCIe2-A_IntProf   | P5G-CU-PCIe2-A_IntSel   | Access            | P5G-CU-PCIe2-A_PolGrp   | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/17      | down | leaf | P5G-Core-PCIe1-A_IntProf | P5G-Core-PCIe1-A_IntSel | Access            | P5G-Core-PCIe1-A_PolGrp | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/18      | down | leaf | P5G-Core-PCIe2-A_IntProf | P5G-Core-PCIe2-A_IntSel | Access            | P5G-Core-PCIe2-A_PolGrp | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/19      | up   | leaf | P5G-Core-MLOM-1_IntProf  | P5G-Core-MLOM-1_IntSel  | Access            | P5G-Core-MLOM-1_PolGrp  | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/20      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/21      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/22      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/23      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/24      | up   | leaf | Infra-BGP_IntProf        | Infra-BGP_IntSel        | Access            | Infra-BGP_PolGrp        | Infra_L3_AAEP           | 
| pod-1/bl205-eu-spdc | 1/25      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/26      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/27      | up   | leaf | SPN_IntProf              | SPN_IntSel              | PC/VPC            | SPN_PolGrp              | SPN_AAEP                | 
| pod-1/bl205-eu-spdc | 1/28      | up   | leaf | SR-Demo-CDC-2            | 1-28-1-28               | Access            | SR-Demo-CDC-2-vlan      | DC                      | 
| pod-1/bl205-eu-spdc | 1/29      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/30      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/31      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/32      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/33      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/34      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/35      | up   | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/36      | up   | fab  |                          |                         |                   |                         |                         | 
+---------------------+-----------+------+------+--------------------------+-------------------------+-------------------+-------------------------+-------------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view pg

{
    "duration": 6970,
    "apic": {
        "read": true,
        "success": 20,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 19,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 6160,
        "total_time": 6550
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

True	390	-	connect apic11o.emea-sp.cisco.com
True	308	13	apic11o.emea-sp.cisco.com class fabricNode
True	300	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	304	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	294	12	apic11o.emea-sp.cisco.com mo uni/infra/nodecfgcont/node-205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	283	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	290	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-PCIe1-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	299	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-HX1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	300	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-SR-Demo-CDC-2 query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	297	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-SPN_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	282	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-HX1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	299	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-MLOM-1_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	300	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-Infra-BGP_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	317	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-CU-PCIe1-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	323	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-PCIe2-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	278	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-CU-PCIe2-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	292	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	539	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	350	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	505	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
```

[[Back]](./InterfacePhy.md)