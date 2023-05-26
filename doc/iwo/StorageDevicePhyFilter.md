# Intersight Workload Optimizer

## Filter by physical machine name

```
# iserver get iwo storage --phy esx41

Summary
-------
- Active   : 6/6
- Severity : 1/1/4/0
- Current  : 6/6


+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| State  | Severity   | Staleness | Name                            | Physical Machine Severity | Physical Machine        |
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| ACTIVE | Minor (2)  | CURRENT   | ESX41-Datastore-host            | 0/0/1/0                   | esx41-eu-spdc.cisco.com | 
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| ACTIVE | Minor (9)  | CURRENT   | EU-SPDC-Datastore-SNAS          | 1/0/2/30                  | esx00-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx01-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx1-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx10-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx11-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx12-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx13-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx14-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx2-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx20-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx21-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx3-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx31-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx32-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx33-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx34-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx35-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx36-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx37-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx4-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx41-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx42-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx43-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx44-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx5-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx51-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx52-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx53-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx54-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx6-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx7-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx8-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx9-eu-spdc.cisco.com  | 
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| ACTIVE | Minor (97) | CURRENT   | EU-SPDC-Datastore-WNAS          | 1/0/2/31                  | esx00-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx01-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx1-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx10-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx11-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx12-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx13-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx14-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx2-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx20-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx21-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx22-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx3-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx31-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx32-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx33-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx34-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx35-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx36-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx37-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx4-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx41-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx42-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx43-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx44-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx5-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx51-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx52-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx53-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx54-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx6-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx7-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx8-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx9-eu-spdc.cisco.com  | 
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| ACTIVE | Minor (5)  | CURRENT   | EU-SPDC-Datastore-YNAS          | 1/0/2/31                  | esx00-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx01-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx1-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx10-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx11-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx12-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx13-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx14-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx2-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx20-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx21-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx22-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx3-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx31-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx32-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx33-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx34-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx35-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx36-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx37-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx4-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx41-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx42-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx43-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx44-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx5-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx51-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx52-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx53-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx54-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx6-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx7-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx8-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx9-eu-spdc.cisco.com  | 
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| ACTIVE | Minor (56) | CURRENT   | EU-SPDC-Datastore-ZNAS          | 1/0/2/31                  | esx00-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx01-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx1-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx10-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx11-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx12-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx13-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx14-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx2-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx20-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx21-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx22-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx3-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx31-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx32-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx33-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx34-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx35-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx36-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx37-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx4-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx41-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx42-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx43-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx44-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx5-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx51-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx52-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx53-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx54-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx6-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx7-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx8-eu-spdc.cisco.com  | 
|        |            |           |                                 |                           | esx9-eu-spdc.cisco.com  | 
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
| ACTIVE | Minor (21) | CURRENT   | EU-SPDC-FlashArray-Blades-Vol01 | 0/0/1/6                   | esx41-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx42-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx43-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx51-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx52-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx53-eu-spdc.cisco.com | 
|        |            |           |                                 |                           | esx54-eu-spdc.cisco.com | 
+--------+------------+-----------+---------------------------------+---------------------------+-------------------------+
```