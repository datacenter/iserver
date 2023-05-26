# Node Protocol - IS-IS

## Show tunnel endpoints for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl -o tunnel

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+---------------+------+----------+
| Node                | Domain  | Id            | Role | Type     |
+---------------------+---------+---------------+------+----------+
| pod-1/rl301-eu-spdc | overlay | 172.16.30.120 | leaf | physical | 
| pod-1/rl301-eu-spdc | overlay | 172.16.30.88  | leaf | physical | 
| pod-1/rl302-eu-spdc | overlay | 172.16.30.160 | leaf | physical | 
| pod-1/rl302-eu-spdc | overlay | 172.16.30.88  | leaf | physical | 
+---------------------+---------+---------------+------+----------+
```

[[Back]](./ProtocolIsis.md)