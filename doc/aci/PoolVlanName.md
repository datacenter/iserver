# VLAN Pool

## Filter by name

```
# iserver get aci pool vlan --apic apic21 --name HX*

Apic: apic21

+----------------+-----------------+----------------------+----------+-------------+-----------+
| VLAN Pool Name | Allocation Mode | Encapsulation Block  | Role     | Domain      | EPG Usage |
+----------------+-----------------+----------------------+----------+-------------+-----------+
| HX1_VlanPool   | static          | [70-79] (static)     | external | HX1_PhysDom | 0/3059    | 
|                |                 | [1000-4048] (static) | external |             |           | 
+----------------+-----------------+----------------------+----------+-------------+-----------+
```

[[Back]](./PoolVlan.md)