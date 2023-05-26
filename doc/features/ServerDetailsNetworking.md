# Server Details - Networking

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --net

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

+--------------+---------+--------------------------------------------+-------------+-------------------+-----+-----+-----+
| Name         | PciSlot | Model                                      | Serial      | Vendor            | Eth | HBA | DCE |
+--------------+---------+--------------------------------------------+-------------+-------------------+-----+-----+-----+
| Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 |             |                   | 2   | 0   | 0   | 
| Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 |             |                   | 2   | 0   | 0   | 
| Adapter L    | L       | Cisco(R) LOM X550-T2                       |             |                   | 2   | 0   | 0   | 
| Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | FCH24157D1V | Cisco Systems Inc | 4   | 4   | 4   | 
+--------------+---------+--------------------------------------------+-------------+-------------------+-----+-----+-----+

+----------------------------------------+---------------+-------------------+
| Adapter Dn                             | DCE Interface | MAC Address       |
+----------------------------------------+---------------+-------------------+
| sys/rack-unit-1/adaptor-MLOM/ext-eth-0 | 0             | 3C:57:31:CC:0E:3E | 
| sys/rack-unit-1/adaptor-MLOM/ext-eth-1 | 1             | 3C:57:31:CC:0E:40 | 
| sys/rack-unit-1/adaptor-MLOM/ext-eth-2 | 2             | 3C:57:31:CC:0E:3F | 
| sys/rack-unit-1/adaptor-MLOM/ext-eth-3 | 3             | 3C:57:31:CC:0E:41 | 
+----------------------------------------+---------------+-------------------+

+--------------+----------------+-------------------+
| Adapter Name | Interface Name | MAC Address       |
+--------------+----------------+-------------------+
| Adapter 3    | eth-1          | 3c:fd:fe:ee:2c:30 | 
| Adapter 3    | eth-2          | 3c:fd:fe:ee:2c:31 | 
| Adapter 6    | eth-1          | 3c:fd:fe:ee:2d:60 | 
| Adapter 6    | eth-2          | 3c:fd:fe:ee:2d:61 | 
| Adapter L    | eth-1          | 5c:71:0d:26:37:b2 | 
| Adapter L    | eth-2          | 5c:71:0d:26:37:b3 | 
| Adapter MLOM | eth0           | 3C:57:31:CC:0E:46 | 
| Adapter MLOM | eth1           | 3C:57:31:CC:0E:47 | 
| Adapter MLOM | eth2           | 3C:57:31:CC:0E:48 | 
| Adapter MLOM | eth3           | 3C:57:31:CC:0E:49 | 
+--------------+----------------+-------------------+

+--------------+----------------+-------------------------+-------------------------+
| Adapter Name | Interface Name | WWNN                    | WWPN                    |
+--------------+----------------+-------------------------+-------------------------+
| Adapter MLOM | fc0            | 10:00:3C:57:31:CC:0E:4A | 20:00:3C:57:31:CC:0E:4A | 
| Adapter MLOM | fc1            | 10:00:3C:57:31:CC:0E:4B | 20:00:3C:57:31:CC:0E:4B | 
| Adapter MLOM | fc2            | 10:00:3C:57:31:CC:0E:4C | 20:00:3C:57:31:CC:0E:4C | 
| Adapter MLOM | fc3            | 10:00:3C:57:31:CC:0E:4D | 20:00:3C:57:31:CC:0E:4D | 
+--------------+----------------+-------------------------+-------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --net

