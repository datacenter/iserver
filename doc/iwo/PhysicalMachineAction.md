# Intersight Workload Optimizer

## Show selected storage devices with action details

```
# iserver get iwo phy --name esx2 --show-actions

Summary
-------
- Active   : 5/8
- Severity : 1/0/0/7
- Current  : 8/8


+--------+--------------+-----------+------------------------+----------+---------+-------------+
| State  | Severity     | Staleness | Physical Machine Name  | Location | Type    | Data Center |
+--------+--------------+-----------+------------------------+----------+---------+-------------+
| ACTIVE | Critical (1) | CURRENT   | esx2-eu-spdc.cisco.com | ONPREM   | vCenter | eu-spdc-dc  | 
+--------+--------------+-----------+------------------------+----------+---------+-------------+

+----------+----------------+-----------------------+--------------------------------------------------------------+
| Severity | Description    | Category              | Details                                                      |
+----------+----------------+-----------------------+--------------------------------------------------------------+
| critical | Mem Congestion | Performance Assurance | Provision Physical Machine similar to esx2-eu-spdc.cisco.com | 
+----------+----------------+-----------------------+--------------------------------------------------------------+
```