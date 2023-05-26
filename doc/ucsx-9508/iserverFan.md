# UCSX-9508 fan monitoring with iserver

```
# iserver get chassis --serial FOX2611PPHP --fan

Fan State Summary
-----------------
- Fan Module : 4/4/4
- Fan        : 8/8/8


Fan Control Configuration
-------------------------
- Mode : LowPower


+---------------+------------+-----------+--------------------+-------+
| Fan Module    | Module Id  | Presence  | Operational State  | Fans  |
+---------------+------------+-----------+--------------------+-------+
| Fan Module 1  | 1          | equipped  | OK                 | 2     | 
| Fan Module 2  | 2          | equipped  | OK                 | 2     | 
| Fan Module 3  | 3          | equipped  | OK                 | 2     | 
| Fan Module 4  | 4          | equipped  | OK                 | 2     | 
+---------------+------------+-----------+--------------------+-------+

+-----------------------+------------+---------+-----------+--------------------+----------------+--------------+--------------+
| Fan                   | Module Id  | Fan Id  | Presence  | Operational State  | Model          | Serial       | Part Number  |
+-----------------------+------------+---------+-----------+--------------------+----------------+--------------+--------------+
| Fan Module 1 - Fan 1  | 1          | 1       | equipped  | OK                 | UCSX-9508-FAN  | FCH2546722R  | 73-19422-04  | 
| Fan Module 1 - Fan 2  | 1          | 2       | equipped  | OK                 | UCSX-9508-FAN  | FCH2546722R  | 73-19422-04  | 
| Fan Module 2 - Fan 1  | 2          | 1       | equipped  | OK                 | UCSX-9508-FAN  | FCH254670WG  | 73-19422-04  | 
| Fan Module 2 - Fan 2  | 2          | 2       | equipped  | OK                 | UCSX-9508-FAN  | FCH254670WG  | 73-19422-04  | 
| Fan Module 3 - Fan 1  | 3          | 1       | equipped  | OK                 | UCSX-9508-FAN  | FCH254671AW  | 73-19422-04  | 
| Fan Module 3 - Fan 2  | 3          | 2       | equipped  | OK                 | UCSX-9508-FAN  | FCH254671AW  | 73-19422-04  | 
| Fan Module 4 - Fan 1  | 4          | 1       | equipped  | OK                 | UCSX-9508-FAN  | FCH254671WX  | 73-19422-04  | 
| Fan Module 4 - Fan 2  | 4          | 2       | equipped  | OK                 | UCSX-9508-FAN  | FCH254671WX  | 73-19422-04  | 
+-----------------------+------------+---------+-----------+--------------------+----------------+--------------+--------------+
```

## JSON output

```
# iserver get chassis --serial FOX2611PPHP --fan -o json

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
        "FanModulesOn": 4,
        "FanModuleCount": 4,
        "FanModuleSummary": "4/4/4",
        "FanOn": 8,
        "FanCount": 8,
        "FanSummary": "8/8/8"
    },
    "FanControlInfo": {
        "Moid": "632b15b476752d3236304c55",
        "Dn": "chassis-1-fan-control",
        "Mode": "LowPower"
    },
    "FanModuleInfo": [
        {
            "Moid": "632b15b576752d3236304cf8",
            "ModuleId": 1,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-1",
            "On": true,
            "Name": "Fan Module 1",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304cf9",
                "632b15b576752d3236304d01"
            ]
        },
        {
            "Moid": "632b15b576752d3236304d08",
            "ModuleId": 2,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-2",
            "On": true,
            "Name": "Fan Module 2",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304d09",
                "632b15b576752d3236304d10"
            ]
        },
        {
            "Moid": "632b15b576752d3236304d17",
            "ModuleId": 3,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-3",
            "On": true,
            "Name": "Fan Module 3",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304d18",
                "632b15b576752d3236304d1f"
            ]
        },
        {
            "Moid": "632b15b576752d3236304d27",
            "ModuleId": 4,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-4",
            "On": true,
            "Name": "Fan Module 4",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304d28",
                "632b15b576752d3236304d30"
            ]
        }
    ],
    "FanInfo": [
        {
            "Dn": "chassis-1-tray-1-mod-1-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 1,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH2546722R",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 1 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-1-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 1,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH2546722R",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 1 - Fan 2"
        },
        {
            "Dn": "chassis-1-tray-1-mod-2-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 2,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254670WG",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 2 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-2-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 2,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254670WG",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 2 - Fan 2"
        },
        {
            "Dn": "chassis-1-tray-1-mod-3-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 3,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671AW",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 3 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-3-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 3,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671AW",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 3 - Fan 2"
        },
        {
            "Dn": "chassis-1-tray-1-mod-4-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 4,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671WX",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 4 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-4-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 4,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671WX",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 4 - Fan 2"
        }
    ]
}
```

