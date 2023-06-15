# Node Interface

## Single node selection

Usage:
- define node name (or part of node name)
- if value matches multiple nodes, then command follows [multiple nodes](./InterfaceNodes.md) behavior
- name 'any' and 'all' matches [all nodes](./InterfaceNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if node name is left undefined, last-used-node-name per apic is used

Example:

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/cl201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:02.581+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

[[Back]](./Interface.md)