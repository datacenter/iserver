# Policy Group - Access Interface VPC

## JSON

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* -o json

[
    {
        "__Output": {},
        "annotation": "",
        "descr": "ACI1 HX1-FI-A Policy Group (Created by Ansible)",
        "dn": "uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp",
        "lagT": "node",
        "name": "HX1-FI-A_PolGrp",
        "aaep_name": "HX1_AAEP",
        "policy": {
            "infraRsCdpIfPol": "CDP_enable",
            "infraRsMcpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsLacpPol": "LACP-active",
            "infraRsMonIfInfraPol": "",
            "infraAccBndlSubgrp": "",
            "infraRsStpIfPol": "default",
            "infraRsAttEntP": "",
            "infraRsSpanVSrcGrp": "",
            "infraRsSpanVDestGrp": "",
            "infraRsL2IfPol": "L2-local_Pol",
            "infraRsStormctrlIfPol": "default",
            "infraRsQosEgressDppIfPol": "",
            "infraRsQosIngressDppIfPol": "",
            "infraRsQosSdIfPol": "",
            "infraRsQosPfcIfPol": "",
            "infraRsL2PortSecurityPol": "default",
            "infraRsFcIfPol": "default",
            "infraRsMacsecIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "ACI1 HX1-FI-B Policy Group (Created by Ansible)",
        "dn": "uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp",
        "lagT": "node",
        "name": "HX1-FI-B_PolGrp",
        "aaep_name": "HX1_AAEP",
        "policy": {
            "infraRsCdpIfPol": "CDP_enable",
            "infraRsMcpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsLacpPol": "LACP-active",
            "infraRsMonIfInfraPol": "",
            "infraAccBndlSubgrp": "",
            "infraRsStpIfPol": "default",
            "infraRsAttEntP": "",
            "infraRsSpanVSrcGrp": "",
            "infraRsSpanVDestGrp": "",
            "infraRsL2IfPol": "L2-local_Pol",
            "infraRsStormctrlIfPol": "default",
            "infraRsQosEgressDppIfPol": "",
            "infraRsQosIngressDppIfPol": "",
            "infraRsQosSdIfPol": "",
            "infraRsQosPfcIfPol": "",
            "infraRsL2PortSecurityPol": "default",
            "infraRsFcIfPol": "default",
            "infraRsMacsecIfPol": "default"
        }
    }
]
```

[[Back]](./PgAccessInterfaceVpc.md)