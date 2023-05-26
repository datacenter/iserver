# UCSX-9508 power monitoring with iserver

```
# iserver get chassis --serial FOX2611PPHP --power

Power Control Configuration
---------------------------
- Power Save Mode                           : Enabled
- Extended Power Capacity                   : Enabled
- Dynamic Power Rebalancing                 : Enabled
- Maximum Required Power                    : 8079 W
- Minimum Required Power                    : 4392 W
- Maximum Available Non-Redundant Power (N) : 12174 W
- Maximum Available Grid Power (N+N)        : 7000 W
- Maximum Available N1 Power (N+1)          : 10500 W
- Maximum Available N2 Power (N+2)          : 7000 W


Psu Control State
-----------------
- Input Power Health  : OK
- Output Power Health : OK
- Redundancy Health   : OK
- Redundancy Mode     : N+1


Psu State Summary
-----------------
- Psu : 4/6/6


+------------------+--------+----------+------------------+--------------+
| Chassis PSU      | On     | Voltage  | Model            | Serial       |
+------------------+--------+----------+------------------+--------------+
| chassis-1-psu-1  | True   | 226      | UCSX-PSU-2800AC  | DTM2611028K  | 
| chassis-1-psu-2  | True   | 226      | UCSX-PSU-2800AC  | DTM261100A0  | 
| chassis-1-psu-3  | False  | 0        | UCSX-PSU-2800AC  | DTM2611029S  | 
| chassis-1-psu-4  | True   | 223      | UCSX-PSU-2800AC  | DTM2611028F  | 
| chassis-1-psu-5  | True   | 223      | UCSX-PSU-2800AC  | DTM2611009H  | 
| chassis-1-psu-6  | False  | 0        | UCSX-PSU-2800AC  | DTM261100A4  | 
+------------------+--------+----------+------------------+--------------+
```

## JSON output

```
# iserver get chassis --serial FOX2611PPHP --power -o json

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
        "PsuCount": 6,
        "PsuOn": 4,
        "PsuSummary": "4/6/6"
    },
    "PowerControlStateInfo": {
        "Moid": "632b15b576752d3236304cf0",
        "AllocatedPower": 0,
        "ExtendedPowerCapacity": "Enabled",
        "GridMaxPower": 7000,
        "MaxRequiredPower": 8079,
        "MinRequiredPower": 4392,
        "N1MaxPower": 10500,
        "N2MaxPower": 7000,
        "NonRedundantMaxPower": 12174,
        "PowerRebalancing": "Enabled",
        "PowerSaveMode": "Enabled",
        "MoidUnit": "632b15b576752d3236304cf0 W",
        "AllocatedPowerUnit": "0 W",
        "GridMaxPowerUnit": "7000 W",
        "MaxRequiredPowerUnit": "8079 W",
        "MinRequiredPowerUnit": "4392 W",
        "N1MaxPowerUnit": "10500 W",
        "N2MaxPowerUnit": "7000 W",
        "NonRedundantMaxPowerUnit": "12174 W"
    },
    "PsuControlStateInfo": {
        "Model": "",
        "Serial": "",
        "Vendor": "",
        "Dn": "chassis-1-psu-control",
        "InputPowerState": "OK",
        "OperState": "OK",
        "OutputPowerState": "OK",
        "Redundancy": "N+1"
    },
    "PsuInfo": [
        {
            "Moid": "632b15b576752d3236304ccd",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611028K",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-1",
            "On": true,
            "Voltage": "226"
        },
        {
            "Moid": "632b15b576752d3236304cd4",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM261100A0",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-2",
            "On": true,
            "Voltage": "226"
        },
        {
            "Moid": "632b15b576752d3236304cd8",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611029S",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-3",
            "On": false,
            "Voltage": "0"
        },
        {
            "Moid": "632b15b576752d3236304cdd",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611028F",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-4",
            "On": true,
            "Voltage": "223"
        },
        {
            "Moid": "632b15b576752d3236304ce1",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611009H",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-5",
            "On": true,
            "Voltage": "223"
        },
        {
            "Moid": "632b15b576752d3236304ce5",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM261100A4",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-6",
            "On": false,
            "Voltage": "0"
        }
    ]
}
```

## YAML output

