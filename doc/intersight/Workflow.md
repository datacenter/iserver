# Workflow

Get workflow's detail selected by Moid in table, json or yaml formats.

```
# iserver get workflow --help

Usage: iserver.py get workflow [OPTIONS] WORKFLOW_ID

  Get workflow

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.
```

Default output

```
# iserver get workflow 6399884f696f6e2d306e11f1

Get server workflow info...

Server
- Name: comp-4-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 6399884f696f6e2d306e11f1
- Name: Turn On Locator
- Status: COMPLETED
- Create Time: 2022-12-14T08:24:47.461Z
- Start Time: 2022-12-14T08:24:47.63Z
- End Time: 2022-12-14T08:24:50.443Z
- Duration: 00:00:03


+--------------------------+---------------------------------+--------------------------+-----------+----------+--------------------------+
| Task Moid                | Description                     | Create Time              | Status    | Duration | Details                  |
+--------------------------+---------------------------------+--------------------------+-----------+----------+--------------------------+
| 6399884f696f6e2d306e1204 | workflow.StartWorkflowTask      | 2022-12-14T08:24:47.757Z | COMPLETED | 00:00:00 |                          | 
| 6399884f696f6e2d306e120d | Turn on Locator LED             | 2022-12-14T08:24:47.849Z | COMPLETED | 00:00:02 | Locator LED is turned on | 
| 63998851696f6e2d306e1225 | Turn on the Locator LED         | 2022-12-14T08:24:49.702Z | NO_OP     | 00:00:00 |                          | 
| 63998851696f6e2d306e1237 | Turn on the Locator LED         | 2022-12-14T08:24:49.896Z | NO_OP     |          |                          | 
| 63998851696f6e2d306e123c | Update Server Inventory         | 2022-12-14T08:24:49.997Z | COMPLETED | 00:00:01 | State synchronized.      | 
| 63998852696f6e2d306e1248 | workflow.SuccessEndWorkflowTask | 2022-12-14T08:24:50.351Z | COMPLETED | 00:00:00 |                          | 
+--------------------------+---------------------------------+--------------------------+-----------+----------+--------------------------+
```

JSON output

