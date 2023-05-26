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
        "cdp": {
            "cap": "igmp-filter,router,stp-dispute,switch",
            "devId": "r22-eu-spdc.emea-sp.cisco.com(FDO24200H8B)",
            "dn": "topology/pod-1/node-201/sys/cdp/inst/if-[mgmt0]/adj-2",
            "duplex": "full",
            "index": "2",
            "name": "",
            "nativeVlan": "12",
            "platId": "N9K-C92348GC-X",
            "portId": "Ethernet1/25",
            "stQual": "",
            "status": "",
            "sysName": "r22-eu-spdc",
            "sysObjIdL": "12",
            "sysObjIdV": "1,3,6,1,4,1,9,12,3,1,3,2239,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
            "ver": "Cisco Nexus Operating System (NX-OS) Software, Version 9.3(9)",
            "pod_id": "pod-1",
            "node_id": "node-201",
            "interface_id": "mgmt0"
        },
        "lldp": {
            "capability": "bridge,router",
            "chassisIdT": "mac",
            "dn": "topology/pod-1/node-201/sys/lldp/inst/if-[mgmt0]/adj-1",
            "enCap": "bridge,router",
            "id": "1",
            "mgmtId": "83886080",
            "mgmtIp": "10.58.234.142",
            "mgmtPortMac": "70:61:7B:D8:60:D8",
            "portDesc": "***** CL-201-201 ACI1 Management *****",
            "portIdT": "if-name",
            "portIdV": "Ethernet1/25",
            "portVlan": "12",
            "stQual": "",
            "status": "",
            "sysDesc": "Cisco Nexus Operating System (NX-OS) Software 9.3(9)\nTAC support: http://www.cisco.com/tac\nCopyright (c) 2002-2022, Cisco Systems, Inc. All rights reserved.",
            "sysName": "r22-eu-spdc.emea-sp.cisco.com",
            "ttl": "120",
            "pod_id": "pod-1",
            "node_id": "node-201",
            "interface_id": "mgmt0",
            "pod_node_name": "pod-pod-1/cl201-eu-spdc"
        },
        "faults": {
            "crit": "0",
            "critAcked": "0",
            "critAckedandDelegated": "0",
            "critDelegated": "0",
            "maj": "0",
            "majAcked": "0",
            "majAckedandDelegated": "0",
            "majDelegated": "0",
            "minor": "0",
            "minorAcked": "0",
            "minorAckedandDelegated": "0",
            "minorDelegated": "0",
            "warn": "0",
            "warnAckedandDelegated": "0",
            "warnDelegated": "0"
        },
        "state": {
            "__Output": {
                "operSt": "Green"
            },
            "backplaneMac": "4C:71:0D:23:FA:38",
            "dn": "topology/pod-1/node-201/sys/mgmt-[mgmt0]/mgmt",
            "lastLinkStChg": "2023-03-03T01:15:14.143+02:00",
            "operDuplex": "full",
            "operMtu": "1500",
            "operRouterMac": "4C:71:0D:23:FA:38",
            "operSpeed": "1G",
            "operSt": "up",
            "operStQual": "link-up",
            "vdcId": "1"
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
            "vpcPeer": "0.0.0.0"
        }
    }
]
```

[[Back]](./InterfaceMgmt.md)