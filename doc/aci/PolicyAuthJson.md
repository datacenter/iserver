# Policy - 802.1X

## JSON

```
# iserver get aci policy auth --apic apic11 --name default -o json

[
    {
        "__Output": {
            "adminSt": "Red"
        },
        "adminSt": "disabled",
        "annotation": "",
        "dn": "uni/infra/portauthpol-default",
        "hostMode": "single-host",
        "name": "default",
        "tf": false,
        "tfTick": "",
        "relnFrom": [
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-BERLIN-35-RDC-3-vlan]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-BERLIN-35-RDC-3-vlan",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "BERLIN-35-RDC-3-vlan"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-ESX-CDC-DVS_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-ESX-CDC-DVS_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "ESX-CDC-DVS_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-ESX-CDC_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-ESX-CDC_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "ESX-CDC_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-ESX-R3DC-DVS_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-ESX-R3DC-DVS_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "ESX-R3DC-DVS_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-IKS1-mgmt_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-IKS1-mgmt_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "IKS1-mgmt_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-IKS2-mgmt_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-IKS2-mgmt_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "IKS2-mgmt_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-Infra-BGP_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-Infra-BGP_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "Infra-BGP_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-Infra-L3_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-Infra-L3_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "Infra-L3_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-Infra_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-Infra_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "Infra_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-ACI1-Napoli_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-ACI1-Napoli_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-ACI1-Napoli_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-CU-PCIe1-A_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-CU-PCIe1-A_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-CU-PCIe1-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-CU-PCIe2-A_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-CU-PCIe2-A_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-CU-PCIe2-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-Core-MLOM-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-Core-MLOM-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-Core-MLOM-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-Core-PCIe1-A_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-Core-PCIe1-A_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-Core-PCIe1-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-Core-PCIe2-A_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-Core-PCIe2-A_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-Core-PCIe2-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-P5G-LOM_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-P5G-LOM_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "P5G-LOM_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-SR-Demo-CDC-2-vlan]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-SR-Demo-CDC-2-vlan",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "SR-Demo-CDC-2-vlan"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-SR-Demo-RDC-3-vlan]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-SR-Demo-RDC-3-vlan",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "SR-Demo-RDC-3-vlan"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-cvim4-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-cvim4-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "cvim4-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-cvim4-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-cvim4-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "cvim4-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-nidemo-dummy]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-nidemo-dummy",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "nidemo-dummy"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-AIO-1-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-AIO-1-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-AIO-1-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-AIO-1-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-AIO-1-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-AIO-1-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-AIO-2-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-AIO-2-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-AIO-2-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-AIO-2-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-AIO-2-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-AIO-2-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-AIO-3-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-AIO-3-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-AIO-3-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-AIO-3-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-AIO-3-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-AIO-3-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-COMP-1-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-COMP-1-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-COMP-1-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-COMP-1-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-COMP-1-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-COMP-1-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-COMP-2-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-COMP-2-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-COMP-2-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-COMP-2-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-COMP-2-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-COMP-2-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-SRIOV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-SRIOV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-SRIOV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-SRIOV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-SRIOV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-SRIOV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod1a-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod1a-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod1a-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-AIO-1-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-AIO-1-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-AIO-1-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-AIO-1-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-AIO-1-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-AIO-1-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-AIO-2-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-AIO-2-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-AIO-2-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-AIO-2-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-AIO-2-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-AIO-2-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-AIO-3-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-AIO-3-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-AIO-3-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-AIO-3-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-AIO-3-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-AIO-3-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-COMP-1-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-COMP-1-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-COMP-1-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-COMP-1-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-COMP-1-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-COMP-1-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-COMP-2-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-COMP-2-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-COMP-2-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-COMP-2-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-COMP-2-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-COMP-2-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-COMP-3-SRIoV-0_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-COMP-3-SRIoV-0_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-COMP-3-SRIoV-0_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accportgrp-pod4a-COMP-3-SRIoV-1_PolGrp]",
                "tCl": "infraAccPortGrp",
                "tDn": "uni/infra/funcprof/accportgrp-pod4a-COMP-3-SRIoV-1_PolGrp",
                "policyType": "Leaf Access Port Policy Group",
                "policyName": "pod4a-COMP-3-SRIoV-1_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "HX1-FI-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "HX1-FI-B_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-Infra-2_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-Infra-2_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "Infra-2_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-Infra_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-Infra_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "Infra_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-NXOS_FABRIC_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-NXOS_FABRIC_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "NXOS_FABRIC_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-SPN_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-SPN_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "SPN_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "UCSB1-FI-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-UCSB1-FI-B_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-UCSB1-FI-B_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "UCSB1-FI-B_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-A_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-A_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "UCSB1-R3DC-FI-A_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-UCSB1-R3DC-FI-B_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "UCSB1-R3DC-FI-B_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod-4a-br-API]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod-4a-br-API",
                "policyType": "PC/VPC Interface",
                "policyName": "pod-4a-br-API"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-AIO-1-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-AIO-1-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-AIO-1-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-AIO-1-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-AIO-1-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-AIO-2-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-AIO-2-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-AIO-2-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-AIO-2-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-AIO-2-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-AIO-3-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-AIO-3-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-AIO-3-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-AIO-3-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-AIO-3-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-API_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-API_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-API_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-COMP-1-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-COMP-1-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-COMP-1-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-COMP-1-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-COMP-1-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-COMP-2-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-COMP-2-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-COMP-2-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-COMP-2-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-COMP-2-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-MX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-MX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-MX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod1a-NVBench_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod1a-NVBench_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod1a-NVBench_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-AIO-1-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-AIO-1-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-AIO-1-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-AIO-1-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-AIO-1-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-AIO-2-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-AIO-2-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-AIO-2-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-AIO-2-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-AIO-3-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-AIO-3-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-AIO-3-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-AIO-3-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-COMP-1-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-COMP-1-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-COMP-1-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-COMP-1-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-COMP-2-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-COMP-2-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-COMP-2-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-COMP-2-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-COMP-3-PET_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-COMP-3-PET_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-COMP-3-PET_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-COMP-3-SAMX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-COMP-3-SAMX_PolGrp"
            },
            {
                "class": "l2PortAuthPol",
                "rn": "rtinfraL2PortAuthPol-[uni/infra/funcprof/accbundle-pod4a-MX_PolGrp]",
                "tCl": "infraAccBndlGrp",
                "tDn": "uni/infra/funcprof/accbundle-pod4a-MX_PolGrp",
                "policyType": "PC/VPC Interface",
                "policyName": "pod4a-MX_PolGrp"
            }
        ],
        "references": 83,
        "l1RsL2PortAuthCons": [],
        "interfaces": 0,
        "nodeInterfaces": []
    }
]
```

[[Back]](./PolicyAuth.md)