## YAML output

```
# iserver get chassis --serial FOX2611PPHP --fan -o yaml

Chassis:
  AlarmCritical: 0
  AlarmWarning: 2
  ConnectionPath: A,B
  ConnectionStatus: A,B
  ConnectionSummary: A,B / A,B
  Description: Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots
  DeviceMoId: 632999466f72612d39b26942
  Dn: chassis-1
  FanCount: 8
  FanMax: 8
  FanModuleCount: 4
  FanModuleMax: 4
  FanModuleSummary: 4/4/4
  FanModulesOn: 4
  FanOn: 8
  FanSummary: 8/8/8
  Health: Warnings
  HealthSummary: Warnings (2)
  IfmMax: 2
  Model: UCSX-9508
  Moid: 632b13c876752d32362fc175
  Name: ucsX-1
  NodeMax: 8
  OperState: OK
  PartNumber: 68-6847-03
  Pid: UCSX-9508
  ProductName: Cisco UCSX 9508 Chassis
  PsuMax: 6
  Serial: FOX2611PPHP
  Sku: UCSX-9508
  Vendor: Cisco Systems Inc
FanControlInfo:
  Dn: chassis-1-fan-control
  Mode: LowPower
  Moid: 632b15b476752d3236304c55
FanInfo:
- Dn: chassis-1-tray-1-mod-1-fan-1
  FanId: 1
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 1
  Name: Fan Module 1 - Fan 1
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH2546722R
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-1-fan-2
  FanId: 2
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 1
  Name: Fan Module 1 - Fan 2
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH2546722R
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-2-fan-1
  FanId: 1
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 2
  Name: Fan Module 2 - Fan 1
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH254670WG
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-2-fan-2
  FanId: 2
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 2
  Name: Fan Module 2 - Fan 2
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH254670WG
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-3-fan-1
  FanId: 1
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 3
  Name: Fan Module 3 - Fan 1
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH254671AW
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-3-fan-2
  FanId: 2
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 3
  Name: Fan Module 3 - Fan 2
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH254671AW
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-4-fan-1
  FanId: 1
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 4
  Name: Fan Module 4 - Fan 1
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH254671WX
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
- Dn: chassis-1-tray-1-mod-4-fan-2
  FanId: 2
  FanModuleId: 0
  Model: UCSX-9508-FAN
  ModuleId: 4
  Name: Fan Module 4 - Fan 2
  'On': true
  OperState: OK
  PartNumber: 73-19422-04
  Pid: UCSX-9508-FAN
  Presence: equipped
  Serial: FCH254671WX
  Sku: UCSX-9508-FAN
  TrayId: 1
  Vendor: Cisco Systems Inc
FanModuleInfo:
- Dn: chassis-1-tray-1-mod-1
  FanCount: 2
  FanMoids:
  - 632b15b576752d3236304cf9
  - 632b15b576752d3236304d01
  ModuleId: 1
  Moid: 632b15b576752d3236304cf8
  Name: Fan Module 1
  'On': true
  OperState: OK
  Presence: equipped
- Dn: chassis-1-tray-1-mod-2
  FanCount: 2
  FanMoids:
  - 632b15b576752d3236304d09
  - 632b15b576752d3236304d10
  ModuleId: 2
  Moid: 632b15b576752d3236304d08
  Name: Fan Module 2
  'On': true
  OperState: OK
  Presence: equipped
- Dn: chassis-1-tray-1-mod-3
  FanCount: 2
  FanMoids:
  - 632b15b576752d3236304d18
  - 632b15b576752d3236304d1f
  ModuleId: 3
  Moid: 632b15b576752d3236304d17
  Name: Fan Module 3
  'On': true
  OperState: OK
  Presence: equipped
- Dn: chassis-1-tray-1-mod-4
  FanCount: 2
  FanMoids:
  - 632b15b576752d3236304d28
  - 632b15b576752d3236304d30
  ModuleId: 4
  Moid: 632b15b576752d3236304d27
  Name: Fan Module 4
  'On': true
  OperState: OK
  Presence: equipped
```

