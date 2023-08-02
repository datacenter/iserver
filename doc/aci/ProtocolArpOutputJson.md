# Node Protocol - ARP

## JSON output

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc -o json
    --when any
    --view all

[
    {
        "instance": {
            "__Output": {
                "adminSt": "Green",
                "health": "Green",
                "faults": ":R.M.Y.G"
            },
            "adminSt": "enabled",
            "childAction": "",
            "ctrl": "",
            "dn": "topology/pod-1/node-2205/sys/arp/inst",
            "lcOwn": "local",
            "modTs": "2023-06-18T09:37:05.297+02:00",
            "monPolDn": "uni/fabric/monfab-default",
            "name": "",
            "operErr": "",
            "status": "",
            "healthInst": {
                "childAction": "",
                "chng": "0",
                "cur": "100",
                "maxSev": "cleared",
                "prev": "100",
                "rn": "health",
                "status": "",
                "twScore": "100",
                "updTs": "2023-06-18T09:37:07.519+02:00"
            },
            "faultCounts": {
                "childAction": "",
                "crit": "0",
                "critAcked": "0",
                "critAckedandDelegated": "0",
                "critDelegated": "0",
                "maj": "0",
                "majAcked": "0",
                "majAckedandDelegated": "0",
                "majDelegated": "0",
                "minor": "0",
                "minorAcked": "0",
                "minorAckedandDelegated": "0",
                "minorDelegated": "0",
                "rn": "fltCnts",
                "status": "",
                "warn": "0",
                "warnAcked": "0",
                "warnAckedandDelegated": "0",
                "warnDelegated": "0"
            },
            "pod_node_name": "pod-1/bl2205-eu-spdc",
            "enable": true,
            "health": "100",
            "faults": "0 0 0 0",
            "isAnyFault": false
        },
        "domain": [
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-black-hole",
                "encap": "vxlan-16777200",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:37:25.380+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "black-hole",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:38:06.313+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-common:Infra_privIP_VRF",
                "encap": "vxlan-2326529",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:30.147+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_privIP_VRF",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:07.577+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-common:Infra_privIP_VRF/db-ip/adj-[eth1/25.17]-[192.168.254.74]",
                        "ifId": "eth1/25.17",
                        "ip": "192.168.254.74",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/25",
                        "status": "",
                        "upTS": "2023-08-02T14:28:36.062+02:00",
                        "domain_name": "common:Infra_privIP_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-common:Infra_VRF",
                "encap": "vxlan-2818048",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:35.487+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_VRF",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:13.373+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-common:Infra_VRF/db-ip/adj-[eth1/25.18]-[192.168.254.9]",
                        "ifId": "eth1/25.18",
                        "ip": "192.168.254.9",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/25",
                        "status": "",
                        "upTS": "2023-08-02T14:28:37.342+02:00",
                        "domain_name": "common:Infra_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-Ericsson_PACO:PDN",
                "encap": "vxlan-3112962",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:34.749+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "Ericsson_PACO:PDN",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:12.457+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-management",
                "encap": "vxlan-2195456",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:30.147+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "management",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:07.577+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-mgmt:EU-SPDC-ERSPAN-VRF",
                "encap": "vxlan-2883584",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:26.007+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "mgmt:EU-SPDC-ERSPAN-VRF",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:03.277+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-mgmt:inb",
                "encap": "vxlan-3080192",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:35.487+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "mgmt:inb",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:13.373+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-mgmt:inb/db-ip/adj-[eth1/25.19]-[192.168.254.25]",
                        "ifId": "eth1/25.19",
                        "ip": "192.168.254.25",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/25",
                        "status": "",
                        "upTS": "2023-08-02T14:28:36.112+02:00",
                        "domain_name": "mgmt:inb",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-nidemo:streamz-vrf",
                "encap": "vxlan-2424834",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:44.330+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "nidemo:streamz-vrf",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:21.892+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-overlay-1",
                "encap": "vxlan-16777199",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:37:25.380+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "overlay-1",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:37:07.672+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-SPN_IntraLab:SPN_VRF1",
                "encap": "vxlan-3080193",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:44.330+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "SPN_IntraLab:SPN_VRF1",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:21.892+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF",
                "encap": "vxlan-2785280",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:34.749+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "vEPC_demo:ACC_VRF",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:12.456+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.1]",
                        "ifId": "vlan1",
                        "ip": "192.168.23.1",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.954+02:00",
                        "domain_name": "vEPC_demo:ACC_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.2]",
                        "ifId": "vlan1",
                        "ip": "192.168.23.2",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.955+02:00",
                        "domain_name": "vEPC_demo:ACC_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.3]",
                        "ifId": "vlan1",
                        "ip": "192.168.23.3",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.956+02:00",
                        "domain_name": "vEPC_demo:ACC_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.4]",
                        "ifId": "vlan1",
                        "ip": "192.168.23.4",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.957+02:00",
                        "domain_name": "vEPC_demo:ACC_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.5]",
                        "ifId": "vlan1",
                        "ip": "192.168.23.5",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.959+02:00",
                        "domain_name": "vEPC_demo:ACC_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    }
                ],
                "adjacency_count": 5
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "health": "Green",
                    "faults": ":R.M.Y.G"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF",
                "encap": "vxlan-2424833",
                "lcOwn": "local",
                "modTs": "2023-06-18T09:45:34.749+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "vEPC_demo:INT_VRF",
                "status": "",
                "healthInst": {
                    "childAction": "",
                    "chng": "0",
                    "cur": "100",
                    "maxSev": "cleared",
                    "prev": "100",
                    "rn": "health",
                    "status": "",
                    "twScore": "100",
                    "updTs": "2023-06-18T09:45:12.457+02:00"
                },
                "faultCounts": {
                    "childAction": "",
                    "crit": "0",
                    "critAcked": "0",
                    "critAckedandDelegated": "0",
                    "critDelegated": "0",
                    "maj": "0",
                    "majAcked": "0",
                    "majAckedandDelegated": "0",
                    "majDelegated": "0",
                    "minor": "0",
                    "minorAcked": "0",
                    "minorAckedandDelegated": "0",
                    "minorDelegated": "0",
                    "rn": "fltCnts",
                    "status": "",
                    "warn": "0",
                    "warnAcked": "0",
                    "warnAckedandDelegated": "0",
                    "warnDelegated": "0"
                },
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "health": "100",
                "faults": "0 0 0 0",
                "isAnyFault": false,
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.1]",
                        "ifId": "vlan20",
                        "ip": "192.168.24.1",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.948+02:00",
                        "domain_name": "vEPC_demo:INT_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.2]",
                        "ifId": "vlan20",
                        "ip": "192.168.24.2",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.949+02:00",
                        "domain_name": "vEPC_demo:INT_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.3]",
                        "ifId": "vlan20",
                        "ip": "192.168.24.3",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.950+02:00",
                        "domain_name": "vEPC_demo:INT_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.4]",
                        "ifId": "vlan20",
                        "ip": "192.168.24.4",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.951+02:00",
                        "domain_name": "vEPC_demo:INT_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.5]",
                        "ifId": "vlan20",
                        "ip": "192.168.24.5",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-08-02T14:34:17.953+02:00",
                        "domain_name": "vEPC_demo:INT_VRF",
                        "pod_node_name": "pod-1/bl2205-eu-spdc"
                    }
                ],
                "adjacency_count": 5
            }
        ],
        "adjacency": [
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-common:Infra_privIP_VRF/db-ip/adj-[eth1/25.17]-[192.168.254.74]",
                "ifId": "eth1/25.17",
                "ip": "192.168.254.74",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/25",
                "status": "",
                "upTS": "2023-08-02T14:28:36.062+02:00",
                "domain_name": "common:Infra_privIP_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-common:Infra_VRF/db-ip/adj-[eth1/25.18]-[192.168.254.9]",
                "ifId": "eth1/25.18",
                "ip": "192.168.254.9",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/25",
                "status": "",
                "upTS": "2023-08-02T14:28:37.342+02:00",
                "domain_name": "common:Infra_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-mgmt:inb/db-ip/adj-[eth1/25.19]-[192.168.254.25]",
                "ifId": "eth1/25.19",
                "ip": "192.168.254.25",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/25",
                "status": "",
                "upTS": "2023-08-02T14:28:36.112+02:00",
                "domain_name": "mgmt:inb",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.1]",
                "ifId": "vlan1",
                "ip": "192.168.23.1",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.954+02:00",
                "domain_name": "vEPC_demo:ACC_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.2]",
                "ifId": "vlan1",
                "ip": "192.168.23.2",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.955+02:00",
                "domain_name": "vEPC_demo:ACC_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.3]",
                "ifId": "vlan1",
                "ip": "192.168.23.3",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.956+02:00",
                "domain_name": "vEPC_demo:ACC_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.4]",
                "ifId": "vlan1",
                "ip": "192.168.23.4",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.957+02:00",
                "domain_name": "vEPC_demo:ACC_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:ACC_VRF/db-ip/adj-[vlan1]-[192.168.23.5]",
                "ifId": "vlan1",
                "ip": "192.168.23.5",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.959+02:00",
                "domain_name": "vEPC_demo:ACC_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.1]",
                "ifId": "vlan20",
                "ip": "192.168.24.1",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.948+02:00",
                "domain_name": "vEPC_demo:INT_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.2]",
                "ifId": "vlan20",
                "ip": "192.168.24.2",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.949+02:00",
                "domain_name": "vEPC_demo:INT_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.3]",
                "ifId": "vlan20",
                "ip": "192.168.24.3",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.950+02:00",
                "domain_name": "vEPC_demo:INT_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.4]",
                "ifId": "vlan20",
                "ip": "192.168.24.4",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.951+02:00",
                "domain_name": "vEPC_demo:INT_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-2205/sys/arp/inst/dom-vEPC_demo:INT_VRF/db-ip/adj-[vlan20]-[192.168.24.5]",
                "ifId": "vlan20",
                "ip": "192.168.24.5",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-08-02T14:34:17.953+02:00",
                "domain_name": "vEPC_demo:INT_VRF",
                "pod_node_name": "pod-1/bl2205-eu-spdc"
            }
        ],
        "interface": [
            {
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "interface": "eth1/25.17",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "interface": "eth1/25.18",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "interface": "eth1/25.19",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "interface": "vlan1",
                "count": 5
            },
            {
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "interface": "vlan20",
                "count": 5
            }
        ],
        "faultInst": [],
        "faultRecord": [],
        "eventLog": [
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2205/sys/arp/inst",
                "cause": "admin-state-change",
                "changeSet": "adminSt:enabled",
                "childAction": "",
                "code": "E4208089",
                "created": "2023-06-18T09:37:07.519+02:00",
                "descr": "ARP instance is administratively Enabled",
                "dn": "subj-[topology/pod-1/node-2205/sys/arp/inst]/rec-8598297981",
                "id": "8598297981",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671623800",
                "user": "internal",
                "podId": "1",
                "nodeId": "2205",
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "descrT": [
                    "ARP instance is administratively ",
                    "Enabled"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2205/sys/arp/",
                    "inst]/rec-8598297981"
                ],
                "affectedT": [
                    "topology/pod-1/node-2205/sys/arp/inst"
                ],
                "timestamp": 1687073827,
                "severityT": "Info"
            },
            {
                "__Output": {
                    "severityT": "Blue"
                },
                "affected": "topology/pod-1/node-2205/sys/arp/inst",
                "cause": "admin-state-change",
                "changeSet": "adminSt:enabled",
                "childAction": "",
                "code": "E4208089",
                "created": "2023-06-12T09:51:01.479+02:00",
                "descr": "ARP instance is administratively Enabled",
                "dn": "subj-[topology/pod-1/node-2205/sys/arp/inst]/rec-8598242954",
                "id": "8598242954",
                "ind": "state-transition",
                "modTs": "never",
                "severity": "info",
                "status": "",
                "trig": "oper",
                "txId": "18374686479671623803",
                "user": "internal",
                "podId": "1",
                "nodeId": "2205",
                "pod_node_name": "pod-1/bl2205-eu-spdc",
                "descrT": [
                    "ARP instance is administratively ",
                    "Enabled"
                ],
                "dnT": [
                    "subj-[topology/pod-1/node-2205/sys/arp/",
                    "inst]/rec-8598242954"
                ],
                "affectedT": [
                    "topology/pod-1/node-2205/sys/arp/inst"
                ],
                "timestamp": 1686556261,
                "severityT": "Info"
            }
        ]
    }
]
```

[[Back]](./ProtocolArp.md)