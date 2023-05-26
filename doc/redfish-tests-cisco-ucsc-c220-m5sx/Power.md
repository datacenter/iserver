# Redfish Template Power

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
    --template power

Power Consumption (Watt)
------------------------
- Current      : 252
- Min          : 172
- Average      : 268
- Max          : 366
- Limit action : NoAction


+-----------------+----------+---------+---------+------------------+
| Name            | State    | Health  | Volts   | Upper Threshold  |
+-----------------+----------+---------+---------+------------------+
| PSU1_VOUT       | Enabled  | OK      | 12.1    | 14               | 
| PSU2_VOUT       | Enabled  | OK      | 12.1    | 14               | 
| P12V            | Enabled  | OK      | 11.774  | 13.166           | 
| P3V_BAT_SCALED  | Enabled  | OK      | 2.933   | 3.588            | 
+-----------------+----------+---------+---------+------------------+

+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| Name  | State    | Health  | Serial       | Firmware  | Output (Watt)  | Input (Watt)  | Max (V)  | Min (V)  | Max (Hz)  | Min (Hz)  |
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| PSU1  | Enabled  | OK      | ART2302FHS5  | 12002217  | 112            | 126           | 264      | 90       | 63        | 47        | 
| PSU2  | Enabled  | OK      | ART2302FHS2  | 12002217  | 121            | 136           | 264      | 90       | 63        | 47        | 
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
```