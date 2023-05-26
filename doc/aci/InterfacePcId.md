# Node Interface - Port Channel (PC)

## Filter by port channel id

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name          | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po1 | pod-4a-br-API | up    | enabled   | up    |        | active    | 100        | 1            | 
+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

[[Back]](./InterfacePc.md)