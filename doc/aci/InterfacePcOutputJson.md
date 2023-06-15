# Node Interface - Port Channel (PC)

## JSON output

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1 -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Green",
            "switchingSt": "Green",
            "pcMode": "Green",
            "operChannelMode": "Green",
            "vpcDomain": "Yellow"
        },
        "activePorts": "1",
        "adminSt": "up",
        "autoNeg": "on",
        "bw": "0",
        "ctrl": "fast-sel-hot-stdby",
        "delay": "1",
        "dn": "topology/pod-1/node-201/sys/aggr-[po1]",
        "dot1qEtherType": "0x8100",
        "ethpmCfgFailedBmp": "",
        "ethpmCfgFailedTs": "00:00:00:00.000",
        "ethpmCfgState": "0",
        "fcotChannelNumber": "Channel32",
        "fop": "eth1/4",
        "hashDist": "adaptive",
        "id": "po1",
        "iod": "134",
        "isPlatformSupported": "yes",
        "isReflectiveRelayCfgSupported": "Supported",
        "lastBundleMbr": "eth1/4",
        "lastBundleTime": "19520:08:35:06.241",
        "lastSt": "successful",
        "lastStCause": "",
        "lastUnbundleMbr": "unspecified",
        "lastUnbundleTime": "00:00:00:00.000",
        "layer": "Layer2",
        "linkDebounce": "100",
        "ltl": "8198",
        "maxActive": "16",
        "maxLinks": "16",
        "mdix": "auto",
        "medium": "broadcast",
        "minLinks": "1",
        "mode": "trunk",
        "mtu": "9000",
        "name": "pod1a-AIO-2-SAMX_PolGrp",
        "operChannelMode": "active",
        "pcId": "1",
        "pcMode": "active",
        "pcmCfgFailedBmp": "",
        "pcmCfgFailedTs": "00:00:00:00.000",
        "pcmCfgState": "0",
        "portT": "leaf",
        "prioFlowCtrl": "auto",
        "reflectiveRelayEn": "off",
        "routerMac": "not-applicable",
        "snmpTrapSt": "enable",
        "spanMode": "not-a-span-dest",
        "speed": "inherit",
        "suspMinlinks": "no",
        "switchingSt": "enabled",
        "usage": "epg",
        "state": {
            "__Output": {
                "operSt": "Green"
            },
            "accessVlan": "vlan-75",
            "activeMbrs": "eth1/4,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified",
            "allowedVlans": "32-33,74-75,330-331,469-470,472,492-493,496-497",
            "backplaneMac": "4C:71:0D:23:FA:3C",
            "bundleBupId": "1",
            "bundleIndex": "unspecified",
            "cfgAccessVlan": "vlan-75",
            "cfgNativeVlan": "vlan-75",
            "errVlans": "",
            "hwBdId": "0",
            "hwResourceId": "0",
            "intfT": "phy",
            "iod": "134",
            "lastErrors": "0",
            "lastLinkStChg": "2023-06-12T16:52:40.787+02:00",
            "nativeVlan": "vlan-75",
            "numActivePorts": "1",
            "numMbrUp": "1",
            "operDceMode": "edge",
            "operDuplex": "full",
            "operMode": "trunk",
            "operRouterMac": "4C:71:0D:23:FA:E3",
            "operSpeed": "10G",
            "operSt": "up",
            "operStQual": "",
            "operVlans": "32-33,74-75,330-331,469-470,472,492-493,496-497",
            "primaryVlan": "vlan-1",
            "portId": [
                "eth1/4"
            ],
            "portIds": "eth1/4"
        },
        "podId": "1",
        "nodeId": "201",
        "apic": "apic11",
        "pod_node_name": "pod-1/cl201-eu-spdc",
        "layerT": "switched",
        "up": true,
        "vpcDomain": "100"
    }
]
```

[[Back]](./InterfacePc.md)