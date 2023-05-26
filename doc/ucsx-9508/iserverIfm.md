# UCSX-9508 IFM monitoring with iserver

Use '-m|--module' option with '.|*|all' value to select all modules.

```
# iserver get chassis --serial FOX2611PPHP -m .

+------------------+-------+-----------+------------+------------------+--------------+--------------+----------+-------------+----------------+
| I/O Module       | Path  | Presence  | OperState  | Model            | Serial       | P/N          | Version  | Host Ports  | Network Ports  |
+------------------+-------+-----------+------------+------------------+--------------+--------------+----------+-------------+----------------+
| IFM #1 (top)     | B     | True      | OK         | UCSX-I-9108-25G  | FCH261770KU  | 73-20533-03  | 4.2(2c)  | 0/33        | 4/4/8          | 
| IFM #2 (bottom)  | A     | True      | OK         | UCSX-I-9108-25G  | FCH261770RN  | 73-20533-03  | 4.2(2c)  | 0/33        | 4/4/8          | 
+------------------+-------+-----------+------------+------------------+--------------+--------------+----------+-------------+----------------+

+------------------+-----------------+-------------+-------+
| I/O Module       | Management IP   | Gateway     | VLAN  |
+------------------+-----------------+-------------+-------+
| IFM #1 (top)     | 10.90.90.49/24  | 10.90.89.1  | 89    | 
| IFM #2 (bottom)  | 10.90.90.48/24  | 10.90.89.1  | 89    | 
+------------------+-----------------+-------------+-------+
```

## Select module by slot ID

Use '-m|--module 1|2' option to select module by slot ID

```
# iserver get chassis --serial FOX2611PPHP -m 1

I/O Module State
----------------
- I/O Module    : IFM #1 (top)
- Path          : B
- Presence      : True
- OperState     : OK
- Model         : UCSX-I-9108-25G
- Serial        : FCH261770KU
- P/N           : 73-20533-03
- Version       : 4.2(2c)
- Host Ports    : 0/33
- Network Ports : 4/4/8
- Management IP : 10.90.90.49/24
- Gateway       : 10.90.89.1
- VLAN          : 89
```

## Select module by fabric path

Use '-m|--module a|b|A|B' option to select module by fabric path

```
# iserver get chassis --serial FOX2611PPHP -m a

I/O Module State
----------------
- I/O Module    : IFM #2 (bottom)
- Path          : A
- Presence      : True
- OperState     : OK
- Model         : UCSX-I-9108-25G
- Serial        : FCH261770RN
- P/N           : 73-20533-03
- Version       : 4.2(2c)
- Host Ports    : 0/33
- Network Ports : 4/4/8
- Management IP : 10.90.90.48/24
- Gateway       : 10.90.89.1
- VLAN          : 89
```

## JSON output

