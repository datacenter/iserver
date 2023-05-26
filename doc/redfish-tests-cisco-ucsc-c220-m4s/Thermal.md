# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSC-C220-M4S

```
# iserver get redfish endpoint
    --cache ucsc-ucs-c220-m4s-fch2017v24j-4.1.2g-off
    --type ucsc
    --ip 10.58.50.59
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
| FP_TEMP_SENSOR    | Enabled  | OK      | Front             | 19               | 45                         | 
| MLOM_TMP          | Enabled  | OK      | NetworkingDevice  | 27               | 90                         | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply       | 33               | 65                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply       | 32               | 65                         | 
| RISER1_INLET_TMP  | Enabled  | OK      | SystemBoard       | 29               | 70                         | 
| RISER1_OUTLETTMP  | Enabled  | OK      | SystemBoard       | 33               | 70                         | 
| RISER2_INLET_TMP  | Enabled  | OK      | SystemBoard       | 32               | 70                         | 
| RISER2_OUTLETTMP  | Enabled  | OK      | SystemBoard       | 36               | 70                         | 
+-------------------+----------+---------+-------------------+------------------+----------------------------+

+-------+--------+---------+--------+
| Name  | State  | Health  | Value  |
+-------+--------+---------+--------+
+-------+--------+---------+--------+
```