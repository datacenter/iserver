# Bridge Domain

## JSON output

```
# iserver get aci bd --apic apic21 --name vk8s_1* --view verbose -o json

[
    {
        "__Output": {
            "mcastAllowTick": "Red",
            "ipv6McastAllowTick": "Red",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "arpFlood": "yes",
        "bcastP": "225.1.58.128",
        "descr": "Cloud_1_BD (Managed by Terraform)",
        "dn": "uni/tn-k8s/BD-vk8s_1_BD",
        "epClear": "no",
        "epMoveDetectMode": "",
        "hostBasedRouting": "no",
        "intersiteBumTrafficAllow": "no",
        "intersiteL2Stretch": "no",
        "ipLearning": "yes",
        "ipv6McastAllow": "no",
        "limitIpLearnToSubnets": "yes",
        "llAddr": "::",
        "mac": "00:22:BD:C8:11:FF",
        "mcastARPDrop": "no",
        "mcastAllow": "no",
        "mtu": "inherit",
        "multiDstPktAct": "bd-flood",
        "name": "vk8s_1_BD",
        "pcTag": "16399",
        "seg": "15007706",
        "type": "regular",
        "unicastRoute": "yes",
        "unkMacUcastAct": "flood",
        "unkMcastAct": "flood",
        "v6unkMcastAct": "flood",
        "vmac": "",
        "unkMacUcastActT": "Flood",
        "multiDstPktActT": "Flood in BD",
        "arpFloodTick": "\u2713",
        "epClearTick": "\u2717",
        "intersiteL2StretchTick": "\u2717",
        "unicastRouteTick": "\u2713",
        "ipLearningTick": "\u2713",
        "limitIpLearnToSubnetsTick": "\u2713",
        "hostBasedRoutingTick": "\u2717",
        "vmacT": "--",
        "epMoveDetectModeT": "--",
        "mcastAllowTick": "\u2717",
        "unkMcastActT": "Flood",
        "ipv6McastAllowTick": "\u2717",
        "v6unkMcastActT": "Flood",
        "tenant": "k8s",
        "nameTenant": "k8s/vk8s_1_BD",
        "fvSubnet": [
            {
                "__Output": {},
                "ip": "10.58.24.174/28",
                "ipDPLearning": "enabled",
                "preferred": "no",
                "rn": "subnet-[10.58.24.174/28]",
                "scope": "public",
                "virtual": "no",
                "preferredTick": "\u2717",
                "virtualTick": "\u2717",
                "ipDPLearningTick": "\u2713",
                "network": "10.58.24.160/28",
                "gateway": "10.58.24.174",
                "size": 14,
                "endpoints": 10,
                "usage": "10/14",
                "available": 4
            }
        ],
        "fvSubnetCount": 1,
        "fvSubnets": "10.58.24.174/28",
        "fvRsCtx": {
            "__Output": {},
            "dn": "uni/tn-common/ctx-Infra_VRF",
            "state": "formed",
            "tenant": "common",
            "name": "Infra_VRF",
            "nameTenant": "common/Infra_VRF"
        },
        "fvRsBDToOut": [
            {
                "__Output": {},
                "tenant": "common",
                "name": "Infra_L3out",
                "nameTenant": "common/Infra_L3out"
            }
        ],
        "l3OutCount": 1,
        "fvRsIgmpsn": {
            "__Output": {},
            "state": "formed",
            "tenant": "common",
            "configuredPolicyName": "",
            "actualPolicyName": "default",
            "name": "default",
            "nameTenant": "common/default",
            "policy": {
                "__Output": {
                    "adminSt": "Green"
                },
                "adminSt": "enabled",
                "dn": "uni/tn-common/snPol-default",
                "lastMbrIntvl": "1",
                "name": "default",
                "queryIntvl": "125",
                "rspIntvl": "10",
                "startQueryCnt": "2",
                "startQueryIntvl": "31",
                "tenant": "common",
                "nameTenant": "common/default"
            }
        },
        "fvRsMldsn": {
            "__Output": {},
            "tenant": "common",
            "configuredPolicyName": "",
            "actualPolicyName": "default",
            "name": "default",
            "nameTenant": "common/default",
            "policy": {
                "__Output": {
                    "adminSt": "Red"
                },
                "adminSt": "disabled",
                "dn": "uni/tn-common/mldsnoopPol-default",
                "lastMbrIntvl": "1",
                "name": "default",
                "queryIntvl": "125",
                "rspIntvl": "10",
                "startQueryCnt": "2",
                "startQueryIntvl": "31",
                "ver": "v2",
                "tenant": "common",
                "nameTenant": "common/default"
            }
        },
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "fvCtx": {
            "__Output": {
                "health": "Green",
                "faults": ":R.M.Y.G"
            },
            "bdEnforcedEnable": "no",
            "descr": "",
            "dn": "uni/tn-common/ctx-Infra_VRF",
            "ipDataPlaneLearning": "enabled",
            "knwMcastAct": "permit",
            "name": "Infra_VRF",
            "pcEnfDir": "ingress",
            "pcEnfPref": "unenforced",
            "pcTag": "49153",
            "seg": "2818048",
            "userdom": ":all:common:",
            "vrfIndex": "0",
            "tenant": "common",
            "nameTenant": "common/Infra_VRF",
            "pcTagT": "49153",
            "ipDataPlaneLearningTick": "\u2713",
            "bdEnforcedEnableTick": "\u2717",
            "knwMcastActTick": "\u2713",
            "health": "100",
            "faults": "0 0 0 0",
            "isAnyFault": false
        },
        "fvAEPg": [
            {
                "__Output": {
                    "adminUpTick": "Green",
                    "configSt": "Green",
                    "contractTick": "Green",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "annotation": "orchestrator:terraform",
                "configSt": "applied",
                "descr": "",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1",
                "exceptionTag": "",
                "floodOnEncap": "disabled",
                "hasMcastSource": "no",
                "isAttrBasedEPg": "no",
                "matchT": "AtleastOne",
                "name": "vk8s_1",
                "nameAlias": "",
                "pcEnfPref": "unenforced",
                "pcTag": "49162",
                "prefGrMemb": "exclude",
                "prio": "unspecified",
                "shutdown": "no",
                "adminUp": true,
                "adminUpTick": "\u2713",
                "pcTagT": "49162",
                "tenant": "k8s",
                "nameTenant": "k8s/vk8s_1",
                "application_profile": "k8s_ANP",
                "nameApTenant": "k8s/k8s_ANP/vk8s_1",
                "contractConsumed": [
                    {
                        "dn": "uni/tn-common/brc-k8s_vm",
                        "tenant": "common",
                        "name": "k8s_vm",
                        "nameTenant": "common/k8s_vm"
                    }
                ],
                "contractProvided": [],
                "contractTaboo": [],
                "contractCount": 1,
                "contractTick": "\u2713",
                "bd_tenant_name": "k8s",
                "bd_name": "vk8s_1_BD",
                "bd_state": "formed",
                "staticPort": [],
                "staticPortCount": 0,
                "domain": [
                    {
                        "__Output": {},
                        "annotation": "orchestration:terraform",
                        "bindingType": "none",
                        "childAction": "",
                        "classPref": "encap",
                        "configIssues": "",
                        "customEpgName": "vk8s_1",
                        "delimiter": "|",
                        "encap": "unknown",
                        "encapMode": "auto",
                        "epgCos": "Cos0",
                        "epgCosPref": "disabled",
                        "extMngdBy": "",
                        "forceResolve": "yes",
                        "instrImedcy": "immediate",
                        "lagPolicyName": "",
                        "lcOwn": "local",
                        "modTs": "2023-01-10T16:08:13.888+02:00",
                        "mode": "default",
                        "monPolDn": "uni/tn-common/monepg-default",
                        "netflowDir": "both",
                        "netflowPref": "disabled",
                        "numPorts": "0",
                        "portAllocation": "none",
                        "primaryEncap": "unknown",
                        "primaryEncapInner": "unknown",
                        "rType": "mo",
                        "resImedcy": "immediate",
                        "rn": "rsdomAtt-[uni/vmmp-VMware/dom-EU-SPDC-POD2B]",
                        "secondaryEncapInner": "unknown",
                        "state": "formed",
                        "stateQual": "none",
                        "status": "",
                        "switchingMode": "native",
                        "tCl": "vmmDomP",
                        "tDn": "uni/vmmp-VMware/dom-EU-SPDC-POD2B",
                        "tType": "mo",
                        "triggerSt": "triggerable",
                        "txId": "7493989779970926464",
                        "uid": "15374",
                        "untagged": "no",
                        "userdom": ":all:common:",
                        "vnetOnly": "no",
                        "type": "vmmDomP",
                        "typeT": "VMM",
                        "vmmType": "VMware",
                        "vmmName": "EU-SPDC-POD2B",
                        "name": "VMware/EU-SPDC-POD2B"
                    },
                    {
                        "__Output": {},
                        "annotation": "orchestrator:terraform",
                        "bindingType": "none",
                        "childAction": "",
                        "classPref": "encap",
                        "configIssues": "",
                        "customEpgName": "",
                        "delimiter": "",
                        "encap": "unknown",
                        "encapMode": "auto",
                        "epgCos": "Cos0",
                        "epgCosPref": "disabled",
                        "extMngdBy": "",
                        "forceResolve": "yes",
                        "instrImedcy": "lazy",
                        "lagPolicyName": "",
                        "lcOwn": "local",
                        "modTs": "2023-04-05T21:31:58.171+02:00",
                        "mode": "default",
                        "monPolDn": "uni/tn-common/monepg-default",
                        "netflowDir": "both",
                        "netflowPref": "disabled",
                        "numPorts": "0",
                        "portAllocation": "none",
                        "primaryEncap": "unknown",
                        "primaryEncapInner": "unknown",
                        "rType": "mo",
                        "resImedcy": "lazy",
                        "rn": "rsdomAtt-[uni/phys-k8s_esx_PhysDom]",
                        "secondaryEncapInner": "unknown",
                        "state": "formed",
                        "stateQual": "none",
                        "status": "",
                        "switchingMode": "native",
                        "tCl": "physDomP",
                        "tDn": "uni/phys-k8s_esx_PhysDom",
                        "tType": "mo",
                        "triggerSt": "not_triggerable",
                        "txId": "7493989779975624787",
                        "uid": "15374",
                        "untagged": "no",
                        "userdom": ":all:common:",
                        "vnetOnly": "no",
                        "type": "physDomP",
                        "typeT": "Physical",
                        "name": "k8s_esx_PhysDom"
                    }
                ],
                "domainCount": 2,
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "fvBD": {
                    "__Output": {
                        "mcastAllowTick": "Red",
                        "ipv6McastAllowTick": "Red",
                        "health": "Green",
                        "faults": ":R.M.Y.G"
                    },
                    "arpFlood": "yes",
                    "bcastP": "225.1.58.128",
                    "descr": "Cloud_1_BD (Managed by Terraform)",
                    "dn": "uni/tn-k8s/BD-vk8s_1_BD",
                    "epClear": "no",
                    "epMoveDetectMode": "",
                    "hostBasedRouting": "no",
                    "intersiteBumTrafficAllow": "no",
                    "intersiteL2Stretch": "no",
                    "ipLearning": "yes",
                    "ipv6McastAllow": "no",
                    "limitIpLearnToSubnets": "yes",
                    "llAddr": "::",
                    "mac": "00:22:BD:C8:11:FF",
                    "mcastARPDrop": "no",
                    "mcastAllow": "no",
                    "mtu": "inherit",
                    "multiDstPktAct": "bd-flood",
                    "name": "vk8s_1_BD",
                    "pcTag": "16399",
                    "seg": "15007706",
                    "type": "regular",
                    "unicastRoute": "yes",
                    "unkMacUcastAct": "flood",
                    "unkMcastAct": "flood",
                    "v6unkMcastAct": "flood",
                    "vmac": "",
                    "unkMacUcastActT": "Flood",
                    "multiDstPktActT": "Flood in BD",
                    "arpFloodTick": "\u2713",
                    "epClearTick": "\u2717",
                    "intersiteL2StretchTick": "\u2717",
                    "unicastRouteTick": "\u2713",
                    "ipLearningTick": "\u2713",
                    "limitIpLearnToSubnetsTick": "\u2713",
                    "hostBasedRoutingTick": "\u2717",
                    "vmacT": "--",
                    "epMoveDetectModeT": "--",
                    "mcastAllowTick": "\u2717",
                    "unkMcastActT": "Flood",
                    "ipv6McastAllowTick": "\u2717",
                    "v6unkMcastActT": "Flood",
                    "tenant": "k8s",
                    "nameTenant": "k8s/vk8s_1_BD",
                    "fvSubnet": [
                        {
                            "__Output": {},
                            "ip": "10.58.24.174/28",
                            "ipDPLearning": "enabled",
                            "preferred": "no",
                            "rn": "subnet-[10.58.24.174/28]",
                            "scope": "public",
                            "virtual": "no",
                            "preferredTick": "\u2717",
                            "virtualTick": "\u2717",
                            "ipDPLearningTick": "\u2713",
                            "network": "10.58.24.160/28",
                            "gateway": "10.58.24.174",
                            "size": 14,
                            "endpoints": 10,
                            "usage": "10/14",
                            "available": 4
                        }
                    ],
                    "fvSubnetCount": 1,
                    "fvSubnets": "10.58.24.174/28",
                    "fvRsCtx": {
                        "__Output": {},
                        "dn": "uni/tn-common/ctx-Infra_VRF",
                        "state": "formed",
                        "tenant": "common",
                        "name": "Infra_VRF",
                        "nameTenant": "common/Infra_VRF"
                    },
                    "fvRsBDToOut": [
                        {
                            "__Output": {},
                            "tenant": "common",
                            "name": "Infra_L3out",
                            "nameTenant": "common/Infra_L3out"
                        }
                    ],
                    "l3OutCount": 1,
                    "fvRsIgmpsn": {
                        "__Output": {},
                        "state": "formed",
                        "tenant": "common",
                        "configuredPolicyName": "",
                        "actualPolicyName": "default",
                        "name": "default",
                        "nameTenant": "common/default"
                    },
                    "fvRsMldsn": {
                        "__Output": {},
                        "tenant": "common",
                        "configuredPolicyName": "",
                        "actualPolicyName": "default",
                        "name": "default",
                        "nameTenant": "common/default"
                    },
                    "health": "100",
                    "faults": "0 0 0 0",
                    "isAnyFault": false,
                    "fvCtx": {
                        "__Output": {
                            "health": "Green",
                            "faults": ":R.M.Y.G"
                        },
                        "bdEnforcedEnable": "no",
                        "descr": "",
                        "dn": "uni/tn-common/ctx-Infra_VRF",
                        "ipDataPlaneLearning": "enabled",
                        "knwMcastAct": "permit",
                        "name": "Infra_VRF",
                        "pcEnfDir": "ingress",
                        "pcEnfPref": "unenforced",
                        "pcTag": "49153",
                        "seg": "2818048",
                        "userdom": ":all:common:",
                        "vrfIndex": "0",
                        "tenant": "common",
                        "nameTenant": "common/Infra_VRF",
                        "pcTagT": "49153",
                        "ipDataPlaneLearningTick": "\u2713",
                        "bdEnforcedEnableTick": "\u2717",
                        "knwMcastActTick": "\u2713",
                        "health": "100",
                        "faults": "0 0 0 0",
                        "isAnyFault": false
                    }
                },
                "fvCEp": [
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:04:A1",
                        "name": "00:50:56:B4:04:A1",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.163",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            },
                            {
                                "__Output": {},
                                "addr": "10.58.24.170",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17021]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17021",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx72_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:1F:B2",
                        "name": "00:50:56:B4:1F:B2",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.168",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17022]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17022",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:2B:BE",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:2B:BE",
                        "name": "00:50:56:B4:2B:BE",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.169",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17020]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17020",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:70:AD",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/protpaths-2207-2208/pathep-[k8s_esx71_PolGrp]",
                        "lcC": "vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:70:AD",
                        "name": "00:50:56:B4:70:AD",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "V",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17015]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17015",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:CE:19",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:CE:19",
                        "name": "00:50:56:B4:CE:19",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.161",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17014]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17014",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D3:91",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx72_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:D3:91",
                        "name": "00:50:56:B4:D3:91",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.165",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17019]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17019",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:DE:16",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:DE:16",
                        "name": "00:50:56:B4:DE:16",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.166",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17017]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17017",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                            "tType": "mo"
                        }
                    },
                    {
                        "__Output": {},
                        "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                        "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E7:C4",
                        "encap": "vlan-1367",
                        "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx72_PolGrp]",
                        "lcC": "learned,vmm",
                        "lcOwn": "local",
                        "mac": "00:50:56:B4:E7:C4",
                        "name": "00:50:56:B4:E7:C4",
                        "userdom": "all",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                        "flags": "LV",
                        "encapT": "1367",
                        "tenant": "k8s",
                        "vrfTenant": "common",
                        "vrfName": "Infra_VRF",
                        "vrfNameTenant": "common/Infra_VRF",
                        "bdTenant": "k8s",
                        "bdName": "vk8s_1_BD",
                        "bdNameTenant": "k8s/vk8s_1_BD",
                        "epgName": "vk8s_1",
                        "apName": "k8s_ANP",
                        "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                        "fvIp": [
                            {
                                "__Output": {},
                                "addr": "10.58.24.162",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            },
                            {
                                "__Output": {},
                                "addr": "10.58.24.167",
                                "baseEpgDn": "",
                                "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                            }
                        ],
                        "fvRsToVm": {
                            "__Output": {},
                            "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17018]",
                            "state": "formed",
                            "tCl": "compVm",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17018",
                            "tType": "mo"
                        },
                        "fvRsHyper": {
                            "__Output": {},
                            "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014]",
                            "state": "formed",
                            "tCl": "compHv",
                            "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                            "tType": "mo"
                        }
                    }
                ],
                "endpointCount": 8
            }
        ],
        "epgCount": 1,
        "fvCEp": [
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:04:A1",
                "name": "00:50:56:B4:04:A1",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.163",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    },
                    {
                        "__Output": {},
                        "addr": "10.58.24.170",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17021]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17021",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17021",
                    "name": "devel-fnrrp-worker-fvwck",
                    "oid": "vm-17021",
                    "os": "Red Hat Enterprise Linux 8 (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17021/vnic-00:50:56:B4:04:A1",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx71.emea-sp.cisco.com",
                    "oid": "host-11004",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2207 eth1/1/1 (k8s_esx71_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2208 eth1/1/1 (k8s_esx71_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx72_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:1F:B2",
                "name": "00:50:56:B4:1F:B2",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.168",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17022]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17022",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17022",
                    "name": "devel-fnrrp-worker-db2jd",
                    "oid": "vm-17022",
                    "os": "Red Hat Enterprise Linux 8 (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17022/vnic-00:50:56:B4:1F:B2",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx72.emea-sp.cisco.com",
                    "oid": "host-11014",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/2]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/2",
                        "ep": "pod-1 node-2207 eth1/1/2 (k8s_esx72_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/2]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/2",
                        "ep": "pod-1 node-2208 eth1/1/2 (k8s_esx72_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:2B:BE",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:2B:BE",
                "name": "00:50:56:B4:2B:BE",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.169",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17020]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17020",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17020",
                    "name": "devel-fnrrp-worker-tprng",
                    "oid": "vm-17020",
                    "os": "Red Hat Enterprise Linux 8 (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17020/vnic-00:50:56:B4:2B:BE",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx71.emea-sp.cisco.com",
                    "oid": "host-11004",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2207 eth1/1/1 (k8s_esx71_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2208 eth1/1/1 (k8s_esx71_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:70:AD",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/protpaths-2207-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:70:AD",
                "name": "00:50:56:B4:70:AD",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "V",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17015]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17015",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Red"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17015",
                    "name": "devel-fnrrp-rhcos",
                    "oid": "vm-17015",
                    "os": "",
                    "state": "poweredOff",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Red"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17015/vnic-00:50:56:B4:70:AD",
                    "name": "Network adapter 1",
                    "operSt": "down",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx71.emea-sp.cisco.com",
                    "oid": "host-11004",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2207 eth1/1/1 (k8s_esx71_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2208 eth1/1/1 (k8s_esx71_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:CE:19",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:CE:19",
                "name": "00:50:56:B4:CE:19",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.161",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17014]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17014",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Other (32-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17014",
                    "name": "ocp-devel-installer",
                    "oid": "vm-17014",
                    "os": "Red Hat Fedora (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17014/vnic-00:50:56:B4:CE:19",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx71.emea-sp.cisco.com",
                    "oid": "host-11004",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2207 eth1/1/1 (k8s_esx71_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2208 eth1/1/1 (k8s_esx71_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D3:91",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx72_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:D3:91",
                "name": "00:50:56:B4:D3:91",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.165",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17019]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17019",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17019",
                    "name": "devel-fnrrp-master-0",
                    "oid": "vm-17019",
                    "os": "Red Hat Enterprise Linux 8 (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17019/vnic-00:50:56:B4:D3:91",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx72.emea-sp.cisco.com",
                    "oid": "host-11014",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/2]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/2",
                        "ep": "pod-1 node-2207 eth1/1/2 (k8s_esx72_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/2]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/2",
                        "ep": "pod-1 node-2208 eth1/1/2 (k8s_esx72_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:DE:16",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:DE:16",
                "name": "00:50:56:B4:DE:16",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.166",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17017]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17017",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17017",
                    "name": "devel-fnrrp-master-1",
                    "oid": "vm-17017",
                    "os": "Red Hat Enterprise Linux 8 (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17017/vnic-00:50:56:B4:DE:16",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx71.emea-sp.cisco.com",
                    "oid": "host-11004",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2207 eth1/1/1 (k8s_esx71_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/1]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/1",
                        "ep": "pod-1 node-2208 eth1/1/1 (k8s_esx71_PolGrp)"
                    }
                ]
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E7:C4",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx72_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:E7:C4",
                "name": "00:50:56:B4:E7:C4",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "encapT": "1367",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfName": "Infra_VRF",
                "vrfNameTenant": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdName": "vk8s_1_BD",
                "bdNameTenant": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "epgNameApTenant": "k8s/k8s_ANP/vk8s_1",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.162",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    },
                    {
                        "__Output": {},
                        "addr": "10.58.24.167",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17018]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17018",
                    "tType": "mo"
                },
                "fvRsHyper": {
                    "__Output": {},
                    "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014]",
                    "state": "formed",
                    "tCl": "compHv",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                    "tType": "mo"
                },
                "vm": {
                    "__Output": {
                        "state": "Green"
                    },
                    "cfgdOs": "Red Hat Enterprise Linux 8 (64-bit)",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17018",
                    "name": "devel-fnrrp-master-2",
                    "oid": "vm-17018",
                    "os": "Red Hat Enterprise Linux 8 (64-bit)",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "vnic": {
                    "__Output": {
                        "operSt": "Green"
                    },
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-17018/vnic-00:50:56:B4:E7:C4",
                    "name": "Network adapter 1",
                    "operSt": "up",
                    "adapterType": "Vmxnet3"
                },
                "hv": {
                    "__Output": {},
                    "availAdminSt": "gray",
                    "availOperSt": "gray",
                    "countUplink": "0",
                    "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11014",
                    "enteringMaintenance": "no",
                    "mgmtIp": "0.0.0.0",
                    "name": "esx72.emea-sp.cisco.com",
                    "oid": "host-11014",
                    "state": "poweredOn",
                    "vmm": "EU-SPDC-POD2B"
                },
                "fabric": [
                    {
                        "dn": "topology/pod-1/node-2207/sys/phys-[eth1/1/2]",
                        "pod_id": "1",
                        "node_id": "2207",
                        "node_name": "cl2207-eu-spdc",
                        "port_id": "eth1/1/2",
                        "ep": "pod-1 node-2207 eth1/1/2 (k8s_esx72_PolGrp)"
                    },
                    {
                        "dn": "topology/pod-1/node-2208/sys/phys-[eth1/1/2]",
                        "pod_id": "1",
                        "node_id": "2208",
                        "node_name": "cl2208-eu-spdc",
                        "port_id": "eth1/1/2",
                        "ep": "pod-1 node-2208 eth1/1/2 (k8s_esx72_PolGrp)"
                    }
                ]
            }
        ],
        "endpointCount": 8
    }
]
```

[[Back]](./BridgeDomain.md)