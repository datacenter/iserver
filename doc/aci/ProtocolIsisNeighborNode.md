# Node Protocol - IS-IS

## Show neighbor details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc -o neighbor

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+--------------+-------------------+-------+--------------+-------------+-------+
| Node                | Domain  | Interface    | System Id         | Level | Circuit Type | Peer IP     | State |
+---------------------+---------+--------------+-------------------+-------+--------------+-------------+-------+
| pod-1/cl201-eu-spdc | overlay | eth1/108.504 | 41:20:03:0A:00:00 | l1    | bcast        | 10.3.32.65  | up    | 
| pod-1/cl201-eu-spdc | overlay | eth1/107.7   | 41:C0:03:0A:00:00 | l1    | bcast        | 10.3.192.65 | up    | 
+---------------------+---------+--------------+-------------------+-------+--------------+-------------+-------+
```

[[Back]](./ProtocolIsis.md)