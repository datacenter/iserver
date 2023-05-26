# Redfish Template Power

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
    --template power

Power Consumption (Watt)
------------------------
- Current : 260
- Average : 259
- Max     : 288
- Min     : 175


+-------+----------+---------+---------------------+-------------------+
| Name  | State    | Health  | Volts               | Upper Threshold   |
+-------+----------+---------+---------------------+-------------------+
| P12V  | Enabled  | OK      | 12.095000267028809  | 12.6850004196167  | 
+-------+----------+---------+---------------------+-------------------+
```