```
# iserver get chassis --serial FOX2611PPHP --power -o yaml

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
  NodeMax: 8
  OperState: OK
  PartNumber: 68-6847-03
  Pid: UCSX-9508
  ProductName: Cisco UCSX 9508 Chassis
  PsuCount: 6
  PsuMax: 6
  PsuOn: 4
  PsuSummary: 4/6/6
  Serial: FOX2611PPHP
  Sku: UCSX-9508
  Vendor: Cisco Systems Inc
PowerControlStateInfo:
  AllocatedPower: 0
  AllocatedPowerUnit: 0 W
  ExtendedPowerCapacity: Enabled
  GridMaxPower: 7000
  GridMaxPowerUnit: 7000 W
  MaxRequiredPower: 8079
  MaxRequiredPowerUnit: 8079 W
  MinRequiredPower: 4392
  MinRequiredPowerUnit: 4392 W
  Moid: 632b15b576752d3236304cf0
  MoidUnit: 632b15b576752d3236304cf0 W
  N1MaxPower: 10500
  N1MaxPowerUnit: 10500 W
  N2MaxPower: 7000
  N2MaxPowerUnit: 7000 W
  NonRedundantMaxPower: 12174
  NonRedundantMaxPowerUnit: 12174 W
  PowerRebalancing: Enabled
  PowerSaveMode: Enabled
PsuControlStateInfo:
  Dn: chassis-1-psu-control
  InputPowerState: OK
  Model: ''
  OperState: OK
  OutputPowerState: OK
  Redundancy: N+1
  Serial: ''
  Vendor: ''
PsuInfo:
- Dn: chassis-1-psu-1
  Model: UCSX-PSU-2800AC
  Moid: 632b15b576752d3236304ccd
  Name: ''
  'On': true
  Serial: DTM2611028K
  Vendor: Cisco Systems Inc
  Voltage: '226'
- Dn: chassis-1-psu-2
  Model: UCSX-PSU-2800AC
  Moid: 632b15b576752d3236304cd4
  Name: ''
  'On': true
  Serial: DTM261100A0
  Vendor: Cisco Systems Inc
  Voltage: '226'
- Dn: chassis-1-psu-3
  Model: UCSX-PSU-2800AC
  Moid: 632b15b576752d3236304cd8
  Name: ''
  'On': false
  Serial: DTM2611029S
  Vendor: Cisco Systems Inc
  Voltage: '0'
- Dn: chassis-1-psu-4
  Model: UCSX-PSU-2800AC
  Moid: 632b15b576752d3236304cdd
  Name: ''
  'On': true
  Serial: DTM2611028F
  Vendor: Cisco Systems Inc
  Voltage: '223'
- Dn: chassis-1-psu-5
  Model: UCSX-PSU-2800AC
  Moid: 632b15b576752d3236304ce1
  Name: ''
  'On': true
  Serial: DTM2611009H
  Vendor: Cisco Systems Inc
  Voltage: '223'
- Dn: chassis-1-psu-6
  Model: UCSX-PSU-2800AC
  Moid: 632b15b576752d3236304ce5
  Name: ''
  'On': false
  Serial: DTM261100A4
  Vendor: Cisco Systems Inc
  Voltage: '0'
```

## Developer output

```
# iserver get chassis --serial FOX2611PPHP --power

Developer output

{
    "duration": 6707,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 6059
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
        "lines": 126
    }
}

Log: debug
-----------

[2022-11-17 10:14:45.286379]	[chassis_info.get]	{
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
        "PsuCount": 6,
        "PsuOn": 4,
        "PsuSummary": "4/6/6"
    },
    "PowerControlStateInfo": {
        "Moid": "632b15b576752d3236304cf0",
        "AllocatedPower": 0,
        "ExtendedPowerCapacity": "Enabled",
        "GridMaxPower": 7000,
        "MaxRequiredPower": 8079,
        "MinRequiredPower": 4392,
        "N1MaxPower": 10500,
        "N2MaxPower": 7000,
        "NonRedundantMaxPower": 12174,
        "PowerRebalancing": "Enabled",
        "PowerSaveMode": "Enabled",
        "MoidUnit": "632b15b576752d3236304cf0 W",
        "AllocatedPowerUnit": "0 W",
        "GridMaxPowerUnit": "7000 W",
        "MaxRequiredPowerUnit": "8079 W",
        "MinRequiredPowerUnit": "4392 W",
        "N1MaxPowerUnit": "10500 W",
        "N2MaxPowerUnit": "7000 W",
        "NonRedundantMaxPowerUnit": "12174 W"
    },
    "PsuControlStateInfo": {
        "Model": "",
        "Serial": "",
        "Vendor": "",
        "Dn": "chassis-1-psu-control",
        "InputPowerState": "OK",
        "OperState": "OK",
        "OutputPowerState": "OK",
        "Redundancy": "N+1"
    },
    "PsuInfo": [
        {
            "Moid": "632b15b576752d3236304ccd",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611028K",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-1",
            "On": true,
            "Voltage": "226"
        },
        {
            "Moid": "632b15b576752d3236304cd4",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM261100A0",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-2",
            "On": true,
            "Voltage": "226"
        },
        {
            "Moid": "632b15b576752d3236304cd8",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611029S",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-3",
            "On": false,
            "Voltage": "0"
        },
        {
            "Moid": "632b15b576752d3236304cdd",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611028F",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-4",
            "On": true,
            "Voltage": "223"
        },
        {
            "Moid": "632b15b576752d3236304ce1",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM2611009H",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-5",
            "On": true,
            "Voltage": "223"
        },
        {
            "Moid": "632b15b576752d3236304ce5",
            "Name": "",
            "Model": "UCSX-PSU-2800AC",
            "Serial": "DTM261100A4",
            "Vendor": "Cisco Systems Inc",
            "Dn": "chassis-1-psu-6",
            "On": false,
            "Voltage": "0"
        }
    ]
}


Log: isctl
-----------

2022-11-17 10:14:40.800135	True	1587	2	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2022-11-17 10:14:42.259770	True	1454	1	isctl get power controlstate  moid 632b15b576752d3236304cf0 -o json
2022-11-17 10:14:43.616171	True	1354	1	isctl get equipment psucontrol --filter "Parent/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
2022-11-17 10:14:45.283386	True	1664	6	isctl get equipment psu --filter "Parent/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
```