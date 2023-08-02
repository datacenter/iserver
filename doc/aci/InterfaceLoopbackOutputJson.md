# Node Interface - Loopback

## JSON output

```
# iserver get aci intf lb
    --apic apic21
    --node any
    --node bl2205-eu-spdc
    --id lo8 -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-2205/sys/ctx-[vxlan-2785280]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "2205",
        "apic": "apic21",
        "pod_node_name": "pod-1/bl2205-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "83",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "ipv4": {
            "addr": "205.205.205.205/32",
            "dn": "topology/pod-1/node-2205/sys/ipv4/inst/dom-vEPC_demo:ACC_VRF/if-[lo8]/addr-[205.205.205.205/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "205.205.205.205",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-2206/sys/ctx-[vxlan-2424833]/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "2206",
        "apic": "apic21",
        "pod_node_name": "pod-1/bl2206-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "81",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "ipv4": {
            "addr": "206.206.206.206/32",
            "dn": "topology/pod-1/node-2206/sys/ipv4/inst/dom-vEPC_demo:INT_VRF/if-[lo8]/addr-[206.206.206.206/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "206.206.206.206",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-2101/sys/inst-overlay-1/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "2101",
        "apic": "apic21",
        "pod_node_name": "pod-1/s2101-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "99",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "ipv4": {
            "addr": "10.5.0.34/32",
            "dn": "topology/pod-1/node-2101/sys/ipv4/inst/dom-overlay-1/if-[lo8]/addr-[10.5.0.34/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "10.5.0.34",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-2102/sys/inst-overlay-1/lb-[lo8]",
        "id": "lo8",
        "qosPrio": "unspecified",
        "rtdOutDefDn": "",
        "status": "",
        "type": "",
        "iod": 8,
        "podId": "1",
        "nodeId": "2102",
        "apic": "apic21",
        "pod_node_name": "pod-1/s2102-eu-spdc",
        "state": {
            "currErrIndex": "4294967295",
            "iod": "99",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "ipv4": {
            "addr": "10.5.0.34/32",
            "dn": "topology/pod-1/node-2102/sys/ipv4/inst/dom-overlay-1/if-[lo8]/addr-[10.5.0.34/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "10.5.0.34",
            "interface": "lo8"
        }
    }
]
```

[[Back]](./InterfaceLoopback.md)