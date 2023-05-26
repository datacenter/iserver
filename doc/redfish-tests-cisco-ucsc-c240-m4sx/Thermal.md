# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

```
# iserver get redfish endpoint
    --cache ucsc-ucs-c240-m4sx-fch2017v1j7-4.1.2g-off
    --type ucsc
    --ip 10.58.50.48
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
| FP_TEMP_SENSOR    | Enabled  | OK      | Front             | 21               | 45                         | 
| MLOM_TMP          | Enabled  | OK      | NetworkingDevice  | 24               | 90                         | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply       | 28               | 65                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply       | 27               | 65                         | 
| RISER1_INLET_TMP  | Enabled  | OK      | SystemBoard       | 26               | 70                         | 
| RISER1_OUTLETTMP  | Enabled  | OK      | SystemBoard       | 32               | 70                         | 
| RISER2_INLET_TMP  | Enabled  | OK      | SystemBoard       | 27               | 70                         | 
| RISER2_OUTLETTMP  | Enabled  | OK      | SystemBoard       | 28               | 70                         | 
+-------------------+----------+---------+-------------------+------------------+----------------------------+

+-------+--------+---------+--------+
| Name  | State  | Health  | Value  |
+-------+--------+---------+--------+
+-------+--------+---------+--------+
```