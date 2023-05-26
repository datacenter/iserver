# Node Protocol - ARP

## JSON

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc -o json

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
            "modTs": "2023-03-03T01:12:02.244+02:00",
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
            "modTs": "2023-03-03T01:23:19.532+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_BGP_VRF/db-ip/adj-[eth1/24.62]-[192.168.254.1]",
                    "ifId": "eth1/24.62",
                    "ip": "192.168.254.1",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:44:57.317+02:00",
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
            "modTs": "2023-03-03T01:23:16.395+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_privIP_VRF/db-ip/adj-[eth1/24.36]-[192.168.254.66]",
                    "ifId": "eth1/24.36",
                    "ip": "192.168.254.66",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:16.550+02:00",
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
            "modTs": "2023-03-03T01:23:29.861+02:00",
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
            "modTs": "2023-03-03T01:23:26.794+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF/db-ip/adj-[eth1/24.65]-[192.168.254.98]",
                    "ifId": "eth1/24.65",
                    "ip": "192.168.254.98",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:13.777+02:00",
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
            "modTs": "2023-03-03T01:23:26.794+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1_VRF/db-ip/adj-[eth1/24.60]-[192.168.254.102]",
                    "ifId": "eth1/24.60",
                    "ip": "192.168.254.102",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:13.670+02:00",
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
            "modTs": "2023-03-03T01:23:19.532+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/db-ip/adj-[eth1/24.64]-[192.168.254.90]",
                    "ifId": "eth1/24.64",
                    "ip": "192.168.254.90",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:14.823+02:00",
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
            "modTs": "2023-03-03T01:23:27.775+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4_VRF/db-ip/adj-[eth1/24.66]-[192.168.254.94]",
                    "ifId": "eth1/24.66",
                    "ip": "192.168.254.94",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:13.727+02:00",
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
            "modTs": "2023-03-03T01:23:26.794+02:00",
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
            "modTs": "2023-03-03T02:37:01.049+02:00",
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
            "modTs": "2023-03-03T01:23:29.861+02:00",
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
            "modTs": "2023-03-03T01:23:29.861+02:00",
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
            "modTs": "2023-03-03T01:23:16.395+02:00",
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
            "modTs": "2023-03-03T01:23:11.621+02:00",
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
            "modTs": "2023-03-03T01:23:26.794+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-mgmt:inb/db-ip/adj-[eth1/24.67]-[192.168.254.17]",
                    "ifId": "eth1/24.67",
                    "ip": "192.168.254.17",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:14.880+02:00",
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
            "modTs": "2023-03-03T01:23:29.861+02:00",
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
            "modTs": "2023-03-03T01:23:14.560+02:00",
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
            "modTs": "2023-03-03T01:23:29.861+02:00",
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
            "modTs": "2023-03-03T01:23:15.089+02:00",
            "monPolDn": "uni/fabric/monfab-default",
            "name": "MPC-F5T:F5-OUT_VRF",
            "status": "",
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "adjacency": [
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC-F5T:F5-OUT_VRF/db-ip/adj-[vlan63]-[15.2.7.1]",
                    "ifId": "vlan63",
                    "ip": "15.2.7.1",
                    "mac": "00:50:56:B2:80:63",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:48:10.298+02:00",
                    "domain_name": "MPC-F5T:F5-OUT_VRF",
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
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-IN_VRF",
            "encap": "vxlan-2490372",
            "lcOwn": "local",
            "modTs": "2023-03-03T01:23:19.532+02:00",
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
            "modTs": "2023-03-03T01:23:19.532+02:00",
            "monPolDn": "uni/fabric/monfab-default",
            "name": "MPC:MPC-sPBR-OUT_VRF",
            "status": "",
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "adjacency": [
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.252]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.252",
                    "mac": "00:22:BD:CD:C2:BB",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:39:39.880+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.5]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.5",
                    "mac": "00:50:56:B2:0E:D8",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:46:08.751+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.4]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.4",
                    "mac": "00:50:56:B2:62:BB",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:47:09.159+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.3]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.3",
                    "mac": "00:50:56:B2:77:0B",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:48:40.099+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.2]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.2",
                    "mac": "00:50:56:B2:7E:F3",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:44:19.531+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.6]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.6",
                    "mac": "00:50:56:B2:8F:CB",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:44:38.351+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.1]",
                    "ifId": "vlan61",
                    "ip": "15.2.7.1",
                    "mac": "00:50:56:B2:D5:AB",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:47:07.824+02:00",
                    "domain_name": "MPC:MPC-sPBR-OUT_VRF",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                }
            ],
            "adjacency_count": 7
        },
        {
            "__Output": {
                "name": "Yellow"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-NXOS-HandOff_Test:default",
            "encap": "vxlan-2129927",
            "lcOwn": "local",
            "modTs": "2023-03-03T01:23:15.089+02:00",
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
            "modTs": "2023-03-03T01:12:02.244+02:00",
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
                    "upTS": "2023-05-07T14:34:26.479+02:00",
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
            "modTs": "2023-03-03T01:23:19.532+02:00",
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
            "modTs": "2023-03-03T01:23:15.420+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-SPIN_InnoLab:SPIN_VRF1/db-ip/adj-[eth1/24.71]-[192.168.254.41]",
                    "ifId": "eth1/24.71",
                    "ip": "192.168.254.41",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:14.767+02:00",
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
            "modTs": "2023-03-03T01:23:29.861+02:00",
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
            "modTs": "2023-03-03T01:23:14.329+02:00",
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
            "modTs": "2023-03-03T01:23:16.395+02:00",
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
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.108]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.108",
                    "mac": "00:22:BD:F8:19:FF",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:41:30.676+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.104]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.104",
                    "mac": "00:50:56:B2:13:6E",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:48:00.691+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.106]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.106",
                    "mac": "00:50:56:B2:94:45",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:48:28.438+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.99]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.99",
                    "mac": "00:50:56:B2:94:45",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:48:48.410+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.103]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.103",
                    "mac": "00:50:56:B2:9F:42",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:48:12.127+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.98]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.98",
                    "mac": "00:50:56:B2:9F:42",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "tunnel2",
                    "status": "",
                    "upTS": "2023-05-07T14:48:01.984+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.97]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.97",
                    "mac": "00:50:56:B2:A9:62",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:48:08.111+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.102]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.102",
                    "mac": "00:50:56:B2:E3:FD",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:48:27.564+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.105]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.105",
                    "mac": "00:50:56:B2:E7:5B",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:48:16.165+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.101]",
                    "ifId": "vlan35",
                    "ip": "10.58.24.101",
                    "mac": "00:50:56:B2:ED:D0",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "po5",
                    "status": "",
                    "upTS": "2023-05-07T14:45:48.156+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                },
                {
                    "__Output": {
                        "name": "Yellow",
                        "operSt": "Green"
                    },
                    "childAction": "",
                    "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[eth1/24.68]-[192.168.254.105]",
                    "ifId": "eth1/24.68",
                    "ip": "192.168.254.105",
                    "mac": "00:A3:8E:EB:B3:3F",
                    "modTs": "never",
                    "name": "",
                    "operSt": "normal",
                    "physIfId": "eth1/24",
                    "status": "",
                    "upTS": "2023-05-07T14:30:14.713+02:00",
                    "domain_name": "UC3-CL2023-Demo:default",
                    "pod_node_name": "pod-1/bl205-eu-spdc"
                }
            ],
            "adjacency_count": 11
        }
    ],
    "adjacency": [
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_BGP_VRF/db-ip/adj-[eth1/24.62]-[192.168.254.1]",
            "ifId": "eth1/24.62",
            "ip": "192.168.254.1",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:44:57.317+02:00",
            "domain_name": "common:Infra_BGP_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:Infra_privIP_VRF/db-ip/adj-[eth1/24.36]-[192.168.254.66]",
            "ifId": "eth1/24.36",
            "ip": "192.168.254.66",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:16.550+02:00",
            "domain_name": "common:Infra_privIP_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF/db-ip/adj-[eth1/24.65]-[192.168.254.98]",
            "ifId": "eth1/24.65",
            "ip": "192.168.254.98",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:13.777+02:00",
            "domain_name": "common:smi5Gc-cvim1-N3-N4_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim1_VRF/db-ip/adj-[eth1/24.60]-[192.168.254.102]",
            "ifId": "eth1/24.60",
            "ip": "192.168.254.102",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:13.670+02:00",
            "domain_name": "common:smi5Gc-cvim1_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/db-ip/adj-[eth1/24.64]-[192.168.254.90]",
            "ifId": "eth1/24.64",
            "ip": "192.168.254.90",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:14.823+02:00",
            "domain_name": "common:smi5Gc-cvim4-N3-N4_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-common:smi5Gc-cvim4_VRF/db-ip/adj-[eth1/24.66]-[192.168.254.94]",
            "ifId": "eth1/24.66",
            "ip": "192.168.254.94",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:13.727+02:00",
            "domain_name": "common:smi5Gc-cvim4_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-mgmt:inb/db-ip/adj-[eth1/24.67]-[192.168.254.17]",
            "ifId": "eth1/24.67",
            "ip": "192.168.254.17",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:14.880+02:00",
            "domain_name": "mgmt:inb",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC-F5T:F5-OUT_VRF/db-ip/adj-[vlan63]-[15.2.7.1]",
            "ifId": "vlan63",
            "ip": "15.2.7.1",
            "mac": "00:50:56:B2:80:63",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:48:10.298+02:00",
            "domain_name": "MPC-F5T:F5-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.252]",
            "ifId": "vlan61",
            "ip": "15.2.7.252",
            "mac": "00:22:BD:CD:C2:BB",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:39:39.880+02:00",
            "domain_name": "MPC:MPC-sPBR-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.5]",
            "ifId": "vlan61",
            "ip": "15.2.7.5",
            "mac": "00:50:56:B2:0E:D8",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:46:08.751+02:00",
            "domain_name": "MPC:MPC-sPBR-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.4]",
            "ifId": "vlan61",
            "ip": "15.2.7.4",
            "mac": "00:50:56:B2:62:BB",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:47:09.159+02:00",
            "domain_name": "MPC:MPC-sPBR-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.3]",
            "ifId": "vlan61",
            "ip": "15.2.7.3",
            "mac": "00:50:56:B2:77:0B",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:48:40.099+02:00",
            "domain_name": "MPC:MPC-sPBR-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.2]",
            "ifId": "vlan61",
            "ip": "15.2.7.2",
            "mac": "00:50:56:B2:7E:F3",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:44:19.531+02:00",
            "domain_name": "MPC:MPC-sPBR-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.6]",
            "ifId": "vlan61",
            "ip": "15.2.7.6",
            "mac": "00:50:56:B2:8F:CB",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:44:38.351+02:00",
            "domain_name": "MPC:MPC-sPBR-OUT_VRF",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-MPC:MPC-sPBR-OUT_VRF/db-ip/adj-[vlan61]-[15.2.7.1]",
            "ifId": "vlan61",
            "ip": "15.2.7.1",
            "mac": "00:50:56:B2:D5:AB",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:47:07.824+02:00",
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
            "upTS": "2023-05-07T14:34:26.479+02:00",
            "domain_name": "overlay-1",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-SPIN_InnoLab:SPIN_VRF1/db-ip/adj-[eth1/24.71]-[192.168.254.41]",
            "ifId": "eth1/24.71",
            "ip": "192.168.254.41",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:14.767+02:00",
            "domain_name": "SPIN_InnoLab:SPIN_VRF1",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.108]",
            "ifId": "vlan35",
            "ip": "10.58.24.108",
            "mac": "00:22:BD:F8:19:FF",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:41:30.676+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.104]",
            "ifId": "vlan35",
            "ip": "10.58.24.104",
            "mac": "00:50:56:B2:13:6E",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:48:00.691+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.106]",
            "ifId": "vlan35",
            "ip": "10.58.24.106",
            "mac": "00:50:56:B2:94:45",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:48:28.438+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.99]",
            "ifId": "vlan35",
            "ip": "10.58.24.99",
            "mac": "00:50:56:B2:94:45",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:48:48.410+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.103]",
            "ifId": "vlan35",
            "ip": "10.58.24.103",
            "mac": "00:50:56:B2:9F:42",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:48:12.127+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.98]",
            "ifId": "vlan35",
            "ip": "10.58.24.98",
            "mac": "00:50:56:B2:9F:42",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "tunnel2",
            "status": "",
            "upTS": "2023-05-07T14:48:01.984+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.97]",
            "ifId": "vlan35",
            "ip": "10.58.24.97",
            "mac": "00:50:56:B2:A9:62",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:48:08.111+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.102]",
            "ifId": "vlan35",
            "ip": "10.58.24.102",
            "mac": "00:50:56:B2:E3:FD",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:48:27.564+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.105]",
            "ifId": "vlan35",
            "ip": "10.58.24.105",
            "mac": "00:50:56:B2:E7:5B",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:48:16.165+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[vlan35]-[10.58.24.101]",
            "ifId": "vlan35",
            "ip": "10.58.24.101",
            "mac": "00:50:56:B2:ED:D0",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "po5",
            "status": "",
            "upTS": "2023-05-07T14:45:48.156+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        },
        {
            "__Output": {
                "name": "Yellow",
                "operSt": "Green"
            },
            "childAction": "",
            "dn": "topology/pod-1/node-205/sys/arp/inst/dom-UC3-CL2023-Demo:default/db-ip/adj-[eth1/24.68]-[192.168.254.105]",
            "ifId": "eth1/24.68",
            "ip": "192.168.254.105",
            "mac": "00:A3:8E:EB:B3:3F",
            "modTs": "never",
            "name": "",
            "operSt": "normal",
            "physIfId": "eth1/24",
            "status": "",
            "upTS": "2023-05-07T14:30:14.713+02:00",
            "domain_name": "UC3-CL2023-Demo:default",
            "pod_node_name": "pod-1/bl205-eu-spdc"
        }
    ],
    "interface": [
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.36",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.60",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.62",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.64",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.65",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.66",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.67",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.68",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/24.71",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "eth1/28",
            "count": 1
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "vlan35",
            "count": 10
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "vlan61",
            "count": 7
        },
        {
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "interface": "vlan63",
            "count": 1
        }
    ]
}
```

[[Back]](./ProtocolArp.md)