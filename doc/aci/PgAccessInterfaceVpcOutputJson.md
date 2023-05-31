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
        },
        "policies": [
            {
                "type": "infraRsCdpIfPol",
                "name": "CDP_enable"
            },
            {
                "type": "infraRsMcpIfPol",
                "name": "default"
            },
            {
                "type": "infraRsHIfPol",
                "name": "Inherit"
            },
            {
                "type": "infraRsLinkFlapPol",
                "name": "default"
            },
            {
                "type": "infraRsLldpIfPol",
                "name": "LLDP_enable"
            },
            {
                "type": "infraRsLacpPol",
                "name": "LACP-active"
            },
            {
                "type": "infraRsMonIfInfraPol",
                "name": null
            },
            {
                "type": "infraAccBndlSubgrp",
                "name": null
            },
            {
                "type": "infraRsStpIfPol",
                "name": "default"
            },
            {
                "type": "infraRsSpanVSrcGrp",
                "name": null
            },
            {
                "type": "infraRsSpanVDestGrp",
                "name": null
            },
            {
                "type": "infraRsL2IfPol",
                "name": "L2-local_Pol"
            },
            {
                "type": "infraRsStormctrlIfPol",
                "name": "default"
            },
            {
                "type": "infraRsQosEgressDppIfPol",
                "name": null
            },
            {
                "type": "infraRsQosIngressDppIfPol",
                "name": null
            },
            {
                "type": "infraRsQosSdIfPol",
                "name": null
            },
            {
                "type": "infraRsQosPfcIfPol",
                "name": null
            },
            {
                "type": "infraRsQosEgressDppIfPol",
                "name": null
            },
            {
                "type": "infraRsL2PortSecurityPol",
                "name": "default"
            },
            {
                "type": "infraRsFcIfPol",
                "name": "default"
            },
            {
                "type": "infraRsMacsecIfPol",
                "name": "default"
            }
        ]
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
        },
        "policies": [
            {
                "type": "infraRsCdpIfPol",
                "name": "CDP_enable"
            },
            {
                "type": "infraRsMcpIfPol",
                "name": "default"
            },
            {
                "type": "infraRsHIfPol",
                "name": "Inherit"
            },
            {
                "type": "infraRsLinkFlapPol",
                "name": "default"
            },
            {
                "type": "infraRsLldpIfPol",
                "name": "LLDP_enable"
            },
            {
                "type": "infraRsLacpPol",
                "name": "LACP-active"
            },
            {
                "type": "infraRsMonIfInfraPol",
                "name": null
            },
            {
                "type": "infraAccBndlSubgrp",
                "name": null
            },
            {
                "type": "infraRsStpIfPol",
                "name": "default"
            },
            {
                "type": "infraRsSpanVSrcGrp",
                "name": null
            },
            {
                "type": "infraRsSpanVDestGrp",
                "name": null
            },
            {
                "type": "infraRsL2IfPol",
                "name": "L2-local_Pol"
            },
            {
                "type": "infraRsStormctrlIfPol",
                "name": "default"
            },
            {
                "type": "infraRsQosEgressDppIfPol",
                "name": null
            },
            {
                "type": "infraRsQosIngressDppIfPol",
                "name": null
            },
            {
                "type": "infraRsQosSdIfPol",
                "name": null
            },
            {
                "type": "infraRsQosPfcIfPol",
                "name": null
            },
            {
                "type": "infraRsQosEgressDppIfPol",
                "name": null
            },
            {
                "type": "infraRsL2PortSecurityPol",
                "name": "default"
            },
            {
                "type": "infraRsFcIfPol",
                "name": "default"
            },
            {
                "type": "infraRsMacsecIfPol",
                "name": "default"
            }
        ]
    }
]
```

[[Back]](./PgAccessInterfaceVpc.md)