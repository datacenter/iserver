# Intersight Workload Optimizer

## Filter by physical machine severity

```
# iserver get iwo phy --minor

Summary
-------
- Active   : 4/4
- Severity : 1/0/3/0
- Current  : 4/4


+--------+--------------+-----------+-------------------------+----------+---------+----------------+
| State  | Severity     | Staleness | Physical Machine Name   | Location | Type    | Data Center    |
+--------+--------------+-----------+-------------------------+----------+---------+----------------+
| ACTIVE | Critical (1) | CURRENT   | esx2-eu-spdc.cisco.com  | ONPREM   | vCenter | eu-spdc-dc     | 
| ACTIVE | Minor (1)    | CURRENT   | esx36-eu-spdc.cisco.com | ONPREM   | vCenter | eu-spdc-dc     | 
| ACTIVE | Minor (1)    | CURRENT   | esx41-eu-spdc.cisco.com | ONPREM   | vCenter | eu-spdc-dc     | 
| ACTIVE | Minor (1)    | CURRENT   | esx93-eu-spdc.cisco.com | ONPREM   | vCenter | eu-spdc-dmz-dc | 
+--------+--------------+-----------+-------------------------+----------+---------+----------------+
```