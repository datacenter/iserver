# Policy Group - Access Interface - Leaf Access PC/VPC

## AAEP view

```
# iserver get aci pg access intf vpc --apic apic21 --name HX* --view aaep

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface PC/VPC - AAEP [#2]
--------------------------------------------------

+-----------------+----------+-------------+-------------+--------------+----------------------+
| Name            | AAEP     | Domain Type | Domain Name | VLAN Pool    | VLAN Range           |
+-----------------+----------+-------------+-------------+--------------+----------------------+
| HX1-FI-A_PolGrp | HX1_AAEP | Physical    | HX1_PhysDom | HX1_VlanPool | [1000-4048] (static) | 
|                 |          |             |             |              | [70-79] (static)     | 
+-----------------+----------+-------------+-------------+--------------+----------------------+
| HX1-FI-B_PolGrp | HX1_AAEP | Physical    | HX1_PhysDom | HX1_VlanPool | [1000-4048] (static) | 
|                 |          |             |             |              | [70-79] (static)     | 
+-----------------+----------+-------------+-------------+--------------+----------------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --name HX* --view aaep

{
    "duration": 2794,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 459,
        "disconnect_time": 0,
        "mo_time": 1827,
        "total_time": 2286
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

True	459	-	connect apic21o.emea-sp.cisco.com:443
True	530	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	349	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	304	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	332	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	312	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./PgAccessInterfaceVpc.md)