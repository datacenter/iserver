# Policy Group - Access Interface - Leaf Access PC/VPC

## Intf view

```
# iserver get aci pg access intf vpc --apic apic21 --name HX* --view intf

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-group API call

Policy Group - Access Interface PC/VPC - Deployed Interfaces [#2]
-----------------------------------------------------------------

+-----------------+----------+--------------+----------------------+----------------+-----------+
| PG Name         | AAEP     | VLAN Pool    | VLAN Range           | Node           | Intf Name |
+-----------------+----------+--------------+----------------------+----------------+-----------+
| HX1-FI-A_PolGrp | HX1_AAEP | HX1_VlanPool | [1000-4048] (static) | bl2205-eu-spdc | eth1/11   | 
|                 |          |              | [70-79] (static)     | bl2206-eu-spdc | eth1/11   | 
+-----------------+----------+--------------+----------------------+----------------+-----------+
| HX1-FI-B_PolGrp | HX1_AAEP | HX1_VlanPool | [1000-4048] (static) | bl2205-eu-spdc | eth1/12   | 
|                 |          |              | [70-79] (static)     | bl2206-eu-spdc | eth1/12   | 
+-----------------+----------+--------------+----------------------+----------------+-----------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --name HX* --view intf

{
    "duration": 4062,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 428,
        "disconnect_time": 0,
        "mo_time": 3160,
        "total_time": 3588
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

True	428	-	connect apic21o.emea-sp.cisco.com:443
True	517	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	377	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	340	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	369	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	348	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	452	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	296	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	461	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
```

[[Back]](./PgAccessInterfaceVpc.md)