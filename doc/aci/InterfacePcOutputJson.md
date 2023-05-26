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
        "fop": "eth1/68",
        "hashDist": "adaptive",
        "id": "po1",
        "iod": "116",
        "isPlatformSupported": "yes",
        "isReflectiveRelayCfgSupported": "Supported",
        "lastBundleMbr": "eth1/68",
        "lastBundleTime": "19418:23:21:17.919",
        "lastSt": "successful",
        "lastStCause": "",
        "lastUnbundleMbr": "unspecified",
        "lastUnbundleTime": "00:00:00:00.000",
        "layer": "Layer2",
        "linkDebounce": "100",
        "ltl": "8192",
        "maxActive": "16",
        "maxLinks": "16",
        "mdix": "auto",
        "medium": "broadcast",
        "minLinks": "1",
        "mode": "trunk",
        "mtu": "9000",
        "name": "pod-4a-br-API",
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
        "speed": "1G",
        "suspMinlinks": "no",
        "switchingSt": "enabled",
        "usage": "epg",
        "state": {
            "__Output": {
                "operSt": "Green"
            },
            "accessVlan": "vlan-354",
            "activeMbrs": "eth1/68,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified,unspecified",
            "allowedVlans": "353-354",
            "backplaneMac": "4C:71:0D:23:FA:7C",
            "bundleBupId": "1",
            "bundleIndex": "unspecified",
            "cfgAccessVlan": "vlan-354",
            "cfgNativeVlan": "vlan-354",
            "errVlans": "",
            "hwBdId": "0",
            "hwResourceId": "0",
            "intfT": "phy",
            "iod": "116",
            "lastErrors": "0",
            "lastLinkStChg": "2023-03-03T01:23:45.593+02:00",
            "nativeVlan": "vlan-354",
            "numActivePorts": "1",
            "numMbrUp": "1",
            "operDceMode": "edge",
            "operDuplex": "full",
            "operMode": "trunk",
            "operRouterMac": "4C:71:0D:23:FA:E3",
            "operSpeed": "1G",
            "operSt": "up",
            "operStQual": "",
            "operVlans": "353-354",
            "primaryVlan": "vlan-1",
            "portId": [
                "eth1/68"
            ],
            "portIds": "eth1/68"
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