# UCSX-9508 server monitoring with iserver

```
# iserver get chassis --serial FOX2611PPHP --node

+-------+-----------+----------+--------+---------------+--------------+--------------+------------+
| Slot  | Name      | Health   | Power  | Model         | Serial       | CPU          | Memory     |
+-------+-----------+----------+--------+---------------+--------------+--------------+------------+
| 1     | ucsX-1-1  | Healthy  | off    | UCSX-210C-M6  | FCH26167MMZ  | 2S 64C 128T  | 1.0 [TiB]  | 
| 2     | ucsX-1-2  | Healthy  | off    | UCSX-210C-M6  | FCH26167L94  | 2S 64C 128T  | 1.0 [TiB]  | 
| 3     | ucsX-1-3  | Healthy  | off    | UCSX-210C-M6  | FCH26167MQK  | 2S 64C 128T  | 1.0 [TiB]  | 
| 4     | ucsX-1-4  | Healthy  | off    | UCSX-210C-M6  | FCH26167MHB  | 2S 64C 128T  | 1.0 [TiB]  | 
+-------+-----------+----------+--------+---------------+--------------+--------------+------------+
```

## JSON output

```
# iserver get chassis --serial FOX2611PPHP --node -o json

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
        "NodePowerOn": 0,
        "NodeCount": 4,
        "NodeSummary": "0/4/8"
    },
    "NodeInfo": [
        {
            "Moid": "632b174e76752d323630bb47",
            "Dn": "/redfish/v1/Systems/FCH26167MMZ",
            "Name": "ucsX-1-1",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MMZ",
            "HardwareUuid": "8A552335-ED7E-4A28-924D-BE8748DA5BF8",
            "ServiceProfile": "",
            "SlotId": 1,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163d76752d323630734f",
            "Dn": "/redfish/v1/Systems/FCH26167L94",
            "Name": "ucsX-1-2",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167L94",
            "HardwareUuid": "D576BED6-EF35-439C-B088-0735FED04410",
            "ServiceProfile": "",
            "SlotId": 2,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163e76752d32363073aa",
            "Dn": "/redfish/v1/Systems/FCH26167MQK",
            "Name": "ucsX-1-3",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MQK",
            "HardwareUuid": "0607F131-46C2-4CDC-B237-1F872D01E441",
            "ServiceProfile": "",
            "SlotId": 3,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163f76752d32363073f7",
            "Dn": "/redfish/v1/Systems/FCH26167MHB",
            "Name": "ucsX-1-4",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MHB",
            "HardwareUuid": "6918688F-1B00-4DDB-A6E3-D316F6D07F64",
            "ServiceProfile": "",
            "SlotId": 4,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        }
    ]
}
```

## YAML output

```
# iserver get chassis --serial FOX2611PPHP --node -o yaml

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
  IfmMax: 2
  Model: UCSX-9508
  Moid: 632b13c876752d32362fc175
  Name: ucsX-1
  NodeCount: 4
  NodeMax: 8
  NodePowerOn: 0
  NodeSummary: 0/4/8
  OperState: OK
  PartNumber: 68-6847-03
  Pid: UCSX-9508
  ProductName: Cisco UCSX 9508 Chassis
  PsuMax: 6
  Serial: FOX2611PPHP
  Sku: UCSX-9508
  Vendor: Cisco Systems Inc
NodeInfo:
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167MMZ
  HardwareUuid: 8A552335-ED7E-4A28-924D-BE8748DA5BF8
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b174e76752d323630bb47
  Name: ucsX-1-1
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167MMZ
  ServiceProfile: ''
  SlotId: 1
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167L94
  HardwareUuid: D576BED6-EF35-439C-B088-0735FED04410
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b163d76752d323630734f
  Name: ucsX-1-2
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167L94
  ServiceProfile: ''
  SlotId: 2
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167MQK
  HardwareUuid: 0607F131-46C2-4CDC-B237-1F872D01E441
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b163e76752d32363073aa
  Name: ucsX-1-3
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167MQK
  ServiceProfile: ''
  SlotId: 3
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167MHB
  HardwareUuid: 6918688F-1B00-4DDB-A6E3-D316F6D07F64
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b163f76752d32363073f7
  Name: ucsX-1-4
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167MHB
  ServiceProfile: ''
  SlotId: 4
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
```

## Developer output

```
# iserver get chassis --serial FOX2611PPHP --node

Developer output

{
    "duration": 4246,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 3532
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
        "lines": 139
    }
}

Log: debug
-----------

[2022-11-17 10:18:32.356812]	[chassis_info.get]	{
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
        "NodePowerOn": 0,
        "NodeCount": 4,
        "NodeSummary": "0/4/8"
    },
    "NodeInfo": [
        {
            "Moid": "632b174e76752d323630bb47",
            "Dn": "/redfish/v1/Systems/FCH26167MMZ",
            "Name": "ucsX-1-1",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MMZ",
            "HardwareUuid": "8A552335-ED7E-4A28-924D-BE8748DA5BF8",
            "ServiceProfile": "",
            "SlotId": 1,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163d76752d323630734f",
            "Dn": "/redfish/v1/Systems/FCH26167L94",
            "Name": "ucsX-1-2",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167L94",
            "HardwareUuid": "D576BED6-EF35-439C-B088-0735FED04410",
            "ServiceProfile": "",
            "SlotId": 2,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163e76752d32363073aa",
            "Dn": "/redfish/v1/Systems/FCH26167MQK",
            "Name": "ucsX-1-3",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MQK",
            "HardwareUuid": "0607F131-46C2-4CDC-B237-1F872D01E441",
            "ServiceProfile": "",
            "SlotId": 3,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163f76752d32363073f7",
            "Dn": "/redfish/v1/Systems/FCH26167MHB",
            "Name": "ucsX-1-4",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MHB",
            "HardwareUuid": "6918688F-1B00-4DDB-A6E3-D316F6D07F64",
            "ServiceProfile": "",
            "SlotId": 4,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        }
    ]
}


Log: isctl
-----------

2022-11-17 10:18:30.756359	True	1945	2	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2022-11-17 10:18:32.352824	True	1587	4	isctl get compute blade --filter "EquipmentChassis/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
```