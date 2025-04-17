# Intersight Server

## thermal view

```
# iserver get server
    --group test-env -v thermal
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 2
Collect server api objects...


Thermal Summary [#2]
--------------------

+-----------+----------------+-------------+------------------+----------------+-------------+
| Server    | Sensors Health | Highest (C) | Smallest Gap (C) | Over Threshold | Fans Health |
+-----------+----------------+-------------+------------------+----------------+-------------+
| Server324 | True           | 67          | 22               | 0              | True        | 
| Server278 | True           | 61          | 22               | 0              | True        | 
+-----------+----------------+-------------+------------------+----------------+-------------+

Thermal Sensor [#42]
--------------------

+-----------+------------------+---------+--------+------------------+-----------------+---------------------------+
| Server    | Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+-----------+------------------+---------+--------+------------------+-----------------+---------------------------+
| Server324 | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| Server324 | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| Server324 | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| Server324 | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| Server324 | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| Server324 | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| Server324 | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| Server324 | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| Server324 | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| Server324 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| Server324 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| Server324 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| Server324 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 67              | 90                        | 
| Server324 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 67              | 100                       | 
| Server324 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 58.5            | 100                       | 
| Server324 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 49              | 85                        | 
| Server324 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 39              | 65                        | 
| Server324 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 27              | 65                        | 
| Server324 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 37              | 70                        | 
| Server324 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 41              | 70                        | 
| Server324 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        | 
| Server278 | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| Server278 | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| Server278 | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| Server278 | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 35              | 85                        | 
| Server278 | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 36              | 85                        | 
| Server278 | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 37              | 85                        | 
| Server278 | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| Server278 | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| Server278 | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 34              | 85                        | 
| Server278 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 31              | 85                        | 
| Server278 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 31              | 85                        | 
| Server278 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| Server278 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 61              | 90                        | 
| Server278 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       | 
| Server278 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 36              | 100                       | 
| Server278 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 36              | 85                        | 
| Server278 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 29              | 65                        | 
| Server278 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 25              | 65                        | 
| Server278 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 34              | 70                        | 
| Server278 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 39              | 70                        | 
| Server278 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 23              | 45                        | 
+-----------+------------------+---------+--------+------------------+-----------------+---------------------------+

Thermal Fan [#28]
-----------------

+-----------+-----------------+---------+--------+----------+
| Server    | Fan Name        | State   | Health | Value    |
+-----------+-----------------+---------+--------+----------+
| Server324 | MOD1_FAN1_SPEED | Enabled | OK     | 7140 RPM | 
| Server324 | MOD1_FAN2_SPEED | Enabled | OK     | 7210 RPM | 
| Server324 | MOD2_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| Server324 | MOD2_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| Server324 | MOD3_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| Server324 | MOD3_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| Server324 | MOD4_FAN1_SPEED | Enabled | OK     | 7350 RPM | 
| Server324 | MOD4_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| Server324 | MOD5_FAN1_SPEED | Enabled | OK     | 7140 RPM | 
| Server324 | MOD5_FAN2_SPEED | Enabled | OK     | 7210 RPM | 
| Server324 | MOD6_FAN1_SPEED | Enabled | OK     | 7140 RPM | 
| Server324 | MOD6_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| Server324 | MOD7_FAN1_SPEED | Enabled | OK     | 7140 RPM | 
| Server324 | MOD7_FAN2_SPEED | Enabled | OK     | 7416 RPM | 
| Server278 | MOD1_FAN1_SPEED | Enabled | OK     | 6405 RPM | 
| Server278 | MOD1_FAN2_SPEED | Enabled | OK     | 6592 RPM | 
| Server278 | MOD2_FAN1_SPEED | Enabled | OK     | 6405 RPM | 
| Server278 | MOD2_FAN2_SPEED | Enabled | OK     | 6489 RPM | 
| Server278 | MOD3_FAN1_SPEED | Enabled | OK     | 6405 RPM | 
| Server278 | MOD3_FAN2_SPEED | Enabled | OK     | 6489 RPM | 
| Server278 | MOD4_FAN1_SPEED | Enabled | OK     | 6405 RPM | 
| Server278 | MOD4_FAN2_SPEED | Enabled | OK     | 6489 RPM | 
| Server278 | MOD5_FAN1_SPEED | Enabled | OK     | 6300 RPM | 
| Server278 | MOD5_FAN2_SPEED | Enabled | OK     | 6592 RPM | 
| Server278 | MOD6_FAN1_SPEED | Enabled | OK     | 6405 RPM | 
| Server278 | MOD6_FAN2_SPEED | Enabled | OK     | 6489 RPM | 
| Server278 | MOD7_FAN1_SPEED | Enabled | OK     | 6615 RPM | 
| Server278 | MOD7_FAN2_SPEED | Enabled | OK     | 6489 RPM | 
+-----------+-----------------+---------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)