# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

```
# iserver get redfish endpoint
    --cache ucsc-c240-m5sx-wzp23450c8k-4.1.3d-on
    --type ucsc
    --ip 10.58.50.51
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
| DDR4_P1_A1_TMP    | Enabled  | OK      | Memory            | 26               | 85                         | 
| DDR4_P1_B1_TMP    | Enabled  | OK      | Memory            | 26               | 85                         | 
| DDR4_P1_C1_TMP    | Enabled  | OK      | Memory            | 26               | 85                         | 
| DDR4_P1_D1_TMP    | Enabled  | OK      | Memory            | 24               | 85                         | 
| DDR4_P1_E1_TMP    | Enabled  | OK      | Memory            | 25               | 85                         | 
| DDR4_P1_F1_TMP    | Enabled  | OK      | Memory            | 25               | 85                         | 
| DDR4_P2_G1_TMP    | Enabled  | OK      | Memory            | 24               | 85                         | 
| DDR4_P2_H1_TMP    | Enabled  | OK      | Memory            | 24               | 85                         | 
| DDR4_P2_J1_TMP    | Enabled  | OK      | Memory            | 24               | 85                         | 
| DDR4_P2_K1_TMP    | Enabled  | OK      | Memory            | 26               | 85                         | 
| DDR4_P2_L1_TMP    | Enabled  | OK      | Memory            | 26               | 85                         | 
| DDR4_P2_M1_TMP    | Enabled  | OK      | Memory            | 25               | 85                         | 
| MLOM_TEMP         | Enabled  | OK      | NetworkingDevice  | 41               | 90                         | 
| P1_TEMP_SENS      | Enabled  | OK      | CPU               | 29.5             | 101                        | 
| P2_TEMP_SENS      | Enabled  | OK      | CPU               | 28.5             | 101                        | 
| PCH_TEMP_SENS     | Enabled  | OK      | SystemBoard       | 28               | 85                         | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply       | 26               | 65                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply       | 24               | 65                         | 
| RISER1_INLET_TMP  | Enabled  | OK      | SystemBoard       | 28               | 70                         | 
| RISER2_INLET_TMP  | Enabled  | OK      | SystemBoard       | 28               | 70                         | 
| RISER2_TEMP       | Enabled  | OK      | SystemBoard       | 23               | 70                         | 
| TEMP_SENS_FRONT   | Enabled  | OK      | SystemBoard       | 23               | 45                         | 
+-------------------+----------+---------+-------------------+------------------+----------------------------+

+------------------+----------+---------+-----------+
| Name             | State    | Health  | Value     |
+------------------+----------+---------+-----------+
| MOD1_FAN1_SPEED  | Enabled  | OK      | 5757 RPM  | 
| MOD1_FAN2_SPEED  | Enabled  | OK      | 5978 RPM  | 
| MOD2_FAN1_SPEED  | Enabled  | OK      | 5858 RPM  | 
| MOD2_FAN2_SPEED  | Enabled  | OK      | 5978 RPM  | 
| MOD3_FAN1_SPEED  | Enabled  | OK      | 5858 RPM  | 
| MOD3_FAN2_SPEED  | Enabled  | OK      | 5978 RPM  | 
| MOD4_FAN1_SPEED  | Enabled  | OK      | 5757 RPM  | 
| MOD4_FAN2_SPEED  | Enabled  | OK      | 5978 RPM  | 
| MOD5_FAN1_SPEED  | Enabled  | OK      | 5858 RPM  | 
| MOD5_FAN2_SPEED  | Enabled  | OK      | 5880 RPM  | 
| MOD6_FAN1_SPEED  | Enabled  | OK      | 5858 RPM  | 
| MOD6_FAN2_SPEED  | Enabled  | OK      | 5978 RPM  | 
| MOD7_FAN1_SPEED  | Absent   |         |           | 
+------------------+----------+---------+-----------+
```