## Developer output

```
# iserver get chassis --serial FOX2611PPHP --fan

Developer output

{
    "duration": 6289,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 5669
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
        "lines": 237
    }
}

Log: debug
-----------

[2022-11-17 10:14:08.128451]	[chassis_info.get]	{
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
        "FanModulesOn": 4,
        "FanModuleCount": 4,
        "FanModuleSummary": "4/4/4",
        "FanOn": 8,
        "FanCount": 8,
        "FanSummary": "8/8/8"
    },
    "FanControlInfo": {
        "Moid": "632b15b476752d3236304c55",
        "Dn": "chassis-1-fan-control",
        "Mode": "LowPower"
    },
    "FanModuleInfo": [
        {
            "Moid": "632b15b576752d3236304cf8",
            "ModuleId": 1,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-1",
            "On": true,
            "Name": "Fan Module 1",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304cf9",
                "632b15b576752d3236304d01"
            ]
        },
        {
            "Moid": "632b15b576752d3236304d08",
            "ModuleId": 2,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-2",
            "On": true,
            "Name": "Fan Module 2",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304d09",
                "632b15b576752d3236304d10"
            ]
        },
        {
            "Moid": "632b15b576752d3236304d17",
            "ModuleId": 3,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-3",
            "On": true,
            "Name": "Fan Module 3",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304d18",
                "632b15b576752d3236304d1f"
            ]
        },
        {
            "Moid": "632b15b576752d3236304d27",
            "ModuleId": 4,
            "OperState": "OK",
            "Presence": "equipped",
            "Dn": "chassis-1-tray-1-mod-4",
            "On": true,
            "Name": "Fan Module 4",
            "FanCount": 2,
            "FanMoids": [
                "632b15b576752d3236304d28",
                "632b15b576752d3236304d30"
            ]
        }
    ],
    "FanInfo": [
        {
            "Dn": "chassis-1-tray-1-mod-1-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 1,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH2546722R",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 1 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-1-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 1,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH2546722R",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 1 - Fan 2"
        },
        {
            "Dn": "chassis-1-tray-1-mod-2-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 2,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254670WG",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 2 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-2-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 2,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254670WG",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 2 - Fan 2"
        },
        {
            "Dn": "chassis-1-tray-1-mod-3-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 3,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671AW",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 3 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-3-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 3,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671AW",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 3 - Fan 2"
        },
        {
            "Dn": "chassis-1-tray-1-mod-4-fan-1",
            "FanId": 1,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 4,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671WX",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 4 - Fan 1"
        },
        {
            "Dn": "chassis-1-tray-1-mod-4-fan-2",
            "FanId": 2,
            "FanModuleId": 0,
            "Model": "UCSX-9508-FAN",
            "ModuleId": 4,
            "OperState": "OK",
            "On": true,
            "PartNumber": "73-19422-04",
            "Pid": "UCSX-9508-FAN",
            "Presence": "equipped",
            "Serial": "FCH254671WX",
            "Sku": "UCSX-9508-FAN",
            "Vendor": "Cisco Systems Inc",
            "TrayId": 1,
            "Name": "Fan Module 4 - Fan 2"
        }
    ]
}


Log: isctl
-----------

2022-11-17 10:14:03.890760	True	1444	2	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2022-11-17 10:14:05.257095	True	1362	1	isctl get equipment fancontrol  moid 632b15b476752d3236304c55 -o json
2022-11-17 10:14:06.744068	True	1485	4	isctl get equipment fanmodule --filter "Parent/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
2022-11-17 10:14:08.124045	True	1378	8	isctl get equipment fan --filter "Parent/Moid in ('632b15b576752d3236304cf8', '632b15b576752d3236304d08', '632b15b576752d3236304d17', '632b15b576752d3236304d27')"  -o json --top 100
```