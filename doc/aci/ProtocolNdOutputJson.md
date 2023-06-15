# Node Protocol - ND

## JSON

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc -o json

[
    {
        "instance": {
            "__Output": {
                "adminSt": "Green"
            },
            "adminSt": "enabled",
            "agingIntvl": "1380",
            "childAction": "",
            "ctrl": "",
            "dn": "topology/pod-1/node-205/sys/nd/inst",
            "lcOwn": "local",
            "modTs": "2023-06-12T09:17:53.331+02:00",
            "monPolDn": "uni/fabric/monfab-default",
            "name": "",
            "operErr": "",
            "status": "",
            "pod_node_name": "pod-1/bl205-eu-spdc",
            "enable": true,
            "neighborCount": 0,
            "activeInterfaceCount": 0
        },
        "domains": [
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:Infra_BGP_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_BGP_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 6
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:Infra_privIP_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:52.329+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_privIP_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 2
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:Infra_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:58.969+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:Infra_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:36:43.879+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim1-N3-N4_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:smi5Gc-cvim1_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim1_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:12.912+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim4-N3-N4_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-common:smi5Gc-cvim4_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:12.912+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "common:smi5Gc-cvim4_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-ECMP-demo:ACC_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:39.736+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "ECMP-demo:ACC_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-ECMP-demo:INT-ext_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "ECMP-demo:INT-ext_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-ECMP-demo:MPC-CDC-2_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "ECMP-demo:MPC-CDC-2_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-iks-monitoring:iks-mon_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "iks-monitoring:iks-mon_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-management",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "management",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-mgmt:EU-SPDC-ERSPAN-VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.369+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "mgmt:EU-SPDC-ERSPAN-VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-mgmt:inb",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:36.765+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "mgmt:inb",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-MPC-E:CU-DU-Infra_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-E:CU-DU-Infra_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-MPC-E:MPC-E-sPBR-IN_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-E:MPC-E-sPBR-IN_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 5
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-MPC-F5T:F5-IN_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-F5T:F5-IN_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-MPC-F5T:F5-OUT_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:40.610+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC-F5T:F5-OUT_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-MPC:MPC-sPBR-IN_VRF",
                "encap": "vxlan-2490372",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:41:02.138+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC:MPC-sPBR-IN_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 5
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-MPC:MPC-sPBR-OUT_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:13.032+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "MPC:MPC-sPBR-OUT_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-NXOS-HandOff_Test:default",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:46.993+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "NXOS-HandOff_Test:default",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-P5G:P5G_VRF",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:58.969+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "P5G:P5G_VRF",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-SPIN_InnoLab:SPIN_VRF1",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:12.912+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "SPIN_InnoLab:SPIN_VRF1",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 4
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-SPN_IntraLab:SPN_VRF1",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:43.783+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "SPN_IntraLab:SPN_VRF1",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-TESTING_BRUNO:default",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:38:58.969+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "TESTING_BRUNO:default",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 1
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-205/sys/nd/inst/dom-UC3-CL2023-Demo:default",
                "encap": "unknown",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:35:13.032+02:00",
                "monPolDn": "uni/fabric/monfab-default",
                "name": "UC3-CL2023-Demo:default",
                "status": "",
                "neighborsCount": 0,
                "interfacesCount": 0
            }
        ],
        "neighbors": [],
        "interfaces": []
    }
]
```

[[Back]](./ProtocolNd.md)