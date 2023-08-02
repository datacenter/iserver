# Policy Group - Access Interface - Leaf Access Port

## Intf view

```
# iserver get aci pg access intf port --apic apic21 --view intf

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-group API call

Policy Group - Access Interface Port - Deployed Interfaces [#8]
---------------------------------------------------------------

+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| PG Name                   | AAEP            | VLAN Pool           | VLAN Range            | Node           | Intf Name |
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | [2501-2502] (static)  | cl2201-eu-spdc | eth1/31   | 
|                           |                 |                     | [2503-2509] (static)  | cl2201-eu-spdc | eth1/32   | 
|                           |                 |                     | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/33   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/34   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/35   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/36   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/37   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/38   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/39   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/40   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/41   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/42   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/43   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/44   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/45   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/46   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/47   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/31   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/32   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/33   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/34   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/35   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/36   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/37   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/38   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/39   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/40   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/41   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/42   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/43   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/44   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/45   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/46   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/47   | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | ESX-R7DC_VlanPool   | [3701-3800] (dynamic) | rl2701-eu-spdc | eth1/1    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/10   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/11   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/12   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/13   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/2    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/3    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/4    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/5    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/6    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/7    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/8    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/9    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/1    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/10   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/11   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/12   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/13   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/2    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/3    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/4    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/5    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/6    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/7    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/8    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/9    | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| Infra-L3_PolGrp           | Infra_AAEP      | Infra_VlanPool      | [1-1000] (static)     | bl2205-eu-spdc | eth1/25   | 
|                           |                 |                     |                       | bl2206-eu-spdc | eth1/25   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/25   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/25   | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | eth1/3/3  | 
|                           |                 |                     | [810-813] (static)    | cl2207-eu-spdc | eth1/3/4  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/1  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/2  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/3  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/3  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/4  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/1  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/2  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/3  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | eth1/3/1  | 
|                           |                 |                     | [810-813] (static)    | cl2207-eu-spdc | eth1/3/2  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/1  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/2  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | eth1/3/3  | 
|                           |                 |                     | [810-813] (static)    | cl2208-eu-spdc | eth1/3/4  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/1  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/2  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/3  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/3  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/4  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/1  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/2  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/3  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | eth1/3/1  | 
|                           |                 |                     | [810-813] (static)    | cl2208-eu-spdc | eth1/3/2  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/1  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/2  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| nidemo-bare-metal         | nidemo          | nidemo-3000-3001    | [3000-3001] (static)  | rl2701-eu-spdc | eth1/19   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/20   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/19   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/20   | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --view intf

{
    "duration": 10094,
    "apic": {
        "read": true,
        "success": 19,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 18,
        "connect_time": 424,
        "disconnect_time": 0,
        "mo_time": 8129,
        "total_time": 8553
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

True	424	-	connect apic21o.emea-sp.cisco.com:443
True	369	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	373	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	330	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	351	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	348	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	339	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	737	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	325	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	518	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-ESX-CDC-22_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	355	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	527	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-ESX-R7DC_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	350	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	502	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-Infra-L3_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	521	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2207_bm_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	431	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2207_esx_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	441	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2208_bm_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	427	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2208_esx_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	885	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-nidemo-bare-metal query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
```

[[Back]](./PgAccessInterfacePort.md)