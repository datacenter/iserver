# Application Endpoint Group (EPG)

## JSON format

```
# iserver get aci epg --apic apic21 --name vk8s_1 --view verbose -o json

[
    {
        "__Output": {
            "adminUpTick": "Green",
            "configSt": "Green",
            "contractTick": "Green"
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
        "contractTick": "\u2713",
        "bd_tenant_name": "k8s",
        "bd_name": "vk8s_1_BD",
        "fabricNode": [
            {
                "__Output": {
                    "adSt": "Green",
                    "fabricSt": "Green"
                },
                "address": "10.5.240.34",
                "adSt": "on",
                "apicType": "apic",
                "dn": "topology/pod-1/node-2207",
                "id": "2207",
                "fabricSt": "active",
                "model": "N9K-C9336C-FX2",
                "name": "cl2207-eu-spdc",
                "nodeType": "unspecified",
                "role": "leaf",
                "serial": "FDO23490E4G",
                "userdom": "all",
                "vendor": "Cisco Systems, Inc",
                "version": "n9000-15.2(7f)",
                "podId": "1",
                "apic": "apic21",
                "pod_node_name": "pod-1/cl2207-eu-spdc",
                "roleUi": "leaf"
            },
            {
                "__Output": {
                    "adSt": "Green",
                    "fabricSt": "Green"
                },
                "address": "10.5.240.35",
                "adSt": "on",
                "apicType": "apic",
                "dn": "topology/pod-1/node-2208",
                "id": "2208",
                "fabricSt": "active",
                "model": "N9K-C9336C-FX2",
                "name": "cl2208-eu-spdc",
                "nodeType": "unspecified",
                "role": "leaf",
                "serial": "FDO234807ED",
                "userdom": "all",
                "vendor": "Cisco Systems, Inc",
                "version": "n9000-15.2(7f)",
                "podId": "1",
                "apic": "apic21",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "roleUi": "leaf"
            }
        ],
        "fvBD": {
            "__Output": {
                "mcastAllowTick": "Red",
                "ipv6McastAllowTick": "Red"
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
            "mcastARPDrop": "yes",
            "mcastAllow": "no",
            "mtu": "inherit",
            "multiDstPktAct": "bd-flood",
            "name": "vk8s_1_BD",
            "seg": "15007706",
            "type": "regular",
            "unicastRoute": "yes",
            "unkMacUcastAct": "flood",
            "unkMcastAct": "flood",
            "v6unkMcastAct": "flood",
            "vmac": "",
            "tenant": "k8s",
            "nameTenant": "k8s/vk8s_1_BD",
            "mcastAllowTick": "\u2717",
            "ipv6McastAllowTick": "\u2717",
            "health": {
                "__Output": {
                    "score": "Green"
                },
                "score": "100"
            },
            "fvSubnet": [
                {
                    "__Output": {},
                    "ip": "10.58.24.174/28",
                    "ipDPLearning": "enabled",
                    "preferred": "no",
                    "rn": "subnet-[10.58.24.174/28]",
                    "scope": "public",
                    "virtual": "no",
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
            "fvCtxInfo": {
                "__Output": {},
                "bdEnforcedEnable": "no",
                "descr": "",
                "dn": "uni/tn-common/ctx-Infra_VRF",
                "ipDataPlaneLearning": "enabled",
                "knwMcastAct": "permit",
                "name": "Infra_VRF",
                "pcEnfDir": "ingress",
                "pcEnfPref": "unenforced",
                "userdom": ":all:common:",
                "vrfIndex": "0",
                "tenant": "common",
                "nameTenant": "common/Infra_VRF"
            },
            "l3extOutInfo": [
                {
                    "__Output": {
                        "mplsEnabledTick": "Red"
                    },
                    "descr": "",
                    "dn": "uni/tn-common/out-Infra_L3out",
                    "enforceRtctrl": "export",
                    "mplsEnabled": false,
                    "name": "Infra_L3out",
                    "targetDscp": "unspecified",
                    "userdom": ":all:common:",
                    "mplsEnabledTick": "\u2717",
                    "tenant": "common",
                    "nameTenant": "common/Infra_L3out",
                    "l3extRsL3DomAtt": {
                        "__Output": {},
                        "dn": "uni/l3dom-Infra_L3Dom",
                        "name": "Infra_L3Dom"
                    },
                    "bgpExtP": {
                        "__Output": {
                            "enabledTick": "Green"
                        },
                        "enabled": true,
                        "enabledTick": "\u2713"
                    },
                    "ospfExtP": {
                        "__Output": {
                            "enabledTick": "Red"
                        },
                        "enabled": false,
                        "enabledTick": "\u2717"
                    },
                    "eigrpExtP": {
                        "__Output": {
                            "enabledTick": "Red"
                        },
                        "enabled": false,
                        "enabledTick": "\u2717"
                    },
                    "pimExtP": {
                        "__Output": {
                            "enabledTick": "Red"
                        },
                        "enabled": false,
                        "enabledTick": "\u2717"
                    },
                    "l3extRsEctx": {
                        "__Output": {
                            "enabledTick": "Green"
                        },
                        "enabled": true,
                        "enabledTick": "\u2713",
                        "dn": "uni/tn-common/ctx-Infra_VRF",
                        "tenant": "common",
                        "name": "Infra_VRF",
                        "nameTenant": "common/Infra_VRF"
                    },
                    "nodeProfiles": [],
                    "l3extInstP": [
                        {
                            "__Output": {
                                "configSt": "Green"
                            },
                            "annotation": "orchestrator:terraform",
                            "configSt": "applied",
                            "descr": "",
                            "exceptionTag": "",
                            "floodOnEncap": "disabled",
                            "isSharedSrvMsiteEPg": "no",
                            "matchT": "AtleastOne",
                            "name": "Infra_L3out_ExtEPG",
                            "nameAlias": "",
                            "pcEnfPref": "unenforced",
                            "pcTag": "32779",
                            "prefGrMemb": "exclude",
                            "prio": "unspecified",
                            "rn": "instP-Infra_L3out_ExtEPG",
                            "status": "",
                            "targetDscp": "unspecified"
                        }
                    ],
                    "nodes": []
                }
            ]
        },
        "fvCEp": [
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:11:50",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:11:50",
                "name": "00:50:56:B4:11:50",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
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
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14045]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14045",
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
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:3D:19",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:3D:19",
                "name": "00:50:56:B4:3D:19",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.170",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14067]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14067",
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
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:67:1F",
                "name": "00:50:56:B4:67:1F",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.167",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14060]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14060",
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
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:85:73",
                "name": "00:50:56:B4:85:73",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.162",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    },
                    {
                        "__Output": {},
                        "addr": "10.58.24.165",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14058]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14058",
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
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:9C:81",
                "name": "00:50:56:B4:9C:81",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "fvIp": [
                    {
                        "__Output": {},
                        "addr": "10.58.24.163",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    },
                    {
                        "__Output": {},
                        "addr": "10.58.24.168",
                        "baseEpgDn": "",
                        "vrfDn": "uni/tn-common/ctx-Infra_VRF"
                    }
                ],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14068]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14068",
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
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2207/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:9E:D0",
                "name": "00:50:56:B4:9E:D0",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
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
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14069]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14069",
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
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D2:45",
                "encap": "vlan-1367",
                "fabricPathDn": "",
                "lcC": "vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:D2:45",
                "name": "00:50:56:B4:D2:45",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "V",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
                "fvIp": [],
                "fvRsToVm": {
                    "__Output": {},
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14056]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14056",
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
                "fabric": []
            },
            {
                "__Output": {},
                "bdDn": "uni/tn-k8s/BD-vk8s_1_BD",
                "dn": "uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A",
                "encap": "vlan-1367",
                "fabricPathDn": "topology/pod-1/paths-2208/pathep-[k8s_esx71_PolGrp]",
                "lcC": "learned,vmm",
                "lcOwn": "local",
                "mac": "00:50:56:B4:EB:6A",
                "name": "00:50:56:B4:EB:6A",
                "userdom": "all",
                "vrfDn": "uni/tn-common/ctx-Infra_VRF",
                "flags": "LV",
                "tenant": "k8s",
                "vrfTenant": "common",
                "vrfCtx": "Infra_VRF",
                "vrfName": "common/Infra_VRF",
                "bdTenant": "k8s",
                "bdCtx": "vk8s_1_BD",
                "bdName": "k8s/vk8s_1_BD",
                "epgName": "vk8s_1",
                "apName": "k8s_ANP",
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
                    "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14059]",
                    "state": "formed",
                    "tCl": "compVm",
                    "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-14059",
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
            }
        ],
        "endpointsCount": 8,
        "contractConsumedInfo": [
            {
                "__Output": {},
                "descr": "",
                "dn": "uni/tn-common/brc-k8s_vm",
                "intent": "install",
                "name": "k8s_vm",
                "scope": "global",
                "targetDscp": "unspecified",
                "userdom": ":all:common:",
                "tenant": "common",
                "nameTenant": "common/k8s_vm",
                "vzFilter": [
                    {
                        "__Output": {},
                        "descr": "",
                        "dn": "uni/tn-common/flt-any",
                        "name": "any",
                        "userdom": ":all:common:",
                        "tenant": "common",
                        "nameTenant": "common/any",
                        "vzEntry": [
                            {
                                "__Output": {},
                                "applyToFrag": "no",
                                "arpOpc": "",
                                "dFromPort": "unspecified",
                                "dToPort": "unspecified",
                                "descr": "",
                                "etherT": "ipv4",
                                "icmpv4T": "unspecified",
                                "icmpv6T": "unspecified",
                                "matchDscp": "unspecified",
                                "name": "any",
                                "prot": "",
                                "sFromPort": "unspecified",
                                "sToPort": "unspecified",
                                "stateful": "no",
                                "status": "",
                                "tcpRules": "",
                                "source": "",
                                "destination": ""
                            }
                        ],
                        "subjectName": "k8s_tn_bm",
                        "subjectTenant": "k8s",
                        "subjectNameTenant": "k8s/k8s_tn_bm"
                    }
                ],
                "consumerEpg": [
                    {
                        "class": "fvAEPg",
                        "tenant": "k8s",
                        "application_profile": "k8s_ANP",
                        "name": "vk8s_3",
                        "nameTenant": "k8s/vk8s_3",
                        "nameLong": "k8s/k8s_ANP/vk8s_3"
                    },
                    {
                        "class": "fvAEPg",
                        "tenant": "k8s",
                        "application_profile": "k8s_ANP",
                        "name": "vk8s_1",
                        "nameTenant": "k8s/vk8s_1",
                        "nameLong": "k8s/k8s_ANP/vk8s_1"
                    },
                    {
                        "class": "fvAEPg",
                        "tenant": "k8s",
                        "application_profile": "k8s_ANP",
                        "name": "vk8s_4",
                        "nameTenant": "k8s/vk8s_4",
                        "nameLong": "k8s/k8s_ANP/vk8s_4"
                    },
                    {
                        "class": "fvAEPg",
                        "tenant": "k8s",
                        "application_profile": "k8s_ANP",
                        "name": "vk8s_2",
                        "nameTenant": "k8s/vk8s_2",
                        "nameLong": "k8s/k8s_ANP/vk8s_2"
                    }
                ],
                "providerEpg": [
                    {
                        "class": "l3extInstP",
                        "tenant": "common",
                        "l3out": "Infra_L3out",
                        "name": "Infra_L3out_ExtEPG",
                        "nameTenant": "common/Infra_L3out_ExtEPG",
                        "nameLong": "common/Infra_L3out/Infra_L3out_ExtEPG"
                    }
                ]
            }
        ],
        "contractProvidedInfo": []
    }
]
```

[[Back]](./ApplicationEpg.md)