# Intersight Fabric Interconnect - Ethernet interfaces view

[[Back]](./FiInventory.md)

```
# iserver get fi -v eth

+----+-----------------+------+----------+-----------------+---------+--------+------------------+-------------------+----------------+------+--------------------+-----------+
| ID | FI              | Eth  | Admin    | Oper            | Speed   | Mode   | Role             | Mac               | Transceiver    | PC   | Server             | Port      |
+----+-----------------+------+----------+-----------------+---------+--------+------------------+-------------------+----------------+------+--------------------+-----------+
| 1  | fi1 FI-A [ID:A] | 1/1  | enabled  | link-down       | auto    | trunk  | server           | 00:11:11:11:11:08 | h25gaoc3m      | 1025 |                    |           |
| 2  | fi1 FI-A [ID:A] | 1/2  | enabled  | link-down       | auto    | trunk  | server           | 00:11:11:11:11:09 | h25gaoc3m      | 1025 |                    |           |
| 3  | fi1 FI-A [ID:A] | 1/3  | enabled  | link-down       | auto    | trunk  | server           | 00:11:11:11:11:0A | h25gaoc3m      | 1025 |                    |           |
| 4  | fi1 FI-A [ID:A] | 1/4  | enabled  | link-down       | auto    | trunk  | server           | 00:11:11:11:11:0B | h25gaoc3m      | 1025 |                    |           |
...

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)