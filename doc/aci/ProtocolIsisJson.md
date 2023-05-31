# Node Protocol - IS-IS

## JSON

```
# iserver get aci proto isis
    --apic apic11
    --node cl201-eu-spdc
    --view verbose -o json

[
    {
        "instance": {
            "__Output": {
                "adminSt": "Green",
                "operSt": "Green"
            },
            "adminSt": "enabled",
            "childAction": "",
            "dn": "topology/pod-1/node-201/sys/isis",
            "lcOwn": "local",
            "modTs": "2023-03-03T01:13:22.862+02:00",
            "monPolDn": "uni/fabric/monfab-default",
            "name": "",
            "operErr": "",
            "operSt": "enabled",
            "status": "",
            "pod_node_name": "pod-1/cl201-eu-spdc",
            "enable": true,
            "domainCount": 1
        },
        "domain": [
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "aggFabAdjOperSt": "up",
                "areaId": "1",
                "bwRef": "400000",
                "childAction": "",
                "contextId": "4",
                "ctrl": "",
                "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1",
                "fastCsnps": "0",
                "fastLsps": "0",
                "lcOwn": "local",
                "lspPurged": "0",
                "lspRefreshed": "55316",
                "lspSourced": "4",
                "maxEcmp": "18",
                "metricStyle": "narrow",
                "modTs": "2023-03-03T01:24:50.156+02:00",
                "mode": "fabric",
                "monPolDn": "uni/fabric/monfab-default",
                "mtsError": "no",
                "mtu": "1492",
                "nSel": "ip",
                "name": "overlay-1",
                "operSt": "ok",
                "redistribMetric": "63",
                "seqWrapError": "no",
                "spfCalculated": "87",
                "status": "",
                "sysId": "43:C0:03:0A:00:00",
                "systemGipo": "225.0.0.16",
                "systemGipoOperSt": "239.255.255.240",
                "uribError": "no",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "instance": "default",
                "tunnel": [
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.192.64]",
                        "encapt": "unknown",
                        "id": "10.3.192.64",
                        "modTs": "never",
                        "name": "default",
                        "role": "leaf",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.192.65]",
                        "encapt": "unknown",
                        "id": "10.3.192.65",
                        "modTs": "never",
                        "name": "default",
                        "role": "spine",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.192.68]",
                        "encapt": "unknown",
                        "id": "10.3.192.68",
                        "modTs": "never",
                        "name": "default",
                        "role": "leaf",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.32.64]",
                        "encapt": "unknown",
                        "id": "10.3.32.64",
                        "modTs": "never",
                        "name": "default",
                        "role": "leaf",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.32.65]",
                        "encapt": "unknown",
                        "id": "10.3.32.65",
                        "modTs": "never",
                        "name": "default",
                        "role": "spine",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.40.64]",
                        "encapt": "unknown",
                        "id": "10.3.40.64",
                        "modTs": "never",
                        "name": "default",
                        "role": "spine",
                        "status": "",
                        "type": "physical,proxy-acast-v4",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.40.65]",
                        "encapt": "unknown",
                        "id": "10.3.40.65",
                        "modTs": "never",
                        "name": "default",
                        "role": "spine",
                        "status": "",
                        "type": "physical,proxy-acast-mac",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.40.66]",
                        "encapt": "unknown",
                        "id": "10.3.40.66",
                        "modTs": "never",
                        "name": "default",
                        "role": "spine",
                        "status": "",
                        "type": "physical,proxy-acast-v6",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.40.67]",
                        "encapt": "unknown",
                        "id": "10.3.40.67",
                        "modTs": "never",
                        "name": "default",
                        "role": "leaf",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.3.48.64]",
                        "encapt": "unknown",
                        "id": "10.3.48.64",
                        "modTs": "never",
                        "name": "default",
                        "role": "leaf",
                        "status": "",
                        "type": "physical",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    }
                ],
                "lsp": [
                    {
                        "__Output": {},
                        "areaAddr": "",
                        "attached": "no",
                        "childAction": "",
                        "ckSum": "40929",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-ls/lsp-40:20:03:0A:00:00-0-0",
                        "frag": "0",
                        "hostName": "",
                        "lanId": "0",
                        "lifeTime": "1198",
                        "modTs": "never",
                        "name": "",
                        "nlpId": "0.0.0.0",
                        "overload": "no",
                        "partition": "no",
                        "routerId": "",
                        "rrmBitMaps": "",
                        "seqNum": "54739",
                        "srmBitMaps": "",
                        "ssnBitMaps": "",
                        "status": "",
                        "sysId": "40:20:03:0A:00:00",
                        "timerExpiryTS": "2023-05-30T20:20:33.000+02:00",
                        "timerType": "hold",
                        "type": "l1",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "areaAddr": "",
                        "attached": "no",
                        "childAction": "",
                        "ckSum": "22313",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-ls/lsp-40:C0:03:0A:00:00-0-0",
                        "frag": "0",
                        "hostName": "",
                        "lanId": "0",
                        "lifeTime": "1198",
                        "modTs": "never",
                        "name": "",
                        "nlpId": "0.0.0.0",
                        "overload": "no",
                        "partition": "no",
                        "routerId": "",
                        "rrmBitMaps": "",
                        "seqNum": "54714",
                        "srmBitMaps": "",
                        "ssnBitMaps": "",
                        "status": "",
                        "sysId": "40:C0:03:0A:00:00",
                        "timerExpiryTS": "2023-05-30T20:16:39.000+02:00",
                        "timerType": "hold",
                        "type": "l1",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "areaAddr": "",
                        "attached": "no",
                        "childAction": "",
                        "ckSum": "36556",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-ls/lsp-41:20:03:0A:00:00-0-0",
                        "frag": "0",
                        "hostName": "",
                        "lanId": "0",
                        "lifeTime": "1199",
                        "modTs": "never",
                        "name": "",
                        "nlpId": "0.0.0.0",
                        "overload": "no",
                        "partition": "no",
                        "routerId": "",
                        "rrmBitMaps": "",
                        "seqNum": "54793",
                        "srmBitMaps": "",
                        "ssnBitMaps": "",
                        "status": "",
                        "sysId": "41:20:03:0A:00:00",
                        "timerExpiryTS": "2023-05-30T20:18:08.000+02:00",
                        "timerType": "hold",
                        "type": "l1",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "areaAddr": "",
                        "attached": "no",
                        "childAction": "",
                        "ckSum": "22080",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-ls/lsp-41:C0:03:0A:00:00-0-0",
                        "frag": "0",
                        "hostName": "",
                        "lanId": "0",
                        "lifeTime": "1199",
                        "modTs": "never",
                        "name": "",
                        "nlpId": "0.0.0.0",
                        "overload": "no",
                        "partition": "no",
                        "routerId": "",
                        "rrmBitMaps": "",
                        "seqNum": "54785",
                        "srmBitMaps": "",
                        "ssnBitMaps": "",
                        "status": "",
                        "sysId": "41:C0:03:0A:00:00",
                        "timerExpiryTS": "2023-05-30T20:15:51.000+02:00",
                        "timerType": "hold",
                        "type": "l1",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "areaAddr": "",
                        "attached": "no",
                        "childAction": "",
                        "ckSum": "27761",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-ls/lsp-43:C0:03:0A:00:00-0-0",
                        "frag": "0",
                        "hostName": "",
                        "lanId": "0",
                        "lifeTime": "1200",
                        "modTs": "never",
                        "name": "",
                        "nlpId": "0.0.0.0",
                        "overload": "no",
                        "partition": "no",
                        "routerId": "",
                        "rrmBitMaps": "",
                        "seqNum": "54733",
                        "srmBitMaps": "",
                        "ssnBitMaps": "",
                        "status": "",
                        "sysId": "43:C0:03:0A:00:00",
                        "timerExpiryTS": "2023-05-30T20:08:40.000+02:00",
                        "timerType": "refresh",
                        "type": "l1",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "areaAddr": "",
                        "attached": "no",
                        "childAction": "",
                        "ckSum": "39025",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-ls/lsp-44:C0:03:0A:00:00-0-0",
                        "frag": "0",
                        "hostName": "",
                        "lanId": "0",
                        "lifeTime": "1198",
                        "modTs": "never",
                        "name": "",
                        "nlpId": "0.0.0.0",
                        "overload": "no",
                        "partition": "no",
                        "routerId": "",
                        "rrmBitMaps": "",
                        "seqNum": "54757",
                        "srmBitMaps": "",
                        "ssnBitMaps": "",
                        "status": "",
                        "sysId": "44:C0:03:0A:00:00",
                        "timerExpiryTS": "2023-05-30T20:20:33.000+02:00",
                        "timerType": "hold",
                        "type": "l1",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    }
                ],
                "interface": [
                    {
                        "__Output": {
                            "adminSt": "Green",
                            "iibState": "Green"
                        },
                        "adminSt": "enabled",
                        "childAction": "",
                        "cktT": "l1",
                        "ctrl": "",
                        "descr": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[eth1/107.7]",
                        "extdLocalCktId": "436641799",
                        "id": "eth1/107.7",
                        "iibIdx": "2",
                        "iibState": "Ready",
                        "iibUpCtrl": "yes",
                        "initError": "no",
                        "lcOwn": "local",
                        "localCktId": "1",
                        "lspRefreshIntvl": "33",
                        "metric": "1",
                        "modTs": "2023-03-03T01:18:58.830+02:00",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "overlay-1",
                        "nextIIHTs": "2023-03-03T01:20:10.000+02:00",
                        "p2pCktId": "",
                        "status": "",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {
                            "adminSt": "Green",
                            "iibState": "Green"
                        },
                        "adminSt": "enabled",
                        "childAction": "",
                        "cktT": "l1",
                        "ctrl": "",
                        "descr": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[eth1/108.504]",
                        "extdLocalCktId": "436646392",
                        "id": "eth1/108.504",
                        "iibIdx": "4",
                        "iibState": "Ready",
                        "iibUpCtrl": "yes",
                        "initError": "no",
                        "lcOwn": "local",
                        "localCktId": "1",
                        "lspRefreshIntvl": "33",
                        "metric": "1",
                        "modTs": "2023-04-28T11:32:54.213+02:00",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "overlay-1",
                        "nextIIHTs": "2023-04-28T11:31:19.000+02:00",
                        "p2pCktId": "",
                        "status": "",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {
                            "adminSt": "Green",
                            "iibState": "Green"
                        },
                        "adminSt": "enabled",
                        "childAction": "",
                        "cktT": "l1",
                        "ctrl": "advert-tep,passive",
                        "descr": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[lo0]",
                        "extdLocalCktId": "335544320",
                        "id": "lo0",
                        "iibIdx": "3",
                        "iibState": "Ready",
                        "iibUpCtrl": "yes",
                        "initError": "no",
                        "lcOwn": "local",
                        "localCktId": "1",
                        "lspRefreshIntvl": "33",
                        "metric": "1",
                        "modTs": "2023-03-03T01:18:58.830+02:00",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "overlay-1",
                        "nextIIHTs": "2023-03-03T01:18:59.000+02:00",
                        "p2pCktId": "",
                        "status": "",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {
                            "adminSt": "Green",
                            "iibState": "Green"
                        },
                        "adminSt": "enabled",
                        "childAction": "",
                        "cktT": "l1",
                        "ctrl": "advert-tep,passive",
                        "descr": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[lo1]",
                        "extdLocalCktId": "335544321",
                        "id": "lo1",
                        "iibIdx": "5",
                        "iibState": "Ready",
                        "iibUpCtrl": "yes",
                        "initError": "no",
                        "lcOwn": "local",
                        "localCktId": "1",
                        "lspRefreshIntvl": "33",
                        "metric": "1",
                        "modTs": "2023-03-03T01:24:43.101+02:00",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "overlay-1",
                        "nextIIHTs": "2023-03-03T01:21:29.000+02:00",
                        "p2pCktId": "",
                        "status": "",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {
                            "adminSt": "Green",
                            "iibState": "Green"
                        },
                        "adminSt": "enabled",
                        "childAction": "",
                        "cktT": "l1",
                        "ctrl": "passive",
                        "descr": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[lo2]",
                        "extdLocalCktId": "335544322",
                        "id": "lo2",
                        "iibIdx": "6",
                        "iibState": "Ready",
                        "iibUpCtrl": "yes",
                        "initError": "no",
                        "lcOwn": "local",
                        "localCktId": "1",
                        "lspRefreshIntvl": "33",
                        "metric": "1",
                        "modTs": "2023-03-03T01:24:50.156+02:00",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "overlay-1",
                        "nextIIHTs": "2023-03-03T01:21:34.000+02:00",
                        "p2pCktId": "",
                        "status": "",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    }
                ],
                "neighbor": [
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "bfdConfigSt": "down",
                        "bfdOperSt": "down",
                        "childAction": "",
                        "cktType": "bcast",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[eth1/108.504]/adj-l1-adj-41:20:03:0A:00:00",
                        "holdExpTs": "2023-05-30T20:04:25.000+02:00",
                        "lanId": "0",
                        "lastTrans": "2023-04-28T11:31:14.000+02:00",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "4120.030a.0000",
                        "numAdjTrans": "1",
                        "operSt": "up",
                        "peerCktId": "28",
                        "peerCktPrio": "64",
                        "peerGrFlags": "capable",
                        "status": "",
                        "sysId": "41:20:03:0A:00:00",
                        "type": "l1",
                        "isisPeerIpAddr": {
                            "addr": "10.3.32.65",
                            "childAction": "",
                            "modTs": "never",
                            "rn": "addr-[10.3.32.65]",
                            "status": ""
                        },
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "interface": "eth1/108.504"
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "bfdConfigSt": "down",
                        "bfdOperSt": "down",
                        "childAction": "",
                        "cktType": "bcast",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/if-[eth1/107.7]/adj-l1-adj-41:C0:03:0A:00:00",
                        "holdExpTs": "2023-05-30T20:04:19.000+02:00",
                        "lanId": "0",
                        "lastTrans": "2023-03-03T01:20:03.000+02:00",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "41c0.030a.0000",
                        "numAdjTrans": "1",
                        "operSt": "up",
                        "peerCktId": "21",
                        "peerCktPrio": "64",
                        "peerGrFlags": "capable",
                        "status": "",
                        "sysId": "41:C0:03:0A:00:00",
                        "type": "l1",
                        "isisPeerIpAddr": {
                            "addr": "10.3.192.65",
                            "childAction": "",
                            "modTs": "never",
                            "rn": "addr-[10.3.192.65]",
                            "status": ""
                        },
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "interface": "eth1/107.7"
                    }
                ],
                "tree": [
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "6",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-0",
                        "id": "0",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "internal",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-1",
                        "id": "1",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.32.65",
                        "rootPort": "eth1/108.504",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-2",
                        "id": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.32.65",
                        "rootPort": "eth1/108.504",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "6",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-3",
                        "id": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.32.65",
                        "rootPort": "eth1/108.504",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-4",
                        "id": "4",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.32.65",
                        "rootPort": "eth1/108.504",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-5",
                        "id": "5",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-6",
                        "id": "6",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-7",
                        "id": "7",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-8",
                        "id": "8",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-9",
                        "id": "9",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-10",
                        "id": "10",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.192.65",
                        "rootPort": "eth1/107.7",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-11",
                        "id": "11",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.32.65",
                        "rootPort": "eth1/108.504",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "7",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-12",
                        "id": "12",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "operSt": "active",
                        "origin": "isis",
                        "root": "10.3.32.65",
                        "rootPort": "eth1/108.504",
                        "status": "",
                        "usage": "user",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": true
                    },
                    {
                        "__Output": {
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "0",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-13",
                        "id": "13",
                        "modTs": "never",
                        "monPolDn": "",
                        "name": "",
                        "operSt": "inactive",
                        "origin": "static",
                        "root": "0.0.0.0",
                        "rootPort": "unspecified",
                        "status": "",
                        "usage": "internal",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": false
                    },
                    {
                        "__Output": {
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "0",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-14",
                        "id": "14",
                        "modTs": "never",
                        "monPolDn": "",
                        "name": "",
                        "operSt": "inactive",
                        "origin": "static",
                        "root": "0.0.0.0",
                        "rootPort": "unspecified",
                        "status": "",
                        "usage": "internal",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": false
                    },
                    {
                        "__Output": {
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "diaAlert": "inactive",
                        "diameter": "0",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/fmtree-15",
                        "id": "15",
                        "modTs": "never",
                        "monPolDn": "",
                        "name": "",
                        "operSt": "inactive",
                        "origin": "static",
                        "root": "0.0.0.0",
                        "rootPort": "unspecified",
                        "status": "",
                        "usage": "internal",
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay",
                        "enable": false
                    }
                ],
                "route": [
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.0.33/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.0.33/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.0.34/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.0.34/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.0.35/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.0.35/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.152.65/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.152.65/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.152.66/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.152.66/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.152.67/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.152.67/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.192.101/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.192.101/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.192.102/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.192.102/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.192.103/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.192.103/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.192.64/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.192.64/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.192.65/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.192.65/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.192.68/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.192.68/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.32.64/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.32.64/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.32.65/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.32.65/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.40.64/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.40.64/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.40.65/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.40.65/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.40.66/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.40.66/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.40.67/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.40.67/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[10.3.48.64/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "10.3.48.64/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[101.101.101.101/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "101.101.101.101/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[102.102.102.102/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "102.102.102.102/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[111.111.111.111/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "111.111.111.111/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[112.112.112.112/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "112.112.112.112/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[15.16.2.1/32]",
                        "metric": "12",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "15.16.2.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[15.16.2.5/32]",
                        "metric": "12",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "15.16.2.5/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.1.1/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.1.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.10.1/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.10.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.1/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.225/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.225/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.226/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.226/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.227/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.227/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.228/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.228/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.231/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.231/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.233/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.233/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.236/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.236/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.11.237/32]",
                        "metric": "3",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.11.237/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.12.1/32]",
                        "metric": "2",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.12.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.21.0/24]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.21.0/24",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.21.1/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.21.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.22.1/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.22.1/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.30.120/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.30.120/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.30.121/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.30.121/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.30.160/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.30.160/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.30.161/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.30.161/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[172.16.30.88/32]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "172.16.30.88/32",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[192.168.1.0/30]",
                        "metric": "11",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "192.168.1.0/30",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[192.168.1.4/30]",
                        "metric": "11",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "192.168.1.4/30",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[192.168.31.0/30]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "192.168.31.0/30",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    },
                    {
                        "__Output": {},
                        "childAction": "",
                        "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-rt/rt-[192.168.32.0/30]",
                        "metric": "64",
                        "modTs": "never",
                        "monPolDn": "uni/fabric/monfab-default",
                        "name": "",
                        "pfx": "192.168.32.0/30",
                        "pref": "115",
                        "status": "",
                        "isisNexthop": [
                            {
                                "interface": "eth1/107.7",
                                "address": "10.3.192.65"
                            },
                            {
                                "interface": "eth1/108.504",
                                "address": "10.3.32.65"
                            }
                        ],
                        "pod_node_name": "pod-1/cl201-eu-spdc",
                        "instance": "default",
                        "domain": "overlay"
                    }
                ]
            }
        ]
    }
]
```

[[Back]](./ProtocolIsis.md)