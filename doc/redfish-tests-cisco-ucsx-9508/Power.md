# Redfish Template Power

Vendor | Model
--- | ---
Cisco | UCSX-9508

```
# iserver get redfish endpoint
    --cache chassis-UCSX-9508-fox2521p34m
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --template power

Power Control
-------------
- CurrentConsumedWatts : 659


+---------+----------+---------+-----------------------+-----------------------+-------------------+-------------------+----------------+----------------+
| Name    | State    | Health  | AverageConsumedWatts  | CurrentConsumedWatts  | MaxConsumedWatts  | MinConsumedWatts  | MaxPowerWatts  | MinPowerWatts  |
+---------+----------+---------+-----------------------+-----------------------+-------------------+-------------------+----------------+----------------+
| Blade1  | Enabled  | OK      | 259                   | 255                   | 288               | 175               | 1414           | 381            | 
| Blade2  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade3  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade4  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade5  | Enabled  | OK      | 263                   | 260                   | 288               | 13                | 1414           | 381            | 
| Blade6  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade7  | Enabled  | OK      | 143                   | 144                   | 171               | 13                | 1414           | 381            | 
| Blade8  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
+---------+----------+---------+-----------------------+-----------------------+-------------------+-------------------+----------------+----------------+

+-----------------+----------+--------------------+------------------+---------------+
| Name            | State    | Manufacturer       | Model            | SerialNumber  |
+-----------------+----------+--------------------+------------------+---------------+
| Power Supply 1  | Enabled  | Cisco Systems Inc  | UCSX-PSU-2800AC  | ART2510F5AT   | 
| Power Supply 2  | Absent   |                    |                  |               | 
| Power Supply 3  | Absent   |                    |                  |               | 
| Power Supply 4  | Enabled  | Cisco Systems Inc  | UCSX-PSU-2800AC  | ART2510F5AD   | 
| Power Supply 5  | Absent   |                    |                  |               | 
| Power Supply 6  | Absent   |                    |                  |               | 
+-----------------+----------+--------------------+------------------+---------------+
```