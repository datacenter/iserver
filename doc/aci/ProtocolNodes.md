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

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors           | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com | 62235   | 62232       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B  | 62225   | 62230       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A  | 62226   | 62219       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc         | 62234   | 62236       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com | 61676   | 61668       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B  | 61675   | 61674       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A  | 61675   | 61662       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc         | 61676   | 61672       | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

[[Back]](./Protocol.md)