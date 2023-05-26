# Node

## Sensor specific output

```
# iserver get aci node --apic apic11 -o sensor --name bl205*

Apic: apic11

+---------------------+---------------+--------+-------+-----+-----+------------+
| Node                | Sensor        | Type   | Value | Min | Max | Oper State |
+---------------------+---------------+--------+-------+-----+-----+------------+
| pod-1/bl205-eu-spdc | Inlet         | inlet  | 0     | 42  | 70  | normal     | 
| pod-1/bl205-eu-spdc | Outlet        | outlet | 0     | 70  | 80  | normal     | 
| pod-1/bl205-eu-spdc | Wolfridge     | asic   | 0     | 100 | 110 | normal     | 
| pod-1/bl205-eu-spdc | Wolfridge vrm | asic   | 0     | 90  | 120 | normal     | 
| pod-1/bl205-eu-spdc | x86 processor | cpu    | 0     | 80  | 105 | normal     | 
+---------------------+---------------+--------+-------+-----+-----+------------+
```

[[Back]](./Node.md)