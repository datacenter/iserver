# Policy Group - Access Interface VPC

## Port specific output

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* --view port

Apic: apic11 (mode:online, cache:off)

+-----------------+-------------------------+--------------------+---------------+
| Name            | Attached Entity Profile | Deployed Node Name | Deployed Port |
+-----------------+-------------------------+--------------------+---------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | bl205-eu-spdc      | eth1/11       | 
|                 |                         | bl206-eu-spdc      | eth1/11       | 
+-----------------+-------------------------+--------------------+---------------+
| HX1-FI-B_PolGrp | HX1_AAEP                | bl206-eu-spdc      | eth1/12       | 
|                 |                         | bl205-eu-spdc      | eth1/12       | 
+-----------------+-------------------------+--------------------+---------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* --view port

{
    "duration": 7554,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 426,
        "disconnect_time": 0,
        "mo_time": 6748,
        "total_time": 7174
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

True	426	-	connect apic11o.emea-sp.cisco.com
True	633	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	3780	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree-include=full-deployment&target-path=AccBaseGrpToEthIf
True	384	13	apic11o.emea-sp.cisco.com class fabricNode
True	489	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=205&target-path=AccBaseGrpToEthIf
True	484	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=206&target-path=AccBaseGrpToEthIf
True	491	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=206&target-path=AccBaseGrpToEthIf
True	487	1	apic11o.emea-sp.cisco.com mo uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=205&target-path=AccBaseGrpToEthIf
```

[[Back]](./PgAccessInterfaceVpc.md)