{
    "__Output": {
        "FlagState": ":GG.G",
        "FlagManagement": ":GGY",
        "FlagWorkflow": ":GG"
    },
    "Moid": "5fdf9c016176752d35e44795",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Model": "UCSC-C240-M5SN",
    "Serial": "WZP23400AJW",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "Groups": "p2b,pod2b,power",
    "AlarmSummary": {
        "__Output": {
            "Critical": "Red",
            "Warning": "Yellow",
            "Info": "Blue",
            "Cleared": "Green"
        },
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "LocatorLedOn": false,
    "ManagementIp": "10.58.50.41",
    "Redfish": {
        "Capable": true,
        "Enabled": true
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "AvailableMemory": 393216,
    "TotalMemory": 393216,
    "UsedMemory": 0,
    "TotalMemoryUnit": "384 [GiB]",
    "TotalMemoryGB": 384,
    "AvailableMemoryUnit": "384 [GiB]",
    "AvailableMemoryGB": 384,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "AdaptersInfo": [
        {
            "Moid": "5fdf9c886176752d35e477ea",
            "Dn": "sys/rack-unit-1/network-adapter-3",
            "AdapterId": "3",
            "Name": "Adapter 3",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [],
            "ExtEthIfsCount": 0,
            "HostEthIfsIds": [
                "5fdf9c8a6176752d35e478e5",
                "5fdf9c8a6176752d35e478f4"
            ],
            "HostEthIfsCount": 2,
            "HostFcIfsIds": [],
            "HostFcIfsCount": 0,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "3",
            "Thermal": "",
            "Serial": "",
            "Vendor": ""
        },
        {
            "Moid": "5fdf9c886176752d35e477e4",
            "Dn": "sys/rack-unit-1/network-adapter-6",
            "AdapterId": "6",
            "Name": "Adapter 6",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [],
            "ExtEthIfsCount": 0,
            "HostEthIfsIds": [
                "5fdf9c8a6176752d35e478da",
                "5fdf9c8a6176752d35e478e1"
            ],
            "HostEthIfsCount": 2,
            "HostFcIfsIds": [],
            "HostFcIfsCount": 0,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "6",
            "Thermal": "",
            "Serial": "",
            "Vendor": ""
        },
        {
            "Moid": "5fdf9c886176752d35e477f0",
            "Dn": "sys/rack-unit-1/network-adapter-L",
            "AdapterId": "L",
            "Name": "Adapter L",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [],
            "ExtEthIfsCount": 0,
            "HostEthIfsIds": [
                "5fdf9c8a6176752d35e478f6",
                "5fdf9c8a6176752d35e478fb"
            ],
            "HostEthIfsCount": 2,
            "HostFcIfsIds": [],
            "HostFcIfsCount": 0,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "Cisco(R) LOM X550-T2",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "L",
            "Thermal": "",
            "Serial": "",
            "Vendor": ""
        },
        {
            "Moid": "5fdf9bf46176752d35e4426e",
            "Dn": "sys/rack-unit-1/adaptor-MLOM",
            "AdapterId": "MLOM",
            "Name": "Adapter MLOM",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [
                "5fff44fd6176752d3566f25c",
                "5fff44fd6176752d3566f25e",
                "5fff44fd6176752d3566f260",
                "5fff44fd6176752d3566f262"
            ],
            "ExtEthIfsCount": 4,
            "HostEthIfsIds": [
                "6358db4d76752d3139b6e4c9",
                "6358db5276752d3139b6e5c9",
                "6358db5276752d3139b6e5cb",
                "6358db5276752d3139b6e5cd"
            ],
            "HostEthIfsCount": 4,
            "HostFcIfsIds": [
                "6390087976752d313914f241",
                "6390087976752d313914f243",
                "6390087976752d313914f245",
                "6390087976752d313914f247"
            ],
            "HostFcIfsCount": 4,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "UCSC-MLOM-C25Q-04",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "MLOM",
            "Thermal": "",
            "Serial": "FCH24157D1V",
            "Vendor": "Cisco Systems Inc"
        }
    ],
    "ExtEthInfo": [
        {
            "Moid": "5fff44fd6176752d3566f25c",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-0",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "0",
            "MacAddress": "3C:57:31:CC:0E:3E",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        },
        {
            "Moid": "5fff44fd6176752d3566f25e",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-1",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "1",
            "MacAddress": "3C:57:31:CC:0E:40",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        },
        {
            "Moid": "5fff44fd6176752d3566f260",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-2",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "2",
            "MacAddress": "3C:57:31:CC:0E:3F",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        },
        {
            "Moid": "5fff44fd6176752d3566f262",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-3",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "3",
            "MacAddress": "3C:57:31:CC:0E:41",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        }
    ],
    "HostEthInfo": [
        {
            "Moid": "5fdf9c8a6176752d35e478e5",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-3/eth-1",
            "AdapterUnitId": "5fdf9c886176752d35e477ea",
            "AdminState": "",
            "HostEthInterfaceId": 1,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2c:30",
            "Name": "eth-1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 3",
            "AdapterPciSlot": "3"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478f4",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-3/eth-2",
            "AdapterUnitId": "5fdf9c886176752d35e477ea",
            "AdminState": "",
            "HostEthInterfaceId": 2,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2c:31",
            "Name": "eth-2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 3",
            "AdapterPciSlot": "3"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478da",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-6/eth-1",
            "AdapterUnitId": "5fdf9c886176752d35e477e4",
            "AdminState": "",
            "HostEthInterfaceId": 1,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2d:60",
            "Name": "eth-1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 6",
            "AdapterPciSlot": "6"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478e1",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-6/eth-2",
            "AdapterUnitId": "5fdf9c886176752d35e477e4",
            "AdminState": "",
            "HostEthInterfaceId": 2,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2d:61",
            "Name": "eth-2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 6",
            "AdapterPciSlot": "6"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478f6",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-L/eth-1",
            "AdapterUnitId": "5fdf9c886176752d35e477f0",
            "AdminState": "",
            "HostEthInterfaceId": 1,
            "InterfaceType": "",
            "MacAddress": "5c:71:0d:26:37:b2",
            "Name": "eth-1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter L",
            "AdapterPciSlot": "L"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478fb",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-L/eth-2",
            "AdapterUnitId": "5fdf9c886176752d35e477f0",
            "AdminState": "",
            "HostEthInterfaceId": 2,
            "InterfaceType": "",
            "MacAddress": "5c:71:0d:26:37:b3",
            "Name": "eth-2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter L",
            "AdapterPciSlot": "L"
        },
        {
            "Moid": "6358db4d76752d3139b6e4c9",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth0",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:46",
            "Name": "eth0",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6358db5276752d3139b6e5c9",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth1",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:47",
            "Name": "eth1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6358db5276752d3139b6e5cb",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth2",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:48",
            "Name": "eth2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6358db5276752d3139b6e5cd",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth3",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:49",
            "Name": "eth3",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        }
    ],
    "HostFcInfo": [
        {
            "Moid": "6390087976752d313914f241",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc0",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc0",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4A",
            "Wwpn": "20:00:3C:57:31:CC:0E:4A",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6390087976752d313914f243",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc1",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc1",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4B",
            "Wwpn": "20:00:3C:57:31:CC:0E:4B",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6390087976752d313914f245",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc2",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc2",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4C",
            "Wwpn": "20:00:3C:57:31:CC:0E:4C",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6390087976752d313914f247",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc3",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc3",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4D",
            "Wwpn": "20:00:3C:57:31:CC:0E:4D",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        }
    ],
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": "63b5c955696f6e2d30bd0bfb",
        "Last": [
            {
                "__Output": {
                    "Status": "Green"
                },
                "Moid": "63b5c955696f6e2d30bd0bfb",
                "Name": "Turn Off Locator",
                "Progress": 100,
                "CreateTime": "2023-01-04T18:45:41.509Z",
                "StartTime": "2023-01-04T18:45:41.741Z",
                "EndTime": "2023-01-04T18:45:45.353Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1672854341509,
                "StartTimeEpoch": 1672854341741,
                "EndTimeEpoch": 1672854345353,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:04"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "Moid": "63b5c923696f6e2d30bd0b5d",
                "Name": "Turn On Locator",
                "Progress": 100,
                "CreateTime": "2023-01-04T18:44:51.803Z",
                "StartTime": "2023-01-04T18:44:52.467Z",
                "EndTime": "2023-01-04T18:44:57.964Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1672854291803,
                "StartTimeEpoch": 1672854292467,
                "EndTimeEpoch": 1672854297964,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:05"
            }
        ]
    },
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "C2"
}
```

Developer output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --net

Developer output

{
    "duration": 19539,
    "isctl": {
        "read": true,
        "calls": 9,
        "success": 9,
        "failed": 0,
        "total_time": 15657
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
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
        "lines": 466
    }
}

Log: isctl
-----------

2023-01-05 18:50:17.113854	True	3154	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:50:18.597047	True	1482	10	isctl get compute blade   -o json --top 100
2023-01-05 18:50:23.215855	True	1523	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:50:24.936353	True	1718	4	isctl get adapter unit --filter "Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:50:26.639458	True	1699	4	isctl get adapter extethinterface --filter "AdapterUnit/Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:50:28.378421	True	1727	10	isctl get adapter hostethinterface --filter "AdapterUnit/Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:50:29.980041	True	1596	4	isctl get adapter hostfcinterface --filter "AdapterUnit/Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:50:31.331799	True	1332	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:50:32.765690	True	1426	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:50:31.000Z"  -o json --top 100
```
