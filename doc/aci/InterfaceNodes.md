# Node Interface

## Multiple nodes selection

Usage:
- define node name multiple times
- each name is checked against node names in selected APIC
- nodes selected based on full or partial name match
- name 'any' and 'all' matches [all nodes](./InterfaceNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if multiple nodes are defined, last-used-node-name per apic is not updated

Example:

```
# iserver get aci intf mgmt --apic apic11 --node bl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:04.036+02:00 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:46.234+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

[[Back]](./Interface.md)