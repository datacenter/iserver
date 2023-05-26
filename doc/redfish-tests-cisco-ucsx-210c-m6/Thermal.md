# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

```
# iserver get redfish endpoint
    --cache ucsc-ucsx-210c-m6-fch25337ehm-5.0.1f-on
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1
    --template thermal

Summary
-------
- State  : Enabled
- Health : OK


+---------------------+----------+---------+--------------+------------------+----------------------------+
| Name                | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+---------------------+----------+---------+--------------+------------------+----------------------------+
| DDR4_P1_A1_TMP      | Enabled  | OK      | SystemBoard  | 26               | 85                         | 
| DDR4_P1_A2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_B1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_B2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_C1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_C2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_D1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_D2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_E1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_E2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_F1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_F2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_G1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_G2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_H1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_H2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_A1_TMP      | Enabled  | OK      | SystemBoard  | 27               | 85                         | 
| DDR4_P2_A2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_B1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_B2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_C1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_C2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_D1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_D2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_E1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_E2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_F1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_F2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_G1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_G2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_H1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_H2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| NOEVALLEY_PD0_TEMP  | Enabled  | OK      | SystemBoard  | 38               |                            | 
| NOEVALLEY_PD1_TEMP  | Enabled  | OK      | SystemBoard  | 37               |                            | 
| P1_TEMP_SENS        | Enabled  | OK      | CPU          | 43.5             | 101                        | 
| P2_TEMP_SENS        | Enabled  | OK      | CPU          | 53               | 101                        | 
| PWR_BRICK_TEMP      | Enabled  | OK      | SystemBoard  | 52               |                            | 
| TEMP_FRONT          | Enabled  | OK      | SystemBoard  | 15               | 45                         | 
| TEMP_REAR_BOT       | Enabled  | OK      | SystemBoard  | 21               |                            | 
| TEMP_REAR_MID       | Enabled  | OK      | SystemBoard  | 33               |                            | 
| TEMP_REAR_TOP       | Enabled  | OK      | SystemBoard  | 25               |                            | 
+---------------------+----------+---------+--------------+------------------+----------------------------+
```