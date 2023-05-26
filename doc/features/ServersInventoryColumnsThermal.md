# Extra server information - Thermal State

```
# iserver get server --ip 10.58.50.41 --thermal

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
No thermal information found
```

JSON Output

```
# iserver get server --ip 10.58.50.41 --thermal

{
    "__Output": {
        "FlagState": ":GG.G"
    },
    "Moid": "5fdf9c016176752d35e44795",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Model": "UCSC-C240-M5SN",
    "Serial": "WZP23400AJW",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
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
    "ManagementIp": "10.58.50.41",
    "AlarmSummary": {
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "Connected": true,
    "Workflow": {
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "Groups": "p2b,pod2b,power",
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
    "Thermal": null,
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "LocatorLedOn": false,
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --ip 10.58.50.41 --thermal

Developer output

{
    "duration": 6519,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4768
    },
    "redfish": {
        "read": true,
        "success": 0,
        "failed": 1,
        "connect": 1,
        "disconnect": 0,
        "path": 0,
        "connect_time": 1452,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 1452
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
        "read": true,
        "lines": 2
    },
    "info": {
        "read": true,
        "lines": 2
    },
    "debug": {
        "read": true,
        "lines": 53
    }
}

Log: info
----------

[2022-12-13 17:07:54.764136]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'


Log: error
-----------

[2022-12-13 17:07:54.763848]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'


Log: isctl
-----------

2022-12-13 17:07:51.140339	True	2344	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:07:51.930691	True	789	10	isctl get compute blade   -o json --top 100
2022-12-13 17:07:52.429395	True	360	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2022-12-13 17:07:53.305517	True	874	16	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-06T17:07:52.000Z"  -o json --top 100
2022-12-13 17:07:55.165176	True	401	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100


Log: redfish
-------------

2022-12-13 17:07:54.764415	False	1452	connect 10.58.50.41
```
