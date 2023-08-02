# Policy Group - Access Interface - Leaf Access Port

## JSON output

```
# iserver get aci pg access intf port --apic apic21 --name *sriov* -o json

[
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "annotation": "orchestrator:terraform",
        "descr": "k8s_sriov_bm Access Policy",
        "dn": "uni/infra/funcprof/accportgrp-k8s_sriov_2207_bm_PolGrp",
        "name": "k8s_sriov_2207_bm_PolGrp",
        "infraRsAttEntP": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/attentp-k8s_phys_AAEP",
            "tRn": null,
            "name": "k8s_phys_AAEP"
        },
        "infraRsCdpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/cdpIfP-k8s_cdp_enable",
            "tRn": "cdpIfP-k8s_cdp_enable",
            "name": "k8s_cdp_enable"
        },
        "infraRsHIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/hintfpol-k8s_default",
            "tRn": "hintfpol-k8s_default",
            "name": "k8s_default"
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
            "tDn": "uni/infra/lldpIfP-k8s_lldp_enable",
            "tRn": "lldpIfP-k8s_lldp_enable",
            "name": "k8s_lldp_enable"
        },
        "infraRsMonIfInfraPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/moninfra-default",
            "tRn": "moninfra-default",
            "name": "default"
        },
        "infraRsStpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/ifPol-default",
            "tRn": "ifPol-default",
            "name": "default"
        },
        "infraRsMcpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/mcpIfP-default",
            "tRn": "mcpIfP-default",
            "name": "default"
        },
        "infraRsStormctrlIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/stormctrlifp-default",
            "tRn": "stormctrlifp-default",
            "name": "default"
        },
        "faults": "0 0 0 0",
        "isAnyFault": false
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "annotation": "orchestrator:terraform",
        "descr": "k8s_sriov_esx Access Policy",
        "dn": "uni/infra/funcprof/accportgrp-k8s_sriov_2207_esx_PolGrp",
        "name": "k8s_sriov_2207_esx_PolGrp",
        "infraRsAttEntP": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/attentp-k8s_phys_AAEP",
            "tRn": null,
            "name": "k8s_phys_AAEP"
        },
        "infraRsCdpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/cdpIfP-k8s_cdp_enable",
            "tRn": "cdpIfP-k8s_cdp_enable",
            "name": "k8s_cdp_enable"
        },
        "infraRsHIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/hintfpol-k8s_default",
            "tRn": "hintfpol-k8s_default",
            "name": "k8s_default"
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
            "tDn": "uni/infra/lldpIfP-k8s_lldp_enable",
            "tRn": "lldpIfP-k8s_lldp_enable",
            "name": "k8s_lldp_enable"
        },
        "infraRsMonIfInfraPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/moninfra-default",
            "tRn": "moninfra-default",
            "name": "default"
        },
        "infraRsStpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/ifPol-default",
            "tRn": "ifPol-default",
            "name": "default"
        },
        "infraRsMcpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/mcpIfP-default",
            "tRn": "mcpIfP-default",
            "name": "default"
        },
        "infraRsStormctrlIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/stormctrlifp-default",
            "tRn": "stormctrlifp-default",
            "name": "default"
        },
        "faults": "0 0 0 0",
        "isAnyFault": false
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "annotation": "orchestrator:terraform",
        "descr": "k8s_sriov_bm Access Policy",
        "dn": "uni/infra/funcprof/accportgrp-k8s_sriov_2208_bm_PolGrp",
        "name": "k8s_sriov_2208_bm_PolGrp",
        "infraRsAttEntP": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/attentp-k8s_phys_AAEP",
            "tRn": null,
            "name": "k8s_phys_AAEP"
        },
        "infraRsCdpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/cdpIfP-k8s_cdp_enable",
            "tRn": "cdpIfP-k8s_cdp_enable",
            "name": "k8s_cdp_enable"
        },
        "infraRsHIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/hintfpol-k8s_default",
            "tRn": "hintfpol-k8s_default",
            "name": "k8s_default"
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
            "tDn": "uni/infra/lldpIfP-k8s_lldp_enable",
            "tRn": "lldpIfP-k8s_lldp_enable",
            "name": "k8s_lldp_enable"
        },
        "infraRsMonIfInfraPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/moninfra-default",
            "tRn": "moninfra-default",
            "name": "default"
        },
        "infraRsStpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/ifPol-default",
            "tRn": "ifPol-default",
            "name": "default"
        },
        "infraRsMcpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/mcpIfP-default",
            "tRn": "mcpIfP-default",
            "name": "default"
        },
        "infraRsStormctrlIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/stormctrlifp-default",
            "tRn": "stormctrlifp-default",
            "name": "default"
        },
        "faults": "0 0 0 0",
        "isAnyFault": false
    },
    {
        "__Output": {
            "faults": ":R.M.Y.G"
        },
        "annotation": "orchestrator:terraform",
        "descr": "k8s_sriov_esx Access Policy",
        "dn": "uni/infra/funcprof/accportgrp-k8s_sriov_2208_esx_PolGrp",
        "name": "k8s_sriov_2208_esx_PolGrp",
        "infraRsAttEntP": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/attentp-k8s_phys_AAEP",
            "tRn": null,
            "name": "k8s_phys_AAEP"
        },
        "infraRsCdpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/cdpIfP-k8s_cdp_enable",
            "tRn": "cdpIfP-k8s_cdp_enable",
            "name": "k8s_cdp_enable"
        },
        "infraRsHIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/hintfpol-k8s_default",
            "tRn": "hintfpol-k8s_default",
            "name": "k8s_default"
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
            "tDn": "uni/infra/lldpIfP-k8s_lldp_enable",
            "tRn": "lldpIfP-k8s_lldp_enable",
            "name": "k8s_lldp_enable"
        },
        "infraRsMonIfInfraPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/moninfra-default",
            "tRn": "moninfra-default",
            "name": "default"
        },
        "infraRsStpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/ifPol-default",
            "tRn": "ifPol-default",
            "name": "default"
        },
        "infraRsMcpIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/mcpIfP-default",
            "tRn": "mcpIfP-default",
            "name": "default"
        },
        "infraRsStormctrlIfPol": {
            "__Output": {},
            "state": "formed",
            "tDn": "uni/infra/stormctrlifp-default",
            "tRn": "stormctrlifp-default",
            "name": "default"
        },
        "faults": "0 0 0 0",
        "isAnyFault": false
    }
]
```

[[Back]](./PgAccessInterfacePort.md)