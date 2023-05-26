# Extra server information - Environmental State

```
# iserver get server --ip 10.58.50.41 --env

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
No power consumption information found
No thermal information found
```

JSON Output

```
# iserver get server --ip 10.58.50.41 --env

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
    "Power": null,
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
# iserver get server --ip 10.58.50.41 --env

Developer output

{
    "duration": 7435,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4215
    },
    "redfish": {
        "read": true,
        "success": 0,
        "failed": 2,
        "connect": 2,
        "disconnect": 0,
        "path": 0,
        "connect_time": 2926,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 2926
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
        "lines": 3
    },
    "info": {
        "read": true,
        "lines": 3
    },
    "debug": {
        "read": true,
        "lines": 54
    }
}

Log: info
----------

[2022-12-13 17:08:01.854879]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:08:03.226013]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'


Log: error
-----------

[2022-12-13 17:08:01.854588]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:08:03.225667]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'


Log: isctl
-----------

2022-12-13 17:07:58.477493	True	2177	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:07:58.947040	True	469	10	isctl get compute blade   -o json --top 100
2022-12-13 17:07:59.448511	True	362	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2022-12-13 17:08:00.292940	True	842	16	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-06T17:07:59.000Z"  -o json --top 100
2022-12-13 17:08:03.592043	True	365	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100


Log: redfish
-------------

2022-12-13 17:08:01.855271	False	1556	connect 10.58.50.41
2022-12-13 17:08:03.226290	False	1370	connect 10.58.50.41
```
