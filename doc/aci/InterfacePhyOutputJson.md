# Node Interface - Physical

## JSON output

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --id 1/24
    --view verbose -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "switchingSt": "Green",
            "stats.bundleIndex": "Yellow",
            "stats.operSt": "Green"
        },
        "adminSt": "up",
        "autoNeg": "on",
        "bw": "0",
        "delay": "1",
        "descr": "",
        "dfeDelayMs": "0",
        "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]",
        "dot1qEtherType": "0x8100",
        "fecMode": "inherit",
        "id": "eth1/24",
        "layer": "Layer3",
        "linkDebounce": "100",
        "mdix": "auto",
        "medium": "broadcast",
        "mode": "trunk",
        "mtu": "9216",
        "name": "",
        "portPhyMediaType": "auto",
        "portT": "leaf",
        "routerMac": "not-applicable",
        "spanMode": "not-a-span-dest",
        "speed": "inherit",
        "switchingSt": "enabled",
        "usage": "epg",
        "portId": 24,
        "portName": "1/24",
        "podId": "1",
        "nodeId": "205",
        "nodeName": "bl205-eu-spdc",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl205-eu-spdc",
        "uplink": false,
        "downlink": true,
        "layerT": "routed",
        "stats": {
            "__Output": {
                "bundleIndex": "Yellow",
                "operSt": "Green"
            },
            "accessVlan": "vlan-1",
            "allowedVlans": "",
            "backplaneMac": "4C:71:0D:7E:84:08",
            "bundleIndex": "",
            "cfgAccessVlan": "vlan-1",
            "cfgNativeVlan": "vlan-1",
            "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]/phys",
            "encap": "3",
            "intfT": "phy",
            "lastLinkStChg": "2023-06-12T10:37:03.475+02:00",
            "media": "2",
            "nativeVlan": "vlan-1",
            "operDuplex": "full",
            "operErrDisQual": "none",
            "operFecMode": "cl91-rs-fec",
            "operFlowCtrl": "0",
            "operMdix": "auto",
            "operMode": "trunk",
            "operModeDetail": "unknown",
            "operPhyEnSt": "unknown",
            "operRouterMac": "00:00:00:00:00:00",
            "operSpeed": "100G",
            "operSt": "up",
            "operStQual": "connected",
            "operVlans": "",
            "osSum": "failed",
            "resetCtr": "1",
            "primaryVlan": "vlan-1",
            "txT": "unknown"
        },
        "up": true,
        "epg_stats": [],
        "ether_stats": {
            "broadcastPkts": "67",
            "cRCAlignErrors": "0",
            "childAction": "",
            "clearTs": "never",
            "collisions": "0",
            "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]/dbgEtherStats",
            "dropEvents": "0",
            "fragments": "0",
            "jabbers": "0",
            "modTs": "never",
            "multicastPkts": "16154",
            "octets": "13908461941",
            "oversizePkts": "19241",
            "pkts": "34047600",
            "pkts1024to1518Octets": "7106805",
            "pkts128to255Octets": "9442924",
            "pkts256to511Octets": "278847",
            "pkts512to1023Octets": "390150",
            "pkts64Octets": "111303",
            "pkts65to127Octets": "16698330",
            "rXNoErrors": "12701833",
            "rxGiantPkts": "0",
            "rxOversizePkts": "19227",
            "status": "",
            "tXNoErrors": "21345767",
            "txGiantPkts": "0",
            "txOversizePkts": "14",
            "undersizePkts": "0",
            "pod_id": "pod-1",
            "node_id": "node-205",
            "interface_id": "eth1/24"
        },
        "fc_stats": {
            "actualType": "qsfp28",
            "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]/phys/fcot",
            "guiCiscoPID": "QSFP-100G-AOC3M",
            "guiCiscoPN": "10-3174-03",
            "guiName": "CISCO-INNOLIGHT",
            "guiPN": "TF-FC003-NC2",
            "guiRev": "1B",
            "guiSN": "INL24358586-A",
            "isFcotPresent": "yes",
            "state": "inserted",
            "type": "qsfp28",
            "typeName": "QSFP-100G-AOC3M"
        },
        "load": {
            "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]/phys/portcap",
            "mdix": "0",
            "speed": "10000,100000,40000",
            "pod_id": "pod-1",
            "node_id": "node-205",
            "interface_id": "eth1/24"
        },
        "eee": {
            "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]/eeep",
            "eeeLat": "variable",
            "eeeLpi": "aggressive",
            "eeeState": "not-applicable",
            "pod_id": "pod-1",
            "node_id": "node-205",
            "interface_id": "eth1/24"
        },
        "cdp": [
            {
                "cap": "router,stp-dispute,switch",
                "devId": "ipn-eu-spdc.emea-sp.cisco.com(FOX2115PRJV)",
                "dn": "topology/pod-1/node-205/sys/cdp/inst/if-[eth1/24]/adj-1",
                "duplex": "full",
                "index": "1",
                "name": "",
                "nativeVlan": "unspecified",
                "platId": "N9K-C9504",
                "portId": "Ethernet3/25",
                "stQual": "",
                "status": "",
                "sysName": "ipn-eu-spdc",
                "sysObjIdL": "12",
                "sysObjIdV": "1,3,6,1,4,1,9,12,3,1,3,1507,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                "ver": "Cisco Nexus Operating System (NX-OS) Software, Version 9.3(9)",
                "pod_id": "pod-1",
                "node_id": "node-205",
                "interface_id": "eth1/24"
            }
        ],
        "lldp": [
            {
                "capability": "bridge,router",
                "chassisIdT": "mac",
                "chassisIdV": "ec:ce:13:c0:46:34",
                "dn": "topology/pod-1/node-205/sys/lldp/inst/if-[eth1/24]/adj-1",
                "enCap": "bridge,router",
                "id": "1",
                "mgmtId": "83886080",
                "mgmtIp": "10.58.234.128",
                "mgmtPortMac": "EC:CE:13:C0:46:34",
                "portDesc": "***** BGP Peering to ACI1 BL205  *******",
                "portIdT": "if-name",
                "portIdV": "Ethernet3/25",
                "portVlan": "",
                "stQual": "",
                "status": "",
                "sysDesc": "Cisco Nexus Operating System (NX-OS) Software 9.3(9)\nTAC support: http://www.cisco.com/tac\nCopyright (c) 2002-2022, Cisco Systems, Inc. All rights reserved.",
                "sysName": "ipn-eu-spdc.emea-sp.cisco.com",
                "ttl": "120",
                "pod_id": "pod-1",
                "node_id": "node-205",
                "interface_id": "eth1/24",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "portId": "Ethernet3/25",
                "mac": "ec:ce:13:c0:46:34"
            }
        ],
        "policy_selector": {
            "profile": "Infra-BGP_IntProf",
            "name": "Infra-BGP_IntSel",
            "dn": "uni/infra/accportprof-Infra-BGP_IntProf/hports-Infra-BGP_IntSel-typ-range",
            "dn_name": "hports-Infra-BGP_IntSel-typ-range",
            "block": [
                {
                    "fromCard": 1,
                    "toCard": 1,
                    "fromPort": 24,
                    "toPort": 24,
                    "fromSubPort": null,
                    "toSubPort": null
                }
            ],
            "policy_group_type": "infraAccPortGrp",
            "policy_group_type_name": "Access",
            "policy_group_name": "Infra-BGP_PolGrp",
            "policy_group_info": {
                "__Output": {},
                "annotation": "",
                "descr": "",
                "dn": "uni/infra/funcprof/accportgrp-Infra-BGP_PolGrp",
                "name": "Infra-BGP_PolGrp",
                "aaep_name": "Infra_L3_AAEP",
                "policy": {
                    "infraRsAttEntP": "",
                    "infraRsCdpIfPol": "CDP_enable",
                    "infraRsHIfPol": "default",
                    "infraRsLinkFlapPol": "default",
                    "infraRsLldpIfPol": "LLDP_enable",
                    "infraRsMonIfInfraPol": "default",
                    "infraRsStpIfPol": "default",
                    "infraRsMcpIfPol": "default",
                    "infraRsStormctrlIfPol": "default"
                },
                "aaep": {
                    "__Output": {
                        "infraVlanEnabledTick": "Red"
                    },
                    "descr": "",
                    "dn": "uni/infra/attentp-Infra_L3_AAEP",
                    "name": "Infra_L3_AAEP",
                    "infraRtAttEntP": [
                        {
                            "__Output": {},
                            "dn": "uni/infra/funcprof/accportgrp-Infra-BGP_PolGrp",
                            "type": "infraAccPortGrp",
                            "typeName": "Leaf Access Port Policy Group",
                            "name": "Infra-BGP_PolGrp"
                        }
                    ],
                    "infraRsDomP": [
                        {
                            "__Output": {},
                            "forceResolve": "yes",
                            "state": "formed",
                            "tCl": "l3extDomP",
                            "tDn": "uni/l3dom-Infra-BGP_L3Dom",
                            "domainType": "L3",
                            "domainName": "Infra-BGP_L3Dom"
                        },
                        {
                            "__Output": {},
                            "forceResolve": "yes",
                            "state": "formed",
                            "tCl": "l3extDomP",
                            "tDn": "uni/l3dom-Infra_L3Dom",
                            "domainType": "L3",
                            "domainName": "Infra_L3Dom"
                        }
                    ],
                    "infraVlanEnabled": false,
                    "infraVlanEnabledTick": "\u2717"
                }
            }
        },
        "qos": [
            {
                "__Output": {},
                "id": "control-plane",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-control-plane",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 35286320,
                "RxAdmitPacketsCount": 393471,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 7797597077,
                "TxAdmitPacketsCount": 11164355,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "level1",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-level1",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "level2",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-level2",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "level3",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-level3",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 2747274428,
                "RxAdmitPacketsCount": 12309412,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 3329172229,
                "TxAdmitPacketsCount": 10183010,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "level4",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-level4",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "level5",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-level5",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "level6",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-level6",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "policy-plane",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-policy-plane",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            },
            {
                "__Output": {},
                "id": "span",
                "dn": "topology/pod-1/node-205/sys/qosm/if-[eth1/24]/class-span",
                "interface_id": "eth1/24",
                "RxAdmitBytesCount": 0,
                "RxAdmitPacketsCount": 0,
                "RxDropBytesCount": 0,
                "RxDropPacketsCount": 0,
                "TxAdmitBytesCount": 0,
                "TxAdmitPacketsCount": 0,
                "TxDropBytesCount": 0,
                "TxDropPacketsCount": 0
            }
        ],
        "pc": {
            "dn": "topology/pod-1/node-205/sys/phys-[eth1/24]/aggrmbrif",
            "channelingSt": "unknown",
            "pcMode": "on",
            "pod_id": "pod-1",
            "node_id": "node-205",
            "interface_id": "eth1/24"
        }
    }
]
```

[[Back]](./InterfacePhy.md)