# Namespace - State

[[Back]](../README.md) [[Prev]](../create/namespace_task.md) [[Next]](../overview/namespace.md) 

```
# iserver get k8s ns -v udn --cluster bm1
Cluster: bm1 (type: ocp)
|
+----+-----------+--------+-------+
| ID | Namespace | Status | Age   |
+----+-----------+--------+-------+
| 1  | island    | Active | 4h19m |
| 2  | island-a  | Active | 2d    |
| 3  | island-b  | Active | 5h1m  |
| 4  | island-c  | Active | 4h55m |
+----+-----------+--------+-------+

Filter: name
View:   state (def), udn
```