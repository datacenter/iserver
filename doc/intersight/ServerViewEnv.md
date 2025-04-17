# Intersight Server

## env view

```
# iserver get server --group test-env -v env

iaccount demo (cache: any)
Select servers...
Selected servers: 2
Collect server api objects...


Power Consumption [#2]
----------------------

+-----------+---------+-----+---------+-----+--------------+
| Server    | Current | Min | Average | Max | Limit action |
+-----------+---------+-----+---------+-----+--------------+
| Server590 | 324     | 182 | 323     | 563 | NoAction     |
| Server396 | 216     | 175 | 214     | 374 | NoAction     |
+-----------+---------+-----+---------+-----+--------------+

Power Sensor [#8]
-----------------

+-----------+----------------+---------+--------+--------+-----------------+
| Server    | Sensor Name    | State   | Health | Volts  | Upper Threshold |
+-----------+----------------+---------+--------+--------+-----------------+
| Server590 | PSU1_VOUT      | Enabled | OK     | 12.2   | 14              |
| Server590 | PSU2_VOUT      | Enabled | OK     | 12.2   | 14              |
| Server590 | P12V           | Enabled | OK     | 11.774 | 13.166          |
| Server590 | P3V_BAT_SCALED | Enabled | OK     | 3.026  | 3.588           |
| Server396 | PSU1_VOUT      | Enabled | OK     | 12.1   | 14              |
| Server396 | PSU2_VOUT      | Enabled | OK     | 12.2   | 14              |
| Server396 | P12V           | Enabled | OK     | 11.832 | 13.166          |
| Server396 | P3V_BAT_SCALED | Enabled | OK     | 3.042  | 3.588           |
+-----------+----------------+---------+--------+--------+-----------------+

Power Supply [#4]
-----------------

+-----------+----------+---------+--------+-------------+------------+---------------+--------------+---------+---------+----------+----------+
| Server    | PSU Name | State   | Health | Serial      | Firmware   | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+-----------+----------+---------+--------+-------------+------------+---------------+--------------+---------+---------+----------+----------+
| Server590 | PSU1     | Enabled | OK     | Serial590   | Version-42 | 159           | 175          | 264     | 180     | 63       | 47       |
| Server590 | PSU2     | Enabled | OK     | Serial590   | Version-43 | 144           | 170          | 264     | 180     | 63       | 47       |
| Server396 | PSU1     | Enabled | OK     | Serial396   | Version-85 | 102           | 115          | 264     | 180     | 63       | 47       |
| Server396 | PSU2     | Enabled | OK     | Serial396   | Version-14 | 94            | 111          | 264     | 180     | 63       | 47       |
+-----------+----------+---------+--------+-------------+------------+---------------+--------------+---------+---------+----------+----------+

Thermal Summary [#2]
--------------------

+-----------+----------------+-------------+------------------+----------------+-------------+
| Server    | Sensors Health | Highest (C) | Smallest Gap (C) | Over Threshold | Fans Health |
+-----------+----------------+-------------+------------------+----------------+-------------+
| Server590 | True           | 67          | 22               | 0              | True        |
| Server396 | True           | 61          | 22               | 0              | True        |
+-----------+----------------+-------------+------------------+----------------+-------------+

Thermal Sensor [#42]
--------------------

+-----------+------------------+---------+--------+------------------+-----------------+---------------------------+
| Server    | Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+-----------+------------------+---------+--------+------------------+-----------------+---------------------------+
| Server590 | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 37              | 85                        |
| Server590 | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 36              | 85                        |
| Server590 | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 35              | 85                        |
| Server590 | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 37              | 85                        |
| Server590 | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 36              | 85                        |
| Server590 | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 35              | 85                        |
| Server590 | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 33              | 85                        |
| Server590 | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 32              | 85                        |
| Server590 | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 33              | 85                        |
| Server590 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 32              | 85                        |
| Server590 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 32              | 85                        |
| Server590 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 32              | 85                        |
| Server590 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 67              | 90                        |
| Server590 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 67              | 100                       |
| Server590 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 58.5            | 100                       |
| Server590 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 49              | 85                        |
| Server590 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 39              | 65                        |
| Server590 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 27              | 65                        |
| Server590 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 37              | 70                        |
| Server590 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 41              | 70                        |
| Server590 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        |
| Server396 | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 36              | 85                        |
| Server396 | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 36              | 85                        |
| Server396 | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 35              | 85                        |
| Server396 | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 35              | 85                        |
| Server396 | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 36              | 85                        |
| Server396 | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 37              | 85                        |
| Server396 | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 32              | 85                        |
| Server396 | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 33              | 85                        |
| Server396 | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 34              | 85                        |
| Server396 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 31              | 85                        |
| Server396 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 31              | 85                        |
| Server396 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 32              | 85                        |
| Server396 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 61              | 90                        |
| Server396 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       |
| Server396 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 36              | 100                       |
| Server396 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 36              | 85                        |
| Server396 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 29              | 65                        |
| Server396 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 25              | 65                        |
| Server396 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 34              | 70                        |
| Server396 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 39              | 70                        |
| Server396 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        |
+-----------+------------------+---------+--------+------------------+-----------------+---------------------------+

Thermal Fan [#28]
-----------------

+-----------+-----------------+---------+--------+----------+
| Server    | Fan Name        | State   | Health | Value    |
+-----------+-----------------+---------+--------+----------+
| Server590 | MOD1_FAN1_SPEED | Enabled | OK     | 7140 RPM |
| Server590 | MOD1_FAN2_SPEED | Enabled | OK     | 7210 RPM |
| Server590 | MOD2_FAN1_SPEED | Enabled | OK     | 7350 RPM |
| Server590 | MOD2_FAN2_SPEED | Enabled | OK     | 7416 RPM |
| Server590 | MOD3_FAN1_SPEED | Enabled | OK     | 7350 RPM |
| Server590 | MOD3_FAN2_SPEED | Enabled | OK     | 7416 RPM |
| Server590 | MOD4_FAN1_SPEED | Enabled | OK     | 7350 RPM |
| Server590 | MOD4_FAN2_SPEED | Enabled | OK     | 7416 RPM |
| Server590 | MOD5_FAN1_SPEED | Enabled | OK     | 7140 RPM |
| Server590 | MOD5_FAN2_SPEED | Enabled | OK     | 7210 RPM |
| Server590 | MOD6_FAN1_SPEED | Enabled | OK     | 7140 RPM |
| Server590 | MOD6_FAN2_SPEED | Enabled | OK     | 7416 RPM |
| Server590 | MOD7_FAN1_SPEED | Enabled | OK     | 7140 RPM |
| Server590 | MOD7_FAN2_SPEED | Enabled | OK     | 7416 RPM |
| Server396 | MOD1_FAN1_SPEED | Enabled | OK     | 6405 RPM |
| Server396 | MOD1_FAN2_SPEED | Enabled | OK     | 6592 RPM |
| Server396 | MOD2_FAN1_SPEED | Enabled | OK     | 6405 RPM |
| Server396 | MOD2_FAN2_SPEED | Enabled | OK     | 6489 RPM |
| Server396 | MOD3_FAN1_SPEED | Enabled | OK     | 6405 RPM |
| Server396 | MOD3_FAN2_SPEED | Enabled | OK     | 6489 RPM |
| Server396 | MOD4_FAN1_SPEED | Enabled | OK     | 6405 RPM |
| Server396 | MOD4_FAN2_SPEED | Enabled | OK     | 6489 RPM |
| Server396 | MOD5_FAN1_SPEED | Enabled | OK     | 6300 RPM |
| Server396 | MOD5_FAN2_SPEED | Enabled | OK     | 6592 RPM |
| Server396 | MOD6_FAN1_SPEED | Enabled | OK     | 6405 RPM |
| Server396 | MOD6_FAN2_SPEED | Enabled | OK     | 6489 RPM |
| Server396 | MOD7_FAN1_SPEED | Enabled | OK     | 6615 RPM |
| Server396 | MOD7_FAN2_SPEED | Enabled | OK     | 6489 RPM |
+-----------+-----------------+---------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)