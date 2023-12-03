# Intersight Server

## env view

```
# iserver get server --group test-env -v env

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Power Consumption [#2]
----------------------

+--------------------------------+---------+-----+---------+-----+--------------+
| Server                         | Current | Min | Average | Max | Limit action |
+--------------------------------+---------+-----+---------+-----+--------------+
| comp-4-p2b-eu-spdc-WMP240400FM | 288     | 121 | 309     | 743 | NoAction     | 
| comp-6-p2b-eu-spdc-WMP24040059 | 180     | 175 | 214     | 374 | NoAction     | 
+--------------------------------+---------+-----+---------+-----+--------------+

Power Sensor [#8]
-----------------

+--------------------------------+----------------+---------+--------+--------+-----------------+
| Server                         | Sensor Name    | State   | Health | Volts  | Upper Threshold |
+--------------------------------+----------------+---------+--------+--------+-----------------+
| comp-4-p2b-eu-spdc-WMP240400FM | PSU1_VOUT      | Enabled | OK     | 12.2   | 14              | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU2_VOUT      | Enabled | OK     | 12.2   | 14              | 
| comp-4-p2b-eu-spdc-WMP240400FM | P12V           | Enabled | OK     | 11.774 | 13.166          | 
| comp-4-p2b-eu-spdc-WMP240400FM | P3V_BAT_SCALED | Enabled | OK     | 3.042  | 3.588           | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU1_VOUT      | Enabled | OK     | 12.1   | 14              | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU2_VOUT      | Enabled | OK     | 12.2   | 14              | 
| comp-6-p2b-eu-spdc-WMP24040059 | P12V           | Enabled | OK     | 11.832 | 13.166          | 
| comp-6-p2b-eu-spdc-WMP24040059 | P3V_BAT_SCALED | Enabled | OK     | 3.042  | 3.588           | 
+--------------------------------+----------------+---------+--------+--------+-----------------+

Power Supply [#4]
-----------------

+--------------------------------+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| Server                         | PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+--------------------------------+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| comp-4-p2b-eu-spdc-WMP240400FM | PSU1     | Enabled | OK     | APS240201EL | 10252046 | 146           | 163          | 264     | 180     | 63       | 47       | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU2     | Enabled | OK     | ART2601F4S6 | 10252046 | 177           | 156          | 264     | 180     | 63       | 47       | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU1     | Enabled | OK     | APS240201EX | 10252041 | 90            | 104          | 264     | 180     | 63       | 47       | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU2     | Enabled | OK     | ART2601F4SS | 10252046 | 86            | 103          | 264     | 180     | 63       | 47       | 
+--------------------------------+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+

Thermal Summary [#2]
--------------------

+--------------------------------+----------------+-------------+------------------+----------------+-------------+
| Server                         | Sensors Health | Highest (C) | Smallest Gap (C) | Over Threshold | Fans Health |
+--------------------------------+----------------+-------------+------------------+----------------+-------------+
| comp-4-p2b-eu-spdc-WMP240400FM | True           | 72          | 18               | 0              | True        | 
| comp-6-p2b-eu-spdc-WMP24040059 | True           | 69          | 21               | 0              | True        | 
+--------------------------------+----------------+-------------+------------------+----------------+-------------+

Thermal Sensor [#42]
--------------------

+--------------------------------+------------------+---------+--------+------------------+-----------------+---------------------------+
| Server                         | Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+--------------------------------+------------------+---------+--------+------------------+-----------------+---------------------------+
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 72              | 90                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | P1_TEMP_SENS     | Enabled | OK     | CPU              | 69              | 100                       | 
| comp-4-p2b-eu-spdc-WMP240400FM | P2_TEMP_SENS     | Enabled | OK     | CPU              | 63.5            | 100                       | 
| comp-4-p2b-eu-spdc-WMP240400FM | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 50              | 85                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 42              | 65                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 28              | 65                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 38              | 70                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 42              | 70                        | 
| comp-4-p2b-eu-spdc-WMP240400FM | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 39              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 39              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 39              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 39              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 40              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 38              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 69              | 90                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 47.5            | 100                       | 
| comp-6-p2b-eu-spdc-WMP24040059 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 42.5            | 100                       | 
| comp-6-p2b-eu-spdc-WMP24040059 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 39              | 85                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 30              | 65                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 29              | 65                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 38              | 70                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 41              | 70                        | 
| comp-6-p2b-eu-spdc-WMP24040059 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        | 
+--------------------------------+------------------+---------+--------+------------------+-----------------+---------------------------+

Thermal Fan [#28]
-----------------

+--------------------------------+-----------------+---------+--------+-----------+
| Server                         | Fan Name        | State   | Health | Value     |
+--------------------------------+-----------------+---------+--------+-----------+
| comp-4-p2b-eu-spdc-WMP240400FM | MOD1_FAN1_SPEED | Enabled | OK     | 10500 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD1_FAN2_SPEED | Enabled | OK     | 11227 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD2_FAN1_SPEED | Enabled | OK     | 10920 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD2_FAN2_SPEED | Enabled | OK     | 10712 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD3_FAN1_SPEED | Enabled | OK     | 10500 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD3_FAN2_SPEED | Enabled | OK     | 10712 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD4_FAN1_SPEED | Enabled | OK     | 10500 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD4_FAN2_SPEED | Enabled | OK     | 11227 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD5_FAN1_SPEED | Enabled | OK     | 10500 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD5_FAN2_SPEED | Enabled | OK     | 11227 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD6_FAN1_SPEED | Enabled | OK     | 10500 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD6_FAN2_SPEED | Enabled | OK     | 10712 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD7_FAN1_SPEED | Enabled | OK     | 10080 RPM | 
| comp-4-p2b-eu-spdc-WMP240400FM | MOD7_FAN2_SPEED | Enabled | OK     | 11227 RPM | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD1_FAN1_SPEED | Enabled | OK     | 3360 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD1_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD2_FAN1_SPEED | Enabled | OK     | 3255 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD2_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD3_FAN1_SPEED | Enabled | OK     | 3255 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD3_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD4_FAN1_SPEED | Enabled | OK     | 3255 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD4_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD5_FAN1_SPEED | Enabled | OK     | 3255 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD5_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD6_FAN1_SPEED | Enabled | OK     | 3255 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD6_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD7_FAN1_SPEED | Enabled | OK     | 3360 RPM  | 
| comp-6-p2b-eu-spdc-WMP24040059 | MOD7_FAN2_SPEED | Enabled | OK     | 3296 RPM  | 
+--------------------------------+-----------------+---------+--------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test-env -v env

{
    "duration": 19732,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 5563
    },
    "redfish": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 6,
        "disconnect": 0,
        "path": 16,
        "connect_time": 7401,
        "disconnect_time": 0,
        "path_time": 5030,
        "total_time": 12431
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
        "lines": 35
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:21:20.005616	True	2459	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:21:21.601632	True	1593	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:21:23.173845	True	1511	12	isctl get compute blade   -o json --top 100


Log: redfish
-------------

2023-12-03 15:21:24.857060	True	1651	connect 10.58.50.44
2023-12-03 15:21:24.997266	True	136	10.58.50.44:/redfish/v1/Systems
2023-12-03 15:21:25.089327	True	77	10.58.50.44:/redfish/v1/Chassis
2023-12-03 15:21:25.356885	True	255	10.58.50.44:/redfish/v1/Chassis/1
2023-12-03 15:21:26.043677	True	670	10.58.50.44:/redfish/v1/Chassis/1/Power
2023-12-03 15:21:27.647947	True	1570	connect 10.58.50.46
2023-12-03 15:21:27.710522	True	61	10.58.50.46:/redfish/v1/Systems
2023-12-03 15:21:27.780341	True	58	10.58.50.46:/redfish/v1/Chassis
2023-12-03 15:21:27.913421	True	123	10.58.50.46:/redfish/v1/Chassis/1
2023-12-03 15:21:28.586738	True	657	10.58.50.46:/redfish/v1/Chassis/1/Power
2023-12-03 15:21:30.348937	True	1734	connect 10.58.50.44
2023-12-03 15:21:30.477052	True	124	10.58.50.44:/redfish/v1/Systems
2023-12-03 15:21:30.567924	True	73	10.58.50.44:/redfish/v1/Chassis
2023-12-03 15:21:31.001099	True	424	disconnect 10.58.50.46
2023-12-03 15:21:31.203884	True	193	10.58.50.44:/redfish/v1/Chassis/1
2023-12-03 15:21:32.411161	True	1196	10.58.50.44:/redfish/v1/Chassis/1/Thermal
2023-12-03 15:21:34.024024	True	1574	connect 10.58.50.46
2023-12-03 15:21:34.087636	True	60	10.58.50.46:/redfish/v1/Systems
2023-12-03 15:21:34.157574	True	61	10.58.50.46:/redfish/v1/Chassis
2023-12-03 15:21:34.292640	True	125	10.58.50.46:/redfish/v1/Chassis/1
2023-12-03 15:21:35.471596	True	1161	10.58.50.46:/redfish/v1/Chassis/1/Thermal
2023-12-03 15:21:35.958151	True	448	disconnect 10.58.50.46
```

[[Back]](./ServerInventory.md)