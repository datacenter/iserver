# Node Protocol

## Single node selection

Usage:
- define node name (or part of node name)
- if value matches multiple nodes, then command follows [multiple nodes](./ProtocolNodes.md) behavior
- name 'any' and 'all' matches [all nodes](./ProtocolNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if node name is left undefined, last-used-node-name per apic is used

Example:

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors                    | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 2725    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 2727    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 2726    | 5436        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 2726    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 2726    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 2726    | 2717        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 2726    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 2725    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 2727    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 2727    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 2727    | 2717        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 2726    | 2717        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 2726    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 2727    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 2754    | 2753        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2751    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

[[Back]](./Protocol.md)