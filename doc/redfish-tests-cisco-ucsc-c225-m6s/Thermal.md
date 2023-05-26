# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSC-C225-M6S

```
# iserver get redfish endpoint
    --cache ucsc-c225-m6s-wzp262207w0-4.2.2a-off
    --type ucsc
    --ip 10.90.90.133
    --username admin
    --password ******
    --template thermal

Summary
-------
- State  : Enabled
- Health : OK


+------------------+----------+---------+--------------+------------------+----------------------------+
| Name             | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+------------------+----------+---------+--------------+------------------+----------------------------+
| PSU1_TEMP        | Enabled  | OK      | PowerSupply  | 26               | 65                         | 
| PSU2_TEMP        | Enabled  | OK      | PowerSupply  | 24               | 65                         | 
| TEMP_SENS_FRONT  | Enabled  | OK      | SystemBoard  | 22               | 45                         | 
+------------------+----------+---------+--------------+------------------+----------------------------+

+-------+--------+---------+--------+
| Name  | State  | Health  | Value  |
+-------+--------+---------+--------+
+-------+--------+---------+--------+
```