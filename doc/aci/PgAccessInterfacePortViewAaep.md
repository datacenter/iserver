# Policy Group - Access Interface - Leaf Access Port

## AAEP view

```
# iserver get aci pg access intf port --apic apic21 --name *sriov* --view aaep

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface Port - AAEP [#4]
------------------------------------------------

+---------------------------+---------------+-------------+------------------+-------------------+--------------------+
| Name                      | AAEP          | Domain Type | Domain Name      | VLAN Pool         | VLAN Range         |
+---------------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                           |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                           |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                           |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------------+---------------+-------------+------------------+-------------------+--------------------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP | L3          | k8s_phys_L3Dom   | k8s_phys_VlanPool | [800-809] (static) | 
|                           |               | Physical    | k8s_phys_PhysDom |                   | [810-813] (static) | 
+---------------------------+---------------+-------------+------------------+-------------------+--------------------+
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --name *sriov* --view aaep

{
    "duration": 2910,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 2077,
        "total_time": 2491
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

True	414	-	connect apic21o.emea-sp.cisco.com:443
True	361	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	362	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	308	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	345	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	348	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	353	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
```

[[Back]](./PgAccessInterfacePort.md)