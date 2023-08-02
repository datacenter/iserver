# Node Interface - Virtual Port Channel (VPC)

## JSON output

```
# iserver get aci intf tun
    --apic apic21
    --node bl2205-eu-spdc
    --id tunnel16
    --view all -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "operSt": "Green",
            "health": "Green",
            "faults": ":R.M.Y.G"
        },
        "aclTcamStQual": "",
        "adminSt": "up",
        "cfgdMtu": "9000",
        "delInProg": "no",
        "dest": "10.5.80.65",
        "dn": "topology/pod-1/node-2205/sys/tunnel-[tunnel16]",
        "id": "tunnel16",
        "idRequestorDn": "topology/pod-1/node-2205/sys/isis/inst-default/dom-overlay-1/lvl-l1/db-dtep/dtep-[10.5.80.65]",
        "iod": "62",
        "keepAlvIntvl": "10",
        "keepAlvRetries": "3",
        "mac": "00:00:00:00:00:00",
        "operSt": "up",
        "operStQual": "",
        "src": "10.5.216.66/32",
        "tLayer": "l3",
        "tType": "ivxlan",
        "tmCfgFailedBmp": "",
        "tmCfgFailedTs": "00:00:00:00.000",
        "tmCfgState": "0",
        "type": "physical,proxy-acast-v6",
        "underlayVrfName": "",
        "v6Src": "0.0.0.0",
        "vrfName": "overlay-1",
        "podId": "1",
        "nodeId": "2205",
        "apic": "apic21",
        "pod_node_name": "pod-1/bl2205-eu-spdc",
        "src_ip": "10.5.216.66",
        "dest_ip": "10.5.80.65",
        "typeT": [
            "Physical",
            "Proxy Anycast IPv6"
        ],
        "tunnelId": 16,
        "up": true,
        "requestor": "isis",
        "dest_node": [],
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "faultInst": [],
        "faultRecord": [],
        "eventLog": [],
        "auditLog": []
    }
]
```

[[Back]](./InterfaceTunnel.md)