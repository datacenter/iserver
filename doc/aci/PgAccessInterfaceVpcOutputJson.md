# Policy Group - Access Interface - Leaf Access PC/VPC

## JSON output

```
# iserver get aci pg access intf vpc --apic apic21 --name HX* -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "annotation": "",
        "descr": "ACI2 HX1-FI-A Policy Group (Created by Ansible)",
        "dn": "uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp",
        "lagT": "node",
        "name": "HX1-FI-A_PolGrp",
        "infraRsCdpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/cdpIfP-CDP-enable",
            "tRn": "cdpIfP-CDP-enable",
            "name": "CDP-enable"
        },
        "infraRsMcpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/mcpIfP-default",
            "tRn": "mcpIfP-default",
            "name": "default"
        },
        "infraRsHIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/hintfpol-Inherit",
            "tRn": "hintfpol-Inherit",
            "name": "Inherit"
        },
        "infraRsLinkFlapPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/linkflappol-default",
            "tRn": "linkflappol-default",
            "name": "default"
        },
        "infraRsLldpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/lldpIfP-LLDP-enable",
            "tRn": "lldpIfP-LLDP-enable",
            "name": "LLDP-enable"
        },
        "infraRsLacpPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/lacplagp-LACP-active",
            "tRn": "lacplagp-LACP-active",
            "name": "LACP-active"
        },
        "infraRsMonIfInfraPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/moninfra-default",
            "tRn": "moninfra-default",
            "name": "default"
        },
        "infraAccBndlSubgrp": {
            "__Output": {},
            "state": null,
            "tDn": null,
            "tRn": null,
            "name": "--"
        },
        "infraRsStpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/ifPol-default",
            "tRn": "ifPol-default",
            "name": "default"
        },
        "infraRsAttEntP": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/attentp-HX1_AAEP",
            "tRn": null,
            "name": "HX1_AAEP"
        },
        "infraRsSpanVSrcGrp": {
            "__Output": {},
            "state": null,
            "tDn": null,
            "tRn": null,
            "name": "--"
        },
        "infraRsSpanVDestGrp": {
            "__Output": {},
            "state": null,
            "tDn": null,
            "tRn": null,
            "name": "--"
        },
        "infraRsL2IfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/l2IfP-L2-local_Pol",
            "tRn": "l2IfP-L2-local_Pol",
            "name": "L2-local_Pol"
        },
        "infraRsStormctrlIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/stormctrlifp-default",
            "tRn": "stormctrlifp-default",
            "name": "default"
        },
        "infraRsQosEgressDppIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/qosdpppol-default",
            "tRn": "qosdpppol-default",
            "name": "default"
        },
        "infraRsQosIngressDppIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/qosdpppol-default",
            "tRn": "qosdpppol-default",
            "name": "default"
        },
        "infraRsQosSdIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/qossdpol-default",
            "tRn": "qossdpol-default",
            "name": "default"
        },
        "infraRsQosPfcIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/pfc-default",
            "tRn": "pfc-default",
            "name": "default"
        },
        "infraRsL2PortSecurityPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/portsecurityP-default",
            "tRn": "portsecurityP-default",
            "name": "default"
        },
        "infraRsFcIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/fcIfPol-default",
            "tRn": "fcIfPol-default",
            "name": "default"
        },
        "infraRsMacsecIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/macsecifp-default",
            "tRn": "macsecifp-default",
            "name": "default"
        },
        "faults": "0 0 0 0",
        "isAnyFault": false
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "annotation": "",
        "descr": "ACI2 HX1-FI-B Policy Group (Created by Ansible)",
        "dn": "uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp",
        "lagT": "node",
        "name": "HX1-FI-B_PolGrp",
        "infraRsCdpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/cdpIfP-CDP-enable",
            "tRn": "cdpIfP-CDP-enable",
            "name": "CDP-enable"
        },
        "infraRsMcpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/mcpIfP-default",
            "tRn": "mcpIfP-default",
            "name": "default"
        },
        "infraRsHIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/hintfpol-Inherit",
            "tRn": "hintfpol-Inherit",
            "name": "Inherit"
        },
        "infraRsLinkFlapPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/linkflappol-default",
            "tRn": "linkflappol-default",
            "name": "default"
        },
        "infraRsLldpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/lldpIfP-LLDP-enable",
            "tRn": "lldpIfP-LLDP-enable",
            "name": "LLDP-enable"
        },
        "infraRsLacpPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/lacplagp-LACP-active",
            "tRn": "lacplagp-LACP-active",
            "name": "LACP-active"
        },
        "infraRsMonIfInfraPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/moninfra-default",
            "tRn": "moninfra-default",
            "name": "default"
        },
        "infraAccBndlSubgrp": {
            "__Output": {},
            "state": null,
            "tDn": null,
            "tRn": null,
            "name": "--"
        },
        "infraRsStpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/ifPol-default",
            "tRn": "ifPol-default",
            "name": "default"
        },
        "infraRsAttEntP": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/attentp-HX1_AAEP",
            "tRn": null,
            "name": "HX1_AAEP"
        },
        "infraRsSpanVSrcGrp": {
            "__Output": {},
            "state": null,
            "tDn": null,
            "tRn": null,
            "name": "--"
        },
        "infraRsSpanVDestGrp": {
            "__Output": {},
            "state": null,
            "tDn": null,
            "tRn": null,
            "name": "--"
        },
        "infraRsL2IfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/l2IfP-L2-local_Pol",
            "tRn": "l2IfP-L2-local_Pol",
            "name": "L2-local_Pol"
        },
        "infraRsStormctrlIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/stormctrlifp-default",
            "tRn": "stormctrlifp-default",
            "name": "default"
        },
        "infraRsQosEgressDppIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/qosdpppol-default",
            "tRn": "qosdpppol-default",
            "name": "default"
        },
        "infraRsQosIngressDppIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/qosdpppol-default",
            "tRn": "qosdpppol-default",
            "name": "default"
        },
        "infraRsQosSdIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/qossdpol-default",
            "tRn": "qossdpol-default",
            "name": "default"
        },
        "infraRsQosPfcIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/pfc-default",
            "tRn": "pfc-default",
            "name": "default"
        },
        "infraRsL2PortSecurityPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/portsecurityP-default",
            "tRn": "portsecurityP-default",
            "name": "default"
        },
        "infraRsFcIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/fcIfPol-default",
            "tRn": "fcIfPol-default",
            "name": "default"
        },
        "infraRsMacsecIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/macsecifp-default",
            "tRn": "macsecifp-default",
            "name": "default"
        },
        "faults": "0 0 0 0",
        "isAnyFault": false
    }
]
```

[[Back]](./PgAccessInterfaceVpc.md)