# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSS-S3260

```
# iserver get redfish endpoint
    --cache ucsc-ucs-s3260-fch21067808--on
    --type ucsc
    --ip 10.58.50.34
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
| MOBO_L_BOT_TEMP   | Enabled  | OK      | SystemBoard  | 25               | 80                         | 
| MOBO_L_EXP_TEMP   | Enabled  | OK      | SystemBoard  | 34               | 90                         | 
| MOBO_L_IN_TEMP    | Enabled  | OK      | SystemBoard  | 21               | 45                         | 
| MOBO_L_MID_TEMP   | Enabled  | OK      | SystemBoard  | 22               | 60                         | 
| MOBO_L_OUT_TEMP   | Enabled  | OK      | SystemBoard  | 23               | 65                         | 
| MOBO_R_BOT_TEMP   | Enabled  | OK      | SystemBoard  | 25               | 80                         | 
| MOBO_R_EXP_TEMP   | Enabled  | OK      | SystemBoard  | 33               | 90                         | 
| MOBO_R_IN_TEMP    | Enabled  | OK      | SystemBoard  | 22               | 45                         | 
| MOBO_R_MID_TEMP   | Enabled  | OK      | SystemBoard  | 22               | 60                         | 
| MOBO_R_OUT_TEMP   | Enabled  | OK      | SystemBoard  | 26               | 65                         | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply  | 18               | 55                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply  | 20               | 55                         | 
| PSU3_TEMP         | Enabled  | OK      | PowerSupply  | 19               | 55                         | 
| PSU4_TEMP         | Enabled  | OK      | PowerSupply  | 17               | 55                         | 
| SIOC1_BACK_TEMP   | Enabled  | OK      | SystemBoard  | 29               | 80                         | 
| SIOC1_CMC_TEMP    | Enabled  | OK      | SystemBoard  | 42               | 85                         | 
| SIOC1_FRONT_TEMP  | Enabled  | OK      | SystemBoard  | 33               | 80                         | 
| SIOC1_MID_TEMP    | Enabled  | OK      | SystemBoard  | 32               | 80                         | 
| SIOC1_VIC_TEMP    | Enabled  | OK      | SystemBoard  | 34               | 80                         | 
+-------------------+----------+---------+--------------+------------------+----------------------------+

+-------------+----------+---------+-----------+
| Name        | State    | Health  | Value     |
+-------------+----------+---------+-----------+
| FAN1_SPEED  | Enabled  | OK      | 7920 RPM  | 
| FAN2_SPEED  | Enabled  | OK      | 7920 RPM  | 
| FAN3_SPEED  | Enabled  | OK      | 7920 RPM  | 
| FAN4_SPEED  | Enabled  | OK      | 7980 RPM  | 
| FAN5_SPEED  | Enabled  | OK      | 7920 RPM  | 
| FAN6_SPEED  | Enabled  | OK      | 7920 RPM  | 
| FAN7_SPEED  | Enabled  | OK      | 7920 RPM  | 
| FAN8_SPEED  | Enabled  | OK      | 8040 RPM  | 
+-------------+----------+---------+-----------+
```