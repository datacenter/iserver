# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSC-C220-M5SX

```
# iserver get redfish endpoint
    --cache ucsc-c220-m5sx-wzp22490zcu-4.1.3d-on
    --type ucsc
    --ip 10.58.28.41
    --username admin
    --password ******
    --template thermal

Summary
-------
- State  : Enabled
- Health : OK


+-------------------+----------+---------+--------------+------------------+----------------------------+
| Name              | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+-------------------+----------+---------+--------------+------------------+----------------------------+
| DDR4_P1_A1_TMP    | Enabled  | OK      | Memory       | 46               | 85                         | 
| DDR4_P1_B1_TMP    | Enabled  | OK      | Memory       | 44               | 85                         | 
| DDR4_P1_D1_TMP    | Enabled  | OK      | Memory       | 45               | 85                         | 
| DDR4_P1_E1_TMP    | Enabled  | OK      | Memory       | 43               | 85                         | 
| DDR4_P2_G1_TMP    | Enabled  | OK      | Memory       | 42               | 85                         | 
| DDR4_P2_H1_TMP    | Enabled  | OK      | Memory       | 41               | 85                         | 
| DDR4_P2_K1_TMP    | Enabled  | OK      | Memory       | 40               | 85                         | 
| DDR4_P2_L1_TMP    | Enabled  | OK      | Memory       | 39               | 85                         | 
| P1_TEMP_SENS      | Enabled  | OK      | CPU          | 77.5             | 98                         | 
| P2_TEMP_SENS      | Enabled  | OK      | CPU          | 67               | 98                         | 
| PCH_TEMP_SENS     | Enabled  | OK      | SystemBoard  | 58               | 85                         | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply  | 40               | 65                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply  | 34               | 65                         | 
| RISER1_INLET_TMP  | Enabled  | OK      | SystemBoard  | 47               | 70                         | 
| RISER2_INLET_TMP  | Enabled  | OK      | SystemBoard  | 54               | 70                         | 
| TEMP_SENS_FRONT   | Enabled  | OK      | SystemBoard  | 24               | 45                         | 
+-------------------+----------+---------+--------------+------------------+----------------------------+

+------------------+----------+---------+-----------+
| Name             | State    | Health  | Value     |
+------------------+----------+---------+-----------+
| MOD1_FAN1_SPEED  | Enabled  | OK      | 4725 RPM  | 
| MOD1_FAN2_SPEED  | Enabled  | OK      | 4841 RPM  | 
| MOD2_FAN1_SPEED  | Enabled  | OK      | 4725 RPM  | 
| MOD2_FAN2_SPEED  | Enabled  | OK      | 4841 RPM  | 
| MOD3_FAN1_SPEED  | Enabled  | OK      | 4830 RPM  | 
| MOD3_FAN2_SPEED  | Enabled  | OK      | 4738 RPM  | 
| MOD4_FAN1_SPEED  | Enabled  | OK      | 4935 RPM  | 
| MOD4_FAN2_SPEED  | Enabled  | OK      | 4738 RPM  | 
| MOD5_FAN1_SPEED  | Enabled  | OK      | 4620 RPM  | 
| MOD5_FAN2_SPEED  | Enabled  | OK      | 4738 RPM  | 
| MOD6_FAN1_SPEED  | Enabled  | OK      | 4830 RPM  | 
| MOD6_FAN2_SPEED  | Enabled  | OK      | 4841 RPM  | 
| MOD7_FAN1_SPEED  | Enabled  | OK      | 4725 RPM  | 
| MOD7_FAN2_SPEED  | Enabled  | OK      | 4738 RPM  | 
+------------------+----------+---------+-----------+
```