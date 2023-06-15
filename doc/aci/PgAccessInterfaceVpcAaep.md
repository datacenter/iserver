# Policy Group - Access Interface VPC

## Filter by aaep

```
# iserver get aci pg access intf vpc --apic apic11 --aaep Infra_AAEP --view aaep

Apic: apic11 (mode:online, cache:off)

+--------------------+-------------------------+-------------+----------------+
| Name               | Attached Entity Profile | Domain Type | Domain Name    |
+--------------------+-------------------------+-------------+----------------+
| Infra_PolGrp       | Infra_AAEP              | L3          | Infra_L3Dom    | 
|                    |                         | Physical    | Infra_PhysDom  | 
|                    |                         | L2          | VNF-mgmt_L2Dom | 
+--------------------+-------------------------+-------------+----------------+
| NXOS_FABRIC_PolGrp | Infra_AAEP              | L3          | Infra_L3Dom    | 
|                    |                         | Physical    | Infra_PhysDom  | 
|                    |                         | L2          | VNF-mgmt_L2Dom | 
+--------------------+-------------------------+-------------+----------------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic11 --aaep Infra_AAEP --view aaep

{
    "duration": 1715,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 991,
        "total_time": 1410
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

True	419	-	connect apic11o.emea-sp.cisco.com
True	622	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	369	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./PgAccessInterfaceVpc.md)