# Thermal Template

[[Next]](./TemplateAccess.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v thermal

Thermal Summary
---------------
- Sensors Health   : True
- Highest (C)      : 62
- Smallest Gap (C) : 18
- Over Threshold   : 0
- Fans Health      : True


+----+------------------+---------+--------+------------------+-----------------+---------------------------+
| ID | Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+----+------------------+---------+--------+------------------+-----------------+---------------------------+
| 1  | DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| 2  | DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 31              | 85                        | 
| 3  | DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 31              | 85                        | 
| 4  | DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| 5  | DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 33              | 85                        | 
| 6  | DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| 7  | DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 30              | 85                        | 
| 8  | DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 30              | 85                        | 
| 9  | DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 32              | 85                        | 
| 10 | DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 30              | 85                        | 
| 11 | DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 30              | 85                        | 
| 12 | DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 30              | 85                        | 
| 13 | MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 62              | 90                        | 
| 14 | P1_TEMP_SENS     | Enabled | OK     | CPU              | 44.5            | 100                       | 
| 15 | P2_TEMP_SENS     | Enabled | OK     | CPU              | 42              | 100                       | 
| 16 | PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 36              | 85                        |
| 17 | PCIE_SWITCH_TMP  | Enabled | OK     | SystemBoard      | 43              | 100                       |
| 18 | PSU1_TEMP        | Enabled | OK     | PowerSupply      | 26              | 65                        |
| 19 | PSU2_TEMP        | Enabled | OK     | PowerSupply      | 22              | 65                        |
| 20 | RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 37              | 70                        |
| 21 | RISER1_TEMP      | Enabled | OK     | SystemBoard      | 29              | 70                        |
| 22 | RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 35              | 70                        |
| 23 | RISER2_TEMP      | Enabled | OK     | SystemBoard      | 30              | 70                        |
| 24 | TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 27              | 45                        |
+----+------------------+---------+--------+------------------+-----------------+---------------------------+

+----+-----------------+---------+--------+----------+
| ID | Fan Name        | State   | Health | Value    |
+----+-----------------+---------+--------+----------+
| 1  | MOD1_FAN1_SPEED | Enabled | OK     | 6868 RPM |
| 2  | MOD1_FAN2_SPEED | Enabled | OK     | 7350 RPM |
| 3  | MOD2_FAN1_SPEED | Enabled | OK     | 6868 RPM |
| 4  | MOD2_FAN2_SPEED | Enabled | OK     | 7056 RPM |
| 5  | MOD3_FAN1_SPEED | Enabled | OK     | 7070 RPM |
| 6  | MOD3_FAN2_SPEED | Enabled | OK     | 7056 RPM |
| 7  | MOD4_FAN1_SPEED | Enabled | OK     | 6868 RPM |
| 8  | MOD4_FAN2_SPEED | Enabled | OK     | 7350 RPM |
| 9  | MOD5_FAN1_SPEED | Enabled | OK     | 7070 RPM |
| 10 | MOD5_FAN2_SPEED | Enabled | OK     | 7056 RPM |
| 11 | MOD6_FAN1_SPEED | Enabled | OK     | 6868 RPM |
| 12 | MOD6_FAN2_SPEED | Enabled | OK     | 7056 RPM |
| 13 | MOD7_FAN1_SPEED | Absent  |        |          |
+----+-----------------+---------+--------+----------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)