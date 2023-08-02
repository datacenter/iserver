# Policy Group - Access Interface - Leaf Access Port

## Node view

```
# iserver get aci pg access intf port --apic apic21 --view node

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-group API call

Policy Group - Access Interface Port - Deployed Nodes [#8]
----------------------------------------------------------

+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| PG Name                   | AAEP            | VLAN Pool           | VLAN Range            | Node           | Interfaces |
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | [2501-2502] (static)  | cl2201-eu-spdc | 17         | 
|                           |                 |                     | [2503-2509] (static)  | cl2202-eu-spdc | 17         | 
|                           |                 |                     | [2700-2999] (dynamic) |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | ESX-R7DC_VlanPool   | [3701-3800] (dynamic) | rl2701-eu-spdc | 13         | 
|                           |                 |                     |                       | rl2702-eu-spdc | 13         | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| Infra-L3_PolGrp           | Infra_AAEP      | Infra_VlanPool      | [1-1000] (static)     | bl2205-eu-spdc | 1          | 
|                           |                 |                     |                       | bl2206-eu-spdc | 1          | 
|                           |                 |                     |                       | cl2201-eu-spdc | 1          | 
|                           |                 |                     |                       | cl2202-eu-spdc | 1          | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | 10         | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | 4          | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | 10         | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | 4          | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| nidemo-bare-metal         | nidemo          | nidemo-3000-3001    | [3000-3001] (static)  | rl2701-eu-spdc | 2          | 
|                           |                 |                     |                       | rl2702-eu-spdc | 2          | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --view node

{
    "duration": 9057,
    "apic": {
        "read": true,
        "success": 19,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 18,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 7523,
        "total_time": 7945
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

True	422	-	connect apic21o.emea-sp.cisco.com:443
True	385	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	387	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	291	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	339	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	339	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	336	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	720	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	302	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	468	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-ESX-CDC-22_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	323	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	507	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-ESX-R7DC_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	324	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	478	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-Infra-L3_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	462	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2207_bm_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	455	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2207_esx_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	466	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2208_bm_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	463	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2208_esx_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	478	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-nidemo-bare-metal query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
```

[[Back]](./PgAccessInterfacePort.md)