# Node Protocol - ARP

## JSON

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc -o json

[
    {
        "domains": [
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-black-hole",
                "encap": "vxlan-16777200",
                "lcOwn": "local",
                "modTs": "2023-06-12T09:12:42.649+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "black-hole",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_BGP_VRF",
                "encap": "vxlan-2424848",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_BGP_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_BGP_VRF/db-ip/adj-[eth1/24.48]-[192.168.254.1]",
                        "ifId": "eth1/24.48",
                        "ip": "192.168.254.1",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:59:40.468+02:00",
                        "domain_name": "common:Infra_BGP_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_privIP_VRF",
                "encap": "vxlan-2097161",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:52.329+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_privIP_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_privIP_VRF/db-ip/adj-[eth1/24.47]-[192.168.254.66]",
                        "ifId": "eth1/24.47",
                        "ip": "192.168.254.66",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:52.820+02:00",
                        "domain_name": "common:Infra_privIP_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_VRF",
                "encap": "vxlan-2686976",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:58.969+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF",
                "encap": "vxlan-2261001",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:36:43.879+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim1-N3-N4_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF/db-ip/adj-[eth1/24.51]-[192.168.254.98]",
                        "ifId": "eth1/24.51",
                        "ip": "192.168.254.98",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:55.983+02:00",
                        "domain_name": "common:smi5Gc-cvim1-N3-N4_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1_VRF",
                "encap": "vxlan-2883586",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim1_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1_VRF/db-ip/adj-[eth1/24.46]-[192.168.254.102]",
                        "ifId": "eth1/24.46",
                        "ip": "192.168.254.102",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:56.446+02:00",
                        "domain_name": "common:smi5Gc-cvim1_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF",
                "encap": "vxlan-2523141",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:12.912+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim4-N3-N4_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/db-ip/adj-[eth1/24.52]-[192.168.254.90]",
                        "ifId": "eth1/24.52",
                        "ip": "192.168.254.90",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:57.429+02:00",
                        "domain_name": "common:smi5Gc-cvim4-N3-N4_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4_VRF",
                "encap": "vxlan-2621441",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:12.912+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim4_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4_VRF/db-ip/adj-[eth1/24.55]-[192.168.254.94]",
                        "ifId": "eth1/24.55",
                        "ip": "192.168.254.94",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:56.393+02:00",
                        "domain_name": "common:smi5Gc-cvim4_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-ECMP-demo:ACC_VRF",
                "encap": "vxlan-2326534",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:39.736+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "ECMP-demo:ACC_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-ECMP-demo:INT-ext_VRF",
                "encap": "vxlan-2621448",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "ECMP-demo:INT-ext_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-ECMP-demo:MPC-CDC-2_VRF",
                "encap": "vxlan-3047429",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "ECMP-demo:MPC-CDC-2_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-iks-monitoring:iks-mon_VRF",
                "encap": "vxlan-2228231",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "iks-monitoring:iks-mon_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-management",
                "encap": "vxlan-2752512",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "management",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-mgmt:EU-SPDC-ERSPAN-VRF",
                "encap": "vxlan-2555904",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.369+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "mgmt:EU-SPDC-ERSPAN-VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-mgmt:inb",
                "encap": "vxlan-2818048",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:36.765+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "mgmt:inb",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-mgmt:inb/db-ip/adj-[eth1/24.54]-[192.168.254.17]",
                        "ifId": "eth1/24.54",
                        "ip": "192.168.254.17",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:56.033+02:00",
                        "domain_name": "mgmt:inb",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC-E:CU-DU-Infra_VRF",
                "encap": "vxlan-2981889",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-E:CU-DU-Infra_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC-E:MPC-E-sPBR-IN_VRF",
                "encap": "vxlan-2097155",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-E:MPC-E-sPBR-IN_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC-F5T:F5-IN_VRF",
                "encap": "vxlan-2162693",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-F5T:F5-IN_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC-F5T:F5-OUT_VRF",
                "encap": "vxlan-2523139",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-F5T:F5-OUT_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-IN_VRF",
                "encap": "vxlan-2490372",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:47.088+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC:MPC-sPBR-IN_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF",
                "encap": "vxlan-2097154",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:13.032+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC:MPC-sPBR-OUT_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan67]-[15.2.7.2]",
                        "ifId": "vlan67",
                        "ip": "15.2.7.2",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-06-14T08:07:30.525+02:00",
                        "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    },
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Red"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan67]-[15.2.7.5]",
                        "ifId": "vlan67",
                        "ip": "15.2.7.5",
                        "mac": "unspecified",
                        "modTs": "never",
                        "name": "",
                        "operSt": "incomplete",
                        "physIfId": "",
                        "status": "",
                        "upTS": "2023-06-14T08:07:40.045+02:00",
                        "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 2
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-NXOS-HandOff_Test:default",
                "encap": "vxlan-2129927",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:46.993+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "NXOS-HandOff_Test:default",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-overlay-1",
                "encap": "vxlan-16777199",
                "lcOwn": "local",
                "modTs": "2023-06-12T09:12:42.649+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "overlay-1",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-overlay-1/db-ip/adj-[eth1/28]-[15.16.2.1]",
                        "ifId": "eth1/28",
                        "ip": "15.16.2.1",
                        "mac": "00:8A:96:1C:7C:B4",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/28",
                        "status": "",
                        "upTS": "2023-06-14T07:49:18.345+02:00",
                        "domain_name": "overlay-1",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-P5G:P5G_VRF",
                "encap": "vxlan-2883584",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:58.969+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "P5G:P5G_VRF",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-SPIN_InnoLab:SPIN_VRF1",
                "encap": "vxlan-2195458",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:12.912+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "SPIN_InnoLab:SPIN_VRF1",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-SPIN_InnoLab:SPIN_VRF1/db-ip/adj-[eth1/24.50]-[192.168.254.41]",
                        "ifId": "eth1/24.50",
                        "ip": "192.168.254.41",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:52.876+02:00",
                        "domain_name": "SPIN_InnoLab:SPIN_VRF1",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-SPN_IntraLab:SPN_VRF1",
                "encap": "vxlan-2883591",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "SPN_IntraLab:SPN_VRF1",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-TESTING_BRUNO:default",
                "encap": "vxlan-2457600",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:58.969+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "TESTING_BRUNO:default",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [],
                "adjacency_count": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default",
                "encap": "vxlan-3014663",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:13.032+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "UC3-CL2023-Demo:default",
                "status": "",
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "adjacency": [
                    {
                        "__Output": {
                            "name": "Yellow",
                            "operSt": "Green"
                        },
                        "childAction": "",
                        "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[eth1/24.53]-[192.168.254.105]",
                        "ifId": "eth1/24.53",
                        "ip": "192.168.254.105",
                        "mac": "00:A3:8E:EB:B3:3F",
                        "modTs": "never",
                        "name": "",
                        "operSt": "normal",
                        "physIfId": "eth1/24",
                        "status": "",
                        "upTS": "2023-06-14T07:55:52.923+02:00",
                        "domain_name": "UC3-CL2023-Demo:default",
                        "pod_node_name": "pod-1/bl205-eu-spdc"
                    }
                ],
                "adjacency_count": 1
            }
        ],
        "adjacency": [
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_BGP_VRF/db-ip/adj-[eth1/24.48]-[192.168.254.1]",
                "ifId": "eth1/24.48",
                "ip": "192.168.254.1",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:59:40.468+02:00",
                "domain_name": "common:Infra_BGP_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_privIP_VRF/db-ip/adj-[eth1/24.47]-[192.168.254.66]",
                "ifId": "eth1/24.47",
                "ip": "192.168.254.66",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:52.820+02:00",
                "domain_name": "common:Infra_privIP_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF/db-ip/adj-[eth1/24.51]-[192.168.254.98]",
                "ifId": "eth1/24.51",
                "ip": "192.168.254.98",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:55.983+02:00",
                "domain_name": "common:smi5Gc-cvim1-N3-N4_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1_VRF/db-ip/adj-[eth1/24.46]-[192.168.254.102]",
                "ifId": "eth1/24.46",
                "ip": "192.168.254.102",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:56.446+02:00",
                "domain_name": "common:smi5Gc-cvim1_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/db-ip/adj-[eth1/24.52]-[192.168.254.90]",
                "ifId": "eth1/24.52",
                "ip": "192.168.254.90",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:57.429+02:00",
                "domain_name": "common:smi5Gc-cvim4-N3-N4_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4_VRF/db-ip/adj-[eth1/24.55]-[192.168.254.94]",
                "ifId": "eth1/24.55",
                "ip": "192.168.254.94",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:56.393+02:00",
                "domain_name": "common:smi5Gc-cvim4_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-mgmt:inb/db-ip/adj-[eth1/24.54]-[192.168.254.17]",
                "ifId": "eth1/24.54",
                "ip": "192.168.254.17",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:56.033+02:00",
                "domain_name": "mgmt:inb",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan67]-[15.2.7.2]",
                "ifId": "vlan67",
                "ip": "15.2.7.2",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-06-14T08:07:30.525+02:00",
                "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Red"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan67]-[15.2.7.5]",
                "ifId": "vlan67",
                "ip": "15.2.7.5",
                "mac": "unspecified",
                "modTs": "never",
                "name": "",
                "operSt": "incomplete",
                "physIfId": "",
                "status": "",
                "upTS": "2023-06-14T08:07:40.045+02:00",
                "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-overlay-1/db-ip/adj-[eth1/28]-[15.16.2.1]",
                "ifId": "eth1/28",
                "ip": "15.16.2.1",
                "mac": "00:8A:96:1C:7C:B4",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/28",
                "status": "",
                "upTS": "2023-06-14T07:49:18.345+02:00",
                "domain_name": "overlay-1",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-SPIN_InnoLab:SPIN_VRF1/db-ip/adj-[eth1/24.50]-[192.168.254.41]",
                "ifId": "eth1/24.50",
                "ip": "192.168.254.41",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:52.876+02:00",
                "domain_name": "SPIN_InnoLab:SPIN_VRF1",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            },
            {
                "__Output": {
                    "name": "Yellow",
                    "operSt": "Green"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[eth1/24.53]-[192.168.254.105]",
                "ifId": "eth1/24.53",
                "ip": "192.168.254.105",
                "mac": "00:A3:8E:EB:B3:3F",
                "modTs": "never",
                "name": "",
                "operSt": "normal",
                "physIfId": "eth1/24",
                "status": "",
                "upTS": "2023-06-14T07:55:52.923+02:00",
                "domain_name": "UC3-CL2023-Demo:default",
                "pod_node_name": "pod-1/bl205-eu-spdc"
            }
        ],
        "interface": [
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.46",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.47",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.48",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.50",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.51",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.52",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.53",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.54",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/24.55",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "eth1/28",
                "count": 1
            },
            {
                "pod_node_name": "pod-1/bl205-eu-spdc",
                "interface": "vlan67",
                "count": 2
            }
        ]
    }
]
```

[[Back]](./ProtocolArp.md)