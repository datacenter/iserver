# Policy Group - Access Interface - Leaf Access PC/VPC

## Filter by aaep

```
# iserver get aci pg access intf vpc --apic apic21 --aaep *phys* --view aaep

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface PC/VPC - AAEP [#5]
--------------------------------------------------

+---------------------+---------------+-------------+------------------+-------------------+--------------------+
| Name                | AAEP          | Domain Type | Domain Name      | VLAN Pool         | VLAN Range         |
+---------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_ocp_bm_1_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                     |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_ocp_bm_2_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                     |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_ocp_bm_3_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                     |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_ocp_bm_4_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                     |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_ocp_bm_5_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                     |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------+---------------+-------------+------------------+-------------------+--------------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --aaep *phys* --view aaep

{
    "duration": 3192,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 439,
        "disconnect_time": 0,
        "mo_time": 2234,
        "total_time": 2673
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

True	439	-	connect apic21o.emea-sp.cisco.com:443
True	563	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	350	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	332	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	345	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	314	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	330	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
```

[[Back]](./PgAccessInterfaceVpc.md)