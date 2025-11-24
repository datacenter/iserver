# Intersight Hardware Discovery - Get annotations

## Workflow

- get node annotation information defined by [set](./set.md) workflow

## Requirements

None

## Example

```
# iserver get ocp imm --cluster bm1

OpenShift Workflow - Intersight Hardware - Get
==============================================

OpenShift Cluster: bm1

+-------+---------------+------------------+-------+----------------+--------+
| Mode  | Management IP | Intersight Moid  | Name  | Model          | Serial |
+-------+---------------+------------------+-------+----------------+--------+
| bm1-1 | 10.10.10.11   | aaaa1            | comp1 | UCSC-C220-M7SX | AAAA1  |
+-------+---------------+------------------+-------+----------------+--------+
| bm1-2 | 10.10.10.12   | aaaa2            | comp2 | UCSC-C220-M7SX | AAAA2  | 
+-------+---------------+------------------+-------+----------------+--------+
| bm1-3 | 10.10.10.13   | aaaa3            | comp3 | UCSC-C220-M7SX | AAAA3  |
+-------+---------------+------------------+-------+----------------+--------+
```

[[Back]](./README.md)