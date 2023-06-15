# Node Interface

## Multiple nodes selection

Usage:
- define node name multiple times
- each name is checked against node names in selected APIC
- nodes selected based on full or partial name match
- name 'any' and 'all' matches [all nodes](./ProtocolNodesAll.md)

Note:
- if apic name is left undefined, the last-used-apic-name is used
- if multiple nodes are defined, last-used-node-name per apic is not updated

Example:

```
# iserver get aci proto cdp --apic apic11 --node rl --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors           | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com | 2751    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc         | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com | 2751    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc         | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

[[Back]](./Protocol.md)