# Intersight Workload Optimizer

## Filter by virtual machine name

```
# iserver get iwo storage --vm ibc

Summary
-------
- Active   : 1/1
- Severity : 0/0/1/0
- Current  : 1/1


+--------+------------+-----------+---------------------------------+--------------------------+------------------------------------------+
| State  | Severity   | Staleness | Name                            | Virtual Machine Severity | Virtual Machine                          |
+--------+------------+-----------+---------------------------------+--------------------------+------------------------------------------+
| ACTIVE | Minor (21) | CURRENT   | EU-SPDC-FlashArray-Blades-Vol01 | 0/0/5/4                  | ibc-demo-controlpl-8877420f2f            | 
|        |            |           |                                 |                          | ibc-demo-ibc-27801251c0                  | 
|        |            |           |                                 |                          | ibc-demo-ibc-545014a7e0                  | 
|        |            |           |                                 |                          | ibc-demo-ibc-6dd5b97865                  | 
|        |            |           |                                 |                          | ibc-demo-ibc-a0b852c940                  | 
|        |            |           |                                 |                          | vimercate-default-2-controlpl-d98e986ca5 | 
|        |            |           |                                 |                          | vimercate-default-2-worker-6a270556ed    | 
|        |            |           |                                 |                          | vimercate-default-2-worker-ced0cb5a6e    | 
|        |            |           |                                 |                          | vimercate-default-2-worker-f7eace816b    | 
+--------+------------+-----------+---------------------------------+--------------------------+------------------------------------------+
```