# Policy Group - Access Interface - Leaf Access Port

## JSON

```
# iserver get aci pg access intf port --apic apic11 --name P5G* -o json

[
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G ACI1 to Napoli 45 Trunk (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-ACI1-Napoli_PolGrp",
        "name": "P5G-ACI1-Napoli_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G-Core Management Interface on MLOM (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-Core-MLOM-1_PolGrp",
        "name": "P5G-Core-MLOM-1_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G-Core NGU (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-Core-PCIe1-A_PolGrp",
        "name": "P5G-Core-PCIe1-A_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G-Core mgmt,NGC (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-Core-PCIe2-A_PolGrp",
        "name": "P5G-Core-PCIe2-A_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G-CU NGU (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-CU-PCIe1-A_PolGrp",
        "name": "P5G-CU-PCIe1-A_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G-CU mgmt,F1C,F1U,NGC (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-CU-PCIe2-A_PolGrp",
        "name": "P5G-CU-PCIe2-A_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    },
    {
        "__Output": {},
        "annotation": "",
        "descr": "P5G-DU Management Interface (Created by Ansible)",
        "dn": "uni/infra/funcprof/accportgrp-P5G-LOM_PolGrp",
        "name": "P5G-LOM_PolGrp",
        "aaep_name": "Private5G_AAEP",
        "policy": {
            "infraRsAttEntP": "",
            "infraRsCdpIfPol": "default",
            "infraRsHIfPol": "Inherit",
            "infraRsLinkFlapPol": "default",
            "infraRsLldpIfPol": "LLDP_enable",
            "infraRsMonIfInfraPol": "default",
            "infraRsStpIfPol": "default",
            "infraRsMcpIfPol": "default",
            "infraRsStormctrlIfPol": "default"
        }
    }
]
```

[[Back]](./PgAccessInterfacePort.md)