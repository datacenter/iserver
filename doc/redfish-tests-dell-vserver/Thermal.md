# Redfish Template Thermal

Vendor | Model
--- | ---
Dell | vServer

```
# iserver get redfish endpoint
    --cache dell-poweredge-r650-ygfcbtjso8womr-5.10.00.00-on
    --type dell
    --ip 10.58.24.210
    --port 49153
    --username administrator
    --password ******
    --template thermal

+----------------------------+----------+---------+--------------+------------------+----------------------------+
| Name                       | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+----------------------------+----------+---------+--------------+------------------+----------------------------+
| CPU1 Temp                  | Enabled  | OK      | CPU          | 57               | 98                         | 
| CPU2 Temp                  | Enabled  | OK      | CPU          | 54               | 98                         | 
| System Board Exhaust Temp  | Enabled  | OK      | SystemBoard  | 34               | 80                         | 
| System Board Inlet Temp    | Enabled  | OK      | SystemBoard  | 18               | 42                         | 
+----------------------------+----------+---------+--------------+------------------+----------------------------+

+---------------------+----------+---------+-----------+
| Name                | State    | Health  | Value     |
+---------------------+----------+---------+-----------+
| System Board Fan1A  | Enabled  | OK      | 9000 RPM  | 
| System Board Fan1B  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan1C  | Enabled  | OK      | 9240 RPM  | 
| System Board Fan1D  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan2A  | Enabled  | OK      | 9120 RPM  | 
| System Board Fan2B  | Enabled  | OK      | 5520 RPM  | 
| System Board Fan2C  | Enabled  | OK      | 9240 RPM  | 
| System Board Fan2D  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan3A  | Enabled  | OK      | 9240 RPM  | 
| System Board Fan3B  | Enabled  | OK      | 5520 RPM  | 
| System Board Fan3C  | Enabled  | OK      | 9120 RPM  | 
| System Board Fan3D  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan4A  | Enabled  | OK      | 9000 RPM  | 
| System Board Fan4B  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan4C  | Enabled  | OK      | 9120 RPM  | 
| System Board Fan4D  | Enabled  | OK      | 5400 RPM  | 
+---------------------+----------+---------+-----------+
```