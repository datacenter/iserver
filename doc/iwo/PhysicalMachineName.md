# Intersight Workload Optimizer

## Filter by physical machine name

```
# iserver get iwo phy --name esx9

Summary
-------
- Active   : 10/12
- Severity : 0/0/1/11
- Current  : 12/12


+-------------+-----------+-----------+--------------------------------------------+----------+----------------+----------------+
| State       | Severity  | Staleness | Physical Machine Name                      | Location | Type           | Data Center    |
+-------------+-----------+-----------+--------------------------------------------+----------+----------------+----------------+
| ACTIVE      | Normal    | CURRENT   | esx9-eu-spdc-FCH2016V23J: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         | 
| ACTIVE      | Normal    | CURRENT   | esx9-eu-spdc.cisco.com                     | ONPREM   | vCenter        | eu-spdc-dc     | 
| ACTIVE      | Normal    | CURRENT   | esx91-eu-spdc-WZP234411LW: sys/rack-unit-1 | ONPREM   | Intersight UCS | UCS-DC         | 
| ACTIVE      | Normal    | CURRENT   | esx91-eu-spdc.cisco.com                    | ONPREM   | vCenter        | eu-spdc-dmz-dc | 
| ACTIVE      | Normal    | CURRENT   | esx92-eu-spdc-FCH2017V2AF: sys/rack-unit-1 | ONPREM   | Intersight UCS | UCS-DC         | 
| ACTIVE      | Normal    | CURRENT   | esx92-eu-spdc.cisco.com                    | ONPREM   | vCenter        | eu-spdc-dmz-dc | 
| ACTIVE      | Normal    | CURRENT   | esx93-eu-spdc-FCH2108V1HE: sys/rack-unit-1 | ONPREM   | Intersight UCS | UCS-DC         | 
| ACTIVE      | Minor (1) | CURRENT   | esx93-eu-spdc.cisco.com                    | ONPREM   | vCenter        | eu-spdc-dmz-dc | 
| ACTIVE      | Normal    | CURRENT   | esx94-eu-spdc-FCH2017V2AH: sys/rack-unit-1 | ONPREM   | Intersight UCS | UCS-DC         | 
| MAINTENANCE | Normal    | CURRENT   | esx94-eu-spdc.cisco.com                    | ONPREM   | vCenter        | eu-spdc-dmz-dc | 
| ACTIVE      | Normal    | CURRENT   | esx95-eu-spdc-FCH2017V241: sys/rack-unit-1 | ONPREM   | Intersight UCS | UCS-DC         | 
| MAINTENANCE | Normal    | CURRENT   | esx95-eu-spdc.cisco.com                    | ONPREM   | vCenter        | eu-spdc-dmz-dc | 
+-------------+-----------+-----------+--------------------------------------------+----------+----------------+----------------+
```