```
# iserver get chassis --serial FOX2611PPHP -m . -o json

{
    "Chassis": {
        "ConnectionPath": "A,B",
        "ConnectionStatus": "A,B",
        "Description": "Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots",
        "Dn": "chassis-1",
        "DeviceMoId": "632999466f72612d39b26942",
        "Moid": "632b13c876752d32362fc175",
        "Model": "UCSX-9508",
        "Name": "ucsX-1",
        "OperState": "OK",
        "PartNumber": "68-6847-03",
        "Pid": "UCSX-9508",
        "ProductName": "Cisco UCSX 9508 Chassis",
        "Serial": "FOX2611PPHP",
        "Sku": "UCSX-9508",
        "Vendor": "Cisco Systems Inc",
        "Health": "Warnings",
        "HealthSummary": "Warnings (2)",
        "AlarmWarning": 2,
        "AlarmCritical": 0,
        "ConnectionSummary": "A,B / A,B",
        "NodeMax": 8,
        "IfmMax": 2,
        "FanModuleMax": 4,
        "FanMax": 8,
        "PsuMax": 6,
        "IfmOn": 2,
        "IfmCount": 2,
        "IfmSummary": "2/2/2",
        "HostPortCount": 66,
        "HostPortUp": 0,
        "HostPortSummary": "0/66",
        "NetworkPortUp": 8,
        "NetworkPortCount": 8,
        "NetworkPortMax": 16,
        "NetworkPortSummary": "8/8/16"
    },
    "IfmInfo": [
        {
            "Moid": "632b13c976752d32362fc244",
            "Dn": "chassis-1-ioc-1",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "B",
            "ConnectionStatus": "B",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.49",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.49/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b178c76752d323630ceca",
                "632b178c76752d323630ced9",
                "632b178c76752d323630cee8"
            ],
            "HostPorts": [
                "632b175c6373582d42a02271",
                "632b175c6373582d42a02275",
                "632b175c6373582d42a0227a",
                "632b175c6373582d42a0227d",
                "632b175c6373582d42a02280",
                "632b175c6373582d42a02277",
                "632b175c6373582d42a02272",
                "632b175c6373582d42a0227b",
                "632b175c6373582d42a02286",
                "632b175c6373582d42a02289",
                "632b175c6373582d42a02270",
                "632b175c6373582d42a02274",
                "632b175c6373582d42a02278",
                "632b175c6373582d42a0228b",
                "632b175c6373582d42a0226d",
                "632b175c6373582d42a0226e",
                "632b175c6373582d42a02276",
                "632b175c6373582d42a0227c",
                "632b175c6373582d42a02284",
                "632b175c6373582d42a0226f",
                "632b175c6373582d42a0227f",
                "632b175c6373582d42a02281",
                "632b175c6373582d42a02288",
                "632b175c6373582d42a02273",
                "632b175c6373582d42a02279",
                "632b175c6373582d42a0227e",
                "632b175c6373582d42a02282",
                "632b175c6373582d42a02287",
                "632b175c6373582d42a0228a",
                "632b175c6373582d42a0226c",
                "632b175c6373582d42a02283",
                "632b175c6373582d42a02285",
                "632b1fcc6373582d42a023ab"
            ],
            "NetworkPorts": [
                "632b13c976752d32362fc25a",
                "632c81ec76752d32369daa08",
                "632c81f276752d32369dac8d",
                "632c820576752d32369db290"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #1 (top)",
            "ModuleId": 1,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770KU",
            "Side": "top",
            "Version": "4.2(2c)",
            "HostPortCount": 33,
            "HostPortUp": 0,
            "HostPortSummary": "0/33",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        },
        {
            "Moid": "632b13c876752d32362fc17c",
            "Dn": "chassis-1-ioc-2",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "A",
            "ConnectionStatus": "A",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.48",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.48/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b15b576752d3236304d3d",
                "632b15b576752d3236304d58",
                "632b15b576752d3236304d6f"
            ],
            "HostPorts": [
                "632b158c6373582d415a5ad6",
                "632b158c6373582d415a5ac0",
                "632b158c6373582d415a5acc",
                "632b158c6373582d415a5abf",
                "632b158c6373582d415a5ac6",
                "632b158c6373582d415a5ac7",
                "632b158c6373582d415a5ad4",
                "632b158c6373582d415a5ad8",
                "632b158c6373582d415a5ac1",
                "632b158c6373582d415a5ac4",
                "632b158c6373582d415a5acf",
                "632b158c6373582d415a5ad2",
                "632b158c6373582d415a5ad3",
                "632b158c6373582d415a5ac9",
                "632b158c6373582d415a5ad5",
                "632b158c6373582d415a5adb",
                "632b158c6373582d415a5ac2",
                "632b158c6373582d415a5ac8",
                "632b158c6373582d415a5add",
                "632b158c6373582d415a5aca",
                "632b158c6373582d415a5acb",
                "632b158c6373582d415a5acd",
                "632b158c6373582d415a5ace",
                "632b158c6373582d415a5ac5",
                "632b158c6373582d415a5ac3",
                "632b158c6373582d415a5ad0",
                "632b158c6373582d415a5adc",
                "632b158c6373582d415a5ad7",
                "632b158c6373582d415a5abe",
                "632b158c6373582d415a5ad1",
                "632b158c6373582d415a5ad9",
                "632b158c6373582d415a5ada",
                "632c6acd6373582d415a8b96"
            ],
            "NetworkPorts": [
                "632b13c876752d32362fc189",
                "632c81e776752d32369da82f",
                "632c81ed76752d32369daa9c",
                "632c81fe76752d32369db10a"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #2 (bottom)",
            "ModuleId": 2,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770RN",
            "Side": "bottom",
            "Version": "4.2(2c)",
            "HostPortCount": 33,
            "HostPortUp": 0,
            "HostPortSummary": "0/33",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        }
    ],
    "HostPortInfo": [
        {
            "Moid": "632b175c6373582d42a02282",
            "Dn": "chassis-1-ioc-1-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:83",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eab",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02283",
            "Dn": "chassis-1-ioc-1-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:84",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eac",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02284",
            "Dn": "chassis-1-ioc-1-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:85",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02285",
            "Dn": "chassis-1-ioc-1-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:86",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02286",
            "Dn": "chassis-1-ioc-1-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:87",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc0",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02287",
            "Dn": "chassis-1-ioc-1-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:88",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02288",
            "Dn": "chassis-1-ioc-1-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:89",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02289",
            "Dn": "chassis-1-ioc-1-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0228a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8B",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0228b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8C",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc6",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8F",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:90",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02270",
            "Dn": "chassis-1-ioc-1-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:91",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02271",
            "Dn": "chassis-1-ioc-1-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:92",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02272",
            "Dn": "chassis-1-ioc-1-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:93",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02273",
            "Dn": "chassis-1-ioc-1-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:94",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02274",
            "Dn": "chassis-1-ioc-1-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:95",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02275",
            "Dn": "chassis-1-ioc-1-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:96",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02276",
            "Dn": "chassis-1-ioc-1-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:97",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02277",
            "Dn": "chassis-1-ioc-1-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:98",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02278",
            "Dn": "chassis-1-ioc-1-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:99",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02279",
            "Dn": "chassis-1-ioc-1-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9B",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9C",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9F",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02280",
            "Dn": "chassis-1-ioc-1-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02281",
            "Dn": "chassis-1-ioc-1-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b1fcc6373582d42a023ab",
            "Dn": "chassis-1-ioc-1-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b158c6373582d415a5abe",
            "Dn": "chassis-1-ioc-2-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C3",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316ea9",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5abf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C4",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eaa",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C7",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bb7",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C8",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bbe",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CB",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CC",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5aca",
            "Dn": "chassis-1-ioc-2-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CF",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee1",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D0",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee2",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acd",
            "Dn": "chassis-1-ioc-2-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ace",
            "Dn": "chassis-1-ioc-2-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D3",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D4",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D7",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D8",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DB",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DC",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ada",
            "Dn": "chassis-1-ioc-2-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DF",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5adb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5adc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5add",
            "Dn": "chassis-1-ioc-2-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c6acd6373582d415a8b96",
            "Dn": "chassis-1-ioc-2-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        }
    ],
    "NetworkPortInfo": [
        {
            "Moid": "632b13c976752d32362fc25a",
            "Dn": "chassis-1-ioc-1-slot-1-port-1",
            "Name": "1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a64",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632c81ec76752d32369daa08",
            "Dn": "chassis-1-ioc-1-slot-1-port-2",
            "Name": "1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6a",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632c81f276752d32369dac8d",
            "Dn": "chassis-1-ioc-1-slot-1-port-3",
            "Name": "1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a14",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632c820576752d32369db290",
            "Dn": "chassis-1-ioc-1-slot-1-port-4",
            "Name": "1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6c",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b13c876752d32362fc189",
            "Dn": "chassis-1-ioc-2-slot-2-port-1",
            "Name": "2/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd9923",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c81e776752d32369da82f",
            "Dn": "chassis-1-ioc-2-slot-2-port-2",
            "Name": "2/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98da",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c81ed76752d32369daa9c",
            "Dn": "chassis-1-ioc-2-slot-2-port-3",
            "Name": "2/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98dd",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c81fe76752d32369db10a",
            "Dn": "chassis-1-ioc-2-slot-2-port-4",
            "Name": "2/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98d0",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        }
    ]
}
```

