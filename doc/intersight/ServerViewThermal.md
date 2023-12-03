# Intersight Server

## thermal view

```
# iserver get server --group test-env -v thermal

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Thermal Summary [#2]
--------------------

+--------------------------------+----------------+-------------+------------------+----------------+-------------+
| Server                         | Sensors Health | Highest (C) | Smallest Gap (C) | Over Threshold | Fans Health |
+--------------------------------+----------------+-------------+------------------+----------------+-------------+
| comp-4-p2b-eu-spdc-WMP240400FM | True           | 73          | 20               | 0              | True        | 
| comp-6-p2b-eu-spdc-WMP24040059 | True           | 68          | 22               | 0              | True        | 
+--------------------------------+----------------+-------------+------------------+----------------+-------------+

Thermal Sensor [#42]
--------------------

+--------------------------------+------------------+---------+--------+------------------+-----------------+---------------------------+
| Server                         | Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+--------------------------------+------------------+---------+--------+------------------+-----------------+---------------------------+
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 70              | 90                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | P1_TEMP_SENS     | Enabled | OK     | CPU              | 73              | 100                       | 
| comp-4-p2b-eu-spdc-WMP240400FM | P2_TEMP_SENS     | Enabled | OK     | CPU              | 69              | 100                       | 
| comp-4-p2b-eu-spdc-WMP240400FM | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 48              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 43              | 65                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 27              | 65                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 38              | 70                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 42              | 70                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 39              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 40              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 68              | 90                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 46.5            | 100                       | 
| comp-6-p2b-eu-spdc-WMP24040059 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 42              | 100                       | 
| comp-6-p2b-eu-spdc-WMP24040059 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 37              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 29              | 65                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 28              | 65                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 37              | 70                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 40              | 70                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        | 
+--------------------------------+------------------+---------+--------+------------------+-----------------+---------------------------+

Thermal Fan [#28]
-----------------

+--------------------------------+-----------------+---------+--------+----------+
| Server                         | Fan Name        | State   | Health | Value    |
+--------------------------------+-----------------+---------+--------+----------+
| comp-4-p2b-eu-spdc-WMP240400FM | MOD1_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD1_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD2_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD2_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD3_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD3_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD4_FAN1_SPEED | Enabled | OK     | 7140 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD4_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD5_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD5_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD6_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD6_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD7_FAN1_SPEED | Enabled | OK     | 7140 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD7_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD1_FAN1_SPEED | Enabled | OK     | 3255 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD1_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD2_FAN1_SPEED | Enabled | OK     | 3360 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD2_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD3_FAN1_SPEED | Enabled | OK     | 3255 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD3_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD4_FAN1_SPEED | Enabled | OK     | 3360 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD4_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD5_FAN1_SPEED | Enabled | OK     | 3255 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD5_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD6_FAN1_SPEED | Enabled | OK     | 3255 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD6_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD7_FAN1_SPEED | Enabled | OK     | 3360 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD7_FAN2_SPEED | Enabled | OK     | 3296 RPM | 
+--------------------------------+-----------------+---------+--------+----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test-env -v thermal

{
    "duration": 14330,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 5558
    },
    "redfish": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 3,
        "disconnect": 0,
        "path": 8,
        "connect_time": 3923,
        "disconnect_time": 0,
        "path_time": 3068,
        "total_time": 6991
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
        "lines": 22
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:29:15.198078	True	2258	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:29:16.848025	True	1648	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:29:18.553560	True	1652	12	isctl get compute blade   -o json --top 100


Log: redfish
-------------

2023-12-03 15:29:20.265594	True	1684	connect 10.58.50.44
2023-12-03 15:29:20.392728	True	125	10.58.50.44:/redfish/v1/Systems
2023-12-03 15:29:20.539753	True	125	10.58.50.44:/redfish/v1/Chassis
2023-12-03 15:29:20.741352	True	196	10.58.50.44:/redfish/v1/Chassis/1
2023-12-03 15:29:21.887054	True	1131	10.58.50.44:/redfish/v1/Chassis/1/Thermal
2023-12-03 15:29:23.623231	True	1713	connect 10.58.50.46
2023-12-03 15:29:23.683574	True	58	10.58.50.46:/redfish/v1/Systems
2023-12-03 15:29:23.754192	True	63	10.58.50.46:/redfish/v1/Chassis
2023-12-03 15:29:23.898193	True	127	10.58.50.46:/redfish/v1/Chassis/1
2023-12-03 15:29:25.168502	True	1243	10.58.50.46:/redfish/v1/Chassis/1/Thermal
2023-12-03 15:29:25.727232	True	526	disconnect 10.58.50.46
```

[[Back]](./ServerInventory.md)