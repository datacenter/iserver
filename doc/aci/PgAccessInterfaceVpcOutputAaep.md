# Policy Group - Access Interface VPC

## AAEP specific output

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* --view aaep

Apic: apic11

+-----------------+-------------------------+-------------+-------------+
| Name            | Attached Entity Profile | Domain Type | Domain Name |
+-----------------+-------------------------+-------------+-------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | Physical    | HX1_PhysDom | 
+-----------------+-------------------------+-------------+-------------+
| HX1-FI-B_PolGrp | HX1_AAEP                | Physical    | HX1_PhysDom | 
+-----------------+-------------------------+-------------+-------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* --view aaep

{
    "duration": 1485,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 961,
        "total_time": 1380
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
    }
}

Log: apic
----------

True	419	-	connect apic11o.emea-sp.cisco.com
True	616	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	345	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./PgAccessInterfaceVpc.md)