# Node Interface - Loopback

## JSON output

```
# iserver get aci intf lb --apic apic11 --node any --id lo8 -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-205/sys/ctx-[vxlan-2818048]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "205",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl205-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "112",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "205.205.205.205/32",
            "dn": "topology/pod-1/node-205/sys/ipv4/inst/dom-mgmt:inb/if-[lo8]/addr-[205.205.205.205/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-206/sys/ctx-[vxlan-2261001]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "206",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl206-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "102",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "122.122.122.122/32",
            "dn": "topology/pod-1/node-206/sys/ipv4/inst/dom-common:smi5Gc-cvim1-N3-N4_VRF/if-[lo8]/addr-[122.122.122.122/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-201/sys/ctx-[vxlan-2392070]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "201",
        "apic": "apic11",
        "pod_node_name": "pod-1/cl201-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "200",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "15.254.101.6/32",
            "dn": "topology/pod-1/node-201/sys/ipv4/inst/dom-common:smi5Gc-cvim1-N6_VRF/if-[lo8]/addr-[15.254.101.6/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-202/sys/ctx-[vxlan-2883586]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "202",
        "apic": "apic11",
        "pod_node_name": "pod-1/cl202-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "201",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "15.254.101.9/32",
            "dn": "topology/pod-1/node-202/sys/ipv4/inst/dom-common:smi5Gc-cvim1_VRF/if-[lo8]/addr-[15.254.101.9/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-301/sys/ctx-[vxlan-2981888]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "301",
        "apic": "apic11",
        "pod_node_name": "pod-1/rl301-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "93",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "172.24.3.15/32",
            "dn": "topology/pod-1/node-301/sys/ipv4/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/if-[lo8]/addr-[172.24.3.15/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-302/sys/ctx-[vxlan-2097155]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "302",
        "apic": "apic11",
        "pod_node_name": "pod-1/rl302-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "72",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "132.132.132.132/32",
            "dn": "topology/pod-1/node-302/sys/ipv4/inst/dom-MPC-E:MPC-E-sPBR-IN_VRF/if-[lo8]/addr-[132.132.132.132/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-101/sys/inst-overlay-1/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "101",
        "apic": "apic11",
        "pod_node_name": "pod-1/s101-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "56",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "10.3.0.33/32",
            "dn": "topology/pod-1/node-101/sys/ipv4/inst/dom-overlay-1/if-[lo8]/addr-[10.3.0.33/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-102/sys/inst-overlay-1/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "102",
        "apic": "apic11",
        "pod_node_name": "pod-1/s102-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "18",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "10.3.0.33/32",
            "dn": "topology/pod-1/node-102/sys/ipv4/inst/dom-overlay-1/if-[lo8]/addr-[10.3.0.33/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0"
        }
    }
]
```

[[Back]](./InterfaceLoopback.md)