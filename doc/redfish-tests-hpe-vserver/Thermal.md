# Redfish Template Thermal

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
    --template thermal

+-------------------+----------+---------+--------------+------------------+----------------------------+
| Name              | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+-------------------+----------+---------+--------------+------------------+----------------------------+
| 01-Inlet Ambient  | Enabled  | OK      | Intake       | 23               | 42                         | 
| 02-CPU 1          | Enabled  | OK      | CPU          | 40               | 70                         | 
| 03-CPU 2          | Enabled  | OK      | CPU          | 40               | 70                         | 
| 04-P1 DIMM 1-8    | Absent   |         | SystemBoard  | 0                | None                       | 
| 05-P1 PMM 1-8     | Absent   |         | SystemBoard  | 0                | None                       | 
| 06-P1 DIMM 9-16   | Enabled  | OK      | SystemBoard  | 31               | 85                         | 
| 07-P1 PMM 9-16    | Absent   |         | SystemBoard  | 0                | None                       | 
| 08-P2 DIMM 1-8    | Absent   |         | SystemBoard  | 0                | None                       | 
| 09-P2 PMM 1-8     | Absent   |         | SystemBoard  | 0                | None                       | 
| 10-P2 DIMM 9-16   | Enabled  | OK      | SystemBoard  | 31               | 85                         | 
| 11-P2 PMM 9-16    | Absent   |         | SystemBoard  | 0                | None                       | 
| 12-VR P1          | Enabled  | OK      | SystemBoard  | 38               | 110                        | 
| 13-VR P2          | Enabled  | OK      | SystemBoard  | 39               | 110                        | 
| 14-VR P1 Mem 1    | Enabled  | OK      | SystemBoard  | 30               | 110                        | 
| 15-VR P1 Mem 2    | Enabled  | OK      | SystemBoard  | 32               | 110                        | 
| 16-VR P2 Mem 1    | Enabled  | OK      | SystemBoard  | 33               | 110                        | 
| 17-VR P2 Mem 2    | Enabled  | OK      | SystemBoard  | 31               | 110                        | 
| 18-Chipset        | Enabled  | OK      | SystemBoard  | 39               | 100                        | 
| 19-BMC            | Enabled  | OK      | SystemBoard  | 65               | 110                        | 
| 20-HD Max         | Enabled  | OK      | SystemBoard  | 40               | 60                         | 
| 21-Exp Bay Drive  | Absent   |         | SystemBoard  | 0                | None                       | 
| 22-Stor Batt      | Enabled  | OK      | SystemBoard  | 24               | 60                         | 
| 23-E-Fuse         | Enabled  | OK      | SystemBoard  | 32               | 100                        | 
| 24-P/S 1          | Enabled  | OK      | PowerSupply  | 40               | None                       | 
| 25-P/S 1 Inlet    | Enabled  | OK      | PowerSupply  | 35               | None                       | 
| 26-P/S 2          | Enabled  | OK      | PowerSupply  | 40               | None                       | 
| 27-P/S 2 Inlet    | Enabled  | OK      | PowerSupply  | 35               | None                       | 
| 29-LOM Card       | Enabled  | OK      | SystemBoard  | 40               | 95                         | 
| 30-HD Controller  | Absent   |         | SystemBoard  | 0                | None                       | 
| 31-HD Cntlr Zone  | Absent   |         | SystemBoard  | 0                | None                       | 
| 32-Board Inlet    | Enabled  | OK      | SystemBoard  | 26               | 60                         | 
| 33-BMC Zone       | Enabled  | OK      | SystemBoard  | 38               | 90                         | 
| 34-P/S 2 Zone     | Enabled  | OK      | PowerSupply  | 34               | 90                         | 
| 35-I/O Zone       | Enabled  | OK      | SystemBoard  | 33               | 90                         | 
| 36-Battery Zone   | Enabled  | OK      | SystemBoard  | 31               | 90                         | 
| 37-PCI 1          | Enabled  | OK      | SystemBoard  | 40               | 100                        | 
| 38-PCI 1 Zone     | Enabled  | OK      | SystemBoard  | 42               | 90                         | 
| 39-PCI 2          | Absent   |         | SystemBoard  | 0                | None                       | 
| 40-PCI 2 Zone     | Enabled  | OK      | SystemBoard  | 41               | 90                         | 
| 41-PCI 3          | Absent   |         | SystemBoard  | 0                | None                       | 
| 42-PCI 3 Zone     | Absent   |         | SystemBoard  | 0                | None                       | 
| 43-ExpBayBoot     | Enabled  | OK      | SystemBoard  | 35               | 60                         | 
| 46-AHCI HD Max    | Absent   |         | SystemBoard  | 0                | None                       | 
| 50-CPU 1 PkgTmp   | Enabled  | OK      | CPU          | 44               | None                       | 
| 51-CPU 2 PkgTmp   | Enabled  | OK      | CPU          | 39               | None                       | 
+-------------------+----------+---------+--------------+------------------+----------------------------+

+--------+----------+---------+-------------+
| Name   | State    | Health  | Value       |
+--------+----------+---------+-------------+
| Fan 1  | Enabled  | OK      | 16 Percent  | 
| Fan 2  | Enabled  | OK      | 16 Percent  | 
| Fan 3  | Enabled  | OK      | 16 Percent  | 
| Fan 4  | Enabled  | OK      | 16 Percent  | 
| Fan 5  | Enabled  | OK      | 16 Percent  | 
| Fan 6  | Enabled  | OK      | 16 Percent  | 
| Fan 7  | Enabled  | OK      | 16 Percent  | 
+--------+----------+---------+-------------+
```