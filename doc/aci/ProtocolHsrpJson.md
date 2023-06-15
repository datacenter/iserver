# Node Protocol - HSRP

## JSON

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc -o json

[
    {
        "instance": {
            "__Output": {
                "adminSt": "Green",
                "operSt": "Green"
            },
            "adminSt": "enabled",
            "childAction": "",
            "dn": "topology/pod-1/node-201/sys/hsrp",
            "lcOwn": "local",
            "modTs": "2023-06-12T10:39:11.867+02:00",
            "monPolDn": "",
            "name": "",
            "operErr": "",
            "operSt": "enabled",
            "status": "",
            "pod_node_name": "pod-1/cl201-eu-spdc",
            "enable": true
        },
        "domains": [
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-common:smi5Gc-cvim1-N3-N4_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:12.766+02:00",
                "monPolDn": "",
                "name": "common:smi5Gc-cvim1-N3-N4_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-common:smi5Gc-cvim1-N6_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:12.766+02:00",
                "monPolDn": "",
                "name": "common:smi5Gc-cvim1-N6_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-common:smi5Gc-cvim1_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:12.766+02:00",
                "monPolDn": "",
                "name": "common:smi5Gc-cvim1_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-common:smi5Gc-cvim4-N3-N4_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:12.766+02:00",
                "monPolDn": "",
                "name": "common:smi5Gc-cvim4-N3-N4_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-common:smi5Gc-cvim4-N6_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:14.210+02:00",
                "monPolDn": "",
                "name": "common:smi5Gc-cvim4-N6_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-ECMP-demo:ACC-ext_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:12.766+02:00",
                "monPolDn": "",
                "name": "ECMP-demo:ACC-ext_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-MPC-E:MPC-E-sPBR-OUT_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:15.530+02:00",
                "monPolDn": "",
                "name": "MPC-E:MPC-E-sPBR-OUT_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-MPC:MPC-sPBR-IN_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:11.867+02:00",
                "monPolDn": "",
                "name": "MPC:MPC-sPBR-IN_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-MPC:MPC-sPBR-OUT_VRF",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:14.210+02:00",
                "monPolDn": "",
                "name": "MPC:MPC-sPBR-OUT_VRF",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            },
            {
                "__Output": {
                    "name": "Yellow"
                },
                "childAction": "",
                "dn": "topology/pod-1/node-201/sys/hsrp/inst-default/dom-SPIN_InnoLab:SPIN_VRF1",
                "lcOwn": "local",
                "modTs": "2023-06-12T10:39:11.867+02:00",
                "monPolDn": "",
                "name": "SPIN_InnoLab:SPIN_VRF1",
                "status": "",
                "pod_node_name": "pod-1/cl201-eu-spdc",
                "interfacesCount": 0
            }
        ],
        "interfaces": []
    }
]
```

[[Back]](./ProtocolHsrp.md)