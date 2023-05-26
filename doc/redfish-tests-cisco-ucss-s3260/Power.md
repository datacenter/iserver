# Redfish Template Power

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
    --template power

Power Consumption (Watt)
------------------------
- Current      : 392
- Min          : 249
- Average      : 361
- Max          : 642
- Limit action : N/A


+------------------+----------+---------+--------+------------------+
| Name             | State    | Health  | Volts  | Upper Threshold  |
+------------------+----------+---------+--------+------------------+
| SIOC1_P12V       | Enabled  | OK      | 12     | 12.72            | 
| SIOC1_P1V0       | Enabled  | OK      | 1      | 1.064            | 
| SIOC1_P1V2       | Enabled  | OK      | 1.2    | 1.272            | 
| SIOC1_P1V5       | Enabled  | OK      | 1.5    | 1.59             | 
| SIOC1_P2V5       | Enabled  | OK      | 2.492  | 2.646            | 
| SIOC1_P3V3       | Enabled  | OK      | 3.34   | 3.5              | 
| SIOC1_P12V_STBY  | Enabled  | OK      | 12.12  | 12.72            | 
| SIOC1_P3V3_STBY  | Enabled  | OK      | 3.36   | 3.46             | 
| PSU1_VIN         | Enabled  | OK      | 236    | 264              | 
| PSU2_VIN         | Enabled  | OK      | 238    | 264              | 
| PSU3_VIN         | Enabled  | OK      | 242    | 264              | 
| PSU4_VIN         | Enabled  | OK      | 244    | 264              | 
| P5V_1            | Enabled  | OK      | 5.01   | 5.64             | 
| P5V_2            | Enabled  | OK      | 5.01   | 5.64             | 
| P5V_3            | Enabled  | OK      | 5.01   | 5.64             | 
| P5V_4            | Enabled  | OK      | 5.01   | 5.64             | 
| P0V9_EXP1_VCORE  | Enabled  | OK      | 0.92   | 0.976            | 
| P0V9_EXP2_VCORE  | Enabled  | OK      | 0.92   | 0.976            | 
| P0V9_EXP1_AVD    | Enabled  | OK      | 0.92   | 0.976            | 
| P0V9_EXP2_AVD    | Enabled  | OK      | 0.936  | 0.976            | 
| PSU1_VOUT        | Enabled  | OK      | 12.2   | 14               | 
| PSU2_VOUT        | Enabled  | OK      | 12.1   | 14               | 
| PSU3_VOUT        | Enabled  | OK      | 12.1   | 14               | 
| PSU4_VOUT        | Enabled  | OK      | 12.1   | 14               | 
| SIOC1_RTC_BAT    | Enabled  | OK      | 3.14   | 3.42             | 
+------------------+----------+---------+--------+------------------+

+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| Name  | State    | Health  | Serial       | Firmware  | Output (Watt)  | Input (Watt)  | Max (V)  | Min (V)  | Max (Hz)  | Min (Hz)  |
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| PSU1  | Enabled  | N/A     | LIT20422447  | 10062019  | 96             | 103           | 264      | 180      | 63        | 47        | 
| PSU2  | Enabled  | N/A     | LIT2042245H  | 10062019  | 82             | 95            | 264      | 180      | 63        | 47        | 
| PSU3  | Enabled  | N/A     | LIT204224DH  | 10062019  | 89             | 109           | 264      | 180      | 63        | 47        | 
| PSU4  | Enabled  | N/A     | LIT2042243U  | 10062019  | 101            | 118           | 264      | 180      | 63        | 47        | 
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
```