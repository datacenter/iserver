# Node Interface - Virtual Port Channel (VPC)

## JSON output

```
# iserver get aci intf tun
    --apic apic11
    --node bl205-eu-spdc
    --id tunnel16
    --view verbose -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "operSt": "Green"
        },
        "aclTcamStQual": "",
        "adminSt": "up",
        "cfgdMtu": "9000",
        "delInProg": "no",
        "dest": "172.16.30.161",
        "dn": "topology/pod-1/node-205/sys/tunnel-[tunnel16]",
        "id": "tunnel16",
        "idRequestorDn": "topology/pod-1/node-205/sys/bgp/inst/dom-overlay-1/db-dtep/dtep-[172.16.30.161]",
        "iod": "121",
        "keepAlvIntvl": "10",
        "keepAlvRetries": "3",
        "mac": "00:00:00:00:00:00",
        "operSt": "up",
        "operStQual": "",
        "src": "10.3.192.64/32",
        "tLayer": "l3",
        "tType": "ivxlan",
        "tmCfgFailedBmp": "",
        "tmCfgFailedTs": "00:00:00:00.000",
        "tmCfgState": "0",
        "type": "dci-ucast,fabric-ext,physical",
        "underlayVrfName": "",
        "v6Src": "0.0.0.0",
        "vrfName": "overlay-1",
        "podId": "1",
        "nodeId": "205",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl205-eu-spdc",
        "src_ip": "10.3.192.64",
        "dest_ip": "172.16.30.161",
        "typeT": [
            "Fabric External",
            "Physical",
            "dci-ucast"
        ],
        "tunnelId": 16,
        "up": true,
        "requestor": "bgp",
        "dest_node": []
    }
]
```

[[Back]](./InterfaceTunnel.md)