# Node Interface - Encapsulated Routed

## JSON output

```
# iserver get aci intf l3e --apic apic11 --node any --id eth1/36.83 -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "state.operSt": "Green",
            "donorIf": "Yellow"
        },
        "MultiPodDirect": "no",
        "adminSt": "up",
        "delay": "1",
        "dn": "topology/pod-1/node-205/sys/inst-overlay-1/encrtd-[eth1/36.83]",
        "encap": "vlan-2",
        "ethpmCfgFailedBmp": "",
        "ethpmCfgFailedTs": "00:00:00:00.000",
        "ethpmCfgState": "0",
        "id": "eth1/36.83",
        "mplsEnable": "no",
        "mplsMtu": "9000",
        "mtu": "9366",
        "mtuInherit": "yes",
        "pcTag": "any",
        "qosPrio": "unspecified",
        "routerMac": "00:00:00:00:00:00",
        "rtdOutDefDn": "",
        "serviceEnabled": "no",
        "podId": "1",
        "nodeId": "205",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl205-eu-spdc",
        "state": {
            "currErrIndex": "0",
            "fsmState": "3",
            "hwBdId": "1",
            "hwResourceId": "22",
            "iod": "48",
            "lastErrors": "0",
            "operBitset": "38",
            "operMtu": "9366",
            "operSt": "up",
            "operStQual": "",
            "siCfgFlags": "1"
        },
        "donorIf": "lo0",
        "up": true
    }
]
```

[[Back]](./InterfaceL3e.md)