# Intersight Server

## power view

```
# iserver get server --group test-env -v power

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Power Consumption [#2]
----------------------

+--------------------------------+---------+-----+---------+-----+--------------+
| Server                         | Current | Min | Average | Max | Limit action |
+--------------------------------+---------+-----+---------+-----+--------------+
| comp-4-p2b-eu-spdc-WMP240400FM | 270     | 121 | 309     | 743 | NoAction     | 
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
| comp-4-p2b-eu-spdc-WMP240400FM | PSU1     | Enabled | OK     | APS240201EL | 10252046 | 134           | 149          | 264     | 180     | 63       | 47       | 
| comp-4-p2b-eu-spdc-WMP240400FM | PSU2     | Enabled | OK     | ART2601F4S6 | 10252046 | 152           | 143          | 264     | 180     | 63       | 47       | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU1     | Enabled | OK     | APS240201EX | 10252041 | 91            | 106          | 264     | 180     | 63       | 47       | 
| comp-6-p2b-eu-spdc-WMP24040059 | PSU2     | Enabled | OK     | ART2601F4SS | 10252046 | 87            | 101          | 264     | 180     | 63       | 47       | 
+--------------------------------+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test-env -v power

{
    "duration": 16620,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 5747
    },
    "redfish": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 3,
        "disconnect": 0,
        "path": 8,
        "connect_time": 4056,
        "disconnect_time": 0,
        "path_time": 5219,
        "total_time": 9275
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

2023-12-03 15:27:07.977952	True	2698	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:27:09.391513	True	1411	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:27:11.095698	True	1638	12	isctl get compute blade   -o json --top 100


Log: redfish
-------------

2023-12-03 15:27:12.825310	True	1688	connect 10.58.50.44
2023-12-03 15:27:12.944274	True	116	10.58.50.44:/redfish/v1/Systems
2023-12-03 15:27:13.101604	True	147	10.58.50.44:/redfish/v1/Chassis
2023-12-03 15:27:13.253765	True	135	10.58.50.44:/redfish/v1/Chassis/1
2023-12-03 15:27:17.055750	True	3786	10.58.50.44:/redfish/v1/Chassis/1/Power
2023-12-03 15:27:18.699685	True	1610	connect 10.58.50.46
2023-12-03 15:27:18.761474	True	60	10.58.50.46:/redfish/v1/Systems
2023-12-03 15:27:18.844652	True	63	10.58.50.46:/redfish/v1/Chassis
2023-12-03 15:27:18.980832	True	121	10.58.50.46:/redfish/v1/Chassis/1
2023-12-03 15:27:19.788379	True	791	10.58.50.46:/redfish/v1/Chassis/1/Power
2023-12-03 15:27:20.567668	True	758	disconnect 10.58.50.46
```

[[Back]](./ServerInventory.md)