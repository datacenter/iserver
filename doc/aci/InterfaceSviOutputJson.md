# Node Interface - SVI

## JSON output type

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view all
    --when 180d -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "operSt": "Green",
            "sviIf.id": "Blue",
            "sviIf.adminSt": "Green",
            "sviIf.operSt": "Green",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "accEncap": "vlan-812",
        "addr": "00:00:00:00:00:00",
        "adminSt": "active",
        "bdDefDn": "",
        "bridgeMode": "mac",
        "dn": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]",
        "epMoveDetectMode": "",
        "epOperSt": "",
        "epOperStQual": "unspecified",
        "epUpSeqNum": "0",
        "fabEncap": "vxlan-15237056",
        "fwdCtrl": "arp-flood,mdst-flood",
        "fwdMode": "bridge,route",
        "hwId": "40",
        "hwResourceId": "4630",
        "id": "30",
        "ipv6McastAllow": "no",
        "mcastAllow": "no",
        "mcastOperSt": "",
        "operSt": "up",
        "pcTag": "16386",
        "qiqL2ProtTunMask": "",
        "qosPrio": "unspecified",
        "serviceEnabled": "no",
        "servicepcTag": "any",
        "type": "bd-external",
        "unkMacUcastAct": "flood",
        "unkMcastAct": "flood",
        "v6unkMcastAct": "flood",
        "podId": "1",
        "nodeId": "2208",
        "apic": "apic21",
        "pod_node_name": "pod-1/cl2208-eu-spdc",
        "sviIf": {
            "adminSt": "up",
            "bw": "10000000",
            "carDel": "10",
            "delay": "1",
            "descr": "",
            "id": "vlan30",
            "iod": "100",
            "mac": "00:22:BD:F8:19:FF",
            "medium": "bcast",
            "mtu": "1500",
            "operSt": "up",
            "operStQual": "",
            "rn": "svi-[vlan30]",
            "vlanId": "30",
            "vlanT": "bd-external",
            "vmac": "00:00:00:00:00:00",
            "vmacChgQual": "",
            "faultCounts": null,
            "type": "Ext"
        },
        "up": true,
        "counters": {
            "inOctets": "5074959785",
            "inPackets": "79290343",
            "inMcast": "0",
            "inDiscards": "0",
            "inErrors": "0",
            "outOctets": "12464860760",
            "outPackets": "179119535",
            "outMcast": "0",
            "outDiscards": "0",
            "outErrors": "0"
        },
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "accEncapT": "vlan-812",
        "ipv4_address": [
            "169.254.2.254/24",
            "169.254.2.1/24"
        ],
        "ipv4_info": [
            {
                "__Output": {
                    "operSt": "Green"
                },
                "addr": "169.254.2.1/24",
                "iaddr": 2851996161,
                "operSt": "up",
                "operStQual": "",
                "type": "primary",
                "vpcPeer": "0.0.0.0"
            },
            {
                "__Output": {
                    "operSt": "Green"
                },
                "addr": "169.254.2.254/24",
                "iaddr": 2851996414,
                "operSt": "up",
                "operStQual": "",
                "type": "secondary",
                "vpcPeer": "0.0.0.0"
            }
        ],
        "ipv4_addressT": [
            "169.254.2.1/24 (pri)",
            "169.254.2.254/24"
        ],
        "faultInst": [],
        "faultRecord": [
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:4",
                "childAction": "",
                "code": "F112128",
                "created": "2023-07-27T09:00:43.994+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 4 fell below threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885259284",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885259284",
                "ind": "deletion",
                "lc": "",
                "modTs": "never",
                "occur": "2",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "cleared",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 4 fell below ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885259284"
                ],
                "timestamp": 1690441243,
                "severityT": "--"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:4",
                "childAction": "",
                "code": "F112128",
                "created": "2023-07-27T08:00:28.485+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 4 fell below threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885259243",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885259243",
                "ind": "modification",
                "lc": "retaining",
                "modTs": "never",
                "occur": "2",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "cleared",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 4 fell below ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885259243"
                ],
                "timestamp": 1690437628,
                "severityT": "--"
            },
            {
                "__Output": {
                    "severityT": "Green"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:12",
                "childAction": "",
                "code": "F112128",
                "created": "2023-07-27T07:40:22.309+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 12 raised above threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885259174",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885259174",
                "ind": "modification",
                "lc": "raised",
                "modTs": "never",
                "occur": "2",
                "origSeverity": "warning",
                "prevSeverity": "cleared",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "warning",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 12 raised above ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885259174"
                ],
                "timestamp": 1690436422,
                "severityT": "Warn"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:0",
                "childAction": "",
                "code": "F112128",
                "created": "2023-07-27T07:20:19.228+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885259154",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885259154",
                "ind": "modification",
                "lc": "retaining",
                "modTs": "never",
                "occur": "1",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "cleared",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885259154"
                ],
                "timestamp": 1690435219,
                "severityT": "--"
            },
            {
                "__Output": {
                    "severityT": "Green"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:10",
                "childAction": "",
                "code": "F112128",
                "created": "2023-06-18T09:18:08.756+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885256894",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885256894",
                "ind": "creation",
                "lc": "raised",
                "modTs": "never",
                "occur": "1",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "warning",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885256894"
                ],
                "timestamp": 1687072688,
                "severityT": "Warn"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:0",
                "childAction": "",
                "code": "F112128",
                "created": "2023-06-07T14:40:55.223+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885248996",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885248996",
                "ind": "deletion",
                "lc": "",
                "modTs": "never",
                "occur": "2",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "cleared",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885248996"
                ],
                "timestamp": 1686141655,
                "severityT": "--"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:0",
                "childAction": "",
                "code": "F112128",
                "created": "2023-06-07T13:40:41.216+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885248979",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885248979",
                "ind": "modification",
                "lc": "retaining",
                "modTs": "never",
                "occur": "2",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "cleared",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 0 fell below ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885248979"
                ],
                "timestamp": 1686138041,
                "severityT": "--"
            },
            {
                "__Output": {
                    "severityT": "Green"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:10",
                "childAction": "",
                "code": "F112128",
                "created": "2023-05-31T23:56:23.944+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885248519",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885248519",
                "ind": "modification",
                "lc": "raised",
                "modTs": "never",
                "occur": "2",
                "origSeverity": "warning",
                "prevSeverity": "cleared",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "warning",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 10 raised above ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885248519"
                ],
                "timestamp": 1685570183,
                "severityT": "Warn"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:8",
                "childAction": "",
                "code": "F112128",
                "created": "2023-05-31T23:42:20.812+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 8 fell below threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885248500",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885248500",
                "ind": "modification",
                "lc": "retaining",
                "modTs": "never",
                "occur": "1",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "cleared",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 8 fell below ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885248500"
                ],
                "timestamp": 1685569340,
                "severityT": "--"
            },
            {
                "__Output": {
                    "severityT": "Green"
                },
                "ack": "no",
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "threshold-crossed",
                "changeSet": "dropRate:16",
                "childAction": "",
                "code": "F112128",
                "created": "2023-05-31T22:25:19.050+02:00",
                "delegated": false,
                "delegatedFrom": "",
                "descr": "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 16 raised above threshold 10",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/fr-12885248342",
                "domain": "infra",
                "highestSeverity": "warning",
                "id": "12885248342",
                "ind": "creation",
                "lc": "raised",
                "modTs": "never",
                "occur": "1",
                "origSeverity": "warning",
                "prevSeverity": "warning",
                "rule": "tca-l2-ingr-pkts5min-drop-rate",
                "severity": "warning",
                "status": "",
                "subject": "counter",
                "type": "operational",
                "object": "faultRecord",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "TCA: ingress drop packets rate(l2IngrPkts5min:dropRate) value 16 raised above ",
                    "threshold 10"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/fr-12885248342"
                ],
                "timestamp": 1685564719,
                "severityT": "Warn"
            }
        ],
        "eventLog": [
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "operSt (New: up), operStQual (New: none)",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-05-31T22:20:46.437+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886795557",
                "id": "12886795557",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671631426",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "operSt (New: up), operStQual (New: none)"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886795557"
                ],
                "timestamp": 1685564446,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "operSt (New: up), operStQual (New: none), vlanT (New: bd-external)",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-05-31T22:20:45.659+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886795517",
                "id": "12886795517",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671631291",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "operSt (New: up), operStQual (New: none), vlanT (New: bd-external)"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886795517"
                ],
                "timestamp": 1685564445,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "operSt (New: up), operStQual (New: none)",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-05-31T22:20:46.522+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886795571",
                "id": "12886795571",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671631453",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "operSt (New: up), operStQual (New: none)"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886795571"
                ],
                "timestamp": 1685564446,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "iod (New: 109), operSt (New: up), operStQual (New: none), osSum (New: failed), vlanT (New: bd-external), vmacChgQual (New: )",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-05-31T22:20:45.131+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886795462",
                "id": "12886795462",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671631153",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "iod (New: 109), operSt (New: up), operStQual (New: none), osSum (New: failed), ",
                    "vlanT (New: bd-external), vmacChgQual (New: )"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886795462"
                ],
                "timestamp": 1685564445,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "iod (New: 100), operSt (New: up), operStQual (New: none), osSum (New: failed), vlanT (New: bd-external), vmacChgQual (New: )",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-06-18T09:15:12.412+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886862072",
                "id": "12886862072",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671630415",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "iod (New: 100), operSt (New: up), operStQual (New: none), osSum (New: failed), ",
                    "vlanT (New: bd-external), vmacChgQual (New: )"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886862072"
                ],
                "timestamp": 1687072512,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "operSt (New: up), operStQual (New: none), vlanT (New: bd-external)",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-06-18T09:15:13.648+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886862073",
                "id": "12886862073",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671630638",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "operSt (New: up), operStQual (New: none), vlanT (New: bd-external)"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886862073"
                ],
                "timestamp": 1687072513,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "operSt (New: up), operStQual (New: none)",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-06-18T09:15:13.850+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886862074",
                "id": "12886862074",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671630674",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "operSt (New: up), operStQual (New: none)"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886862074"
                ],
                "timestamp": 1687072513,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]",
                "cause": "if-state-change",
                "changeSet": "operSt (New: up), operStQual (New: none)",
                "childAction": "",
                "code": "E4208074",
                "created": "2023-06-18T09:15:13.914+02:00",
                "descr": "Line Protocol on Interface, changed state to up connected",
                "dn": "subj-[topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]]/rec-12886862075",
                "id": "12886862075",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671630690",
                "user": "internal",
                "pod_node_name": "pod-1/cl2208-eu-spdc",
                "interfaceId": "vlan30",
                "descrT": [
                    "Line Protocol on Interface, changed state to up connected"
                ],
                "changeSetT": [
                    "operSt (New: up), operStQual (New: none)"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2208/sys/",
                    "ctx-[vxlan-2293761]/bd-[vxlan-15237056]/",
                    "svi-[vlan30]]/rec-12886862075"
                ],
                "timestamp": 1687072513,
                "severityT": "Info"
            }
        ],
        "auditLog": []
    }
]
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --name vlan30
    --view all
    --when 180d -o json

{
    "duration": 5737,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 372,
        "disconnect_time": 0,
        "mo_time": 4550,
        "total_time": 4922
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	372	-	connect apic21o.emea-sp.cisco.com:443
True	287	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	404	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	272	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	400	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	1333	262	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1258	1547	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=event-logs,no-scoped,subtree
True	596	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/sviIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceSvi.md)