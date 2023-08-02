# Node Interface - Physical

## Policy Group focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view pg

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+------+------------------------+---------------------+-------------------+---------------------+-------------------------+
| Node                 | Interface | Oper | Type | Leaf Interface Profile | Interface Selector  | Policy Group Type | Policy Group Name   | Attached Entity Profile |
+----------------------+-----------+------+------+------------------------+---------------------+-------------------+---------------------+-------------------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | leaf | UCSB1-FI-A_IntProf     | UCSB1-FI-A_IntSel   | PC/VPC            | UCSB1-FI-A_PolGrp   |                         | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | leaf | UCSB1-FI-B_IntProf     | UCSB1-FI-B_IntSel   | PC/VPC            | UCSB1-FI-B_PolGrp   |                         | 
| pod-1/bl2205-eu-spdc | 1/3       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/4       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/5       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/6       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/7       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/8       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/9       | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/10      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | leaf | HX1-FI-A_IntProf       | HX1-FI-A_IntSel     | PC/VPC            | HX1-FI-A_PolGrp     |                         | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | leaf | HX1-FI-B_IntProf       | HX1-FI-B_IntSel     | PC/VPC            | HX1-FI-B_PolGrp     |                         | 
| pod-1/bl2205-eu-spdc | 1/13      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/14      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/15      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/16      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/17      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/18      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | leaf | ESX22-CDC-22_IntProf   | ESX22-CDC-22_IntSel | PC/VPC            | ESX22-CDC-22_PolGrp |                         | 
| pod-1/bl2205-eu-spdc | 1/20      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/21      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/22      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/23      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/24      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | leaf | Infra-BGP_IntProf      | Infra-BGP_IntSel    | Access            | Infra-L3_PolGrp     |                         | 
| pod-1/bl2205-eu-spdc | 1/26      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | leaf | SPN_IntProf            | SPN_IntSel          | PC/VPC            | SPN_PolGrp          |                         | 
| pod-1/bl2205-eu-spdc | 1/28      | down | leaf |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/29      | down | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/30      | down | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/31      | down | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/32      | down | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/33      | down | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/34      | down | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | fab  |                        |                     |                   |                     |                         | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | fab  |                        |                     |                   |                     |                         | 
+----------------------+-----------+------+------+------------------------+---------------------+-------------------+---------------------+-------------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view pg

{
    "duration": 10204,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 8378,
        "total_time": 8784
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

True	406	-	connect apic21o.emea-sp.cisco.com:443
True	316	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	997	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	352	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	334	7	apic21o.emea-sp.cisco.com:443 mo uni/infra/nodecfgcont/node-2205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	332	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-HX1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	318	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-Infra-BGP_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	372	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-ESX22-CDC-22_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	339	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-HX1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	318	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	333	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-UCSB1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	372	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-SPN_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	516	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	395	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	367	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	360	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	325	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	348	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	329	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	325	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	314	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	716	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
```

[[Back]](./InterfacePhy.md)