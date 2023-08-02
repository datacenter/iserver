# Node Interface - Management

## JSON output

```
# iserver get aci intf mgmt --apic apic21 --node bl2205-eu-spdc -o json

[
    {
        "__Output": {
            "adminSt": "Green",
            "switchingSt": "Red",
            "health": "Green",
            "faults": ":R.M.Y.G",
            "state.operSt": "Green"
        },
        "adminSt": "up",
        "autoNeg": "on",
        "dn": "topology/pod-1/node-2205/sys/mgmt-[mgmt0]",
        "fcotChannelNumber": "Channel32",
        "id": "mgmt0",
        "mtu": "9000",
        "name": "",
        "snmpTrapSt": "enable",
        "speed": "1G",
        "status": "",
        "switchingSt": "disabled",
        "podId": "1",
        "nodeId": "2205",
        "apic": "apic21",
        "pod_node_name": "pod-1/bl2205-eu-spdc",
        "up": true,
        "health": "100",
        "faults": "0 0 0 0",
        "isAnyFault": false,
        "state": {
            "__Output": {
                "operSt": "Green"
            },
            "backplaneMac": "3C:13:CC:B9:ED:B0",
            "dn": "topology/pod-1/node-2205/sys/mgmt-[mgmt0]/mgmt",
            "lastLinkStChg": "2023-06-18T09:38:34.501+02:00",
            "operDuplex": "full",
            "operMtu": "1500",
            "operRouterMac": "3C:13:CC:B9:ED:B0",
            "operSpeed": "1G",
            "operSt": "up",
            "operStQual": "link-up",
            "vdcId": "1",
            "pod_id": "pod-1",
            "node_id": "node-2205",
            "interface_id": "mgmt0"
        }
    }
]
```

[[Back]](./InterfaceMgmt.md)