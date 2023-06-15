# Policy Group - Access Interface VPC

## Node specific output

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* --view node

Apic: apic11 (mode:online, cache:off)

+-----------------+-------------------------+--------------------+
| Name            | Attached Entity Profile | Deployed Node Name |
+-----------------+-------------------------+--------------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | bl205-eu-spdc      | 
|                 |                         | bl206-eu-spdc      | 
+-----------------+-------------------------+--------------------+
| HX1-FI-B_PolGrp | HX1_AAEP                | bl206-eu-spdc      | 
|                 |                         | bl205-eu-spdc      | 
+-----------------+-------------------------+--------------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* --view node

{
    "duration": 5908,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 483,
        "disconnect_time": 0,
        "mo_time": 4982,
        "total_time": 5465
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

True	483	-	connect apic11o.emea-sp.cisco.com
True	772	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	3833	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	377	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PgAccessInterfaceVpc.md)