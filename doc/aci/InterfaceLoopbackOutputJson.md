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
            "iod": "106",
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
            "vpcPeer": "0.0.0.0",
            "ip": "205.205.205.205",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-206/sys/ctx-[vxlan-2097154]/lb-[lo8]",
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
            "iod": "106",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "172.24.0.14/32",
            "dn": "topology/pod-1/node-206/sys/ipv4/inst/dom-MPC:MPC-sPBR-OUT_VRF/if-[lo8]/addr-[172.24.0.14/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "172.24.0.14",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-201/sys/ctx-[vxlan-2523141]/lb-[lo8]",
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
            "iod": "201",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "15.254.101.0/32",
            "dn": "topology/pod-1/node-201/sys/ipv4/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/if-[lo8]/addr-[15.254.101.0/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "15.254.101.0",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-202/sys/ctx-[vxlan-2490372]/lb-[lo8]",
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
            "iod": "209",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "202.202.202.202/32",
            "dn": "topology/pod-1/node-202/sys/ipv4/inst/dom-MPC:MPC-sPBR-IN_VRF/if-[lo8]/addr-[202.202.202.202/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "202.202.202.202",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-301/sys/ctx-[vxlan-2818053]/lb-[lo8]",
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
            "iod": "89",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "131.131.131.131/32",
            "dn": "topology/pod-1/node-301/sys/ipv4/inst/dom-MPC-E:MPC-Residential-R3DC_VRF/if-[lo8]/addr-[131.131.131.131/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "131.131.131.131",
            "interface": "lo8"
        }
    },
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "dn": "topology/pod-1/node-302/sys/ctx-[vxlan-2981888]/lb-[lo8]",
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
            "iod": "96",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "172.24.3.14/32",
            "dn": "topology/pod-1/node-302/sys/ipv4/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/if-[lo8]/addr-[172.24.3.14/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "172.24.3.14",
            "interface": "lo8"
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
            "iod": "53",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "172.16.10.1/32",
            "dn": "topology/pod-1/node-101/sys/ipv4/inst/dom-overlay-1/if-[lo8]/addr-[172.16.10.1/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "172.16.10.1",
            "interface": "lo8"
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
            "iod": "54",
            "lastErrors": "0",
            "operSt": "up",
            "operStQual": ""
        },
        "up": true,
        "ipv4": {
            "addr": "172.16.10.1/32",
            "dn": "topology/pod-1/node-102/sys/ipv4/inst/dom-overlay-1/if-[lo8]/addr-[172.16.10.1/32]",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "up",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "ip": "172.16.10.1",
            "interface": "lo8"
        }
    }
]
```

[[Back]](./InterfaceLoopback.md)