```
# iserver get workflow 6399884f696f6e2d306e11f1 -o json

{
    "workflow": {
        "Moid": "6399884f696f6e2d306e11f1",
        "Name": "Turn On Locator",
        "Progress": 100,
        "CreateTime": "2022-12-14T08:24:47.461Z",
        "StartTime": "2022-12-14T08:24:47.63Z",
        "EndTime": "2022-12-14T08:24:50.443Z",
        "Status": "COMPLETED",
        "Type": "UserDefined",
        "CreateTimeEpoch": 1671002687461,
        "StartTimeEpoch": 1671002687630,
        "EndTimeEpoch": 1671002690443,
        "Running": false,
        "Completed": true,
        "Duration": "00:00:03"
    },
    "tasks": [
        {
            "Moid": "6399884f696f6e2d306e1204",
            "Name": "workflow.StartWorkflowTask",
            "Label": "",
            "CreateTime": "2022-12-14T08:24:47.757Z",
            "StartTime": "2022-12-14T08:24:47.751Z",
            "EndTime": "2022-12-14T08:24:47.759Z",
            "Status": "COMPLETED",
            "FailureReason": "",
            "Description": "workflow.StartWorkflowTask",
            "CreateTimeEpoch": 1671002687757,
            "StartTimeEpoch": 1671002687751,
            "EndTimeEpoch": 1671002687759,
            "Duration": "00:00:00"
        },
        {
            "Moid": "6399884f696f6e2d306e120d",
            "Name": "compute.LocatorLedOperationTask",
            "Label": "Turn on Locator LED",
            "CreateTime": "2022-12-14T08:24:47.849Z",
            "StartTime": "2022-12-14T08:24:47.842Z",
            "EndTime": "2022-12-14T08:24:49.584Z",
            "Status": "COMPLETED",
            "FailureReason": "Locator LED is turned on",
            "Description": "Turn on Locator LED",
            "CreateTimeEpoch": 1671002687849,
            "StartTimeEpoch": 1671002687842,
            "EndTimeEpoch": 1671002689584,
            "Duration": "00:00:02"
        },
        {
            "Moid": "63998851696f6e2d306e1225",
            "Name": "compute.LocatorLedRedfishOperationTask",
            "Label": "Turn on the Locator LED",
            "CreateTime": "2022-12-14T08:24:49.702Z",
            "StartTime": "2022-12-14T08:24:49.691Z",
            "EndTime": "2022-12-14T08:24:49.795Z",
            "Status": "NO_OP",
            "FailureReason": "",
            "Description": "Turn on the Locator LED",
            "CreateTimeEpoch": 1671002689702,
            "StartTimeEpoch": 1671002689691,
            "EndTimeEpoch": 1671002689795,
            "Duration": "00:00:00"
        },
        {
            "Moid": "63998851696f6e2d306e1237",
            "Name": "SetLocatorLEDStateInAssistManagedDevices",
            "Label": "Turn on the Locator LED",
            "CreateTime": "2022-12-14T08:24:49.896Z",
            "StartTime": "2022-12-14T08:24:49.889Z",
            "EndTime": "0001-01-01T00:00:00Z",
            "Status": "NO_OP",
            "FailureReason": "",
            "Description": "Turn on the Locator LED",
            "CreateTimeEpoch": 1671002689896,
            "StartTimeEpoch": 1671002689889,
            "EndTimeEpoch": null,
            "Duration": ""
        },
        {
            "Moid": "63998851696f6e2d306e123c",
            "Name": "UpdateServerInventoryTask",
            "Label": "Update Server Inventory",
            "CreateTime": "2022-12-14T08:24:49.997Z",
            "StartTime": "2022-12-14T08:24:49.99Z",
            "EndTime": "2022-12-14T08:24:50.25Z",
            "Status": "COMPLETED",
            "FailureReason": "State synchronized.",
            "Description": "Update Server Inventory",
            "CreateTimeEpoch": 1671002689997,
            "StartTimeEpoch": 1671002689990,
            "EndTimeEpoch": 1671002690250,
            "Duration": "00:00:01"
        },
        {
            "Moid": "63998852696f6e2d306e1248",
            "Name": "workflow.SuccessEndWorkflowTask",
            "Label": "",
            "CreateTime": "2022-12-14T08:24:50.351Z",
            "StartTime": "2022-12-14T08:24:50.345Z",
            "EndTime": "2022-12-14T08:24:50.355Z",
            "Status": "COMPLETED",
            "FailureReason": "",
            "Description": "workflow.SuccessEndWorkflowTask",
            "CreateTimeEpoch": 1671002690351,
            "StartTimeEpoch": 1671002690345,
            "EndTimeEpoch": 1671002690355,
            "Duration": "00:00:00"
        }
    ],
    "server": {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "5fdfa1806176752d35e678c2",
        "DeviceMoId": "5fdfa1686f72612d300b383f",
        "Name": "comp-4-p2b-eu-spdc-WMP240400FM",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP240400FM",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
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
        "ManagementIp": "10.58.50.44",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Groups": "p2b,pod2b,test,self-test-power,power",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "cRi",
        "FlagWorkflow": ""
    }
}
```

YAML output

