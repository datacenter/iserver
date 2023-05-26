# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

```
# iserver get redfish endpoint
    --cache ucsc-c240-m5sn-wzp23400ak4-4.1.3d-on
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --template thermal

Summary
-------
- State  : Enabled
- Health : OK


+-------------------+----------+---------+-------------------+------------------+----------------------------+
| Name              | State    | Health  | Location          | Value (Celcius)  | Upper Threshold (Celcius)  |
+-------------------+----------+---------+-------------------+------------------+----------------------------+
| DDR4_P1_A1_TMP    | Enabled  | OK      | Memory            | 30               | 85                         | 
| DDR4_P1_B1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P1_C1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P1_D1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P1_E1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P1_F1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_G1_TMP    | Enabled  | OK      | Memory            | 28               | 85                         | 
| DDR4_P2_H1_TMP    | Enabled  | OK      | Memory            | 28               | 85                         | 
| DDR4_P2_J1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_K1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_L1_TMP    | Enabled  | OK      | Memory            | 28               | 85                         | 
| DDR4_P2_M1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| MLOM_TEMP         | Enabled  | OK      | NetworkingDevice  | 54               | 90                         | 
| P1_TEMP_SENS      | Enabled  | OK      | CPU               | 40               | 100                        | 
| P2_TEMP_SENS      | Enabled  | OK      | CPU               | 43               | 100                        | 
| PCH_TEMP_SENS     | Enabled  | OK      | SystemBoard       | 34               | 85                         | 
| PCIE_SWITCH_TMP   | Enabled  | OK      | SystemBoard       | 40               | 100                        | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply       | 24               | 65                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply       | 21               | 65                         | 
| RISER1_INLET_TMP  | Enabled  | OK      | SystemBoard       | 33               | 70                         | 
| RISER1_TEMP       | Enabled  | OK      | SystemBoard       | 24               | 70                         | 
| RISER2_INLET_TMP  | Enabled  | OK      | SystemBoard       | 33               | 70                         | 
| RISER2_TEMP       | Enabled  | OK      | SystemBoard       | 29               | 70                         | 
| TEMP_SENS_FRONT   | Enabled  | OK      | SystemBoard       | 26               | 45                         | 
+-------------------+----------+---------+-------------------+------------------+----------------------------+

+------------------+----------+---------+-----------+
| Name             | State    | Health  | Value     |
+------------------+----------+---------+-----------+
| MOD1_FAN1_SPEED  | Enabled  | OK      | 7070 RPM  | 
| MOD1_FAN2_SPEED  | Enabled  | OK      | 7350 RPM  | 
| MOD2_FAN1_SPEED  | Enabled  | OK      | 6868 RPM  | 
| MOD2_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD3_FAN1_SPEED  | Enabled  | OK      | 6868 RPM  | 
| MOD3_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD4_FAN1_SPEED  | Enabled  | OK      | 7070 RPM  | 
| MOD4_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD5_FAN1_SPEED  | Enabled  | OK      | 6868 RPM  | 
| MOD5_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD6_FAN1_SPEED  | Enabled  | OK      | 7070 RPM  | 
| MOD6_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD7_FAN1_SPEED  | Absent   |         |           | 
+------------------+----------+---------+-----------+
```