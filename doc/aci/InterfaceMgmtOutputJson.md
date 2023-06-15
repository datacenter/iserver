# Node Interface - Management

## JSON output

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc -o json

[
    {
        "__Output": {
            "adminSt": "Green",
            "switchingSt": "Red",
            "state.operSt": "Green",
            "stats.operSt": "Green"
        },
        "adminSt": "up",
        "autoNeg": "on",
        "dn": "topology/pod-1/node-201/sys/mgmt-[mgmt0]",
        "fcotChannelNumber": "Channel32",
        "id": "mgmt0",
        "mtu": "9000",
        "name": "",
        "snmpTrapSt": "enable",
        "speed": "1G",
        "status": "",
        "switchingSt": "disabled",
        "podId": "1",
        "nodeId": "201",
        "apic": "apic11",
        "pod_node_name": "pod-1/cl201-eu-spdc",
        "up": true,
        "state": {
            "__Output": {
                "operSt": "Green"
            },
            "backplaneMac": "4C:71:0D:23:FA:38",
            "dn": "topology/pod-1/node-201/sys/mgmt-[mgmt0]/mgmt",
            "lastLinkStChg": "2023-06-12T09:14:02.581+02:00",
            "operDuplex": "full",
            "operMtu": "1500",
            "operRouterMac": "4C:71:0D:23:FA:38",
            "operSpeed": "1G",
            "operSt": "up",
            "operStQual": "link-up",
            "vdcId": "1",
            "pod_id": "pod-1",
            "node_id": "node-201",
            "interface_id": "mgmt0"
        },
        "stats": {
            "__Output": {
                "operSt": "Green"
            },
            "addr": "10.58.28.141/27",
            "dn": "topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0]/addr-[10.58.28.141/27]",
            "ipv4CfgFailedBmp": "",
            "ipv4CfgFailedTs": "00:00:00:00.000",
            "ipv4CfgState": "0",
            "operSt": "up",
            "operStQual": "link-up-connected",
            "pref": "0",
            "type": "primary",
            "vpcPeer": "0.0.0.0",
            "pod_id": "pod-1",
            "node_id": "node-201",
            "interface_id": "mgmt0"
        }
    }
]
```

[[Back]](./InterfaceMgmt.md)