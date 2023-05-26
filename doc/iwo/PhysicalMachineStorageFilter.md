# Intersight Workload Optimizer

## Filter by storage name

```
# iserver get iwo phy --storage znas

Summary
-------
- Active   : 29/34
- Severity : 1/0/2/31
- Current  : 34/34


+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| State       | Severity     | Staleness | Name                    | Storage Severity | Storage                               |
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx00-eu-spdc.cisco.com | 1/2/2/1          | ESX00-Datastore-Host-vCenter-RESERVED | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx01-eu-spdc.cisco.com | 1/2/1/1          | ESX01-Datastore-Host-RESERVED         | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| MAINTENANCE | Normal       | CURRENT   | esx1-eu-spdc.cisco.com  | 1/2/1/1          | ESX1-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx10-eu-spdc.cisco.com | 1/2/2/1          | ESX10-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx11-eu-spdc.cisco.com | 1/2/2/1          | ESX11-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx12-eu-spdc.cisco.com | 1/2/2/1          | ESX12-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx13-eu-spdc.cisco.com | 1/2/2/1          | ESX13-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| MAINTENANCE | Normal       | CURRENT   | esx14-eu-spdc.cisco.com | 1/2/1/1          | ESX14-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Critical (1) | CURRENT   | esx2-eu-spdc.cisco.com  | 1/2/2/1          | ESX2-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| MAINTENANCE | Normal       | CURRENT   | esx20-eu-spdc.cisco.com | 1/2/2/0          | ESX20-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| MAINTENANCE | Normal       | CURRENT   | esx21-eu-spdc.cisco.com | 1/2/2/0          | ESX21-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| MAINTENANCE | Normal       | CURRENT   | esx22-eu-spdc.cisco.com | 1/2/0/1          | ESX22-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx3-eu-spdc.cisco.com  | 1/2/2/1          | ESX3-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx31-eu-spdc.cisco.com | 1/2/1/1          | ESX31-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx32-eu-spdc.cisco.com | 1/2/1/1          | ESX32-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx33-eu-spdc.cisco.com | 1/2/1/1          | ESX33-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx34-eu-spdc.cisco.com | 1/2/2/0          | ESX34-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx35-eu-spdc.cisco.com | 1/2/2/0          | ESX35-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Minor (1)    | CURRENT   | esx36-eu-spdc.cisco.com | 1/2/2/0          | ESX36-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx37-eu-spdc.cisco.com | 1/2/2/0          | ESX37-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx4-eu-spdc.cisco.com  | 1/2/3/1          | ESX4-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-ESX4-Datastore                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Minor (1)    | CURRENT   | esx41-eu-spdc.cisco.com | 1/2/3/0          | ESX41-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx42-eu-spdc.cisco.com | 1/2/3/0          | ESX42-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx43-eu-spdc.cisco.com | 1/2/3/0          | ESX43-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx44-eu-spdc.cisco.com | 1/2/2/0          | ESX44-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx5-eu-spdc.cisco.com  | 1/2/3/1          | ESX5-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-ESX5-Datastore                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx51-eu-spdc.cisco.com | 1/2/3/0          | ESX51-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx52-eu-spdc.cisco.com | 1/2/3/0          | ESX52-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx53-eu-spdc.cisco.com | 1/2/3/0          | ESX53-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx54-eu-spdc.cisco.com | 1/2/3/0          | ESX54-Datastore-host                  | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Blades-Vol01       | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx6-eu-spdc.cisco.com  | 1/2/2/1          | ESX6-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx7-eu-spdc.cisco.com  | 1/2/2/1          | ESX7-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx8-eu-spdc.cisco.com  | 1/2/2/1          | ESX8-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
| ACTIVE      | Normal       | CURRENT   | esx9-eu-spdc.cisco.com  | 1/2/2/1          | ESX9-Datastore-host                   | 
|             |              |           |                         |                  | EU-SPDC-Datastore-SNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-WNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-YNAS                | 
|             |              |           |                         |                  | EU-SPDC-Datastore-ZNAS                | 
|             |              |           |                         |                  | EU-SPDC-FlashArray-Racks-Vol01        | 
+-------------+--------------+-----------+-------------------------+------------------+---------------------------------------+
```