## YAML output

```
# iserver get chassis --serial FOX2611PPHP -m . -o yaml

Chassis:
  AlarmCritical: 0
  AlarmWarning: 2
  ConnectionPath: A,B
  ConnectionStatus: A,B
  ConnectionSummary: A,B / A,B
  Description: Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots
  DeviceMoId: 632999466f72612d39b26942
  Dn: chassis-1
  FanMax: 8
  FanModuleMax: 4
  Health: Warnings
  HealthSummary: Warnings (2)
  HostPortCount: 66
  HostPortSummary: 0/66
  HostPortUp: 0
  IfmCount: 2
  IfmMax: 2
  IfmOn: 2
  IfmSummary: 2/2/2
  Model: UCSX-9508
  Moid: 632b13c876752d32362fc175
  Name: ucsX-1
  NetworkPortCount: 8
  NetworkPortMax: 16
  NetworkPortSummary: 8/8/16
  NetworkPortUp: 8
  NodeMax: 8
  OperState: OK
  PartNumber: 68-6847-03
  Pid: UCSX-9508
  ProductName: Cisco UCSX 9508 Chassis
  PsuMax: 6
  Serial: FOX2611PPHP
  Sku: UCSX-9508
  Vendor: Cisco Systems Inc
HostPortInfo:
- Dn: chassis-1-ioc-1-muxhostport-port-1
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:83
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02282
  Name: 1/1/1
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b19af76752d3236316eab
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1283
  PortId: 1
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-2
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:84
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02283
  Name: 1/1/2
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b19af76752d3236316eac
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1283
  PortId: 2
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-3
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:85
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02284
  Name: 1/1/3
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 3
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-4
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:86
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02285
  Name: 1/1/4
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 4
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-5
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:87
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02286
  Name: 1/1/5
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188b76752d3236311bc0
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1280
  PortId: 5
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-6
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:88
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02287
  Name: 1/1/6
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188b76752d3236311bc5
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1280
  PortId: 6
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-7
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:89
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02288
  Name: 1/1/7
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 7
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-8
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8A
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02289
  Name: 1/1/8
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 8
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-9
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8B
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0228a
  Name: 1/1/9
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188d76752d3236311cc5
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1281
  PortId: 9
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-10
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8C
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0228b
  Name: 1/1/10
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188d76752d3236311cc6
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1281
  PortId: 10
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-11
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8D
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0226c
  Name: 1/1/11
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 11
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-12
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8E
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0226d
  Name: 1/1/12
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 12
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-13
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8F
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0226e
  Name: 1/1/13
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b189176752d3236311ee3
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1282
  PortId: 13
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-14
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:90
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0226f
  Name: 1/1/14
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b189176752d3236311ee4
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1282
  PortId: 14
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-15
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:91
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02270
  Name: 1/1/15
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 15
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-16
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:92
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02271
  Name: 1/1/16
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 16
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-17
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:93
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02272
  Name: 1/1/17
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 17
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-18
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:94
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02273
  Name: 1/1/18
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 18
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-19
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:95
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02274
  Name: 1/1/19
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 19
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-20
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:96
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02275
  Name: 1/1/20
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 20
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-21
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:97
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02276
  Name: 1/1/21
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 21
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-22
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:98
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02277
  Name: 1/1/22
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 22
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-23
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:99
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02278
  Name: 1/1/23
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 23
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-24
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9A
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02279
  Name: 1/1/24
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 24
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-25
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9B
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227a
  Name: 1/1/25
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 25
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-26
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9C
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227b
  Name: 1/1/26
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 26
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-27
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9D
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227c
  Name: 1/1/27
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 27
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-28
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9E
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227d
  Name: 1/1/28
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 28
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-29
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9F
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227e
  Name: 1/1/29
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 29
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-30
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:A0
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227f
  Name: 1/1/30
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 30
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-31
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:A1
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02280
  Name: 1/1/31
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 31
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-32
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:A2
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02281
  Name: 1/1/32
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 32
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-33
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: 00:00:00:00:00:00
  Mode: access
  ModuleId: 1
  Moid: 632b1fcc6373582d42a023ab
  Name: 1/1/33
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 33
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-1
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C3
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5abe
  Name: 1/1/1
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b19af76752d3236316ea9
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1287
  PortId: 1
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-2
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C4
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5abf
  Name: 1/1/2
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b19af76752d3236316eaa
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1287
  PortId: 2
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-3
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C5
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac0
  Name: 1/1/3
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 3
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-4
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C6
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac1
  Name: 1/1/4
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 4
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-5
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C7
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac2
  Name: 1/1/5
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188b76752d3236311bb7
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1284
  PortId: 5
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-6
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C8
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac3
  Name: 1/1/6
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188b76752d3236311bbe
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1284
  PortId: 6
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-7
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C9
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac4
  Name: 1/1/7
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 7
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-8
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CA
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac5
  Name: 1/1/8
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 8
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-9
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CB
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac6
  Name: 1/1/9
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188d76752d3236311cc3
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1285
  PortId: 9
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-10
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CC
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac7
  Name: 1/1/10
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b188d76752d3236311cc4
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1285
  PortId: 10
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-11
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CD
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac8
  Name: 1/1/11
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 11
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-12
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CE
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac9
  Name: 1/1/12
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 12
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-13
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CF
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5aca
  Name: 1/1/13
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b189176752d3236311ee1
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1286
  PortId: 13
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-14
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D0
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5acb
  Name: 1/1/14
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInterfaceId: 632b189176752d3236311ee2
  PeerInterfaceType: adapter.ExtEthInterface
  PortChannelId: 1286
  PortId: 14
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-15
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D1
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5acc
  Name: 1/1/15
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 15
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-16
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D2
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5acd
  Name: 1/1/16
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 16
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-17
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D3
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ace
  Name: 1/1/17
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 17
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-18
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D4
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5acf
  Name: 1/1/18
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 18
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-19
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D5
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad0
  Name: 1/1/19
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 19
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-20
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D6
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad1
  Name: 1/1/20
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 20
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-21
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D7
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad2
  Name: 1/1/21
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 21
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-22
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D8
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad3
  Name: 1/1/22
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 22
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-23
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D9
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad4
  Name: 1/1/23
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 23
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-24
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DA
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad5
  Name: 1/1/24
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 24
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-25
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DB
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad6
  Name: 1/1/25
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 25
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-26
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DC
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad7
  Name: 1/1/26
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 26
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-27
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DD
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad8
  Name: 1/1/27
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 27
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-28
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DE
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad9
  Name: 1/1/28
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 28
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-29
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DF
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ada
  Name: 1/1/29
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 29
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-30
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:E0
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5adb
  Name: 1/1/30
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 30
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-31
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:E1
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5adc
  Name: 1/1/31
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 31
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-32
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:E2
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5add
  Name: 1/1/32
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 32
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-33
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: 00:00:00:00:00:00
  Mode: access
  ModuleId: 1
  Moid: 632c6acd6373582d415a8b96
  Name: 1/1/33
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PortChannelId: 0
  PortId: 33
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
IfmInfo:
- ConnectionPath: B
  ConnectionStatus: B
  Description: Cisco UCS 9108-25G 8 Port IFM
  Dn: chassis-1-ioc-1
  FanMoids:
  - 632b178c76752d323630ceca
  - 632b178c76752d323630ced9
  - 632b178c76752d323630cee8
  HostPortCount: 33
  HostPortSummary: 0/33
  HostPortUp: 0
  HostPorts:
  - 632b175c6373582d42a02271
  - 632b175c6373582d42a02275
  - 632b175c6373582d42a0227a
  - 632b175c6373582d42a0227d
  - 632b175c6373582d42a02280
  - 632b175c6373582d42a02277
  - 632b175c6373582d42a02272
  - 632b175c6373582d42a0227b
  - 632b175c6373582d42a02286
  - 632b175c6373582d42a02289
  - 632b175c6373582d42a02270
  - 632b175c6373582d42a02274
  - 632b175c6373582d42a02278
  - 632b175c6373582d42a0228b
  - 632b175c6373582d42a0226d
  - 632b175c6373582d42a0226e
  - 632b175c6373582d42a02276
  - 632b175c6373582d42a0227c
  - 632b175c6373582d42a02284
  - 632b175c6373582d42a0226f
  - 632b175c6373582d42a0227f
  - 632b175c6373582d42a02281
  - 632b175c6373582d42a02288
  - 632b175c6373582d42a02273
  - 632b175c6373582d42a02279
  - 632b175c6373582d42a0227e
  - 632b175c6373582d42a02282
  - 632b175c6373582d42a02287
  - 632b175c6373582d42a0228a
  - 632b175c6373582d42a0226c
  - 632b175c6373582d42a02283
  - 632b175c6373582d42a02285
  - 632b1fcc6373582d42a023ab
  ManagementCidr: 10.90.90.49/24
  ManagementGateway: 10.90.89.1
  ManagementIp: 10.90.90.49
  ManagementPrefix: 24
  ManagementSubnet: 255.255.255.0
  ManagementVlan: 89
  Model: UCSX-I-9108-25G
  ModuleId: 1
  Moid: 632b13c976752d32362fc244
  Name: 'IFM #1 (top)'
  NetworkPortCount: 4
  NetworkPortMax: 8
  NetworkPortSummary: 4/4/8
  NetworkPortUp: 4
  NetworkPorts:
  - 632b13c976752d32362fc25a
  - 632c81ec76752d32369daa08
  - 632c81f276752d32369dac8d
  - 632c820576752d32369db290
  'On': true
  OperState: OK
  PartNumber: 73-20533-03
  Pid: UCSX-I-9108-25G
  Presence: equipped
  ProductName: Cisco UCS 9108-25G
  Serial: FCH261770KU
  Side: top
  Version: 4.2(2c)
- ConnectionPath: A
  ConnectionStatus: A
  Description: Cisco UCS 9108-25G 8 Port IFM
  Dn: chassis-1-ioc-2
  FanMoids:
  - 632b15b576752d3236304d3d
  - 632b15b576752d3236304d58
  - 632b15b576752d3236304d6f
  HostPortCount: 33
  HostPortSummary: 0/33
  HostPortUp: 0
  HostPorts:
  - 632b158c6373582d415a5ad6
  - 632b158c6373582d415a5ac0
  - 632b158c6373582d415a5acc
  - 632b158c6373582d415a5abf
  - 632b158c6373582d415a5ac6
  - 632b158c6373582d415a5ac7
  - 632b158c6373582d415a5ad4
  - 632b158c6373582d415a5ad8
  - 632b158c6373582d415a5ac1
  - 632b158c6373582d415a5ac4
  - 632b158c6373582d415a5acf
  - 632b158c6373582d415a5ad2
  - 632b158c6373582d415a5ad3
  - 632b158c6373582d415a5ac9
  - 632b158c6373582d415a5ad5
  - 632b158c6373582d415a5adb
  - 632b158c6373582d415a5ac2
  - 632b158c6373582d415a5ac8
  - 632b158c6373582d415a5add
  - 632b158c6373582d415a5aca
  - 632b158c6373582d415a5acb
  - 632b158c6373582d415a5acd
  - 632b158c6373582d415a5ace
  - 632b158c6373582d415a5ac5
  - 632b158c6373582d415a5ac3
  - 632b158c6373582d415a5ad0
  - 632b158c6373582d415a5adc
  - 632b158c6373582d415a5ad7
  - 632b158c6373582d415a5abe
  - 632b158c6373582d415a5ad1
  - 632b158c6373582d415a5ad9
  - 632b158c6373582d415a5ada
  - 632c6acd6373582d415a8b96
  ManagementCidr: 10.90.90.48/24
  ManagementGateway: 10.90.89.1
  ManagementIp: 10.90.90.48
  ManagementPrefix: 24
  ManagementSubnet: 255.255.255.0
  ManagementVlan: 89
  Model: UCSX-I-9108-25G
  ModuleId: 2
  Moid: 632b13c876752d32362fc17c
  Name: 'IFM #2 (bottom)'
  NetworkPortCount: 4
  NetworkPortMax: 8
  NetworkPortSummary: 4/4/8
  NetworkPortUp: 4
  NetworkPorts:
  - 632b13c876752d32362fc189
  - 632c81e776752d32369da82f
  - 632c81ed76752d32369daa9c
  - 632c81fe76752d32369db10a
  'On': true
  OperState: OK
  PartNumber: 73-20533-03
  Pid: UCSX-I-9108-25G
  Presence: equipped
  ProductName: Cisco UCS 9108-25G
  Serial: FCH261770RN
  Side: bottom
  Version: 4.2(2c)
NetworkPortInfo:
- Dn: chassis-1-ioc-1-slot-1-port-1
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632b13c976752d32362fc25a
  Name: 1/1
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a64
  PeerInterfaceType: ether.PhysicalPort
  PortId: 1
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-1-slot-1-port-2
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632c81ec76752d32369daa08
  Name: 1/2
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a6a
  PeerInterfaceType: ether.PhysicalPort
  PortId: 2
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-1-slot-1-port-3
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632c81f276752d32369dac8d
  Name: 1/3
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a14
  PeerInterfaceType: ether.PhysicalPort
  PortId: 3
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-1-slot-1-port-4
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632c820576752d32369db290
  Name: 1/4
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a6c
  PeerInterfaceType: ether.PhysicalPort
  PortId: 4
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-1
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632b13c876752d32362fc189
  Name: 2/1
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd9923
  PeerInterfaceType: ether.PhysicalPort
  PortId: 1
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-2
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632c81e776752d32369da82f
  Name: 2/2
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd98da
  PeerInterfaceType: ether.PhysicalPort
  PortId: 2
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-3
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632c81ed76752d32369daa9c
  Name: 2/3
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd98dd
  PeerInterfaceType: ether.PhysicalPort
  PortId: 3
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-4
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632c81fe76752d32369db10a
  Name: 2/4
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd98d0
  PeerInterfaceType: ether.PhysicalPort
  PortId: 4
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
```

