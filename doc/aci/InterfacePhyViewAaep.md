# Node Interface - Physical

## Attachable Access Entity Profile (AAEP) focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view aaep

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| Node                 | Interface | Oper | Type | Policy Group Name   | Attached Entity Profile | Domain Type | Domain Name           |
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | leaf | UCSB1-FI-A_PolGrp   |                         | L3          | UCSB1_L3Dom           | 
|                      |           |      |      |                     |                         | Physical    | UCSB1_PhysDom         | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/2       | up   | leaf | UCSB1-FI-B_PolGrp   |                         | L3          | UCSB1_L3Dom           | 
|                      |           |      |      |                     |                         | Physical    | UCSB1_PhysDom         | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/3       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/4       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/5       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/6       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/7       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/8       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/9       | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/10      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/11      | up   | leaf | HX1-FI-A_PolGrp     |                         | Physical    | HX1_PhysDom           | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/12      | up   | leaf | HX1-FI-B_PolGrp     |                         | Physical    | HX1_PhysDom           | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/13      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/14      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/15      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/16      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/17      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/18      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/19      | up   | leaf | ESX22-CDC-22_PolGrp |                         | Physical    | Infra_PhysDom         | 
|                      |           |      |      |                     |                         | VMM         | vEPC-Dataplane        | 
|                      |           |      |      |                     |                         | Physical    | vEPC-ESX20_PhysDom    | 
|                      |           |      |      |                     |                         | Physical    | vEPC-ESX21-22_PhysDom | 
|                      |           |      |      |                     |                         | L3          | vEPC_ESX              | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/20      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/21      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/22      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/23      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/24      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/25      | up   | leaf | Infra-L3_PolGrp     |                         | L2          | Infra_L2dom           | 
|                      |           |      |      |                     |                         | L3          | Infra_L3Dom           | 
|                      |           |      |      |                     |                         | Physical    | Infra_PhysDom         | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/26      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/27      | up   | leaf | SPN_PolGrp          |                         | Physical    | SPN_PhysDom           | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/28      | down | leaf |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/29      | down | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/30      | down | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/31      | down | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/32      | down | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/33      | down | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/34      | down | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/35      | up   | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
| pod-1/bl2205-eu-spdc | 1/36      | up   | fab  |                     |                         |             |                       | 
+----------------------+-----------+------+------+---------------------+-------------------------+-------------+-----------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view aaep

{
    "duration": 10690,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 8813,
        "total_time": 9259
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

True	446	-	connect apic21o.emea-sp.cisco.com:443
True	324	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	975	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	320	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	295	7	apic21o.emea-sp.cisco.com:443 mo uni/infra/nodecfgcont/node-2205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	286	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-HX1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	295	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-Infra-BGP_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	295	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-ESX22-CDC-22_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	631	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-HX1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	370	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	347	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-UCSB1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	305	3	apic21o.emea-sp.cisco.com:443 mo uni/infra/accportprof-SPN_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	608	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	387	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	326	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	321	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	334	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	364	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	364	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	431	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	381	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	854	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
```

[[Back]](./InterfacePhy.md)