```
# iserver get workflow 6399884f696f6e2d306e11f1 -o yaml

server:
  AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: false
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdfa1686f72612d300b383f
  FlagManagement: cRi
  FlagState: P- H
  FlagWorkflow: ''
  Groups: p2b,pod2b,test,self-test-power,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.44
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fdfa1806176752d35e678c2
  Name: comp-4-p2b-eu-spdc-WMP240400FM
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'off'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP240400FM
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
  __Output:
    FlagState: :RR.G
tasks:
- CreateTime: '2022-12-14T08:24:47.757Z'
  CreateTimeEpoch: 1671002687757
  Description: workflow.StartWorkflowTask
  Duration: 00:00:00
  EndTime: '2022-12-14T08:24:47.759Z'
  EndTimeEpoch: 1671002687759
  FailureReason: ''
  Label: ''
  Moid: 6399884f696f6e2d306e1204
  Name: workflow.StartWorkflowTask
  StartTime: '2022-12-14T08:24:47.751Z'
  StartTimeEpoch: 1671002687751
  Status: COMPLETED
- CreateTime: '2022-12-14T08:24:47.849Z'
  CreateTimeEpoch: 1671002687849
  Description: Turn on Locator LED
  Duration: 00:00:02
  EndTime: '2022-12-14T08:24:49.584Z'
  EndTimeEpoch: 1671002689584
  FailureReason: Locator LED is turned on
  Label: Turn on Locator LED
  Moid: 6399884f696f6e2d306e120d
  Name: compute.LocatorLedOperationTask
  StartTime: '2022-12-14T08:24:47.842Z'
  StartTimeEpoch: 1671002687842
  Status: COMPLETED
- CreateTime: '2022-12-14T08:24:49.702Z'
  CreateTimeEpoch: 1671002689702
  Description: Turn on the Locator LED
  Duration: 00:00:00
  EndTime: '2022-12-14T08:24:49.795Z'
  EndTimeEpoch: 1671002689795
  FailureReason: ''
  Label: Turn on the Locator LED
  Moid: 63998851696f6e2d306e1225
  Name: compute.LocatorLedRedfishOperationTask
  StartTime: '2022-12-14T08:24:49.691Z'
  StartTimeEpoch: 1671002689691
  Status: NO_OP
- CreateTime: '2022-12-14T08:24:49.896Z'
  CreateTimeEpoch: 1671002689896
  Description: Turn on the Locator LED
  Duration: ''
  EndTime: '0001-01-01T00:00:00Z'
  EndTimeEpoch: null
  FailureReason: ''
  Label: Turn on the Locator LED
  Moid: 63998851696f6e2d306e1237
  Name: SetLocatorLEDStateInAssistManagedDevices
  StartTime: '2022-12-14T08:24:49.889Z'
  StartTimeEpoch: 1671002689889
  Status: NO_OP
- CreateTime: '2022-12-14T08:24:49.997Z'
  CreateTimeEpoch: 1671002689997
  Description: Update Server Inventory
  Duration: 00:00:01
  EndTime: '2022-12-14T08:24:50.25Z'
  EndTimeEpoch: 1671002690250
  FailureReason: State synchronized.
  Label: Update Server Inventory
  Moid: 63998851696f6e2d306e123c
  Name: UpdateServerInventoryTask
  StartTime: '2022-12-14T08:24:49.99Z'
  StartTimeEpoch: 1671002689990
  Status: COMPLETED
- CreateTime: '2022-12-14T08:24:50.351Z'
  CreateTimeEpoch: 1671002690351
  Description: workflow.SuccessEndWorkflowTask
  Duration: 00:00:00
  EndTime: '2022-12-14T08:24:50.355Z'
  EndTimeEpoch: 1671002690355
  FailureReason: ''
  Label: ''
  Moid: 63998852696f6e2d306e1248
  Name: workflow.SuccessEndWorkflowTask
  StartTime: '2022-12-14T08:24:50.345Z'
  StartTimeEpoch: 1671002690345
  Status: COMPLETED
workflow:
  Completed: true
  CreateTime: '2022-12-14T08:24:47.461Z'
  CreateTimeEpoch: 1671002687461
  Duration: 00:00:03
  EndTime: '2022-12-14T08:24:50.443Z'
  EndTimeEpoch: 1671002690443
  Moid: 6399884f696f6e2d306e11f1
  Name: Turn On Locator
  Progress: 100
  Running: false
  StartTime: '2022-12-14T08:24:47.63Z'
  StartTimeEpoch: 1671002687630
  Status: COMPLETED
  Type: UserDefined
```