## Developer output

```
# iserver get chassis --serial FOX2611PPHP -m .

Developer output

{
    "duration": 6535,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 5921
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 2136
    }
}

Log: debug
-----------

[2022-11-17 10:15:20.603698]	[chassis_info.get]	{
    "Chassis": {
        "ConnectionPath": "A,B",
        "ConnectionStatus": "A,B",
        "Description": "Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots",
        "Dn": "chassis-1",
        "DeviceMoId": "632999466f72612d39b26942",
        "Moid": "632b13c876752d32362fc175",
        "Model": "UCSX-9508",
        "Name": "ucsX-1",
        "OperState": "OK",
        "PartNumber": "68-6847-03",
        "Pid": "UCSX-9508",
        "ProductName": "Cisco UCSX 9508 Chassis",
        "Serial": "FOX2611PPHP",
        "Sku": "UCSX-9508",
        "Vendor": "Cisco Systems Inc",
        "Health": "Warnings",
        "HealthSummary": "Warnings (2)",
        "AlarmWarning": 2,
        "AlarmCritical": 0,
        "ConnectionSummary": "A,B / A,B",
        "NodeMax": 8,
        "IfmMax": 2,
        "FanModuleMax": 4,
        "FanMax": 8,
        "PsuMax": 6,
        "IfmOn": 2,
        "IfmCount": 2,
        "IfmSummary": "2/2/2",
        "HostPortCount": 66,
        "HostPortUp": 0,
        "HostPortSummary": "0/66",
        "NetworkPortUp": 8,
        "NetworkPortCount": 8,
        "NetworkPortMax": 16,
        "NetworkPortSummary": "8/8/16"
    },
    "IfmInfo": [
        {
            "Moid": "632b13c976752d32362fc244",
            "Dn": "chassis-1-ioc-1",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "B",
            "ConnectionStatus": "B",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.49",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.49/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b178c76752d323630ceca",
                "632b178c76752d323630ced9",
                "632b178c76752d323630cee8"
            ],
            "HostPorts": [
                "632b175c6373582d42a02271",
                "632b175c6373582d42a02275",
                "632b175c6373582d42a0227a",
                "632b175c6373582d42a0227d",
                "632b175c6373582d42a02280",
                "632b175c6373582d42a02277",
                "632b175c6373582d42a02272",
                "632b175c6373582d42a0227b",
                "632b175c6373582d42a02286",
                "632b175c6373582d42a02289",
                "632b175c6373582d42a02270",
                "632b175c6373582d42a02274",
                "632b175c6373582d42a02278",
                "632b175c6373582d42a0228b",
                "632b175c6373582d42a0226d",
                "632b175c6373582d42a0226e",
                "632b175c6373582d42a02276",
                "632b175c6373582d42a0227c",
                "632b175c6373582d42a02284",
                "632b175c6373582d42a0226f",
                "632b175c6373582d42a0227f",
                "632b175c6373582d42a02281",
                "632b175c6373582d42a02288",
                "632b175c6373582d42a02273",
                "632b175c6373582d42a02279",
                "632b175c6373582d42a0227e",
                "632b175c6373582d42a02282",
                "632b175c6373582d42a02287",
                "632b175c6373582d42a0228a",
                "632b175c6373582d42a0226c",
                "632b175c6373582d42a02283",
                "632b175c6373582d42a02285",
                "632b1fcc6373582d42a023ab"
            ],
            "NetworkPorts": [
                "632b13c976752d32362fc25a",
                "632c81ec76752d32369daa08",
                "632c81f276752d32369dac8d",
                "632c820576752d32369db290"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #1 (top)",
            "ModuleId": 1,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770KU",
            "Side": "top",
            "Version": "4.2(2c)",
            "HostPortCount": 33,
            "HostPortUp": 0,
            "HostPortSummary": "0/33",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        },
        {
            "Moid": "632b13c876752d32362fc17c",
            "Dn": "chassis-1-ioc-2",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "A",
            "ConnectionStatus": "A",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.48",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.48/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b15b576752d3236304d3d",
                "632b15b576752d3236304d58",
                "632b15b576752d3236304d6f"
            ],
            "HostPorts": [
                "632b158c6373582d415a5ad6",
                "632b158c6373582d415a5ac0",
                "632b158c6373582d415a5acc",
                "632b158c6373582d415a5abf",
                "632b158c6373582d415a5ac6",
                "632b158c6373582d415a5ac7",
                "632b158c6373582d415a5ad4",
                "632b158c6373582d415a5ad8",
                "632b158c6373582d415a5ac1",
                "632b158c6373582d415a5ac4",
                "632b158c6373582d415a5acf",
                "632b158c6373582d415a5ad2",
                "632b158c6373582d415a5ad3",
                "632b158c6373582d415a5ac9",
                "632b158c6373582d415a5ad5",
                "632b158c6373582d415a5adb",
                "632b158c6373582d415a5ac2",
                "632b158c6373582d415a5ac8",
                "632b158c6373582d415a5add",
                "632b158c6373582d415a5aca",
                "632b158c6373582d415a5acb",
                "632b158c6373582d415a5acd",
                "632b158c6373582d415a5ace",
                "632b158c6373582d415a5ac5",
                "632b158c6373582d415a5ac3",
                "632b158c6373582d415a5ad0",
                "632b158c6373582d415a5adc",
                "632b158c6373582d415a5ad7",
                "632b158c6373582d415a5abe",
                "632b158c6373582d415a5ad1",
                "632b158c6373582d415a5ad9",
                "632b158c6373582d415a5ada",
                "632c6acd6373582d415a8b96"
            ],
            "NetworkPorts": [
                "632b13c876752d32362fc189",
                "632c81e776752d32369da82f",
                "632c81ed76752d32369daa9c",
                "632c81fe76752d32369db10a"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #2 (bottom)",
            "ModuleId": 2,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770RN",
            "Side": "bottom",
            "Version": "4.2(2c)",
            "HostPortCount": 33,
            "HostPortUp": 0,
            "HostPortSummary": "0/33",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        }
    ],
    "HostPortInfo": [
        {
            "Moid": "632b175c6373582d42a02282",
            "Dn": "chassis-1-ioc-1-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:83",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eab",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02283",
            "Dn": "chassis-1-ioc-1-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:84",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eac",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02284",
            "Dn": "chassis-1-ioc-1-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:85",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02285",
            "Dn": "chassis-1-ioc-1-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:86",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02286",
            "Dn": "chassis-1-ioc-1-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:87",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc0",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02287",
            "Dn": "chassis-1-ioc-1-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:88",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02288",
            "Dn": "chassis-1-ioc-1-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:89",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02289",
            "Dn": "chassis-1-ioc-1-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0228a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8B",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0228b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8C",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc6",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8F",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0226f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:90",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02270",
            "Dn": "chassis-1-ioc-1-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:91",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02271",
            "Dn": "chassis-1-ioc-1-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:92",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02272",
            "Dn": "chassis-1-ioc-1-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:93",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02273",
            "Dn": "chassis-1-ioc-1-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:94",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02274",
            "Dn": "chassis-1-ioc-1-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:95",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02275",
            "Dn": "chassis-1-ioc-1-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:96",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02276",
            "Dn": "chassis-1-ioc-1-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:97",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02277",
            "Dn": "chassis-1-ioc-1-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:98",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02278",
            "Dn": "chassis-1-ioc-1-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:99",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02279",
            "Dn": "chassis-1-ioc-1-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9B",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9C",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9F",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a0227f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02280",
            "Dn": "chassis-1-ioc-1-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b175c6373582d42a02281",
            "Dn": "chassis-1-ioc-1-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b1fcc6373582d42a023ab",
            "Dn": "chassis-1-ioc-1-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b158c6373582d415a5abe",
            "Dn": "chassis-1-ioc-2-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C3",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316ea9",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5abf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C4",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eaa",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C7",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bb7",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C8",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bbe",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CB",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CC",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5aca",
            "Dn": "chassis-1-ioc-2-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CF",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee1",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D0",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee2",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acd",
            "Dn": "chassis-1-ioc-2-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ace",
            "Dn": "chassis-1-ioc-2-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D3",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5acf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D4",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D7",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D8",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DB",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DC",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ad9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ada",
            "Dn": "chassis-1-ioc-2-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DF",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5adb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5adc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632b158c6373582d415a5add",
            "Dn": "chassis-1-ioc-2-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c6acd6373582d415a8b96",
            "Dn": "chassis-1-ioc-2-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        }
    ],
    "NetworkPortInfo": [
        {
            "Moid": "632b13c976752d32362fc25a",
            "Dn": "chassis-1-ioc-1-slot-1-port-1",
            "Name": "1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a64",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632c81ec76752d32369daa08",
            "Dn": "chassis-1-ioc-1-slot-1-port-2",
            "Name": "1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6a",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632c81f276752d32369dac8d",
            "Dn": "chassis-1-ioc-1-slot-1-port-3",
            "Name": "1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a14",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632c820576752d32369db290",
            "Dn": "chassis-1-ioc-1-slot-1-port-4",
            "Name": "1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6c",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1
        },
        {
            "Moid": "632b13c876752d32362fc189",
            "Dn": "chassis-1-ioc-2-slot-2-port-1",
            "Name": "2/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd9923",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c81e776752d32369da82f",
            "Dn": "chassis-1-ioc-2-slot-2-port-2",
            "Name": "2/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98da",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c81ed76752d32369daa9c",
            "Dn": "chassis-1-ioc-2-slot-2-port-3",
            "Name": "2/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98dd",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        },
        {
            "Moid": "632c81fe76752d32369db10a",
            "Dn": "chassis-1-ioc-2-slot-2-port-4",
            "Name": "2/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98d0",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2
        }
    ]
}


Log: isctl
-----------

2022-11-17 10:15:16.063919	True	1420	2	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2022-11-17 10:15:17.291423	True	1223	2	isctl get equipment iocard --filter "Parent/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
2022-11-17 10:15:19.194208	True	1899	66	isctl get ether hostport --filter "EquipmentIoCardBase/Moid in ('632b13c876752d32362fc17c', '632b13c976752d32362fc244')"  -o json --top 100
2022-11-17 10:15:20.587034	True	1379	8	isctl get ether networkport --filter "EquipmentIoCardBase/Moid in ('632b13c876752d32362fc17c', '632b13c976752d32362fc244')"  -o json --top 100
```