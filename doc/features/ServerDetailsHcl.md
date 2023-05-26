# Server Details - HCL

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --hcl

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

HCL Status
----------
- Overall : Not-Listed


HCL - Server Hardware Compliance
--------------------------------
- Status   : Validated
- Model    : UCSC-C240-M5SN
- CPU      : Intel Xeon Processor Scalable Family
- Firmware : 4.2(2)


HCL - Server Software Compliance
--------------------------------
- Status     : Validated
- Reason     : Incompatible-Components
- OS Vendor  : VMware
- OS Version : ESXi 7.0 U3


HCL - Adapter Compliance
------------------------
- Status : Not-Listed
- Reason : Incompatible-Components


+------------+------------+---------------------+---------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| Status     | Hardware   | Software            | Reason              | Model                                                            | Cimc Version | Driver Name | Driver Version | Firmware Version   |
+------------+------------+---------------------+---------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| Not-Listed | Compatible | Incompatible-Driver | Incompatible-Driver | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
| Not-Listed | Compatible | Incompatible-Driver | Incompatible-Driver | Cisco(R) LOM X550-T2                                             | 4.2(2)       | ixgben      | 1.12.3.0       | 0x800016F9-1.826.0 | 
| Validated  | Compatible | Compatible          | Compatible          | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(2)       | lsi_mr3     | 7.718.02.00    | 51.19.0-4296       | 
| Validated  | Compatible | Compatible          | Compatible          | UCSC-MLOM-C25Q-04                                                | 4.2(2)       | nenic       | 1.0.42.0       | 5.2(2)             | 
| Not-Listed | Compatible | Incompatible-Driver | Incompatible-Driver | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
+------------+------------+---------------------+---------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --hcl

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
    "HclInfo": {
        "__Output": {
            "Status": "Yellow",
            "SoftwareStatus": "Green",
            "HardwareStatus": "Green",
            "ComponentStatus": "Yellow"
        },
        "ComponentStatus": "Not-Listed",
        "HardwareStatus": "Validated",
        "HclFirmwareVersion": "4.2(2)",
        "HclModel": "UCSC-C240-M5SN",
        "HclOsVendor": "VMware",
        "HclOsVersion": "ESXi 7.0 U3",
        "HclProcessor": "Intel Xeon Processor Scalable Family",
        "Moid": "5fdf9c0673736f2d31c2a581",
        "Reason": "Incompatible-Components",
        "ServerReason": "Incompatible-Components",
        "SoftwareStatus": "Validated",
        "Status": "Not-Listed",
        "Details": [
            {
                "__Output": {
                    "Status": "Yellow"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "i40en",
                "HclDriverVersion": "2.2.7.0",
                "HclFirmwareVersion": "0x8000B900-1.826.0",
                "HclModel": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
                "Reason": "Incompatible-Driver",
                "SoftwareStatus": "Incompatible-Driver",
                "Status": "Not-Listed",
                "Moid": "6396f6ec73736f2d318a9a3f"
            },
            {
                "__Output": {
                    "Status": "Yellow"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "ixgben",
                "HclDriverVersion": "1.12.3.0",
                "HclFirmwareVersion": "0x800016F9-1.826.0",
                "HclModel": "Cisco(R) LOM X550-T2",
                "Reason": "Incompatible-Driver",
                "SoftwareStatus": "Incompatible-Driver",
                "Status": "Not-Listed",
                "Moid": "6396f6ec73736f2d318a9a40"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "lsi_mr3",
                "HclDriverVersion": "7.718.02.00",
                "HclFirmwareVersion": "51.19.0-4296",
                "HclModel": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
                "Reason": "Compatible",
                "SoftwareStatus": "Compatible",
                "Status": "Validated",
                "Moid": "6396f6ec73736f2d318a9a41"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "nenic",
                "HclDriverVersion": "1.0.42.0",
                "HclFirmwareVersion": "5.2(2)",
                "HclModel": "UCSC-MLOM-C25Q-04",
                "Reason": "Compatible",
                "SoftwareStatus": "Compatible",
                "Status": "Validated",
                "Moid": "6396f6ec73736f2d318a9a3d"
            },
            {
                "__Output": {
                    "Status": "Yellow"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "i40en",
                "HclDriverVersion": "2.2.7.0",
                "HclFirmwareVersion": "0x8000B900-1.826.0",
                "HclModel": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
                "Reason": "Incompatible-Driver",
                "SoftwareStatus": "Incompatible-Driver",
                "Status": "Not-Listed",
                "Moid": "6396f6ec73736f2d318a9a3e"
            }
        ]
    },
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --hcl

Developer output

{
    "duration": 15661,
    "isctl": {
        "read": true,
        "calls": 7,
        "success": 7,
        "failed": 0,
        "total_time": 12018
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

2023-01-05 18:49:03.506686	True	3005	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:49:05.434254	True	1926	10	isctl get compute blade   -o json --top 100
2023-01-05 18:49:09.731931	True	1386	1	isctl get cond hclstatus --filter "ManagedObject/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:49:11.434538	True	1700	5	isctl get cond hclstatusdetail --filter "HclStatus/Moid eq '5fdf9c0673736f2d31c2a581'"  -o json --top 100
2023-01-05 18:49:12.678840	True	1241	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:49:14.100018	True	1418	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:49:15.454984	True	1342	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:49:14.000Z"  -o json --top 100
```
