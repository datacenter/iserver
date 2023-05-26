# Redfish Template Power

Vendor | Model
--- | ---
HPE | vServer

```
# iserver get redfish endpoint
    --cache hpe-proliant-dl360-gen10-plus-vyrbx9uj4s-2.55-on
    --type hpe
    --ip 10.58.24.211
    --port 49153
    --username administrator
    --password ******
    --template power

Power Consumption (Watt)
------------------------
- Current : 165
- Min     : 159
- Average : 167
- Max     : 270


+-----------------------+----------+---------+-----------------+-----------+----------------+------------+
| Name                  | State    | Health  | Serial          | Firmware  | Output (Watt)  | Input (V)  |
+-----------------------+----------+---------+-----------------+-----------+----------------+------------+
| HpeServerPowerSupply  | Enabled  | OK      | 5WBYE0D4DEF1FM  | 1.00      | 89             | 206        | 
| HpeServerPowerSupply  | Enabled  | OK      | 5WBYE0D4DEF1H5  | 1.00      | 76             | 205        | 
+-----------------------+----------+---------+-----------------+-----------+----------------+------------+
```