# Node Protocol - IS-IS

## Show neighbor details for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl -o neighbor

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+------------+-------------------+-------+--------------+---------------+-------+
| Node                | Domain  | Interface  | System Id         | Level | Circuit Type | Peer IP       | State |
+---------------------+---------+------------+-------------------+-------+--------------+---------------+-------+
| pod-1/rl301-eu-spdc | overlay | eth1/33.47 | 78:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.120 | up    | 
| pod-1/rl301-eu-spdc | overlay | eth1/34.48 | 78:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.120 | up    | 
| pod-1/rl302-eu-spdc | overlay | eth1/34.8  | A0:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.160 | up    | 
| pod-1/rl302-eu-spdc | overlay | eth1/33.7  | A0:1E:10:AC:00:00 | l1    | bcast        | 172.16.30.160 | up    | 
+---------------------+---------+------------+-------------------+-------+--------------+---------------+-------+
```

[[Back]](./ProtocolIsis.md)