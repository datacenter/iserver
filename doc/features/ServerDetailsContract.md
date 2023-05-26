# Server Details - Contract

```
# iserver get server --name esx93-eu-spdc-FCH2108V1HE --contract

+------+-----+---------+---------------------------+-------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                      | Model             | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+---------------------------+-------------------+-------------+-------------+------------+-----------+
| P+ H | Cri |         | esx93-eu-spdc-FCH2108V1HE | (R) UCSC-C220-M4S | FCH2108V1HE | 10.58.25.35 | 2S 28C 56T | 256 [GiB] | 
+------+-----+---------+---------------------------+-------------------+-------------+-------------+------------+-----------+

Contract Coverage
-----------------
- Contract Status       : Active
- Contract Number       : 202440144
- Start Date            : 2022-10-28T00:00:00Z
- End Date              : 2024-02-29T00:00:00Z
- Last Updated          : 2023-01-04T18:14:11.021Z
- Service Description   : SNTC 8X5XNBD
- Service Level         : SNT
- Service Sku           : CON-SNT-C220M4S
- Purchase Order Number : 6240050238
- Sales Order Number    : 104064129
```

JSON output

```
# iserver get server --name esx93-eu-spdc-FCH2108V1HE --contract

{
    "__Output": {
        "FlagState": ":GG.G",
        "FlagManagement": ":GYY",
        "FlagWorkflow": ":"
    },
    "Moid": "6141c32376752d313775f536",
    "DeviceMoId": "6141c3186f72612d30d2d8f8",
    "Name": "esx93-eu-spdc-FCH2108V1HE",
    "Model": "UCSC-C220-M4S",
    "Serial": "FCH2108V1HE",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C220-M4S",
    "ContractInfo": {
        "__Output": {
            "ContractStatus": "Green"
        },
        "Moid": "6141c3196265722d30bb3ec0",
        "PurchaseOrderNumber": "6240050238",
        "SalesOrderNumber": "104064129",
        "ContractStatus": "Active",
        "ContractNumber": "202440144",
        "ContractUpdatedTime": "2023-01-04T18:14:11.021Z",
        "ServiceDescription": "SNTC 8X5XNBD",
        "ServiceLevel": "SNT",
        "ServiceSku": "CON-SNT-C220M4S",
        "ServiceStartDate": "2022-10-28T00:00:00Z",
        "ServiceEndDate": "2024-02-29T00:00:00Z",
        "IsValid": true
    },
    "NumCpus": 2,
    "NumCpuCores": 28,
    "NumThreads": 56,
    "Cpu": "2S 28C 56T",
    "Groups": "",
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
    "ManagementIp": "10.58.25.35",
    "Redfish": {
        "Capable": true,
        "Enabled": false
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "AvailableMemory": 262144,
    "TotalMemory": 262144,
    "UsedMemory": 0,
    "TotalMemoryUnit": "256 [GiB]",
    "TotalMemoryGB": 256,
    "AvailableMemoryUnit": "256 [GiB]",
    "AvailableMemoryGB": 256,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "FlagState": "P+ H",
    "FlagManagement": "Cri",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name esx93-eu-spdc-FCH2108V1HE --contract

Developer output

{
    "duration": 15624,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11324
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
        "lines": 431
    }
}

Log: isctl
-----------

2023-01-05 18:47:00.140269	True	3001	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:47:01.949938	True	1806	10	isctl get compute blade   -o json --top 100
2023-01-05 18:47:07.596150	True	1761	1	isctl get asset devicecontractinformation --filter "DeviceId eq 'FCH2108V1HE'"  -o json --top 100
2023-01-05 18:47:09.185366	True	1584	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '6141c3186f72612d30d2d8f8'"  -o json --top 100
2023-01-05 18:47:10.827910	True	1640	1	isctl get asset deviceregistration  moid 6141c3186f72612d30d2d8f8 -o json
2023-01-05 18:47:12.362224	True	1532	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:47:10.000Z"  -o json --top 100
```
